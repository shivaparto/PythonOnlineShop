from DataLayer import article
from DataLayer import order
from BusinessLayer import orderBusiness


def interpretCommand(command: str):
    commandArray = command.split(" ")
    try:
        if str.lower(commandArray[0]) == "add":
            if len(commandArray) != 3:
                print("Command is wrong!")
            else:
                orderBusiness.insert(commandArray)
                print("Product successfully added to your basket!")
        elif str.lower(commandArray[0]) == "show":
            orderList = order.getAll('False')
            if len(orderList)==0:
                print("Your basket is empty!")
            for item in orderList:
                print(item)
        elif str.lower(commandArray[0]) == "buy":
            orderBusiness.buy(commandArray)
            print("Your buying process proceed successfully!")
        elif str.lower(commandArray[0]) == "delete":
            orderBusiness.delete(commandArray)
            print("Your deleting process proceed successfully!")
        else:
            raise NameError
    except NameError:
        print("problem in command")


productList = article.getAll()
for item in productList:
    print(item)

print("Please select a command :")
print("To add a product to the basket use the following command: ")
print("1.Add -id:[Articleid] -ordernumber:[ordernumber] ")
print("To view your basket use the following command :")
print("2.Show")
print("To buy and confirm your order use the following command :")
print("3.Buy -id:[orderid] ")
print("To delete a product from yor basket use the following command")
print("4.Delete -id:[order_id]")



while True:
    command = input()
    if command!="":
        if(command!="exit"):
         interpretCommand(command)
        else:
            break
