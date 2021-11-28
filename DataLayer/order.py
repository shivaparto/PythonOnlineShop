import sqlite3
def getAll(status):
    connection = sqlite3.connect("onlineshop.db")
    cursor = connection.cursor()
    query = "SELECT * FROM  [order] where status ='{status}'".format(status = status)
    order=[]
    for item in cursor.execute(query):
        order.append(item)
    connection.commit()
    connection.close()
    return order
def insert(order):
    connection = sqlite3.connect("onlineshop.db")
    cursor = connection.cursor()
    query="INSERT INTO [Order](Id,article_id,number,status) VALUES(NULL,'{article_id}',{number},'{status}')".format(article_id=order["article_id"],number=order["number"],status=order["status"])
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


def update(orderItem):
    connection = sqlite3.connect("onlineshop.db")
    cursor = connection.cursor()
    query= "UPDATE [order] SET  article_id='{article_id}',number={number},status='{status}' WHERE id='{id}'".format(id=orderItem["id"],article_id=orderItem["article_id"],number=orderItem["number"],status=orderItem["status"])
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
    return result