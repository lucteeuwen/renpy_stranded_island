label Chapter2:
    "Chapter 2"
    "[player], you're on a deserted island and have to survive"
    "You will have the following choices which will be critical for your survival"
    menu:
        "Are you going to panic?":
            jump choice_panic
        "Are you going to cry?":
            jump choice_cry
        "Are you going to start doing some work?":
            jump choice_work

    #Decided to panic
    label choice_panic:
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
        "You decided to cry [player]. That's very understandable. But will it help you survive?"
        "Your crying is becoming louder. Maybe you should stop. You could attract wild animals."
        "Are you going to stop crying?"
        menu:
            "Yes! I will get to work.":
                jump choice_work
            "No! I can't":
                "Your crying will not help you. Didn't you realize there where bears on this island?"
                "Look there you have one. But don't stress..."
                "Well guess it's too late you allready died of fear. I wanted to tell you that these bears are not actually agresive."
                jump death


    label choice_work:
        "You will survive"

jump Chapter3
