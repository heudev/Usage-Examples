from peewee import *

db = SqliteDatabase('data.db')


class BaseModel(Model):
    class Meta:
        database = db


class Table1(BaseModel):
    id = AutoField()
    username = CharField(max_length=50, null=True)
    userid = IntegerField(null=True)
    text = TextField(null=True)


class Table2(BaseModel):
    id = AutoField()
    username = CharField(null=True)
    password = CharField(null=True)


db.connect()
db.create_tables([Table1, Table2], safe=True)
