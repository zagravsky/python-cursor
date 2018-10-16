
def changenum ():
	mylist = []
	for i in range(1,31):
		b = list(map(int,str(i)))
		if len(list(b))==1:
			if i%3==0:
				mylist.append("Buzz")
			elif i%5==0:
				mylist.append("Fuzz")
			else:
				mylist.append(i)
		else:
			if i%3==0 and i%5==0:
				mylist.append("BuzzFuzz")
			elif i%3==0:
				mylist.append("Buzz")
			elif i%5==0:
				mylist.append("Fuzz")
			else:
				mylist.append(i)
	return mylist
print(changenum ())
