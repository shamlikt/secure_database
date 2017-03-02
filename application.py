import peewee
import bcrypt

from playhouse.sqlcipher_ext import *

database='user_data.db'
db = SqlCipherDatabase(database, passphrase='testtest') # Key must store in some secure path ; then import from there


class Category(Model):
    category_id = IntegerField(unique=True)
    category_name = TextField()

    class Meta:
        database = db

class Customer(Model):
    customer_id = IntegerField(unique=True)
    category= ForeignKeyField(Category, related_name='category')
    age = IntegerField()
    phone = CharField()
    address = TextField()
    customer_name = CharField()
    password=CharField()
    class Meta:
        database = db


class DuplicateEntry(Exception):
    def __init__(self, message):
        self.message=message

class DataError(ValueError):
    def __init__(self, message):
        self.message=message

def access_db(password):
    global db
    try:
        db = SqlCipherDatabase(database, passphrase=password)
        if not db.get_tables():
            db.create_tables([Category, Customer])
        return db
    except:
        return None

def hash_password(p_password):
    return bcrypt.hashpw(p_password, bcrypt.gensalt())

def add_category(name, cat_id):
    try:
        obj = Category(category_id=cat_id, category_name=name)
        obj.save()
    except peewee.IntegrityError:
        raise DuplicateEntry('{} is already assigned, Please enter another id'.format(cat_id))

def show_all_category():
    category = []
    for cat in Category.select():
        category.append(cat.category_name)
    return category

def delete_entry(r_id, category=True):
    if category:
        query = Category.delete().where(Category.category_id==r_id)
        query.execute()
    else:
        query = Customer.delete().where(Customer.customer_id==r_id)
        query.execute()
        
def add_customer(c_id, c_name, category, age, phone, address, password):
    password = hash_password(password)
    category = Category.get(category_name=category)

    obj = Customer(customer_id=c_id,
                          customer_name=c_name,
                          category=category,
                          age=age,
                          phone=phone,
                          address=address,
                          password=password
                          )
                          
    try:
        obj.save()
    except peewee.IntegrityError:
        raise DuplicateEntry('{} is already assigned, Please enter another id'.format(c_id))
    return obj

def check_int(value, value_name):
    response={}
    try:
        int(value)
    except ValueError:
        response[value_name] = 'Value must be integer'
    return response

def validate_category(cat_id, cat_name):
    response={}
    response.update(check_int(cat_id, 'category id'))
    if not cat_name:
        response['Category name'] = 'Name not be empty'
    return response

def validate_customer_data(c_id, c_name, category, age, phone, address, password):
    response={}
    response.update(check_int(c_id, 'Customer id'))
    response.update(check_int(age, 'Age'))
    response.update(check_int(phone.strip('+').replace(' ',''), 'Phone number'))
    if not c_name:
        response['Customer name'] = 'Name not be empty'
    if not password:
        response['Password'] = 'Password not be empty'
    return response

def get_data(id, category=True):
    if category:
        try:
            value = Category.get(category_id=id)
            return value
        except Category.DoesNotExist:
            raise DataError('Id Does not exit please try again')
    else:
        try:
            value = Customer.get(category_id=id)
            return value
        except Customer.DoesNotExist:
            raise DataError('Id Does not exit please try again')

def update_category(obj, cat_id, cat_name):
    try:
        value = Category.get(Category.category_id==cat_id)
        if value:
            raise DuplicateEntry('Id already selected assigned for {}'.format(value.category_name))
    except Category.DoesNotExist as e:
        obj.category_id = cat_id
        obj.category_name = cat_name
        obj.save()
