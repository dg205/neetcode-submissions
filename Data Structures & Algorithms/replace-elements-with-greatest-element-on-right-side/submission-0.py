class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            
            greatest = max(arr[i + 1:])  # works, but creates
            arr[i] = greatest
        arr[-1] = -1
        return arr