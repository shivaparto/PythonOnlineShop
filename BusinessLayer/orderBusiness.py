from DataLayer import order
def insert(commandArray:[]):
    article_id = commandArray[1].split(":")
    ordernumber = commandArray[2].split(":")
    order.insert({"article_id": article_id[1], "number": ordernumber[1], "status": "False"})
def buy(commandArray:[]):
    order_id = commandArray[1].split(":")
    order_item=order.getItemById(order_id[1])
    order.update({'id':order_id[1],'article_id':order_item[1],"number":order_item[2],"status":"True"})
def delete(commandArray:[]):
    order_id = commandArray[1].split(":")
    order.delete(order_id[1])
