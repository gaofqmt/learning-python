numbers = []

def num(end_point):
    i = 0
    while i < end_point :
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom is %d" % i

num(8)

print "The numbers: "

for num in numbers:
    print num 


