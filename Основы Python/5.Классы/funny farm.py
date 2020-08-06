class Animals ():                                #General class of animals
  
  hunger = "Yes"                                 #Field that indicates whether the animal is hungry

  def feed(self):                                #The function with which we feed our animals
    if self.hunger == "Yes":
      print ("You fed " + self.name)
      self.hunger = "No"
    else:
      print ("This animal is already fed")

  def voice (self):
    print(self.name + " talking: " + self.voice) #The function by which animals give voice

class Milk (Animals):                            #The general class of lactating animals, i.e. cows and goats

  milk = "Yes"                                   #A field that shows whether the animal can be milked at the moment

  def milk_an_animal (self):                     #The function with which we milk animals
    if self.milk == "Yes":
      print ("You milked " + self.name)
      self.milk = "No"
    else:
      print ("You have already milked this animal")

class Cows (Milk):                        #Cow class

  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight

class Goat (Milk):                        #Goat class

  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight

class Poultry (Animals):                  #General class of poultry

  eggs = "Yes"                            #A field that shows whether it is currently possible to collect eggs from an animal

  def collect_eggs (self):                #The function with which we collect eggs
    if self.eggs == "Yes":
      print ("You collected eggs from " + self.name)
      self.eggs = "No"
    else:
      print ("This animal has already collected eggs")

class Chicken (Poultry):                  #Chicken class
  
  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight
  
class Goose (Poultry):                    #Geese class
  
  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight

class Duck (Poultry):                     #Ducks class
  
  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight

class Sheep (Animals):                    #Sheep class, inherited only from Animals

  wool = "Yes"                            #The field that shows whether it is possible to collect wool from the animal at the moment

  def to_cut (self):                      #The function with which we shear sheep
    if self.wool == "Yes":
      print ("You collected wool from " + self.name)
      self.wool = "No"
    else:
      print ("This animal has already collected wool")

  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight


l_an = []                                  #List with all objects of class Animals

goose_1 = Goose ("goose_1", "gagaga!", 3)
l_an.append(goose_1)
goose_1.feed()
goose_1.collect_eggs()

goose_2 = Goose ("goose_2", "gagaga?!", 2.5)
l_an.append(goose_2)
goose_2.feed()
goose_2.collect_eggs()

cow = Cows ("cow", "Muuu", 500)
l_an.append(cow)
cow.feed()
cow.milk_an_animal()

sheep_1 = Sheep ("sheep_1", "Beee", 60)
l_an.append(sheep_1)
sheep_1.feed()
sheep_1.to_cut()

sheep_2 = Sheep ("sheep_2", "beeeee", 50)
l_an.append(sheep_2)
sheep_2.feed()
sheep_2.to_cut()

chicken_1 = Chicken ("chiken_1", "kudah tah tah", 1.5)
l_an.append(chicken_1)
chicken_1.feed()
chicken_1.collect_eggs()

chicken_2 = Chicken ("chiken_2", "kukareku!", 2)
l_an.append(chicken_2)
chicken_2.feed()
chicken_2.collect_eggs()

goat_1 = Goat ("goat_1", "mmeeee", 40)
l_an.append(goat_1)
goat_1.feed()
goat_1.milk_an_animal()

goat_2 = Goat ("goat_2", "Mee", 55)
l_an.append(goat_2)
goat_2.feed()
goat_2.milk_an_animal()

duck = Duck ("duck", "Crea", 1)
l_an.append(duck)
duck.feed()
duck.collect_eggs()

max_weight = 0                                               #Variable to record the weight of the heaviest animal
max_weight_name = "noon"                                     #Variable to write the name of the heaviest animal
all_weight = 0                                               #Variable to record the total weight of all animals
for animal in l_an:
  all_weight += animal.weight
  if animal.weight > max_weight:
    max_weight = animal.weight
    max_weight_name = animal.name
print ("The heaviest animal is " + max_weight_name)
print ("The weight of all animals is " + str(all_weight))