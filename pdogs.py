class Dog:
    species = "caniche"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.numbers = [] # new number list for each dog
    
    #new method in class dog
    def get_biggest_number(self, numberlist): 
        self.numbers = numberlist
        self.max = max(numberlist)
        return self.max

bambi = Dog("Bambi",5)
mikey = Dog("Mikey",6)

#tree new instances for dogs class
gabi = Dog("Gabi",7)
fofo = Dog("Fofo",8)
miliki = Dog("Miliki",9)

print("{} is {} and {} is {} and {} is {} and {} is {} and {} is {}"
    . format(
        bambi.name, bambi.age, 
        mikey.name, mikey.age,
        gabi.name, gabi.age,
        fofo.name, fofo.age,
        miliki.name, miliki.age))

if bambi.species == "caniche":
        print("{0} is a {1}!". format(
        bambi.name, bambi.species))

#Maximum number in the dog's number list
Maximum = bambi.get_biggest_number([7,12,13,4,8,21,26,27,1,0])

print("{} has this number list: {} in its list"
    . format(
        bambi.name,
        bambi.numbers))

print("{} has this maximum number: {} in its list"
    . format(
        bambi.name,
        Maximum))
