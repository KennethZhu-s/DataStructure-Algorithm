from collections import deque

# q = deque([1,2,3], 3)
# q.append(4)    # rear push
# print(q.popleft())  # front pop

# dequeue
# q.appendleft(1) # front push
# q.pop()     # rear pop

def tail(n):
    with open('te.txt', 'r') as f:
        q = deque(f, n)
        return q

for line in tail(5):
    print(line, end='')

