"""LFU 缓存
题意与思路：按访问频率淘汰，同频淘汰最久未用项；频率桶中维护 OrderedDict。
复杂度：get/put O(1) 期望，O(capacity) 空间。
来源：https://leetcode.cn/problems/lfu-cache/
"""

from collections import defaultdict,OrderedDict

class LFUCache:
    def __init__(self,capacity):
        self.capacity,self.values,self.frequency,self.buckets=capacity,{},{},defaultdict(OrderedDict)
        self.minimum=0
    def _touch(self,key):
        f=self.frequency[key]
        del self.buckets[f][key]
        if not self.buckets[f]:
            del self.buckets[f]
            if self.minimum==f: self.minimum+=1
        self.frequency[key]=f+1
        self.buckets[f+1][key]=None
    def get(self,key):
        if key not in self.values: return -1
        self._touch(key)
        return self.values[key]
    def put(self,key,value):
        if self.capacity==0: return
        if key in self.values:
            self.values[key]=value
            self._touch(key)
            return
        if len(self.values)==self.capacity:
            removed,_=self.buckets[self.minimum].popitem(last=False)
            if not self.buckets[self.minimum]: del self.buckets[self.minimum]
            del self.values[removed],self.frequency[removed]
        self.values[key],self.frequency[key]=value,1
        self.buckets[1][key]=None
        self.minimum=1
