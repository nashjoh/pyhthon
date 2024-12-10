#classes are like blueprints🤷‍♂️

class vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def moves (self):
        print('moves along...')

    def get_make_model(self):
        print(f"i'm a {self.make} {self.model}.")

my_car = vehicle('tesla','model 3')

#print(my_car.make)
#print(my_car.model)
my_car.get_make_model()
my_car.moves()


your_car = vehicle('cardillac','escalade')
your_car.get_make_model()
your_car.moves()


class Airplane(vehicle):
    def __init__(self,make,model,faa_id):
        super().__init__(make,model)#here by super function its gonna inherit the make and model frpm the parent.
        self.faa_id = faa_id
    def moves(self):
        print('flies along...')

class Truck(vehicle):
     def moves(self):
        print('rumbles along...')

class autorikshaw(vehicle):
     pass

cessna = Airplane('cesna','skyhawk','N-123')
mack = Truck ('mack','pinnacle')
mahindra = autorikshaw('mahindra','100')


cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
mahindra.get_make_model()
mahindra.moves()

print("\n\n")

#polymorphism
for v in (my_car,your_car,cessna,mack,mahindra):
    v.get_make_model()
    v.moves()