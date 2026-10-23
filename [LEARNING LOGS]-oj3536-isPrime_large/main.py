"""isPrime"""
number = int(input())

if number < 2:
    print("NO")
elif number == 2:
    print("YES")
elif not number % 2:
    print("NO")
else:
    prime = True
    i = 3
    while i * i <= number:
        if not number % i:
            prime = False
            break
        i += 2

    if prime:
        print("YES")
    else:
        print("NO")
