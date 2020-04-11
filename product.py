import sqlite3

# we connect to the database file, or create the file if not exists
db = sqlite3.connect('productdb.db')

# sql command to select all
select_all = 'SELECT * FROM products'

# create the cursor object to do the database operation
cursor = sqlite3.Cursor(db)

# let cursor do the command
cursor.execute(select_all)

# get all the data from the cursor operation
products = cursor.fetchall()

print(products[0][1])
print(products[1][1])

print("{0} - IDR. {1}".format(products[0][1], products[0][3]))

for item in products:
    print("{0} - IDR. {1} - Stock available: {2}".format(item[1], item[3], item[4]))


def get_product_by_id(id):
    # example: SELECT * FROM products WHERE id=1
    select_product = 'SELECT * FROM products WHERE id={0}'.format(id)
    cursor.execute(select_product)
    product = cursor.fetchone()
    return product

selected_product = get_product_by_id(1)
print("{0} - IDR. {1}".format(selected_product[1], selected_product[3]))

def get_products_by_keyword(keyword):
    select_by_keywords = "SELECT * FROM products WHERE name LIKE '%{0}%'".format(keyword)
    cursor.execute(select_by_keywords)
    selected_products = cursor.fetchall()
    return selected_products

playstation_products = get_products_by_keyword('play')

print(playstation_products)

def get_products_by_max_price(max_price):
    select_by_max_price = 'SELECT * FROM products WHERE price < {0}'.format(max_price)
    cursor.execute(select_by_max_price)
    selected_products = cursor.fetchall()
    return selected_products

cheap_products = get_products_by_max_price(5000000)

print(cheap_products)

def get_products_by_price_range(min_price, max_price):
    pass

def get_products_on_stock():
    pass

def add_product():
    insert_sql = "INSERT INTO products (name, description, price, stock) VALUES ('Code Vein', 'Best game ever', 400000, 5)"
    cursor.execute(insert_sql)
    db.commit()
    print('data added')

add_product()