from datetime import date

from peewee import *

database = SqliteDatabase("C:\\Users\\Admin\\Downloads\\SQLiteDatabaseBrowserPortable\\Data\\example.db")


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    id = IntegerField(null=False, unique=True, primary_key=True)
    username = CharField()
    password = CharField()
    email = CharField()
    join_date = DateTimeField()


users = User.select().order_by(User.username)
# User.create_table([User])
for u in users:
    print(u.__dict__)
# User.insert(User(1, "Ivanov", "111", "i@ukr.net", "01-01-1999"))
# ivanov = User(username='Ivanov', password="222", email="ivanov@mail.com", join_date=date(1999, 1, 12))
# ivanov.save()
