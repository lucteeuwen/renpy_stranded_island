label Chapter2:
    scene bg island
    "Chapter 2"
    if gender == "m":
        show male basic
    "[player], you're on a deserted island and have to survive"
    "You will have the following choices which will be critical for your survival"
    if gender == "m":
        hide male basic
    menu:
        "Are you going to panic?":
            jump choice_panic
        "Are you going to cry?":
            jump choice_cry
        "Are you going to start doing some work?":
            jump choice_work

    #Decided to panic
    label choice_panic:
        if gender == "m":
            show male basic
        "You decided to panic [player]. That's an interesting choice."
        "5 minutes later."
        "You are starting to freak out and as you freak out you slam into a tree and break your arm!"
        "You just passed out."
        "5 hours later."
        "You just woke up and look at what you just encountered yourself with..."
        "A wild bear! I wish you good luck [player]."
        jump death

    #Decided to cry
    label choice_cry:
        if gender == "m":
            show male cry
        "You decided to cry [player]. That's very understandable. But will it help you survive?"
        "Your crying is becoming louder. Maybe you should stop. You could attract wild animals."
        "Are you going to stop crying?"
        if gender == "m":
            hide male cry
        menu:
            "Yes! I will get to work.":
                jump choice_work
            "No! I can't stop crying.":
                if gender == "m":
                    show male cry
                "Your crying will not help you. Didn't you realize there where bears on this island?"
                "Look there you have one. But don't stress..."
                "Well guess it's too late you allready died of fear. I wanted to tell you that these bears are not actually agresive."
                jump death


    label choice_work:
        if gender == "m":
            show male basic
        "You are going to start working, that's a great choice!"
        "Now you're going to start finding coconuts to to feed yourself. You have found a tree and you start climbing up to grab the coconuts."
        "When on top of the tree, you also find a sharp stick. What are you going to do with it?"
        menu:
            "I will grab the sharp stick.":
                jump choice_grab_stick
            "I will not grab the sharp stick.":
                jump choice_no_stick

    label choice_grab_stick:
        "You have grabbed the sharp stick too. That's a great choice!"
        "Now, as you try to go down the tree, you loose your grip and fall. With your fall you have made a lot of noise and you have attracted a bear."
        "But it doesn't matter because you have a sharp stick which will allow you to kill the bear. "
        jump Chapter3

    label choice_no_stick:
        "You didn't grab the stick. Maybe that wasn't the best choice."
        "As you try to go down the tree, you loose your grip and fall. You have made a lot of noise and you have attracted a bear."
        "Now how are you going to protect yourself? I think the bear is going to kill you."
        jump death

jump Chapter3
