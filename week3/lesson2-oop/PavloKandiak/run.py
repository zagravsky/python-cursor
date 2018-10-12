from utils.task1 import *
from utils.task2 import *
from utils.task3 import *



if __name__ == '__main__':
	pd = PythonDeveloper("Pavlo", 1)
	jd = JavaDeveloper('Vasyl', 4)
	rd = RubyDeveloper('Oleg', 6) 
	print(pd)
	print(jd)
	print(rd)
	pd()
	jd()
	rd()

	print(E.mro())

	company = IT('Epam')
	company + pd
	company + jd
	company + rd
	print(company)
	company.release('Vasyl')
	print(company)
	company.release('Vasyl')