class Pet:

    # implement __init__( name , type , tricks ):
    def __init__(self, name , type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = 100
        self.energy = 50

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 4
        self.health += 10
        print(f"{self.name} has {self.health} health and {self.energy} energy")
        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    # noise() - prints out the pet's sound
    def noisee(self):
        print(self.noise)

class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name , treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        print(f"{self.pet.name} play with {self.first_name} so his health will increase by 5  and become {self.pet.health} also  his energy will deacrease by 15 and become {self.pet.energy}")
        return self
    
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):

        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!") #REMOVE THE LAST FOOD THAT THE PET WAS EATING
        else:
            print("Oh no!!! you need more pet food!")
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noisee()

my_treats = ['Snausage','Bacon',"Trash Bag"]
my_pet_food = ['salmon','fish']

fluffy = Pet("Fluffy","cat",['noisy','is invisible'],"mio mio")

asma = Ninja("Asma","manssour",my_treats,my_pet_food, fluffy)
asma.walk()
asma.bathe()
asma.feed()
asma.feed()
asma.feed()
fluffy.eat()










