from copy import deepcopy
n, k = map(int, input().split())
safe = list(map(int, input().split()))
people = []
for _ in range(n):
    people.append(0)
turn = 0

def is_Finished():
    cnt = 0
    for i in range(len(safe)):
        if safe[i] <= 0:
            cnt += 1
    if cnt >= k:
        return True
    else:
        return False

def move_moving_walk():
    a = safe.pop()
    safe.insert(0, a)
    b = people.pop()
    people.insert(0, b)

def move_people():
    
    for i in range(len(people)-2, -1, -1):
        if people[i] == 1 and people[i+1] == 0 and safe[i+1] > 0:
            people[i+1] = 1
            safe[i+1] -= 1
            people[i] = 0
        # if (i + 1) == len(people) - 1 and people[i+1] == 1:
        #     people[i+1] = 0
    # people = test_people
    if people[-1] == 1:
        people[-1] = 0

def add_people():
    if people[0] == 0 and safe[0] > 0:
        people[0] = 1
        safe[0] -= 1

while 1:
    if is_Finished() == True:
        print(turn)
        break
    turn += 1
    move_moving_walk()
    move_people()
    add_people()