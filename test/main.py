def main():
    user_id = input()
    first_4 = user_id[0:4]
    last_4 = user_id[4:]
    if str(first_4) == "6807" and 1 <= int(last_4) <= 328:
        print("Pass")
    else:
        print("Not Pass")
main()
