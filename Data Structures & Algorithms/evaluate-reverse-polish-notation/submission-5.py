class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        res=0

        for i in range(len(tokens)):
            if tokens[i] not in "*+/-":
                stack.append(int(tokens[i]))
            else:
                op2=stack.pop()
                if len(stack)==0:
                    return -1
                op1=stack.pop()

                if tokens[i]=="+":
                    res=op1+op2
                elif tokens[i]=="-":
                    res=op1-op2
                elif tokens[i]=="*":
                    res=op1*op2
                elif tokens[i]=="/":
                    res=int(op1/op2)
                stack.append(res)
        return stack[-1]