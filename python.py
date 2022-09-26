#   Greeting the user who is playing my game
print ("Welcome to my first game")
print ("-----------------")
name = input("What is your name? ")
age = input("What is your age? ")
#   print the user's details
print("Hello", name, "you are", age, "years old")
#  confirm the user is old enough to play
if  int(age) >= 18:
    print("You are old enough to play")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("let's play")
        #   set the users health points
        health = 10
        print("You start with 15 hp")
        #   give the user multiple choices
        left_or_right = input("First choice... left or right (left/right)? ")
        if left_or_right == "left":
            ans = input("You reach a lake... (swim/around): ")

            if ans == "across":
                print("you safely made it across the bridge")
            elif ans == "around":
                print("You were bit by a dangerous fish - you lose 5 hp")
                #   Here the user takes -5 dmg
                health -= 5

                ans = input("you notice a house and a river which do you go to? (river/house): ")
                if ans == "house":
                    #   Here the user takes -5 dmg
                    print("you go to the house and were attacked by a ghoul ... you lose 5 hp")
                    health -= 5
                    #   if the user has lost -10 health the game will end here
                    if health <= 0:
                        print("You now have 0 health game over")
                    else:
                        print("you have survived, game over!")

                else:
                    print ("game over")

            else:
                print("you lost")

        else:
            print("you became lost in the woods")
    else:
        print("invalid input")
else:
    print("you are not old enough to play")
