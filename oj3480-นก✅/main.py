"""นก"""
def main():
    """main"""
    n = int(input())
    heights = [int(x) for x in input().split()]

    count = 0
    for i in range(n):
        left = 0
        right = 0
        if i > 0:
            left = heights[i - 1]
        if i < n - 1:
            right = heights[i + 1]

        if heights[i] > left and heights[i] > right:
            count += 1

    print(count)


main()
