class Stack:
    def __init__(self, cap):
        self.cap = cap
        self.top = -1
        self.a = [0] * cap

    def push(self, x):
        if self.top == self.cap - 1:
            print("overflow")
            return False
        self.top += 1
        self.a[self.top] = x
        return True

    def pop(self):
        if self.top == -1:
            print("underflow")
            return None
        popped = self.a[self.top]
        self.top -= 1
        return popped

    def peek(self):
        if self.top == -1:
            print("stack is empty")
            return -1
        return self.a[self.top]

    def is_empty(self):
        return self.top == -1


# -----------------
S = Stack(5)
S.push(1)
S.push(2)
S.push(3)

print("Top element:", S.peek())   # Should print 3

print("Stack elements:")
while not S.is_empty():
    print(S.peek())   # print top element
    S.pop()           # remove top element
