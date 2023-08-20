products = []
while True:
    selection = int(input("1.Add New Product\n2.Print Product Details"
                          "\n3.Buy Product"
                          "\n4.Delete Product"
                          "\n5.Exit"))
    if selection == 1:
        product_number = input("Enter Product Number :")
        product_name = input("Enter Product Name :")
        product_price = input("Enter Product Price :")
        product_qty = int(input("Enter Product Quantity :"))
        product = {
            "id": product_number,
            "name": product_name,
            "price": product_price,
            "qty": product_qty
        }
        products.append(product)
        print("Product Added Successfully")
    elif selection == 2:
        product_number = input("Enter product number :")
        for i in products:
            if i['id'] == product_number:
                print(i)
                break
    elif selection == 3:
        for i in products:
            product_number = int(input("enter product number:"))
            if i['id'] == product_number:
                while True:
                    qty = int(input('enter product qty'))
                    if qty > i['qty'] or qty <= 0:
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