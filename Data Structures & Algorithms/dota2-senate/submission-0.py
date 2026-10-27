class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        qr=deque()
        qd=deque()

        for i in range(len(senate)):
            if senate[i]=='R':
                qr.append(i)
            if senate[i]=='D':
                qd.append(i)
        
        while qd and qr:
            r=qr.popleft()
            d=qd.popleft()

            if r<d:
                qr.append(r+len(senate))
            else:
                qd.append(d+len(senate))
        if qd:
            return "Dire"
        return "Radiant"



