from datetime import date

from peewee import *

database = SqliteDatabase("C:\\Users\\Admin\\Downloads\\SQLiteDatabaseBrowserPortable\\Data\\example.db")


class BaseModel(Model):
    class Meta:
        database = database


class Vendor(BaseModel):
    cr = CharField()
    ch = CharField()
    name = CharField()


class CarModel(BaseModel):
    created = DateTimeField()
    changed = DateTimeField()
    name = CharField()
    vendor=ForeignKeyField(Vendor)


class CarBodyType(BaseModel):
    cr = CharField()
    ch = CharField()
    name = CharField()


class Car(BaseModel):
    count_wheel = IntegerField()
    vin = CharField()
    created = DateTimeField()
    changed = DateTimeField()
    issued = DateTimeField()
    model = ForeignKeyField(CarModel)
    body_type = ForeignKeyField(CarBodyType)


database.create_tables([Car, Vendor, CarModel, CarBodyType])
# car = Car(count_wheel="4", vin="qwerty", created=date(1990, 1, 1), changed=date(1990, 1, 1), issued=date(1990, 1, 1), model=Model())
# Car.insert(Car())