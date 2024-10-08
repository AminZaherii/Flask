import db


def get_categories():
    query = 'SELECT * FROM category'
    categories_db = db.fetch(query)
    keys = ('id', 'name')
    categories = [
        dict(zip(keys, values))
        for values in categories_db
    ]
    return categories


def add_category(category_name):
    query = f"insert into category(name) values (N'{category_name}')"
    response = db.insert(query)
    return response


def get_category_by_id(category_id):
    query = f"SELECT * FROM category where id = {category_id}"
    category = db.fetch(query)
    return dict(category)
