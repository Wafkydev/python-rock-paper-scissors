import random

computer = random.randint(1, 3)

print("""
==============
Rock Paper Scissors
==============
""")

player = int(input("""1) ✊
2) ✋
3) ✌️
Pick a number: """))

print()  # blank line

# Show player's choice
if player == 1:
    print("You chose: ✊")
elif player == 2:
    print("You chose: ✋")
elif player == 3:
    print("You chose: ✌️")

# Show CPU's choice
if computer == 1:
    print("CPU chose: ✊")
elif computer == 2:
    print("CPU chose: ✋")
elif computer == 3:
    print("CPU chose: ✌️")

print("\n--------------------\n")

# Determine winner
if player == computer:
    print("🤝 Tie!")
elif player == 1 and computer == 3:
    print("🎉 The player won!")
elif player == 2 and computer == 1:
    print("🎉 The player won!")
elif player == 3 and computer == 2:
    print("🎉 The player won!")
else:
    print("💻 The CPU won!")