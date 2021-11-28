

import  sqlite3
connection = sqlite3.connect("Artikel.db")

cursor = connection.cursor()


for row in cursor.execute('SELECT * FROM Artikel'):
    print(row)

# Artikeln anzeigen
artikeln = [
    {'id': 1, 'artikel-nr': 10010, 'name':'Pullover', 'description':'das ist die beschreibung des Artikels','price':20.55,'status':True,'lagerbestand':100,'created_at': '2021-11-19 16:09:10','updated_at':  '',},
    {'id': 2, 'artikel-nr': 10020, 'name':'Hose', 'description':'das ist die beschreibung des Artikels','price':50.99,'status':True,'lagerbestand':100,'created_at': '2021-11-19 16:09:10','updated_at':  '',},
    {'id': 3, 'artikel-nr': 10030, 'name':'T-Shirt', 'description':'das ist die beschreibung des Artikels','price':20.55,'status':True,'lagerbestand':100,'created_at': '2021-11-19 16:09:10','updated_at':  '',},
    {'id': 4, 'artikel-nr': 10040, 'name':'Schale', 'description':'das ist die beschreibung des Artikels','price':20.55,'status':True,'lagerbestand':100,'created_at': '2021-11-19 16:09:10','updated_at':  '',},
    {'id': 5, 'artikel-nr': 10050, 'name':'Mütze', 'description':'das ist die beschreibung des Artikels','price':20.55,'status':True,'lagerbestand':100,'created_at': '2021-11-19 16:09:10','updated_at':  '',},
    {'id': 6, 'artikel-nr': 10060, 'name':'Unterhose', 'description':'das ist die beschreibung des Artikels','price':20.55,'status':True,'lagerbestand':100,'created_at': '2021-11-19 16:09:10','updated_at':  '',},
    {'id': 7, 'artikel-nr': 10070, 'name':'Soken', 'description':'das ist die beschreibung des Artikels','price':20.55,'status':True,'lagerbestand':100,'created_at': '2021-11-19 16:09:10','updated_at':  '',},
]

#Wahrenkorb
korb = [
    {'id': 1, 'count':3},
]

#print(artikeln)




def ArtileIndex():
    #Artikel anzeigen
    print('alle Artikeln anzeigen')
    # gib mir alle daten aus der Datenbank
    for value in artikeln:
        print(artikeln[value]['name'], 'Prise: ', artikeln[value]['price'])

def ArtikelStore():
    # Artikel store
    artikel = {
        'id': 8,
        'artikel-nr': 10080,
        'name':'Rosa Lutscher',
        'description':'das ist die beschreibung des Artikels',
        'price':20.55,
        'status':True,
        'lagerbestand':100,
        'created_at': '2021-11-19 16:09:10',
        'updated_at':  '',
    }
    artikeln.append(artikel)

    print(artikeln)

    print('Artikeln eingabe speichern')

#funktion aufruf der store methode
#ArtikelStore()


def ArtikelEdit(id):
    # Artikel edit
    print('Artikeln bearbeiten')
    for item in artikeln:
        #print(item['id'])
        if item['id'] == id:
            print(item)
    # frontend übergabe


# funktion methode aufrufen
#ArtikelEdit(5)


def ArtikelUpdate(id,request):
    # Artikel update
    #print(request['name'])
    print('Artikeln update')
    for item in artikeln:
        #print(item['id'])
        if item['id'] == id:
            print('Vorher: ',item)
            item['name'] = request['name']
            item['description'] = request['description']
            item['price'] = request['price']
            item['lagerbestand'] = request['lagerbestand']

            print('Nacher: ',item)



# update methode
update_variable = {
    'name':'Rote Hose',
    'description':'ich bin der Test mit der Roten Hose',
    'price':99.50,
    'lagerbestand':50
}

#ArtikelUpdate(3, update_variable)


def ArtikelDelete(id):
    # Artikel delete
    print('Artikeln löschen')
    print(artikeln)
    for index,item in enumerate(artikeln):
        #print(item['id'])
        if item['id'] == id:
            artikeln.pop(index)
            print(index)

    print(repr(artikeln))

#ArtikelDelete(7)

def warenKorb(id):
    # wahrenkorb erweitern
    # um einen Artikel mit der ID
    for item in artikeln:
        if item['id'] == id:
            korb.append(item)
            print("die artikel now gewählt" ,korb)
#funktions aufruf
#warenKorb(7)


def artikelstand():
    print(len(korb))
    if len(korb) > 0:
        print('korb ist nicht leer')
    else:
        print('korb ist leer')


#functions aufruf
artikelstand()



#frontend
def allArticls():
    for value in artikeln:
        print(value['name'],value['id'],)

allArticls()