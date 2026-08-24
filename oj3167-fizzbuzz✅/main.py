"""fizz buzz"""
n = int(input())
for _ in range(1,n+1):
    if not _ % 3  and not _ % 5:
        print("FizzBuzz")
    elif not _ % 3:
        print("Fizz")
    elif not _ % 5:
        print("Buzz")
    else:
        print(_)
 