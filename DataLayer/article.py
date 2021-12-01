import sqlite3
from Entities.article import Article


def getAll():
    connection = sqlite3.connect("onlineshop.db")
    cursor = connection.cursor()
    articleList = []

    for row in cursor.execute('SELECT * FROM Article'):
        articls = Article(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
        articleList.append(articls)

    connection.commit()
    connection.close()
    return articleList


def insert(item:Article):
    connection = sqlite3.connect("onlineshop.db")
    cursor = connection.cursor()
    query = "INSERT INTO Article(Id,articleNum,name,description) VALUES(NULL,{articleNum},'{name}','{description}')".format(
     articleNum=item.articleNum, name=item.name,description=item.description)
    cursor.execute(query)

    connection.commit()
    connection.close()


def update(articleItem:Article):
    connection = sqlite3.connect("onlineshop.db")
    cursor = connection.cursor()
    query = "UPDATE Article SET \
    name='{name}',\
    articleNum={articleNum},\
    description='{description}',\
    price={price},\
    status='{status}',\
    stock={stock},\
    created_a='{created_a}' \
    WHERE id='{id}'".format(name=articleItem.name, articleNum=articleItem.articleNum,
                            description=articleItem.description, price=articleItem.price,
                            status=articleItem.status, stock=articleItem.stock,
                            created_a=articleItem.created_a, id=articleItem.id)
    cursor.execute(query)
    connection.commit()
    connection.close()


def delete(artikelId):
    connection = sqlite3.connect("onlineshop.db")
    cursor = connection.cursor()
    query = "DELETE FROM Article WHERE id='{id}'".format(id=artikelId)
    cursor.execute(query)
    connection.commit()
    connection.close()
