
report = list(map(int, open('day1.txt', 'r')))

count = 0

for x in range(len(report)-1):
    if report[x+1] > report[x]:
        count += 1

print(count)


for x in range(3,len(report)):
    a = report[x-3] + report[x-2] + report[x-1]
    b = report[x] + report[x-1] + report[x-2]
    if a < b:
        count += 1
    

print(count)