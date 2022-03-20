#SELECT MAX(ID) AS LastID FROM Persons
from unicodedata import name
from peewee import SqliteDatabase,CharField,Model,IntegerField,fn

db = SqliteDatabase('Ollivanders.sqlite')
class Item(Model):
    name = CharField()
    sell_in = IntegerField()
    quality = IntegerField()
    class Meta:
        database = db

from repository.sqlite_db import Database

def get_last_id():
    db.connect()
    query = Item.select(fn.MAX(Item.id)) ##para obtener SELECT MAX(id) AS LastID FROM Item
    last_id = query.scalar() ##para tener un registro
    db.close()
    return last_id