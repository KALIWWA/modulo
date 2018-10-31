a=[]
how_many = int(input('How many numbers do you want to see?: '))
for i in range(100,1000):
	if i % 9==0 or i % 7==0:
		a.append(i)
for i in range(how_many):
	print(f'{a[i]}')
		

