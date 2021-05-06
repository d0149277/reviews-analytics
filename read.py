data = []
count = 0 
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		if count % 10000 == 0:
			print(data[count])
			print('---------------------------------------------------------------------------')
		count += 1
sum_len = 0
for  y in data:
	sum_len += len(y)
print('檔案讀取完了，共', len(data), '筆留言')
print('每筆留言平均為', sum_len / len(data))