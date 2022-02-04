label Chapter1:
    "Chapter 1"
    "[player], You wake up from a nap on the airplane because of a loud thud"
    "You notice that people have started to panic and you look around to figure out why"
    "The panic level starts to escelate and you finally look out the window of the plane and realize what is going on"
    "The Left engine has completley burnt off, leaving you in a dicy situation"
    "You only have a few seconds to grab something or someone as the plane starts to go down"
    menu:
        "Your Newborn Baby":
            jump choice_baby
        "Your Wife who is bleeding from her head":
            jump choice_wife
        "A random seat cushion":
            jump choice_cushion
        "A life jacket":
            jump choice_lifejacket

    #Grabbed the Baby
    label choice_baby:
        "You have decided to save your Newborn child"
        "That is what most parents would do no?"
        "Well that was a bad choice as it won't help you survive"
        jump death

    #Grabbed the wife
    label choice_wife:
        "You have decided that your wife is more important than your child"
        "Well that isn't good parenting now is it"
        "Well anyways it was the wrong choice as it won't help you survive"
        jump death

    #Grabbed a seat cushion
    label choice_cushion:
        "So you have decided to leave your wife and your child on the plane"
        "You were probably a terrible parent anyway"
        "But somehow it was the right choice"
        jump Chapter2

    #Grabbed life jacket
    label choice_lifejacket:
        "So your Wife and Newborn are useless are they?"
        "Well even when leaving your family to die you still chose the wrong thing"
        "You Need to be more compasionate"
        jump death
jump Chapter2
