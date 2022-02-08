label harel:
    "Would you like to play as a boring defualt?"
    menu:
        "Yes":
            jump Chapter1

        "No":
            jump choose_player

    label choose_player:
        $ player = renpy.input("What is your name?")
        if player == "Shuarya":
            jump death
        if player == "Parsa":
            "You're a fuckin gamer"
            jump death

        "What gender are you?"
        menu:
            "Male":
                $ gender = "m"
            "Female":
                $ gender = "f"
        jump Chapter1
