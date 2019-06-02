print('소프트웨어공학과-2019620104-신명규')
products = {'notebook': 1000,'scissors':1500,'crayon': 15000,'sketchbook': 3000}
print('1. products list:',products)
catalog = {'fountain pen':14000,'color pencil':6500,'glue stick':800}
print('2. catalog list:',catalog)
products.update(catalog)
print('3. The price of color pencil?:',products['color pencil'])
print('4. products:',end=" ")
for key1 in products.keys():
    print(key1,end=" ")
print()
products['ruler'] = 2800
print('5. ruler 2,800 추가:',products)
products.pop('glue stick')
print('6. glue stick 제거:',products)
products['notebook']=1500
print('7. notebook 가격을 1,500으로 변경:',products)
print('8. 총 상품 개수:',len(products))
#key1 in products.keys()
#value1 in products.values()
print('9. 상품리스트: ', end="")
for key,values in products.items():
    print('{}의 가격은 {}입니다'.format(key,values),end=".")
print()
while True:
    a = input("10. 가격 검색(소문자입력) : ")
    if a in products.keys():
        print('{}의 가격은 {}입니다.'.format(a,products[a]))
    elif a == 'end' or a == 'END':
        break
    else:
        print('데이터가 없습니다.')
