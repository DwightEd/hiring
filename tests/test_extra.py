"""补充题逐题用例，含缓存淘汰和流式分块边界。"""
import copy
import json
import random
import unittest
from tests.support import catalog,module,solution,linked,values,tree,inorder

CASES=[
(8,'myAtoi',['   -42'],-42),(8,'myAtoi',['91283472332'],2147483647),
(9,'isPalindrome',[1221],True),(9,'isPalindrome',[10],False),
(10,'isMatch',['aab','c*a*b'],True),(10,'isMatch',['mississippi','mis*is*p*.'],False),
(43,'multiply',['123','456'],'56088'),(43,'multiply',['0','999'],'0'),
(50,'myPow',[2.0,-2],0.25),(69,'mySqrt',[8],2),
(91,'numDecodings',['226'],3),(91,'numDecodings',['06'],0),
(93,'restoreIpAddresses',['25525511135'],['255.255.11.135','255.255.111.35']),
(122,'maxProfit',[[7,1,5,3,6,4]],7),
(123,'maxProfit',[[3,3,5,0,0,3,1,4]],6),
(127,'ladderLength',['hit','cog',['hot','dot','dog','lot','log','cog']],5),
(127,'ladderLength',['hit','cog',['hot','dot','dog','lot','log']],0),
(151,'reverseWords',['  the sky  is blue '],'blue is sky the'),
(165,'compareVersion',['1.00000000000000000000000001','1.1'],0),
(165,'compareVersion',['1.0','1.0.1'],-1),
(179,'largestNumber',[[3,30,34,5,9]],'9534330'),(179,'largestNumber',[[0,0]],'0'),
(209,'minSubArrayLen',[7,[2,3,1,2,4,3]],2),
(221,'maximalSquare',[[list('10100'),list('10111'),list('11111'),list('10010')]],4),
(224,'calculate',['(1+(4+5+2)-3)+(6+8)'],23),(224,'calculate',['- (3 + (4 - 5))'],-2),
(309,'maxProfit',[[1,2,3,0,2]],3),
(402,'removeKdigits',['1432219',3],'1219'),(402,'removeKdigits',['10200',1],'200'),
(415,'addStrings',['999','1'],'1000'),
(503,'nextGreaterElements',[[1,2,1]],[2,-1,2]),
(518,'change',[5,[1,2,5]],4),
(547,'findCircleNum',[[[1,1,0],[1,1,0],[0,0,1]]],2),
(714,'maxProfit',[[1,3,2,8,4,9],2],8),
(718,'findLength',[[1,2,3,2,1],[3,2,1,4,7]],3),
(743,'networkDelayTime',[[[2,1,1],[2,3,1],[3,4,1]],4,2],2),
(743,'networkDelayTime',[[[1,2,1]],2,2],-1),
(862,'shortestSubarray',[[2,-1,2],3],3),(862,'shortestSubarray',[[1,2],4],-1),
(912,'sortArray',[[5,1,1,2,0,0]],[0,0,1,1,2,5]),
(1012,'numDupDigitsAtMostN',[100],10),
(1584,'minCostConnectPoints',[[[0,0],[2,2],[3,10],[5,2],[7,0]]],20),
]
SPECIAL={92,103,110,143,210,232,297,460,'top_k_numbers','sorted_intersection',
 'tree_substructure','character_complement','rectangle_overlap','partition_pivots','quicksort',
 'max_length_sum_k','bubble_sort','tool_log_statistics','weighted_unique_topk','city_order_totals','stream_json'}


