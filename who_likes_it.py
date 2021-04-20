#https://www.codewars.com/kata/5266876b8f4bf2da9b000362
#my solution
def likes(names):
	#code here
	if len(names) == 0:
		return 'no one likes this'
	elif len(names) == 1:
		return names[0] + ' likes this'
	elif len(names) == 2:
		return names[0] + ' and ' + names[1] + ' like this'
	elif len(names) == 3:
		return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
	elif len(names) > 3:
		return names[0] + ', ' + names[1] + ' and ' + str(len(names)-2) + ' others like this'

#print(likes(['Jay','Kelly', 'Mark', 'Ryan']));


#top solutions

def likes2(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this',
		5: '{}, {}, {}, {}, and {others} others like this',
		6: '{}, {}, {}, {} and {others} others like this'
    }[min(6, n)].format(*names[:4], others=n-2)


print(likes2(['Jay','Kelly', 'Ryan', 'Josh', 'Crystal']));	

def likes3(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)

#print(likes(['Brent','Kelly', 'Mark', 'Ryan']));