data = []
count = 0 
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		if count % 10000 == 0:
			print(data[count])
			print('---------------------------------------------------------------------------')
		count += 1
print(len(data))