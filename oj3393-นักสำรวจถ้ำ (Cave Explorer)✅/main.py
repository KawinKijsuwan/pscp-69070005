"""นักสำรวจถ้ำ (Cave Explorer)"""
n = int(input())
c = input().split()
s = input().strip()

p = 0
while p < n:
    if c[p] == "1":
        break
    p = p + 1

i = 0
while i < len(s):
    cmd = s[i]
    nxt = p
    if cmd == "R":
        nxt = p + 1
    elif cmd == "L":
        nxt = p - 1

    if nxt >= 0:
        if nxt < n:
            got = c[nxt] == "2"
            c[p] = "0"
            c[nxt] = "1"
            p = nxt
            if got:
                break
    i = i + 1

print(" ".join(c))
