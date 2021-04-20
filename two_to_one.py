#https://www.codewars.com/kata/5656b6906de340bd1b0000ac
#my answer
def longest(a1, a2):
	# your code
	full_str = a1 + a2
	final_str = ''
	#print(full_str)
	for char in full_str:
		if char not in final_str:
			final_str += char
	return ''.join(sorted(final_str))

#expected output aehrsty
print(longest('aretheyhere','yestheyarehere'))

#best practices 
def longest2(a1, a2):
    return "".join(sorted(set(a1 + a2)))

print(longest2('aretheyhere','yestheyarehere'))

#example of set function for further understanding
# initializing list
lis1 = [ 3, 4, 1, 4, 5 ]
 
# initializing tuple
tup1 = (3, 4, 1, 4, 5)
 
# Printing iterables before conversion
print("The list before conversion is : " + str(lis1))
print("The tuple before conversion is : " + str(tup1))
 
# Iterables after conversion are
# notice distinct and elements
print("The list after conversion is : " + str(set(lis1)))
print("The tuple after conversion is : " + str(set(tup1)))

str1 = 'aretheyhereyestheyarehere'
print(sorted(set(str1)))