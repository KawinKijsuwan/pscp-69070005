"""ไพ่44ใบ"""
user_input = input().upper()

suit = {
    "D" : "Diamonds",
    "H" : "Hearts",
    "S" : "Spades",
    "C" : "Clubs"
}
face = {
    "A" : "Ace",
    "J" : "Jack",
    "Q" : "Queen",
    "K" : "King"
}

rank = user_input[:-1]
suit_code = user_input[-1]

suit_name = suit[suit_code]
rank_name = face.get(rank, rank)

print(f"{rank_name} of {suit_name}")
