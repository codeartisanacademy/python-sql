import sqlite3

class Location:
    def __init__(self, name, population):
        self.name = name
        self.population = population
    
    # self is a must if the function inside a class
    def connect(self, db):
        db = sqlite3.connect(db)
        return db

    def insert(self):
        db = self.connect('locationapp/locationdb.db')
        cursor = sqlite3.Cursor(db)
        insert = "INSERT INTO locations (name, population) VALUES ('{0}', '{1}')".format(self.name, self.population)
        cursor.execute(insert)
        db.commit()
        print("inserted")

# jakarta = Location(name='Jakarta', population=12000000)
#jakarta.insert()

# bandung = Location(name='Bandung', population=3000000)
#bandung.insert()

city_name = input('Enter the name of the city: ')

city_popuplation = input('Enter the population: ')

city = Location(name=city_name, population=int(city_popuplation))
city.insert()
