print "you enter a dark room with two doors. do you go through #1 or door #2?"


door = raw_input('>')

if door == "1":
    print "There is a giant bear here eating a cheese cake. What do you do.?"
    print "1. Take the cake"
    print "2. SCream at  the bear."

    bear = raw_input('>')

    if bear == "1":
        print "the bear eats your face off"
    elif bear == "2":
        print "the bear eats your legs off"
    else:
        print "well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "you atre into endless abyss at cthulhu's retina"
    print "1. Blueberries."
    print "2. Yellow jacket clothespins"
    print "3. Unserstanding revolvers yelling melodies"
    insanity = raw_input('>')
    if insanity == "1" or insanity =="2":
        print "your body survives powdered"
    else:
        print "the insanity rots your eyes"

else:
    print "you stamble around and fall"
