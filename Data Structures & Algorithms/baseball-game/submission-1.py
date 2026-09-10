class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]

        for i in range(len(operations)):
            ch=operations[i]

            if ch=="+":
                num1=stack[-1]
                num2=stack[-2]
                stack.append(num1+num2)
            elif ch=="C":
                stack.pop()
            elif ch=="D":
                prev=stack[-1]
                stack.append(prev*2)
            else:
                stack.append(int(ch))
        return sum(stack)