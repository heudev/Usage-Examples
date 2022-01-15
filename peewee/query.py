from database import *

# Yeni kayıt oluşturur
save = Table1.create(username="D1STANG3R", userid=234)
save.save()

# ------------------------------------------------

# Tüm tabloyu getirir.
data = Table1.select()
for x in data:
    print(x.id, x.username)

# Belirtilen değere ait kayıtları getirir.
data = Table1.select().where(Table1.username == "D1STANG3R")
for x in data:
    print(x.id, x.username)

# Belirtilen değere göre alfabetik olarak sıralar.
data = Table1.select().where(Table1.username == "D1STANG3R").order_by(Table1.id.desc())
for x in data:
    print(x.id, x.username)

# Belirtilen değere göre alfabenin tersi olarak sıralar.
data = Table1.select().where(Table1.username == "D1STANG3R").order_by(Table1.id.asc())
for x in data:
    print(x.id, x.username)

# Belirtilen değere ait kayıt sayısını söyler.
count = Table1.select().where(Table1.username == "D1STANG3R" and Table1.id == 3).count()
print(count)

# Belirtilen miktarda kayıt getirir
data = Table1.select().where(Table1.username == "D1STANG3R").limit(3)
for x in data:
    print(x.id, x.username)

# username kolonunda "D1STANG3R" değerini içeren kayıtları getirir.
data = Table1.select().where(Table1.username.contains("D1STANG3R"))
for x in data:
    print(x.id, x.username)

# Random kayıt getirir.
data = Table1.select().order_by(fn.Random()).limit(1)
for x in data:
    print(x.id, x.username)

# ------------------------------------------------

# Table1 tablosunu siler.
Table1.drop_table()

# Table1 tablosundaki tüm kayıtları siler.
Table1.delete().execute()

# Belirtilen değere ait kayıtları siler.
Table1.delete().where(Table1.username == "D1STANG3R").execute()

# ------------------------------------------------

# username tablosunda "D1STANG3R" değerine sahip olan kayıtları "DISTANGER" ve 12 olarak değiştirir.
Table1.update({Table1.username: "DISTANGER", Table1.userid: 12}).where(Table1.username == "D1STANG3R").execute()
