import random
que = []
for i in range(0,10):
    que.append(random.randint(0,100))

print(que)

for i in que:
    while len(que) > 0:
      num = que.pop(0)
      print('current number is {} and the que is {}'.format(num,que))
    