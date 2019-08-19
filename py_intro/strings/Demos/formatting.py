import math

#Fixed Point
print('pi equals {:f}'.format(math.pi))
#outputs 'pi equals 3.141593'

#No Type Specified
print('pi equals {}'.format(math.pi))
#outputs 'pi equals 3.141592653589793'

#Precision
print('pi equals {:.2f}'.format(math.pi))
#outputs 'pi equals 3.14'

#Separate by Thousands
print('{:,.2f}'.format(1000000))
#outputs '1,000,000.00'

#WIDTH EXAMPLES
##Example 1
print('{:5}'.format('abc'))
##outputs 'abc  '

##Example 2
print('{:5}'.format(123))
##outputs '  123'

##Example 3
print('{:5.2f}'.format(123))
##outputs '123.00'

#Forcing sign to show
print('pi equals {:+.2f}'.format(math.pi))
#outputs 'pi equals +3.14'

#ALIGNMENT EXAMPLES
print('{:>5}'.format('abc'))
##outputs '  abc'

print('{:<5}'.format(123))
##outputs '123  '

print('{:^5}'.format(123))
##outputs ' 123 '

print('{:=+5}'.format(123))
##outputs '+ 123'

#Fill
'{:.^10.2f}'.format(math.pi)
#Note the period after the colon
#outputs '...3.14...' instead of '   3.14   '

#Percentage
questions = 25
correct = 18
grade = correct / questions
print(grade)
#outputs 0.72
print('{:.2%}'.format(grade))
#outputs 72.00%
print('{:.0%}'.format(grade))
#outputs 72%