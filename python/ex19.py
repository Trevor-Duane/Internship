#function taking in two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "you have %d of cheese!" % cheese_count
    print "you have %d boxes of crackers" % boxes_of_crackers
    print "man! thats not enough for the party"
    print "get a blanket\n"

#function being passed value to manuplate directly
print "we can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#values to the function being passewd through a script
print "OR, we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 30

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#performing some addtion within the function
print "we can also do some math"
cheese_and_crackers(10 + 20, 5 + 6)

#combining the two script and math
print"and we can combine the two variablesand math"

cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)