class ExtraTests(unittest.TestCase):
    def test_catalog_coverage(self):
        ids=[row['id'] for row in catalog('extra')]
        self.assertEqual(len(ids),len(set(ids)))
        self.assertEqual(set(ids),{row[0] for row in CASES}|SPECIAL)

    def test_trees_and_lists(self):
        self.assertEqual(values(solution('extra',92).reverseBetween(linked([1,2,3,4,5]),2,4)),[1,4,3,2,5])
        head=linked([1,2,3,4,5]);solution('extra',143).reorderList(head)
        self.assertEqual(values(head),[1,5,2,4,3])
        root=tree([3,9,20,None,None,15,7])
        self.assertEqual(solution('extra',103).zigzagLevelOrder(root),[[3],[20,9],[15,7]])
        self.assertTrue(solution('extra',110).isBalanced(root))
        self.assertFalse(solution('extra',110).isBalanced(tree([1,2,None,3,None,4])))
        codec=module('extra',297).Codec();serialized=codec.serialize(root)
        self.assertEqual(codec.serialize(codec.deserialize(serialized)),serialized)
        self.assertIsNone(codec.deserialize(codec.serialize(None)))
        self.assertTrue(module('extra','tree_substructure').is_substructure(tree([3,4,5,1,2]),tree([4,1])))
        self.assertFalse(module('extra','tree_substructure').is_substructure(root,None))

    def test_course_order(self):
        edges=[[1,0],[2,0],[3,1],[3,2]]
        result=solution('extra',210).findOrder(4,edges)
        self.assertEqual(set(result),set(range(4)))
        for end,start in edges:self.assertLess(result.index(start),result.index(end))
        self.assertEqual(solution('extra',210).findOrder(2,[[0,1],[1,0]]),[])

    def test_queue_lfu(self):
        queue=module('extra',232).MyQueue();queue.push(1);queue.push(2)
        self.assertEqual(queue.peek(),1);self.assertEqual(queue.pop(),1)
        queue.push(3);self.assertEqual(queue.pop(),2);self.assertEqual(queue.pop(),3)
        self.assertTrue(queue.empty())
        cache=module('extra',460).LFUCache(2)
        cache.put(1,1);cache.put(2,2);self.assertEqual(cache.get(1),1)
        cache.put(3,3);self.assertEqual(cache.get(2),-1);self.assertEqual(cache.get(3),3)
        cache.put(4,4);self.assertEqual(cache.get(1),-1)
        self.assertEqual(cache.get(3),3);self.assertEqual(cache.get(4),4)
        cache.put(4,40);self.assertEqual(cache.get(4),40)
        cache=module('extra',460).LFUCache(0);cache.put(1,1);self.assertEqual(cache.get(1),-1)

    def test_custom_algorithms(self):
        self.assertEqual(module('extra','top_k_numbers').top_k_numbers([1,5,2,5],2),[5,5])
        self.assertEqual(module('extra','top_k_numbers').top_k_numbers([1,5,2,5],2,False),[1,2])
        self.assertEqual(module('extra','sorted_intersection').sorted_intersection([1,1,2,3],[1,1,3,4]),[1,3])
        self.assertEqual(module('extra','character_complement').character_complement('abacad','bc'),'ad')
        self.assertEqual(module('extra','rectangle_overlap').overlap_area([0,0,3,3],[1,1,4,4]),4)
        self.assertEqual(module('extra','partition_pivots').partition_pivots([1,3,2,4]),[0,3])
        self.assertEqual(module('extra','partition_pivots').partition_pivots([1,1]),[])
        self.assertEqual(module('extra','max_length_sum_k').max_length_sum_k([1,-1,5,-2,3],3),4)
        self.assertEqual(module('extra','max_length_sum_k').max_length_sum_k([0,0,0],0),3)
        rng=random.Random(42)
        for _ in range(90):
            nums=[rng.randrange(-9,10) for _ in range(rng.randrange(30))]
            for name in ['quicksort','bubble_sort']:
                copy_nums=nums[:];getattr(module('extra',name),name)(copy_nums)
                self.assertEqual(copy_nums,sorted(nums))
        for n in [1,10,20,98,345,1000]:
            brute=sum(len(set(str(i)))<len(str(i)) for i in range(1,n+1))
            self.assertEqual(solution('extra',1012).numDupDigitsAtMostN(n),brute)

    def test_practice_variants(self):
        result=module('extra','tool_log_statistics').tool_log_statistics([('a',True),('a',False),('b',False)])
        self.assertEqual(result,({'a':.5,'b':0},'a'))
        self.assertEqual(module('extra','tool_log_statistics').tool_log_statistics([]),({},None))
        result=module('extra','weighted_unique_topk').weighted_unique_topk([('a',[1,1]),('b',[2,1]),('a',[4,1]),('c',[2,1])],[2,1],3)
        self.assertEqual(result,[('a',9),('b',5),('c',5)])
        self.assertEqual(module('extra','city_order_totals').city_order_totals([('北京',100),('上海',250),('北京',-20)]),{'北京':80,'上海':250})

    def test_json_every_split(self):
        objects=[{'x':'含引号"与反斜杠\\以及{}[]','y':[1,True,None]},[{'z':2}],{}]
        stream=' \n'.join(json.dumps(x,ensure_ascii=False) for x in objects)
        for split in range(len(stream)+1):
            parser=module('extra','stream_json').JSONStream()
            output=parser.feed(stream[:split])+parser.feed(stream[split:]);parser.finish()
            self.assertEqual(output,objects)
        parser=module('extra','stream_json').JSONStream();output=[]
        for char in stream:output.extend(parser.feed(char))
        parser.finish();self.assertEqual(output,objects)
        parser=module('extra','stream_json').JSONStream();parser.feed('{"x":')
        with self.assertRaises(ValueError):parser.finish()
        with self.assertRaises(ValueError):module('extra','stream_json').JSONStream().feed('{]')


def attach(row,index):
    identifier,method,args,expected=row
    def check(self):
        actual=getattr(solution('extra',identifier),method)(*copy.deepcopy(args))
        if identifier==93:actual=sorted(actual)
        self.assertEqual(actual,expected)
    setattr(ExtraTests,f'test_{identifier:04d}_{index:03d}',check)


for index,row in enumerate(CASES):attach(row,index)
