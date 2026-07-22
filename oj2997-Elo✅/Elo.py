"""Elo"""
def main():
    """main"""
Ra = int(input())
Rb = int(input())
Elo = input()
EA = 1 / (1 + 10 ** ((Rb - Ra) / 400))
EB = 1 / (1 + 10 ** ((Ra - Rb) / 400))
if Elo == "A":
    print(f"{EA:.2f}")
else:
    print(f"{EB:.2f}")
main()
