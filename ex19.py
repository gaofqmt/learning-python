def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

print " We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def a_func(dogs, cats):
    print "I have %d dogs." % dogs
    print "I have %d cats." % cats

print "How many dogs do you have?",
dogs = int (raw_input())

print "How many cats do you have?",
cats = int ( raw_input())

a_func(dogs,cats)
