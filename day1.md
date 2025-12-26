**Day 1**
1. Leetcode 26 删除有序数组的重复项
- 重述题目：删除重复出现的数组，使每个元素只出现一次，得到不含重复元素的长度，注意元素的相对顺序不变
- 分析：注意这里是已经整理好顺序的数组，我们选择构建两指针，a指针用于读取数组中的每一个数据，b指针用于记录有效数组
- Python
```python
class Solution:
    def removeDuplicates(self,nums:List[int])->int:
        b = 0
        for a in range(len(nums)):
            if a==0 or nums[a] != nums[a-1]:
              nums[b] = nums[a]
              b+=1
        return b  
```
- Java
```java
class Solution{
    public int removeDuplicates(int[] nums){
        int b = 0;
        for (int a=0;a<len(nums);a++){
            if (nums[a] == 0 || nums[a]!=nums[a-1]){
                nums[b] = nums[a];
                b++;
            }
        }
        return b;
    }
}
```

2. Leetcode 27 移除元素
   和上面的思路一样都是先建立俩指针，一个指针用于遍历，另外一个指针用于重新赋值数组，用索引的当前序号来判断序列长度。
- python
```python
class Solution:
    def removeElement(self,nums:List[int],val:int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j+=1
        return j 
```
- java  
```java
class Solution{
    public int removeElement(int[] nums,val:int){
        int j = 0;
        for (int i = 0;i<=len(nums);i++){
            if nums[i] != val{
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
    }
}
```

3. Leetcode 283 移动零
- java
```java
class Solution{
    public void moveZeros(int[] nums){
        int slow = 0;
        for (fast = 0;fast <nums.length;fast++){
          if (nums[fast] != 0){
            nums[slow] = nums[fast];
            slow++;
          }  
        }
        for(int i = slow;i<nums.length;i++){
            nums[i]=0;
        }
    }
}
```
- python
```python
class Solution:
    def moveZeros(self,nums:List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] !=0:
                nums[slow] = nums[fast]
                slow += 1
        for i in range(slow,len(nums)):
            nums[i] = 0
```

4. Leetcode 485:最大连续1的个数
- python
``` python
class Solution:
    def moveZeros(self,nums):
        lastZeros = -1
        ans = 0
        for i,num in enumerate(nums):
            if nums[i] = 0:
                lastZeros = i
            else:
                ans = max(ans,i-lastZeros)
        return ans
```
```java
class Solution{
    public int movezeros(int[]nums){
        int lastZeros = -1;
        int ans = 0;
        for (int i=0;i<nums.length;i++){
            if nums[i] = 0{
                lastZeros = 1;
            }else{
                ans = Math.max(ans,i-lastZeros);
            }
        }
        return ans;
    }
}
```