print('''

                                                    ____
                                         v        _(    )
        _ ^ _                          v         (___(__)
       '_\V/ `
       ' oX`
          X                            v
          X             -HELP!
          X                                                 .
          X        \O/                                      |\
          X.a##a.   M                                       |_\
       .aa########a.>>                                    __|__
    .a################aa.                                 \   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

print("You wake up at an mysterious Island. Find a way to escape")
print("You have two paths, Left and Right. The left looks Bushy and the right looks muddy")
first_path = input('you\'re to choose between "Left" or "Right": ').lower()

if first_path == "left":
    print("You Tried to walk on quicksand and died.")
    print("Game Over.")
elif first_path == "right":
    print("You observe some dangerous looking cannibal tribes coming towards ur path.")
    print("Do u want to run away or hide in the bushes.")
    sec_path = input('you\'re to choose between "Run" or "Hide": ').lower()


    if sec_path == "hide":
        print("You been caught by the cannibals as they noticed u hide.")
        print("Game Over.")
    elif sec_path == "run":
        print("You ran away from the cannibals.")
        print("You see a plane coming towards the island and also that there is a boat that is slowly drifting away from the island.")
        third_path = input('you\'re to choose between "Boat" or "SOS": ').lower()


        if third_path == "sos":
            print("You failed. You made a SOS sign but plane never noticed the SOS and the boat drifted away from the island.")
            print("Game Over.")
        elif third_path == "boat":
            print("You caught the boat and escaped from the island")
            print("You Escaped!.")
        else:
            print("Please choose a valid option")
    else:
        print("choose a valid option.")
else:
    print("Choose a valid option.")
