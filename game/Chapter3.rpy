label Chapter3:
    "Chapter 3"
    "with the new food and coconut you survive for a few days"
    "you suddenly decide to create a house... "
    "one day you see a ship on the horizon. a chance of survival..."
    menu:
        "burn the trusty stick":
            jump burn_stick
        "yell louder":
            jump yell_loud
        "cry by yourself":
            jump cry_by_yourself


label burn_stick:
    "the mother bear sees that you dont have a weapon anymore and eats you"
    jump death
label yell_loud:
    "you yell hard and your throat gets dry."
    "so you try to drink some water"
    "but the bear has heared you "
    "the bear eats you while you where drinking water"
    jump death
label cry_by_yourself:
        "you choose to cry while sitting bellow a three"
        "you cry so much you get dehydration "
        "you drink coconut water"
        "you dont get saved"
        "but next day some guy comes with a plane and rescues you"
        "you SURVIVED "
