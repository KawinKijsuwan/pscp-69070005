"""หวยก็ไม่ถูก"""
reward_a,reward_num = input().split()
user_a,user_num = input().split()
reward = 0

if reward_a == user_a and reward_num == user_num:
    reward = 1000000
elif reward_num == user_num:
    reward = 100000
elif reward_num[-3:] == user_num[-3:] and reward_a == user_a:
    reward = 2000
elif reward_num[-2:] == user_num[-2:] and reward_a == user_a:
    reward = 1000
elif reward_num[-3:] == user_num[-3:]:
    reward = 200
elif reward_num[-2:] == user_num[-2:]:
    reward = 100
elif reward_a == user_a:
    reward = 20
else:
    reward = 0
print(reward)
