"""100 题逐题用例；原地操作、节点身份、恢复输入与深树单独检查。"""
import copy
import itertools
import random
import unittest
from tests.support import catalog, module, solution, Node, linked, values, tree, inorder

# (题号, 方法, 参数, 期望值)；顺序不唯一的输出另行归一化。
CASES = [
(1,'twoSum',[[2,7,11,15],9],[0,1]),
(1,'twoSum',[[3,3],6],[0,1]),
(49,'groupAnagrams',[['eat','tea','tan','ate','nat','bat']],[['eat','tea','ate'],['tan','nat'],['bat']]),
(128,'longestConsecutive',[[100,4,200,1,3,2,2]],4),
(11,'maxArea',[[1,8,6,2,5,4,8,3,7]],49),
(15,'threeSum',[[-1,0,1,2,-1,-4]],[[-1,-1,2],[-1,0,1]]),
(42,'trap',[[0,1,0,2,1,0,1,3,2,1,2,1]],6),
(3,'lengthOfLongestSubstring',['abba'],2),
(3,'lengthOfLongestSubstring',[''],0),
(438,'findAnagrams',['cbaebabacd','abc'],[0,6]),
(438,'findAnagrams',['abab','ab'],[0,1,2]),
(560,'subarraySum',[[1,-1,0],0],3),
(239,'maxSlidingWindow',[[1,3,-1,-3,5,3,6,7],3],[3,3,5,5,6,7]),
(76,'minWindow',['ADOBECODEBANC','ABC'],'BANC'),
(76,'minWindow',['a','aa'],''),
(53,'maxSubArray',[[-2,1,-3,4,-1,2,1,-5,4]],6),
(53,'maxSubArray',[[-3,-2,-5]],-2),
(56,'merge',[[[1,3],[2,6],[8,10],[15,18]]],[[1,6],[8,10],[15,18]]),
(238,'productExceptSelf',[[1,2,3,4]],[24,12,8,6]),
(238,'productExceptSelf',[[0,2,0]],[0,0,0]),
(41,'firstMissingPositive',[[3,4,-1,1]],2),
(54,'spiralOrder',[[[1,2,3],[4,5,6],[7,8,9]]],[1,2,3,6,9,8,7,4,5]),
(54,'spiralOrder',[[[1],[2],[3]]],[1,2,3]),
(240,'searchMatrix',[[[1,4,7],[2,5,8],[3,6,9]],6],True),
(240,'searchMatrix',[[[1]],2],False),
(200,'numIslands',[[list('11000'),list('11000'),list('00100'),list('00011')]],3),
(994,'orangesRotting',[[[2,1,1],[1,1,0],[0,1,1]]],4),
(994,'orangesRotting',[[[2,1,1],[0,1,1],[1,0,1]]],-1),
(207,'canFinish',[2,[[1,0]]],True),
(207,'canFinish',[2,[[1,0],[0,1]]],False),
(46,'permute',[[1,2,3]],list(map(list,itertools.permutations([1,2,3])))),
(78,'subsets',[[1,2]],[[],[1],[2],[1,2]]),
(17,'letterCombinations',['23'],['ad','ae','af','bd','be','bf','cd','ce','cf']),
(17,'letterCombinations',[''],[]),
(39,'combinationSum',[[2,3,6,7],7],[[2,2,3],[7]]),
(22,'generateParenthesis',[3],['((()))','(()())','(())()','()(())','()()()']),
(79,'exist',[[list('ABCE'),list('SFCS'),list('ADEE')],'ABCCED'],True),
(79,'exist',[[list('ABCE'),list('SFCS'),list('ADEE')],'ABCB'],False),
(131,'partition',['aab'],[['a','a','b'],['aa','b']]),
(35,'searchInsert',[[1,3,5,6],2],1),
(74,'searchMatrix',[[[1,3,5],[7,9,11]],7],True),
(34,'searchRange',[[5,7,7,8,8,10],8],[3,4]),
(34,'searchRange',[[],0],[-1,-1]),
(33,'search',[[4,5,6,7,0,1,2],0],4),
(33,'search',[[1],0],-1),
(153,'findMin',[[4,5,1,2,3]],1),
(4,'findMedianSortedArrays',[[1,3],[2]],2.0),
(4,'findMedianSortedArrays',[[],[1,2]],1.5),
(20,'isValid',['([{}])'],True),
(20,'isValid',['([)]'],False),
(394,'decodeString',['3[a2[c]]'],'accaccacc'),
(394,'decodeString',['2[abc]3[cd]ef'],'abcabccdcdcdef'),
(739,'dailyTemperatures',[[73,74,75,71,69,72,76,73]],[1,1,4,2,1,1,0,0]),
(84,'largestRectangleArea',[[2,1,5,6,2,3]],10),
(215,'findKthLargest',[[3,2,3,1,2,4,5,5,6],4],4),
(347,'topKFrequent',[[1,1,1,2,2,3],2],[1,2]),
(121,'maxProfit',[[7,1,5,3,6,4]],5),
(55,'canJump',[[2,3,1,1,4]],True),
(55,'canJump',[[3,2,1,0,4]],False),
(45,'jump',[[2,3,1,1,4]],2),
(763,'partitionLabels',['ababcbacadefegdehijhklij'],[9,7,8]),
(70,'climbStairs',[45],1836311903),
(70,'climbStairs',[1],1),
(118,'generate',[5],[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
(198,'rob',[[2,7,9,3,1]],12),
(279,'numSquares',[12],3),
(279,'numSquares',[13],2),
(322,'coinChange',[[1,2,5],11],3),
(322,'coinChange',[[2],3],-1),
(139,'wordBreak',['leetcode',['leet','code']],True),
(139,'wordBreak',['catsandog',['cats','dog','sand','and','cat']],False),
(300,'lengthOfLIS',[[10,9,2,5,3,7,101,18]],4),
(300,'lengthOfLIS',[[2,2,2]],1),
(152,'maxProduct',[[-2,3,-4]],24),
(416,'canPartition',[[1,5,11,5]],True),
(416,'canPartition',[[1,2,3,5]],False),
(32,'longestValidParentheses',[')()())'],4),
(62,'uniquePaths',[3,7],28),
(64,'minPathSum',[[[1,3,1],[1,5,1],[4,2,1]]],7),
(5,'longestPalindrome',['babad'],'bab'),
(5,'longestPalindrome',['cbbd'],'bb'),
(1143,'longestCommonSubsequence',['abcde','ace'],3),
(72,'minDistance',['horse','ros'],3),
(72,'minDistance',['','abc'],3),
(136,'singleNumber',[[4,1,2,1,2]],4),
(169,'majorityElement',[[2,2,1,1,1,2,2]],2),
(287,'findDuplicate',[[1,3,4,2,2]],2),
]
INPLACE = [
(283,'moveZeroes',[[0,1,0,3,12]],[1,3,12,0,0]),
(189,'rotate',[[1,2,3,4,5,6,7],3],[5,6,7,1,2,3,4]),
(73,'setZeroes',[[[1,1,1],[1,0,1],[1,1,1]]],[[1,0,1],[0,0,0],[1,0,1]]),
(73,'setZeroes',[[[0,1],[2,3]]],[[0,0],[0,3]]),
(48,'rotate',[[[1,2,3],[4,5,6],[7,8,9]]],[[7,4,1],[8,5,2],[9,6,3]]),
(75,'sortColors',[[2,0,2,1,1,0]],[0,0,1,1,2,2]),
(31,'nextPermutation',[[1,3,2]],[2,1,3]),
(31,'nextPermutation',[[3,2,1]],[1,2,3]),
]
SPECIAL = {160,206,234,141,142,21,2,19,24,25,138,148,23,146,
           94,104,226,101,543,102,108,98,230,199,114,105,437,236,124,208,51,155,295}


def normalize(identifier, value):
    if identifier in {49,15,78,39}:
        return sorted(tuple(sorted(row)) for row in value)
    if identifier in {17,22,347}:
        return sorted(value)
    if identifier in {46,131}:
        return sorted(map(tuple,value))
    return value


class Hot100Tests(unittest.TestCase):
    def test_catalog_complete(self):
        ids = [row['id'] for row in catalog('hot100')]
        self.assertEqual(len(ids),100)
        self.assertEqual(len(set(ids)),100)
        self.assertEqual(set(ids),{row[0] for row in CASES+INPLACE}|SPECIAL)

    def test_linked_lists(self):
        for identifier,method,raw,args,expected in [
            (206,'reverseList',[1,2,3],[],[3,2,1]),
            (19,'removeNthFromEnd',[1,2,3,4,5],[2],[1,2,3,5]),
            (19,'removeNthFromEnd',[1],[1],[]),
            (24,'swapPairs',[1,2,3,4,5],[],[2,1,4,3,5]),
            (25,'reverseKGroup',[1,2,3,4,5],[3],[3,2,1,4,5]),
            (148,'sortList',[4,2,1,3,2],[],[1,2,2,3,4]),
        ]:
            with self.subTest(id=identifier):
                self.assertEqual(values(getattr(solution('hot100',identifier),method)(linked(raw),*args)),expected)
        self.assertEqual(values(solution('hot100',21).mergeTwoLists(linked([1,2,4]),linked([1,3,4]))),[1,1,2,3,4,4])
        self.assertEqual(values(solution('hot100',2).addTwoNumbers(linked([9,9]),linked([1]))),[0,0,1])
        self.assertEqual(values(solution('hot100',23).mergeKLists([linked([1,4,5]),linked([1,3,4]),linked([2,6])])),[1,1,2,3,4,4,5,6])
        common=linked([8,9]);a=Node(1,next=common);b=Node(2,next=Node(3,next=common))
        self.assertIs(solution('hot100',160).getIntersectionNode(a,b),common)
        self.assertIsNone(solution('hot100',160).getIntersectionNode(linked([1]),linked([1])))
        head=linked([1,2,3]);entry=head.next;head.next.next.next=entry
        self.assertTrue(solution('hot100',141).hasCycle(head))
        self.assertIs(solution('hot100',142).detectCycle(head),entry)
        self.assertFalse(solution('hot100',141).hasCycle(linked([1])))
        self.assertIsNone(solution('hot100',142).detectCycle(None))
        for raw,expected in [([1,2,2,1],True),([1,2,3,2,1],True),([1,2],False)]:
            head=linked(raw)
            self.assertEqual(solution('hot100',234).isPalindrome(head),expected)
            self.assertEqual(values(head),raw, '回文检测应恢复输入链表')
        a,b=Node(7),Node(9);a.next=b;a.random=b;b.random=b
        clone=solution('hot100',138).copyRandomList(a)
        self.assertEqual(values(clone),[7,9]);self.assertIsNot(clone,a)
        self.assertIsNot(clone.next,b);self.assertIs(clone.random,clone.next)
        self.assertIs(clone.next.random,clone.next);self.assertIs(a.next,b)

    def test_trees(self):
        root=tree([3,9,20,None,None,15,7])
        for identifier,method,expected in [(94,'inorderTraversal',[9,3,15,20,7]),(104,'maxDepth',3),(543,'diameterOfBinaryTree',3),(102,'levelOrder',[[3],[9,20],[15,7]]),(199,'rightSideView',[3,20,7])]:
            with self.subTest(id=identifier):
                self.assertEqual(getattr(solution('hot100',identifier),method)(root),expected)
        self.assertEqual(inorder(solution('hot100',226).invertTree(copy.deepcopy(root))),[7,20,15,3,9])
        self.assertTrue(solution('hot100',101).isSymmetric(tree([1,2,2,3,4,4,3])))
        self.assertFalse(solution('hot100',101).isSymmetric(tree([1,2,2,None,3,None,3])))
        bst=solution('hot100',108).sortedArrayToBST([-10,-3,0,5,9])
        self.assertEqual(inorder(bst),[-10,-3,0,5,9]);self.assertTrue(solution('hot100',98).isValidBST(bst))
        self.assertFalse(solution('hot100',98).isValidBST(tree([5,1,4,None,None,3,6])))
        self.assertEqual(solution('hot100',230).kthSmallest(bst,3),0)
        built=solution('hot100',105).buildTree([3,9,20,15,7],[9,3,15,20,7])
        self.assertEqual(solution('hot100',102).levelOrder(built),[[3],[9,20],[15,7]])
        solution('hot100',114).flatten(built);seq=[]
        while built:
            self.assertIsNone(built.left);seq.append(built.val);built=built.right
        self.assertEqual(seq,[3,9,20,15,7])
        self.assertEqual(solution('hot100',437).pathSum(tree([10,5,-3,3,2,None,11,3,-2,None,1]),8),3)
        root=tree([3,5,1,6,2,0,8,None,None,7,4])
        self.assertIs(solution('hot100',236).lowestCommonAncestor(root,root.left,root.left.right.right),root.left)
        self.assertIs(solution('hot100',236).lowestCommonAncestor(root,root.left.left,root.right.right),root)
        self.assertEqual(solution('hot100',124).maxPathSum(tree([-10,9,20,None,None,15,7])),42)
        self.assertEqual(solution('hot100',124).maxPathSum(tree([-3])),-3)

    def test_deep_trees(self):
        root=Node(1);node=root
        for _ in range(2499):
            node.right=Node(1);node=node.right
        self.assertEqual(solution('hot100',104).maxDepth(root),2500)
        self.assertEqual(solution('hot100',543).diameterOfBinaryTree(root),2499)
        self.assertEqual(solution('hot100',124).maxPathSum(root),2500)
        self.assertEqual(solution('hot100',437).pathSum(root,2),2499)
        self.assertIs(solution('hot100',236).lowestCommonAncestor(root,root.right,node),root.right)

    def test_design_classes(self):
        cache=module('hot100',146).LRUCache(2)
        cache.put(1,1);cache.put(2,2);self.assertEqual(cache.get(1),1)
        cache.put(3,3);self.assertEqual(cache.get(2),-1)
        cache.put(4,4);self.assertEqual(cache.get(1),-1)
        self.assertEqual(cache.get(3),3);self.assertEqual(cache.get(4),4)
        cache.put(4,40);self.assertEqual(cache.get(4),40)
        stack=module('hot100',155).MinStack()
        for n in [-2,0,-3]:stack.push(n)
        self.assertEqual(stack.getMin(),-3);stack.pop()
        self.assertEqual(stack.top(),0);self.assertEqual(stack.getMin(),-2)
        trie=module('hot100',208).Trie();trie.insert('apple')
        self.assertTrue(trie.search('apple'));self.assertFalse(trie.search('app'))
        self.assertTrue(trie.startsWith('app'));trie.insert('app');self.assertTrue(trie.search('app'))
        median=module('hot100',295).MedianFinder();median.addNum(1);median.addNum(2)
        self.assertEqual(median.findMedian(),1.5);median.addNum(3);self.assertEqual(median.findMedian(),2)

    def test_n_queens(self):
        boards=solution('hot100',51).solveNQueens(4)
        self.assertEqual(len(boards),2)
        for board in boards:
            cols=[row.index('Q') for row in board]
            self.assertEqual(len(set(cols)),4)
            self.assertEqual(len({i-c for i,c in enumerate(cols)}),4)
            self.assertEqual(len({i+c for i,c in enumerate(cols)}),4)
        self.assertEqual(solution('hot100',51).solveNQueens(1),[['Q']])
        readable=solution('hot100',51).solveNQueensReadable(4)
        self.assertEqual({tuple(board) for board in readable},{tuple(board) for board in boards})
        self.assertEqual(solution('hot100',51).solveNQueensReadable(1),[['Q']])
        step_by_step=solution('hot100',51).solveNQueens1(4)
        self.assertEqual({tuple(board) for board in step_by_step},{tuple(board) for board in boards})
        self.assertEqual(solution('hot100',51).solveNQueens1(1),[['Q']])

    def test_random_against_bruteforce(self):
        rng=random.Random(2026)
        for _ in range(180):
            nums=[rng.randrange(-4,5) for _ in range(rng.randrange(1,12))]
            k=rng.randrange(1,len(nums)+1)
            self.assertEqual(solution('hot100',215).findKthLargest(nums[:],k),sorted(nums)[-k])
            target=rng.randrange(-4,5)
            sums=[sum(nums[i:j]) for i in range(len(nums)) for j in range(i+1,len(nums)+1)]
            self.assertEqual(solution('hot100',560).subarraySum(nums,target),sums.count(target))
            self.assertEqual(solution('hot100',53).maxSubArray(nums),max(sums))
            heights=[abs(x) for x in nums]
            area=max(min(heights[i:j])*(j-i) for i in range(len(nums)) for j in range(i+1,len(nums)+1))
            self.assertEqual(solution('hot100',84).largestRectangleArea(heights),area)
            s=''.join(rng.choice('abc') for _ in range(rng.randrange(1,15)))
            pal=solution('hot100',5).longestPalindrome(s)
            length=max(j-i for i in range(len(s)) for j in range(i+1,len(s)+1) if s[i:j]==s[i:j][::-1])
            self.assertEqual(len(pal),length);self.assertEqual(pal,pal[::-1])
            left=sorted(nums[:k]);right=sorted(nums[k:]);ordered=sorted(nums)
            expected=(ordered[(len(nums)-1)//2]+ordered[len(nums)//2])/2
            self.assertEqual(solution('hot100',4).findMedianSortedArrays(left,right),expected)


def attach_case(row, index, inplace=False):
    identifier,method,args,expected=row
    def check(self):
        local=copy.deepcopy(args)
        result=getattr(solution('hot100',identifier),method)(*local)
        if inplace:result=local[0]
        self.assertEqual(normalize(identifier,result),normalize(identifier,expected))
        if identifier==79:self.assertEqual(local,args,'回溯应恢复棋盘')
    setattr(Hot100Tests,f'test_{identifier:04d}_{index:03d}',check)


for index,row in enumerate(CASES):attach_case(row,index)
for index,row in enumerate(INPLACE):attach_case(row,index+len(CASES),True)
