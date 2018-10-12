class IT:
	def __init__(self, name):
		self.name = name
		self.it_dev = []

	def __add__(self, dev):
		if dev.years_experience >= 3:
			self.it_dev.append(dev)
			return self
		else:
			print('Sorry, experience is not enough')

	def __str__(self):
		st = ''
		it_dev_sort = sorted(self.it_dev, key = lambda dev: dev.years_experience)
		for d in it_dev_sort:
			st += str(d)
		return st

	def __len__(self):
		return len(self.it_dev)

	def release(self, name_dev):
		for dev in self.it_dev:
			if dev.name == name_dev:
				self.it_dev.remove(dev)
				break
			else:
				print('An employee with this name is not found')
				break