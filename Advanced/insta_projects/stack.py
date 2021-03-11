stack = []
for i in range(5):
    stack.append(i)
    # print("Stack =>",stack)
print("Stack =>", stack)
print("stack.pop() =>", stack.pop())
print("Current stack =>", stack)
#Get number at the top without removing it
print("stack.peek() or stack[-1] =>", stack[-1])
print("Current stack =>", stack)