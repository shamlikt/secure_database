import datetime

from playhouse.sqlcipher_ext import *

db = SqlCipherDatabase('user_data.db', passphrase='testtest')


class Category(Model):
    category_id = IntegerField()
    category_name = CharField()

    class Meta:
        database = db

class Customer(Model):
    customer_id = IntegerField()
    category_id = ForeignKeyField(Category, related_name='category')
    age = IntegerField()
    phone = CharField()
    address = TextField()
    customer_name = CharField()

    class Meta:
        database = db
