class MinStack:
    """
    Two stacks: my_list for all values, min_list tracks running minimums.
    Push to min_list only when new value <= current min (handles duplicates).
    Pop from min_list only when the popped value was the current min.
    All operations O(1) time, O(n) space worst case.
    """

    def __init__(self):
        self.my_list = []
        self.min_list = []

    def push(self, value: int) -> None:
        self.my_list.append(value)

        if not self.min_list or value <= self.min_list[-1]:
            self.min_list.append(value)

    def pop(self) -> None:
        if self.my_list.pop() == self.min_list[-1]:
            self.min_list.pop()

    def top(self) -> int:
        return self.my_list[-1]

    def getMin(self) -> int:
        return self.min_list[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
