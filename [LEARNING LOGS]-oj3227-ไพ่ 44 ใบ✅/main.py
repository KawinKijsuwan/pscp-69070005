"""ไพ่44ใบ"""
user_input = input().upper()

suit = {
    "D" : "diamonds",
    "H" : "hearts",
    "S" : "spades",
    "C" : "clubs"
}
face = {
    "A" : "ace",
    "J" : "jack",
    "Q" : "queen",
    "K" : "king"
}

rank = user_input[:-1]
suit_code = user_input[-1]

suit_name = suit[suit_code]
rank_name = face.get(rank, rank)

print(f"{rank_name} of {suit_name}")
