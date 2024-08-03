class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        max_val = 1001 
        count_target = [0] * max_val
        count_arr = [0] * max_val
        for num in target:
            count_target[num] += 1
        for num in arr:
            count_arr[num] += 1
        for i in range(max_val):
            if count_target[i] != count_arr[i]:
                return False

        return True
        