from pymongo import MongoClient
#pip install pymongo[srv]
#pip install dnspython==2.0.0

myclient = MongoClient("mongodb+srv://")
mydb = myclient["qwe"] #db
mycol = mydb["qwe"] #cluster

# Tüm veritabanlarını listeler
print(myclient.list_database_names())

# Tüm cluster'ları listeler
print(mydb.list_collection_names())

#---------------------------------------------------------------------

# Kayıt ekleme.
mydict = { "name": "Peter", "address": "Lowstreet 27" }
x = mycol.insert_one(mydict)  
print(x.inserted_id)

# Birden çok kayıt ekleme.
mylist = [
  { "_id": 1, "name": "John", "address": "istanbul"},
  { "_id": 2, "name": "Peter", "address": "izmir"},
  { "name": "William", "address": "Central st 954"},
]
x = mycol.insert_many(mylist)
print(x.inserted_ids)

#---------------------------------------------------------------------

# Tüm kayıtları listeler.
for x in mycol.find():
  print(x["name"])

#Koşullu listeleme.
for x in mycol.find({ "_id": 0, "name": "enes" }):
  print(x)

# Belirli sayıda kayıt listeler.
myresult = mycol.find().limit(5)
for x in myresult:
  print(x)

# address colonunda S ile başlayan kayıtları listeler.
for x in mycol.find({ "address": { "$regex": "^S" } }):
  print(x)

# sonuçları name'e göre alfabetik olarak sıralar.
mydoc = mycol.find().sort("name")
for x in mydoc:
  print(x)

# sonuçları name'e göre alfabetik olarak ters sıralar.
mydoc = mycol.find().sort("name", -1)
for x in mydoc:
  print(x)

#---------------------------------------------------------------------

# Belirtilen değere ait kayıtları siler.
mycol.delete_one({ "address": "Mountain 21" })

# Collection'daki tüm kayıtıları siler.
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")

# Collection'ı siler.
mycol.drop()

#---------------------------------------------------------------------

# Belirtilen kaydı yeni kayıt ile günceller.
myquery = { "address": "mugla" }
newvalues = { "$set": { "address": "aydin" } }
x = mycol.update_one(myquery, newvalues)
print(x.modified_count, "documents updated.")

# S harfi ile başlayan tüm kayıtları günceller.
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }
x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "documents updated.")
