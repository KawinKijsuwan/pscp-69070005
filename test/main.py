s = input().strip()
s_lower = s.lower()

max_u = 0
for i in range(len(s_lower)):
    if s_lower[i] == 'b':
        j = i + 1
        count = 0
        while j < len(s_lower) and s_lower[j] == 'u':
            count += 1
            j += 1
        if count >= 2 and count > max_u:
            max_u = count

if max_u > 0:
    print(f"Yes {max_u}")
elif 'b' in s_lower:
    b_idx = s_lower.index('b')
    print(s[:b_idx + 1] + 'U' * (len(s) - b_idx - 1))
else:
    print(("BUU" * len(s))[:len(s)])
    