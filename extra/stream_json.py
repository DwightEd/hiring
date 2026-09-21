"""流式 JSON 对象/数组分帧，支持半包、粘包、字符串内括号和转义。

来源主题：快手 Agent 面经 https://www.nowcoder.com/discuss/931679347587444736
原帖未说明协议。本练习限定 UTF-8 已解码的 str 分块，顶层只允许对象/数组；
每个完整帧交给标准库验证 JSON 语法。不是任意顶层数字流解析器。
括号扫描保留跨分块状态，每个字符扫描一次；解析每帧再线性扫描一次。
时间 O(总字符数)，工作空间 O(最长未完成帧)，另计本次输出对象。
"""
import json


class JSONStream:
    def __init__(self):
        self.characters = []
        self.depth = 0
        self.in_string = False
        self.escaped = False

    def feed(self, chunk):
        results = []
        for char in chunk:
            if self.depth == 0:
                if char.isspace():
                    continue
                if char not in "[{":
                    raise ValueError("顶层必须是 JSON 对象或数组")
            self.characters.append(char)
            if self.in_string:
                if self.escaped:
                    self.escaped = False
                elif char == "\\":
                    self.escaped = True
                elif char == '"':
                    self.in_string = False
            elif char == '"':
                self.in_string = True
            elif char in "[{":
                self.depth += 1
            elif char in "]}":
                self.depth -= 1
                if self.depth == 0:
                    frame = "".join(self.characters)
                    self.characters.clear()
                    results.append(json.loads(frame))
        return results

    def finish(self):
        if self.characters:
            raise ValueError("输入结束时仍有未完成的 JSON 帧")
