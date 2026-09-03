"""สินค้าส่งออก"""
total_sum = 0
even_count = 0
odd_count = 0
N = int(input())
for _ in range(N):
    stock = int(input())
    total_sum = total_sum + stock
    if not stock % 2:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print("SUM",total_sum)
print("EVEN",even_count)
print("ODD",odd_count)
