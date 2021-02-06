def input_product(products):#使用者輸入，回傳商品,價格
    while True:
        name = input('請輸入商品名稱')
        if name == 'q':
            break
        price = int(input('請輸入價格'))
        products.append([name, price])
    return products
#寫回檔案，輸入檔案名、寫入清單
def write_back(file_name, products):
    with open(file_name, 'w', encoding= 'utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')
#讀取檔案，回傳商品、價格
def read_file(file_name):
    products = []
    with open(file_name, 'r', encoding= 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
        #print(products)
    return products

def main(file_name):
	products = []
	if os.path.isfile(file_name):
		products = read_file(file_name)
	else:
		print('file does not exist')
	products = input_product(products)
	write_back(file_name, products)
	print(products)

import os
main('products.csv')