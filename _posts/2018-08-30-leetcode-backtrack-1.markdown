---
layout: post
title: LeetCode中求子集、全排列等问题的回溯算法总结
---

LeetCode中有关寻找数组的子集问题（78，90）、全排列（46，47）、在数组中找出等于固定值元素的集合（39，40），可以使用回溯法进行求解。

#### **回溯法**
回溯算法实际上是一个类似枚举的搜索尝试过程，在搜索尝试中寻找问题的最优解，当发现已不满足求解条件时就“回溯”，尝试别的路径。

回溯法是一种优选搜索法，按选优条件向前搜索，以达到目标。但当探索到某一步时，发现原选择并不优或达不到目标，就退回一步重新选择，这种走不通就退回再走的技术称为回溯法，满足回溯条件的某个状态点称为“回溯点”。

许多复杂的，规模较大的问题都可以使用回溯法，回溯法是五大常用算法之一。

##### **基本思想**
在包含问题的所有解的解空间树中，按照**深度优先搜索的策略**，从根节点出发深度搜索解空间树。当探索到某一结点时，先判断该结点是否包含问题的解，如果包含，就从该结点出发继续探索下去，如果该结点不包含问题的解，则逐层向其祖先结点回溯。

若用回溯法求问题的所有解时，要回溯到根，且根结点的所有可行的子树都要被搜索遍才结束。

而若使用回溯法求任一个解时，只要搜索到问题的一个解就可以结束。

##### **解题步骤**
1.&nbsp针对给定问题，确定问题的解空间，即首先明确问题的解空间，问题的解空间应至少包含问题的一个（最优）解
2.&nbsp确定结点的扩展搜索规则
3.&nbsp以深度优先的方式搜索解空间，并在搜索过程中使用剪枝函数避免无效搜索

##### **算法框架**
1.&nbsp非递归回溯框架
```cpp
int a[n], i; //初始化数组a[];
i = 1;
while(i > 0(有路可走) and (未达到目标)) //还未回溯到头
{
    if(i > n) //搜索到叶结点
    {   
	    搜索到一个解，输出；
    }
    else //处理第i个元素
    {
        a[i]第一个可能的值；
        while(a[i]在不满足约束条件且在搜索空间内)
        {
            a[i]下一个可能的值；
        }
        if(a[i]在搜索空间内)
        {
             标识占用的资源；
             i = i + 1; //扩展下一个结点
        }
        else
        {
             清理所占的状态空间; //回溯
             i = i – 1;
	    }
    }
}

```
2.&nbsp递归回溯框架
回溯法是对解空间的深度优先搜索，在一般情况下使用递归函数来实现回溯法比较简单，其中i为搜索深度，框架如下：
```cpp
int a[n];
try(int i)
{
    if(i > n)
	    输出结果;
    else
    {
		for(j = 下界; j <= 上界; j = j + 1) //枚举i所有可能的路径
        {
	        if(fun(j)) //满足限界函数和约束条件
            {
	            a[i] = j;
                ...  // 其他操作
                try(i + 1);
                回溯前的清理工作（如a[i]置空值等）;
             }
        }
	}
}
```

##### **LeetCode解题过程**
**78.&nbspSubset**

Given a set of **distinct** integers, nums, return all possible subsets (the power set).

**Note:** The solution set must not contain duplicate subsets.

**Example:**
```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

**Solution:**
```java
class Solution {
	public List<List<Integer>> subsets(int[] nums) {
		List<List<Integer>> list = new ArrayList<>();
		backTrack(list, new ArrayList<Integer>(), nums, 0);
		return list;
	}
	
	public void backTrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int start) {
		list.add(new ArrayList<>(tempList));
		for (int i = start; i < nums.length; i++) {
			tempList.add(nums[i]);
			backTrack(list, tempList, nums, i + 1);
			tempList.remove(tempList.size() - 1);
		}
	}
}
```

**90.&nbspSubsets II**
Given a collection of integers that might contain duplicates, **nums**, return all possible subsets (the power set).

**Note:** The solution set must not contain duplicate subsets.

**Example:**
```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```
**Solution:**
```java
class Solution {
	public List<List<Integer>> subsetWithDup(int[] nums) {
		Arrays.sort(nums);
		List<List<Integer>> list = new ArrayList<>();
		backTrack(list, new ArrayList<Integer>(), nums, 0);
		return list;
	}

	public void backTrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int start) {
		list.add(new ArrayList<>(tempList));
		for (int i = start; i < nums.length; i++) {
			if (i > start && nums[i] == nums[i - 1])
				continue;
			tempList.add(nums[i]);
			backTrack(list, tempList, nums, i + 1);
			tempList.remove(tempList.size() - 1);
		}
	}
}
```

**46.&nbspPermutations**
Given a collection of **distinct** integers, return all possible permutations.

**Example:**
```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```
**Solution:**
```java
class Solution {
	public List<List<Integer>> permute(int[] nums) {
		List<List<Integer>> list = new ArrayList<>();
		backTrack(list, new ArrayList<Integer>(), nums);
		return list;
	}

	public void backTrack(List<List<Integer>> list, List<Integer> tempList, int[] nums) {
		if (tempList.size() == nums.length)
			list.add(new ArrayList<>(tempList));
		else {
			for (int i = 0; i < nums.length; i++) {
				if (tempList.contains(nums[i]))
					continue;
				tempList.add(nums[i]);
				backTrack(list, tempList, nums);
				tempList.remove(tempList.size() - 1);
			}
		}	
	}
}
```

**47.&nbspPermutations II**
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

**Example:**
```
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```
**Solution:**
```java
class Solution {
	public List<List<Integer>> permuteUnique(int[] nums) {
		Arrays.sort(nums);
		List<List<Integer>> list = new ArrayList<>();
		backTrack(list, new ArrayList<Integer>(), nums, new boolean[nums.length]);
		return list;
	}

	public void backTrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, boolean[] used) {
		if (tempList.size() == nums.length)
			list.add(new ArrayList<>(tempList));
		else {
			for (int i = 0; i < nums.length; i++) {
				if(used[i] || i > 0 && nums[i] == nums[i - 1] && !used[i - 1])
					continue;
				tempList.add(nums[i]);
				used[i] = true;
				backTrack(list, tempList, nums, used);
				used[i] = false;
				tempList.remove(tempList.size() - 1);
			}
		}	
	}
}
```



