class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        q = self._queue
        q.append(x)
        for i in range(len(q)-1):
            q.append(q.pop())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self._queue.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._queue[-1] if self._queue else None

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self._queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()