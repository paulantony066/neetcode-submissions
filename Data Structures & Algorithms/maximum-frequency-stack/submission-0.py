class FreqStack:

    def __init__(self):
        self.stck={

        }
        self.index=0

        

    def push(self, val: int) -> None:

        self.index+=1

        if val in self.stck:
            self.stck[val]["index"].append(self.index)
            self.stck[val]["freq"]+=1
        else:
            self.stck[val]={"index":[self.index],"freq":1}
        

    def pop(self) -> int:
        best_val = None
        max_freq = 0
        latest_idx = -1

        for val, data in self.stck.items():
           
            if data["freq"] > max_freq or (
                data["freq"] == max_freq and data["index"][-1] > latest_idx
            ):
                max_freq = data["freq"]
                latest_idx = data["index"][-1]
                best_val = val

        
        self.stck[best_val]["index"].pop()
        self.stck[best_val]["freq"] -= 1
        if self.stck[best_val]["freq"] == 0:
            del self.stck[best_val]

        return best_val
                
                 

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()