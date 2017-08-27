import os

#Dictionary
dic={1:'Hello','grand':2000}
print dic[1], dic['grand']
n=10
qua = ['chuoi', 'tao',  'xoai']

#Variable-lengh
def print_number(arg, *tup):
	print arg

	for var in tup:
		print var
print_number(1,3)
print_number(5)

#Lambda
square=lambda x:x*x
print square(5)
r=float(raw_input("Get"))
print r*r