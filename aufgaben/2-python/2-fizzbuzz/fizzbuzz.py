
# encoding: utf-8
from __future__ import (print_function,
                        division,
                        unicode_literals,
                        absolute_import)


for n in range(1, 101):
	rest_3 = n % 3
	rest_5 = n % 5
	if(rest_3 == 0):
		if(rest_5 == 0):
			print("FizzBuzz")
		else:
			print("Fizz")
	elif(rest_5 == 0):
		print("Buzz")
	else:
		print(n)

		

    

  
