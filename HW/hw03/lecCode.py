def slice(num):
	return num//10,num%10

def count(num):
	if num<10:
		return num
	besides,last_digit=slice(num)
	return count(besides)+last_digit

def neighbor_digits(num,prev_digit=-1):
	if n<10:
		return 0
	if (num%10==prev_digit)|(num%100=n%10):
		return 1	
