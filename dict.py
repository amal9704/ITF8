
products = []
while True:
    selection = int(input("1.add product\n2.print details\n"
                          "3.buy product\n"
                          "4.delete product\n"
                          "5.exit"))
    if selection == 1:
        product_num = int(input("enter the product number"))
        product_name = input("enter the product name")
        product_price = int(input('enter product price'))
        product_qty = int(input("enter product quantity"))
        product = {
            "id" : product_num,
            "name" : product_name,
            "price" : product_price,
            "qty" : product_qty
        }
        products.append(product)
        print("product added successfully")
    elif selection == 2:

        for i in products:
            print(i)
            break
    elif selection == 3:
        product_num = int(input('enter the product number'))
        for i in products:
            if i['id'] == product_num:
                while True:
                    qty = int(input("enter product quantity"))
                    if qty > i['id'] or qty <= 0:
                        print("invalid quantity")
                    else:
                        break
                i['qty'] = i['qty'] - qty
                break
    elif selection == 4:
        product_number = input('enter product number')
        for i in products[:]:
            if i['id'] == product_number:
                products.remove(i)
                break
    else:
        exit()









































