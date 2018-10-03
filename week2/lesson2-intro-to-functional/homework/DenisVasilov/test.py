def first_function(data: list) -> int:
	l = data.copy()
	return l.pop()

def second_function(data: list) -> int:
	return data[len(data)-1]

def third_function(data: list) -> int:
	return data[-1]

def main():
	data = [1, 2, 3, 4]
	variants = (first_function, second_function, third_function)
	for variant in variants:
		print(variant(data))

if __name__ == "__main__":
	main()
