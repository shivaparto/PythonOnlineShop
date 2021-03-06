import sqlite3
from Entities.order import Order
def getAll(status):
    connection = sqlite3.connect("onlineshop.db")
    cursor = connection.cursor()
    query = "SELECT * FROM  [order] where status ='{status}'".format(status = status)
    order=[]
    for item in cursor.execute(query):
        orderItem = Order(item[0],item[1],item[2],item[3])
        order.append(orderItem)
    connection.commit()
    connection.close()
    return order
def insert(order:Order):
    connection = sqlite3.connect("onlineshop.db")
    cursor = connection.cursor()
    query="INSERT INTO [Order](Id,article_id,number,status) VALUES(NULL,'{article_id}',{number},'{status}')".format(article_id=order.article_id,number=order.number,status=order.status)
    cursor.execute(query)
    connection.commit()
    connection.close()
def delete(id):
    connection = sqlite3.connect("onlineshop.db")
    cursor = connection.cursor()
    query = "DELETE FROM [order] WHERE id='{id}'".format(id=id)
    cursor.execute(query)
    connection.commit()
    connection.close()


def update(orderItem:Order):
    connection = sqlite3.connect("onlineshop.db")
    cursor = connection.cursor()
    query= "UPDATE [order] SET  article_id='{article_id}',number={number},status='{status}' WHERE id='{id}'".format(id=orderItem.id,article_id=orderItem.article_id,number=orderItem.number,status=orderItem.status)
    cursor.execute(query)
    connection.commit()
    connection.close()
def getItemById(orderid):
    connection = sqlite3.connect("onlineshop.db")
    cursor = connection.cursor()
    query= "SELECT * FROM  [order] where id='{id}'".format(id=orderid)
    result=cursor.execute(query).fetchone()
    connection.commit()
    connection.close()
    return Order(result[0], result[1], result[2], result[3])