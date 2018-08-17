import numpy

print "This app will print the median from a list of numbers!"
print "  When you are done entering numbers, please enter any"
print "  nonnumber character to get the result"

# Create empty list to hold the numbers
numbers = []
# Collect numbers
while True:
    try:
        number = float(raw_input("Please enter a floating point number: "))
        numbers.append(number)
    except ValueError:
        break

if numbers:
    print "\nThese are the numbers you entered:"
    print numbers
    print "\nThis is the median: " + str(numpy.median(numbers))
else:
    print "  Sorry, you did not enter any numbers!  Exiting..."
