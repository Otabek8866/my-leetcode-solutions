
class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        while self.queue:
            self.extra.append(self.queue.pop())
        self.queue.append(x)
        while self.extra:
            self.queue.append(self.extra.pop())
        return None

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return False if len(self.queue) else True
