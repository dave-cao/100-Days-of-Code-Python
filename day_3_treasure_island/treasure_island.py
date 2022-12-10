# A choose your own adventure game that uses if/else statements to
# decide your fate
print(
    """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ : : : : : : : : : : : : : : : @
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 |                             |
 |  \|/        %%%        \|/  |
 |  -t-     %%%%%%%%%     -t-  |
 |  /|\     \  %%%  /     /|\  |
 |         \ / %%% \ /         |
 \        - |  %%%  | -        /
  \       - |  %%%  | -       /
   \       / \     / \       /
    \        / --- \        /
     \         ! !         /
      \ __ ___ __ ___ ___ /
      ( ___ ___ __ _ ___  )
       (88888888888888888)
        --\ --------- /--
          ((((((o))))))
           \         /
            | | | | |
            | | | | |
            | | | | |
            | | | | |
            | | | | |
            | | | | |
            | | | | |
            | | | | |
          _(IIIIIIIII)_
       __/_____________\__
  ____/___________________\____
 /_____________________________\
(_______________________________)
"""
)

print("Welcome to Treasure Island.\n Your mission is to find the treasure")

choice1 = input("left or right? ")


end_game = False
while not end_game:
    if choice1 == "right":
        print("Fall into hole. Game Over")
        end_game = True
        break

    choice2 = input("swim or wait? ")
    if choice2 == "swim":
        print("Attacked by trout. Game Over")
        end_game = True
        break

    choice3 = input("Which door? red, blue, yellow")
    if choice3 == "red":
        print("Burned by fire. Game Over")
        end_game = True
        break
    if choice3 == "blue":
        print("Eaten by beasts. Game Over")
        end_game = True
        break

    if choice3 == "yellow":
        print("You Win! ")
        end_game = True
        break
