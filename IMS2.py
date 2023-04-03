unit_price={}
description={}
stock={}


from IMS1 import *



cart=[]

c="y"
 
 
 
print("Welcome to Inventory Management System")
print()
print("A-Add an item")
print("R-Remove an item")
print("E-Edit specifics of an item")
print("L-List all items")
print("P-Purchase")
print("C-Checkout")
print("S-Show all items purchased")
print("Q-Quit")
print("remove-Remove an item from the cart")
print("help-See all commands again")
print()


 
 
while(c!= "q" or c!= "Q"):
    c = input("What would you like to do? ")
    
    if(c=="q" or c=="Q"):
        break
        
    elif(c=="A" or c=="a"):
        add_item()
        
    elif(c=="E" or c=="e"):
        edit_item()
    
            
    elif(c=="R" or c=="r"):
        remove_item()
        
    elif(c=="L" or c=="l"):
        list_items()

    elif(c=="P" or c=="p"):
        purchase_item()
        
    elif(c=="C" or c=="c"):
        checkout()
        
    elif(c=="help"):
        help()
        
    elif(c=="remove" or c=="Remove"):#To remove an item from the cart
        remove()

    elif(c=="s" or c=="S"):
        show_cart()
        
    else:
            print()
            print("ERROR! Contact manager for help!")
            print()
 
 
 
    if(total_cost>0 and flag == 0):
        print()
        print("You bought: ",cart)
        print("Total: ","₹",round(total_cost,2))
        tax= round(0.12*total_cost,2)
        print("Tax is 12%: ","₹",tax)
        total = round(total_cost+tax,2)
        print("After Tax: ","₹",total)
    
 
    print("Thank you for using Inventory Management System")
