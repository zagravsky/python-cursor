def changenum():
	my_list = []
	for i in range(1,31):
		list_part = list(map(int,str(i)))
		item_part = str(i)
		if len(list(list_part))==1:
			if i%3==0:
				item_part = "Buzz"
			elif i%5==0:
				item_part = "Fuzz"
		else:
			if i%3==0 and i%5==0:
				item_part = "BuzzFuzz"
			elif i%3==0:
				item_part = "Buzz"
			elif i%5==0:
				item_part = "Fuzz"
		my_list.append(item_part)
	return my_list
print(changenum())
