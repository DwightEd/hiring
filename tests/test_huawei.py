"""华为题：独立穷举/全排序参考实现，验证并集、并列分数、精确 K 段。"""
import itertools
import random
import subprocess
import sys
import unittest
from companies.huawei.global_window_attention import global_window_attention
from companies.huawei.pipeline_partition import minimum_peak,split_exactly_k
from companies.huawei.moe_capacity_routing import route
from tests.support import ROOT


class HuaweiTests(unittest.TestCase):
    def test_partition_exhaustive_cuts(self):
        rng=random.Random(918)
        for n in range(1,9):
            for _ in range(15):
                times=[rng.randrange(0,10) for _ in range(n)]
                for k in range(1,n+1):
                    brute=min(max(sum(times[a:b]) for a,b in zip((0,)+cuts,cuts+(n,)))
                              for cuts in itertools.combinations(range(1,n),k-1))
                    limit,parts=split_exactly_k(times,k)
                    self.assertEqual(limit,brute);self.assertEqual(len(parts),k)
                    self.assertEqual(parts[0][0],0);self.assertEqual(parts[-1][1],n)
                    self.assertTrue(all(a<b and sum(times[a:b])<=limit for a,b in parts))
                    self.assertTrue(all(parts[i][1]==parts[i+1][0] for i in range(k-1)))
        with self.assertRaises(ValueError):minimum_peak([1,-1],1)
        with self.assertRaises(ValueError):minimum_peak([1],2)

    def test_attention_reference(self):
        rng=random.Random(5467)
        for _ in range(150):
            n,d=rng.randrange(1,9),rng.randrange(1,5)
            q,k,v=[[[rng.randrange(-3,4) for _ in range(d)] for _ in range(n)] for _ in range(3)]
            global_positions=rng.sample(range(n),rng.randrange(n+1))
            window,top=rng.randrange(n+1),rng.randrange(n+2)
            expected=[]
            for i in range(n):
                candidates=set(range(n)) if i in global_positions else set(global_positions)|set(range(max(0,i-window),min(n,i+window+1)))
                scores=[(sum(a*b for a,b in zip(q[i],k[j])),j) for j in candidates]
                selected=sorted((score,j) for score,j in scores if score>0)
                selected=sorted(selected,key=lambda item:(-item[0],item[1]))[:top]
                expected.append([sum(score*v[j][axis] for score,j in selected) for axis in range(d)])
            self.assertEqual(global_window_attention(q,k,v,global_positions,window,top),expected)
        # 相同正分数只留最小下标；全局位和窗口重叠不得重复累加。
        self.assertEqual(global_window_attention([[1],[1]],[[1],[1]],[[2],[9]],[0],1,1),[[2],[2]])

    def test_moe(self):
        self.assertEqual(route([[1,5,4],[8,1,2],[3,6,5],[2,7,9]],3,2,2),(9,[1,2,2]))
        self.assertEqual(route([[5,5,5,1],[2,8,8,9],[1,2,9,9],[7,7,1,1]],4,2,2),(13,[2,2,1,2]))
        self.assertEqual(route([[5,5,4],[5,5,4]],3,2,1),(2,[1,1,0]))
        self.assertEqual(route([[1,2]],2,1,0),(0,[0,0]))

    def test_cli(self):
        cases=[('pipeline_partition','5 2\n7 2 5 10 8\n','18\n'),
               ('moe_capacity_routing','4 3 2 2\n1 5 4\n8 1 2\n3 6 5\n2 7 9\n','9\n1 2 2\n'),
               ('global_window_attention','2 1 1 1 1\n0\n1\n1\n1\n1\n2\n9\n','2\n2\n')]
        for name,input_text,expected in cases:
            result=subprocess.run([sys.executable,str(ROOT/'companies'/'huawei'/(name+'.py'))],input=input_text,text=True,capture_output=True,check=True)
            self.assertEqual(result.stdout,expected)
