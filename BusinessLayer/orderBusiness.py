from DataLayer import order
from DataLayer import article
from Entities.order import Order
from Entities.article import Article
def insert(commandArray:[]):
    article_id = commandArray[1].split(":")
    ordernumber = commandArray[2].split(":")
    orderitem=Order(None,article_id[1],ordernumber[1],"False")
    order.insert(orderitem)
def buy(commandArray:[]):
    order_id = commandArray[1].split(":")
    order_item=order.getItemById(order_id[1])
    order_item.status="True"
    article_item = article.getItemById(order_item.article_id)
    if order_item.number > article_item.stock:
        raise ValueError('you cant')

    article_item.stock -= order_item.number
    article.update(article_item)
    order.update(order_item)
    return ValueError
def delete(commandArray:[]):
    order_id = commandArray[1].split(":")
    order.delete(order_id[1])

