
def changenum():
	my_list = []
	for i in range(1,31):
		b = list(map(int,str(i)))
		c = ''
		if len(list(b))==1:
			if i%3==0:
				c = "Buzz"
			elif i%5==0:
				c = "Fuzz"
			else:
				c = str(i)
		else:
			if i%3==0 and i%5==0:
				c = "BuzzFuzz"
			elif i%3==0:
				c = "Buzz"
			elif i%5==0:
				c = "Fuzz"
			else:
				c = str(i)
		my_list.append(c)
	return my_list
print(changenum ())
