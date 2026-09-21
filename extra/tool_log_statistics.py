"""统计工具成功率及失败次数最多的工具。

来源主题：字节 AI Agent 面经 https://www.nowcoder.com/discuss/931682493218947072
原帖未给日志格式和并列规则。本仓库练习约定：输入 (工具名, bool成功)；
失败数并列取首次出现者；无失败时最差工具为 None；空输入返回 ({}, None)。
只扫描一次累计次数，再扫描工具表。时间 O(n+m)，空间 O(m)，m 为工具种数。
"""


def tool_log_statistics(logs):
    counts = {}
    for name, success in logs:
        if not isinstance(success, bool):
            raise ValueError("success 必须是 bool，不能直接传入字符串 'false'")
        if name not in counts:
            counts[name] = [0, 0]
        counts[name][0] += 1
        counts[name][1] += success
    rates = {}
    worst, most_failures = None, 0
    for name, (total, successes) in counts.items():
        rates[name] = successes / total
        if total - successes > most_failures:
            most_failures = total - successes
            worst = name
    return rates, worst
