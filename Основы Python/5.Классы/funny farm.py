class Animals ():                                  #Общий класс животных
  
  hunger = "Yes"                                   #Поле, которое показывает, голодно ли животное

  def feed(self):                                  #Функция, с помощью которой мы кормим наших животных
    if self.hunger == "Yes":
      print ("Вы покормили " + self.name)
      self.hunger = "No"
    else:
      print ("Это животное уже покормленно")

  def voice (self):
    print(self.name + " говорит: " + self.voice)   #Функция, с помощь которой животные подают голос

class Milk (Animals):                              #Общий класс молокодающих животных, т.е. коров и коз

  milk = "Yes"                                     #Поле, которое показывает, можно ли в данный момент подоить животное

  def milk_an_animal (self):                       #Функция, с помощь которой мы доим животных
    if self.milk == "Yes":
      print ("Вы подоили " + self.name)
      self.milk = "No"
    else:
      print ("Это животное уже подоино")

class Cows (Milk):                                 #Класс коров

  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight

class Goat (Milk):                                 #Класс коз

  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight

class Poultry (Animals):                           #Общий класс домашней птицы

  eggs = "Yes"                                     #Поле, которое показывает, можно ли в данный момент мобрать яйца у животного

  def collect_eggs (self):                         #Функция, с помощь которой мы собираем яйца
    if self.eggs == "Yes":
      print ("Вы собрали яйца у " + self.name)
      self.eggs = "No"
    else:
      print ("У этого животного яйца уже собраны")

class Chicken (Poultry):                           #Класс куриц
  
  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight
  
class Goose (Poultry):                             #Класс гусей
  
  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight

class Duck (Poultry):                              #Класс уток
  
  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight

class Sheep (Animals):                             #Класс овец, наследуеться только от Animals

  wool = "Yes"                                     #Поле, которгое показывает, можно ли собрать шерся у животного в данный момент

  def to_cut (self):                               #Функция, с помощью которой мы стрижем овец
    if self.wool == "Yes":
      print ("Вы собрали шерсть у " + self.name)
      self.wool = "No"
    else:
      print ("У этого животного шерсть уже собрана")

  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight


l_an = []                                          #Список со всеми объектами класса Animals

goose_1 = Goose ("goose_1", "гагага!", 3)
l_an.append(goose_1)
goose_1.feed()
goose_1.collect_eggs()

goose_2 = Goose ("goose_2", "гагага?!", 2.5)
l_an.append(goose_2)
goose_2.feed()
goose_2.collect_eggs()

cow = Cows ("cow", "мууу", 500)
l_an.append(cow)
cow.feed()
cow.milk_an_animal()

sheep_1 = Sheep ("sheep_1", "бее", 60)
l_an.append(sheep_1)
sheep_1.feed()
sheep_1.to_cut()

sheep_2 = Sheep ("sheep_2", "бее", 50)
l_an.append(sheep_2)
sheep_2.feed()
sheep_2.to_cut()

chicken_1 = Chicken ("chiken_1", "кудах тах тах", 1.5)
l_an.append(chicken_1)
chicken_1.feed()
chicken_1.collect_eggs()

chicken_2 = Chicken ("chiken_2", "кукареку!", 2)
l_an.append(chicken_2)
chicken_2.feed()
chicken_2.collect_eggs()

goat_1 = Goat ("goat_1", "ммееее", 40)
l_an.append(goat_1)
goat_1.feed()
goat_1.milk_an_animal()

goat_2 = Goat ("goat_2", "Меее", 55)
l_an.append(goat_2)
goat_2.feed()
goat_2.milk_an_animal()

duck = Duck ("duck", "Кря кря", 1)
l_an.append(duck)
duck.feed()
duck.collect_eggs()

max_weight = 0                                               #Переменная, в которую записываеться вес самого тяжелого животного
max_weight_name = "noon"                                     #Переменная, в которую записываеться имя самого тяжелого животного
all_weight = 0                                               #Переменная, в которую записываеться общий вес всех животных
for animal in l_an:
  all_weight += animal.weight
  if animal.weight > max_weight:
    max_weight = animal.weight
    max_weight_name = animal.name
print ("Самое тяжелое животное: " + max_weight_name)
print ("Вес всех животных равен: " + str(all_weight))