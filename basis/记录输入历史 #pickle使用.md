### deque  pickle
```
from collections import deque
import pickle


N = randint(0, 100)
q = deque([], 5)
def guess(N, U):
    if U == N:
        print('you are right')
        return True
    elif U < N:
        print('the number is less than N')
    elif U > N:
        print('the numger is larger than N')

    return False

while True:
    user_input = input('please input your number:\n')
    if user_input.isdigit():
        q.append(user_input)
        if guess(N, int(user_input)):
            break
    elif user_input == 'history' or user_input == 'h?':
        print(list(q))
        print(tuple(q))

pickle.dump(q,open('history.txt','w'))
pickle.load(q,open('history.txt'))
```