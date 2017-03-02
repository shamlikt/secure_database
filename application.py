import peewee
import bcrypt

from model import Category, Customer

class DuplicateEntry(Exception):
    def __init__(self, message):
        self.message=message

class DataError(ValueError):
    def __init__(self, message):
        self.message=message
    
def hash_password(p_password):
    return bcrypt.hashpw(p_password, bcrypt.gensalt())

def add_category(name, cat_id):
    try:
        obj = Category.create(category_id=cat_id, category_name=name)
        return obj
    except peewee.IntegrityError:
        raise DuplicateEntry('{} is already assigned, Please enter another id'.format(cat_id))

def add_customer(c_id, c_name, category, age, phone, address, password):
    password = hash_password(password)
    obj = Customer(customer_id=c_id,
                          customer_name=c_name,
                          category=category,
                          age=age,
                          phone=phone,
                          addrss=address,
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

def update_category(obj, cat_id, cat_name):
    try:
        value = Category.get(Category.category_id==cat_id)
        if value:
            raise DuplicateEntry('Id already selected assigned for {}'.format(value.category_name))
    except Category.DoesNotExist as e:
        obj.category_id = cat_id
        obj.category_name = cat_name
        obj.save()

# def update_customer(obj, cat_obj, c_id, c_name, age, phone, address, password ):
#     try:
#         value = Category.get(Category.category_id==cat_id)
#         if value:
#             raise DuplicateEntry('Id already selected assigned for {}'.format(value.category_name))
#     except Category.DoesNotExist as e:
#         obj.category_id = cat_id
#         obj.category_name = cat_name
#         obj.save()

