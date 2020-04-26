from HW4.orm import Modules


class User_info(Modules.Module):
    def __init__(self):
        self.name = Modules.TextField()
        self.surname = Modules.TextField()
        self.currency = Modules.IntegerField()


u = User_info()
u.create_table()
val = ('Nikita', "Tarasov", 1345)
u.add(val)
val = ("Alex", 'Jones', 2312)
u.add(val)
print(u.all())
print(u.get(name='Nikita'))
u.delete(currency=2312)


