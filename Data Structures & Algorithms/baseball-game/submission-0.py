class Solution:
    def calPoints(self, operations: List[str]) -> int:

        temp = []

        for op in operations:
            if op == "C":
                temp.pop()
            elif op == "D":
                temp.append(temp[-1]*2)
            elif op == "+":
                temp.append(temp[-1] + temp[-2]) 
            else:
                temp.append(int(op))
        
        return sum(temp)
        