#https://www.codewars.com/kata/56269eb78ad2e4ced1000013

from math import sqrt,pow

def find_next_square(sq):
	# Return the next square if sq is a square, -1 otherwise
	if sq%sq**0.5==0:
		return pow((sqrt(sq)+1),2)
	else:	
		return -1



print(find_next_square(114))
print('--------------')
print(find_next_square(121))
print('--------------')
print(find_next_square(625))
print('--------------')
print(find_next_square(319225))
print('--------------')
print(find_next_square(15241383936))
print('--------------')