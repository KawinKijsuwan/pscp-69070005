"""โรงแรมกลางกรุง ไม่มีชั้น 13"""
room = input()
n1 = ""
n2 = ""
n3 = ""
if int(room[0]) > 5:
    n1 = "9"
elif int(room[1]) > 5:
    n1 = "10"
elif int(room[2]) > 5:
    n1 = "11"
elif int(room[3]) > 5:
    n1 = "12"
elif int(room[4]) > 5:
    n1 = "14"
else:
    n1 = "13"

is_palindrome = room == room[::-1]
if is_palindrome:
    if int(room[0]) + int(room[4]) > 5:
        n2 = "1"
    elif int(room[1]) * int(room[3]) > 5:
        n2 = "2"
    else:
        n2 = "0"
else:
    if int(room[4]) and int(room[0]) // int(room[4]) > 5:
        n2 = "1"
    elif int(room[1]) - int(room[4]) > 5:
        n2 = "2"
    else:
        n2 = "0"

if int(room[0]) + int(room[1]) + int(room[2]) + int(room[3]) + int(room[4]) > 25:
    n3 = "1"
elif int(room[0]) * int(room[1]) * int(room[2]) * int(room[3]) * int(room[4]) > 55:
    n3 = "2"
else:
    n3 = "0"
print(f"{n1}{n2}{n3}")
