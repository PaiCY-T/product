def input_product(products):#使用者輸入
	while True:
		name = input('請輸入商品名稱')
		if name == 'q':
			break
		price = int(input('請輸入價格'))
		products.append([name, price])
	return products
def write_back(file_name, products):#寫回檔案
	with open(file_name, 'w', encoding= 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')
def read_file(file_name):#讀取檔案
	products = []
	if os.path.isfile(file_name):
		with open(file_name, 'r', encoding= 'utf-8') as f:
			for line in f:
				if '商品,價格' in line:
					continue
				name, price = line.strip().split(',')
				products.append([name, price])
		#print(products)
	else:
		print('file does not exist')
	return products

import os
file_name = 'products.csv'
products = read_file(file_name)
products = input_product(products)
write_back(file_name, products)
print(products)

