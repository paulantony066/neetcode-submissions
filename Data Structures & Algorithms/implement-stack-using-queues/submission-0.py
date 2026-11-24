class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        for _ in range(len(self.q2)-1):
            self.q2.append(self.q2.popleft())

    def pop(self) -> int:
        return self.q2.popleft()

    def top(self) -> int:
        return self.q2[0]

    def empty(self) -> bool:
        return len(self.q2) == 0