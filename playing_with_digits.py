#https://www.codewars.com/kata/5552101f47fc5178b1000050
def dig_pow(n,p):
	#your code
	num = str(n)
	total = sum([int(num[i]) ** (p + i) for i in range(len(num))])
	return total / n if (total % n) == 0 else -1

print(dig_pow(2360688,3))
print('--------------')
print(dig_pow(89,1))
print('--------------')
print(dig_pow(46288, 3))
print('--------------')
print(dig_pow(1377, 1))
print('--------------')
print(dig_pow(7388, 2))
print('--------------')
print(dig_pow(2697, 3))