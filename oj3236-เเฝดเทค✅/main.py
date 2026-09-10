"""เเฝดเทค"""
size = int(input())
student1 = input()
student2 = input()
count = 0

for i in range(size):
    if int(student1[i]) + int(student2[i]) != 9:
        count += 1

if not count:
    print("YES")
else:
    print(f"NO {count}")
