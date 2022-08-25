while True:
    print("Choose 'Admin', if you are admin,\nChoose 'Client', if you are client ")
    num = input('')
    import psycopg2
    import time
        
    connection = psycopg2.connect(
            host = 'localhost',
            port = '5432',
            database = 'postgres',
            user= 'postgres',
            password = 'postgres'
        )
    cursor = connection.cursor()
    if num == 'Client':
        
        
        print('Welcome to my our shop <<TECHNICAL WORLD>>')
        print('Under you  can see a list of our products')
        query = "SELECT productname FROM products;"
        cursor.execute(query)
        product = []
        for i in cursor:
            # print(*i)
            product.append(*i)
        # print(*product)
        for n in product:
            print(n)
        
        
        phone = input('What do you want to buy? ')
        if phone in product:
            tel = f"SELECT productcount FROM products WHERE productname = '{phone}'; "
            cursor.execute(tel)
            connection.commit()
            telephone = cursor.fetchone()
            price_phone = f"SELECT price FROM products WHERE productname = '{phone}';"
            cursor.execute(price_phone)
            connection.commit()
            telephone2 = cursor.fetchone()
            print(f"At the moment we have {telephone[0]} pieces {phone} ")
            phone2 = int(input('How many do you want to buy? '))
            tel2 = int(telephone2[0]) * int(phone2)
            # print(tel2)
            if phone2 <= telephone[0]:
                count_total=int(telephone[0])- int(phone2)
                name =input("Your name: ")
                s_name=input("Your surname: ")
                Address = input('Your address: ')
                tel_number2 = int(input('Your phone number: '))
                localtime = time.time()
                nur = time.ctime(localtime)
                
                
                print(f"""                         YOUR CHECK
                    
                            <<TECHNICAL WORLD>>
                ----------------------------------------------------
                {phone}        {phone2}x{telephone2[0]}= {tel2} 
        
                Name: {name} 
                Surname: {s_name}
                Phone name: {phone}
                Phone quantity: {phone2} 
                Total price: {tel2}
                Time: {nur}
                -----------------------------------------------------
                                        Number of the check: 12325462
                                        PHP: 256847520
                                        Tel: +996551444267
                                        Cashier: Nurseit Zhutanov
        
                        Thank you for your purchase 
                        
                        """)
                query1=f"UPDATE products SET productcount = {count_total} WHERE productname  = '{phone}'"
                cursor.execute(query1)
                connection.commit()
                query2 =f"INSERT INTO clients(name,surname, address, tel_number, productname, productquantity, time, productprice) VALUES ('{name}','{s_name}','{Address}',{tel_number2},'{phone}',{phone2},'{nur}','{tel2}')"
                cursor.execute(query2)
                connection.commit()
        
                cursor.close()
                connection.close()
            else:
                print(f"We don not have {phone}")
        
        else:
            print("At the moment we don't have this phone.SORRY")

    elif num == 'Admin': 
        a = 'nurseit.zhutanov@gmail.com'      
        b = '123456789'
        for i in range(0,3):
            login = input('Your login: ')
            Password = input('Your password: ')
            if login in a and Password in b:
                print("Choose 'new',if you will add new product,\nChoose 'old',if you will add old product")
                choice = input('')
                if choice == 'new':
                    a = input('Name of the product: ')
                    d = input('Company: ')
                    b = input('How many do you want to add? ')
                    c = input('Product price: ')

                    cursor.execute(f"INSERT INTO products(productname,company,productcount,price) VALUES('{a}','{d}',{b},{c})")
                    connection.commit()
                    cursor.execute("SELECT * FROM products;")
                    connection.commit()
                    product = cursor.fetchall()
                    for i in product:
                        print(*i)
                        break
                if choice =='old':
                    name_product = input('Which product do you want to add')
                    count_product = int(input('How many do you want to add? '))
                    cursor.execute(f"UPDATE products SET productname = '{name_product}' WHERE productcount = {count_product} ")
                    connection.commit()
                    product1 =cursor.fetchone()
            else:
                print('Try again. NOT FOUND')
        else:
            break
    elif num != "Admin" and "Client":
        print("Choose correct variant: Admin or Client" )

    
    

print(7542)




















