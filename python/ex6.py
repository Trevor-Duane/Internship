x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't" 
y = "Those who know %s and those who dont %s." % (binary, do_not)
print y
print x
print "I said: %r." % x
print "i also said: '%s'." % y

hilarious = False
joke_evaluation = "isnt that joke funny!? %r"

print joke_evaluation % hilarious

w = "this is the left side of......"
e = "a string with a right side."

print w + e
