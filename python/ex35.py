from sys import exit

def gold_room():
    print "this room is full of gold. How much do you take"

    next = raw_input("> ")

    if "0" in next or "1" in next:
        how_much = int(next)

    else:
        dead("Man, learn to type a number. ")

    if how_much < 50:

        print "Nice you're not greedy, you are good"
        exit(0)

    else:
        dead("you greedy bustard")

def bear_room():
    print "there is a bear here."
    print "the bear has a bunch  of honey"
    print "the fat bear is in front of another"
    print "how a you going to move the bears"
    bear_moved = False

    while true:
        next = raw_input("> ")

        if next == "take honey":
            dead("the bear looks at you and slapsyour face off")
        elif next == "taunt bear" and not bear_moved:
            print "the bear has moved from the door. you can go thru it now."
            bnear_moved = True
       ## elif next "taunt bear" and bear_moved:
           ## dead("the bear gets pissed off and chews your legs off")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "i got no idea what that means"
