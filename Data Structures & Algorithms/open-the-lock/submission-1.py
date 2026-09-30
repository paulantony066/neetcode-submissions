class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        

        curr="0000"

        stck=deque()


        dead=set(deadends)

        if curr in deadends:
            return -1
        visited=set()

        stck.append(curr)
        moves=0

        while stck:

            for _ in range(len(stck)):

                state=stck.popleft()
                if state==target:
                    return moves

                nexts=[]
                for i in range(4):
                    dig=int(state[i])
                    num1=(1+dig)%10
                    num2=(dig-1)%10

                    newnum1=state[:i]+str(num1)+state[i+1:]
                    newnum2=state[:i]+str(num2)+state[i+1:]

                    if newnum1 not in visited and newnum1 not in dead:
                        stck.append(newnum1)
                        visited.add(newnum1)
                    if newnum2 not in visited and newnum2 not in dead:
                        stck.append(newnum2)
                        visited.add(newnum2)
            moves+=1
        return -1
                    

                

