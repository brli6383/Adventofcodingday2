
file = open('2021day1.py' , 'r')

horizontal = 0; depth = 0

for line in file:
    coordinate = int(line)
    if direction == "forward":
        horizontal += coordinate
    if direction == "down":
        depth += coordinate
    if direction == "up":
        depth -= coordinate

        print("answer",(horizontal * depth))
        # print(depth)
        # print(horizontal)