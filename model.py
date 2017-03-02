

from playhouse.sqlcipher_ext import *

database='user_data.db'


db = SqlCipherDatabase(database, passphrase='testtest')

class Category(Model):
    category_id = IntegerField(unique=True)
    category_name = CharField()

    class Meta:
        database = db

class Customer(Model):
    customer_id = IntegerField(unique=True)
    category_id = ForeignKeyField(Category, related_name='category')
    age = IntegerField()
    phone = CharField()
    address = TextField()
    customer_name = CharField()
    password=CharField()
    class Meta:
        database = db

if not db.get_tables():
    db.create_tables([Category, Customer])
    
