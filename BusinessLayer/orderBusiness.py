from DataLayer import order
from Entities.order import Order
def insert(commandArray:[]):
    article_id = commandArray[1].split(":")
    ordernumber = commandArray[2].split(":")
    orderitem=Order(None,article_id[1],ordernumber[1],"False")
    order.insert(orderitem)
def buy(commandArray:[]):
    order_id = commandArray[1].split(":")
    order_item=order.getItemById(order_id[1])
    order_item.status="True"
    order.update(order_item)
def delete(commandArray:[]):
    order_id = commandArray[1].split(":")
    order.delete(order_id[1])
