def divisors(n):
	a=1
	while a<=n:
		#print a
		if n%a==0:
			print a
		a+=1

if __name__ == "__main__":
	n=int(raw_input("write a number"))
	divisors(n)