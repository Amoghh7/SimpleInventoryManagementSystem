unit_price={}
description={}
stock={}
item_no=[]
cart=[]

total_cost = 0

def add_item():
    p_no = int(input("Enter item number: "))
    p_pr = float(input("Enter item price: "))
    p_desc = input("Enter item description: ")
    p_stock = int(input("Enter item stock: "))

    if(p_no in unit_price):
        p_no+=1
        print()
        print("That item number already exists : changing value to ",p_no)

    item_no.append(p_no)
    unit_price.update({p_no: p_pr})
    description.update({p_no: p_desc})
    if(p_stock > -1):
        stock.update({p_no: p_stock})
    else:
        p_stock = 0
        stock.update({p_no: p_stock})
        print("The stock of an item cannot be negative, the stock has been set to 0.")
    print()
    update_stock_file()
    print("Item number: ",p_no," Description: ",description.get(p_no)," Price: ",unit_price.get(p_no)," Stock: ",stock.get(p_no))
    print("Item was added successfully!")
    print()


def edit_item():
    print()
    p_no = int(input("Enter item number: "))
    if(p_no in unit_price):
        p_pr = float(input("Enter item price: "))
        p_desc = input("Enter item description: ")
        p_stock = int(input("Enter item stock: "))
                
        unit_price.update({p_no: p_pr})
        description.update({p_no: p_desc})
        stock.update({p_no: p_stock})
        update_stock_file()
    else:
        print("That item does not exist, to add an item use a")
        print()


def remove_item():
    print()
    p_no = int(input("Enter item number: "))
    if(p_no in unit_price):
        are_you_sure = input("Are you sure you want to remove that item(y/n)? ")
        if(are_you_sure=="y" or are_you_sure=="Y"):
            unit_price.pop(p_no)
            description.pop(p_no)
            stock.pop(p_no)
            print("Item successfully removed!")
            update_stock_file()
        print()
    else:
        print("Sorry, we don't have such an item!")
        print()

def list_items():
    print()
    print("Item and their prices: ",unit_price)
    print("Descriptions: ",description)
    print("Stock left of Item: ",stock)
    print()




def purchase_item():
    print()
    global total_cost
    p_no = int(input("Enter Item number: "))
    if(p_no in unit_price):
        stock_current = stock.get(p_no)
        if(stock_current>0):
            stock_current = stock.get(p_no)
            stock[p_no] = stock_current-1
            item_price = unit_price.get(p_no)
            total_cost = total_cost+item_price
            print(description.get(p_no),"added to cart: ","₹",item_price)
            cart.append(p_no)
            update_stock_file()
        else:
            print("Sorry! We don't have that item in stock!")
    else:
            print("Sorry! We don't have such an item!")
    print()


def checkout():
    print()
    global total_cost
    print("You bought the following items: ",cart)
    print("Total: ","₹",round(total_cost,2))
    tax= round(0.12*total_cost,2)
    print("Tax is 12%: ","₹",tax)
    total = round(total_cost+tax,2)
    print("After Tax: ","₹",total)
    total_cost=0
    del cart[:]
    print()
    print("You can still purchase items after check out, your cart has been reset. To quit press q")
    print()

def help():
    print()
    print("Help Centre")
    print("A-Add an item")
    print("R-Remove an item")
    print("E-Edit specifics of an item")
    print("L-List all items")
    print("P-Purchase")
    print("C-Checkout")
    print("S-Show all items purchased")
    print("remove-Remove an item from the cart")
    print("help-See all commands again")
    print("If you have any other questions or concerns please contact the manager.")
    print()

def remove():
    print()
    global total_cost
    are_you_sure = input("Are you sure you want to remove an item from the cart(y/n)? ")
    if(are_you_sure=="y"):
        p_no = int(input("Enter item number to remove from cart: "))
        if(p_no in cart):
            stock_current = stock.get(p_no)
            stock[p_no] = stock_current+1
            item_price = unit_price.get(p_no)
            total_cost = total_cost-item_price
            for i in range(0,len(cart)):
                if(cart[i]==p_no):
                    cart.pop(i)
                    break
            print(description.get(p_no),"removed from cart: ")
            print()
            update_stock_file()
        else:
            print()
            print("That item is not in your cart!")
            print()

def show_cart():
    print()
    print(cart)
    print()

def update_stock_file():
    try:
        f = open(r"D:\Codes\Python Projects\Stock.txt", "w+")
        for i in item_no:
            temp = {}
            t1 = []
            t1.append(unit_price[i])
            t1.append(description[i])
            t1.append(stock[i])
            temp.update({i: t1})
            f.write(repr(temp) + "\n")

    except:
        print("Error while updating stock file")

    finally:
        f.close()
