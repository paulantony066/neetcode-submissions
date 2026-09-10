class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stck=[]
        for ch in tokens:
            if ch in "+-/*":
                num2=stck.pop()
                num1=stck.pop()
                if ch=="+":
                    stck.append(num1+num2)
                elif ch=="*":
                    stck.append(num1*num2)
                elif ch=="-":
                    stck.append(num1-num2)
                else:
                    stck.append(int(num1/num2))
            else:
                stck.append(int(ch))
                
                        
        return stck[-1]