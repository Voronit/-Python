class Animals ():                                  #����� ����� ��������
  
  hunger = "Yes"                                   #����, ������� ����������, ������� �� ��������

  def feed(self):                                  #�������, � ������� ������� �� ������ ����� ��������
    if self.hunger == "Yes":
      print ("�� ��������� " + self.name)
      self.hunger = "No"
    else:
      print ("��� �������� ��� �����������")

  def voice (self):
    print(self.name + " �������: " + self.voice)   #�������, � ������ ������� �������� ������ �����

class Milk (Animals):                              #����� ����� ������������ ��������, �.�. ����� � ���

  milk = "Yes"                                     #����, ������� ����������, ����� �� � ������ ������ ������� ��������

  def milk_an_animal (self):                       #�������, � ������ ������� �� ���� ��������
    if self.milk == "Yes":
      print ("�� ������� " + self.name)
      self.milk = "No"
    else:
      print ("��� �������� ��� �������")

class Cows (Milk):                                 #����� �����

  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight

class Goat (Milk):                                 #����� ���

  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight

class Poultry (Animals):                           #����� ����� �������� �����

  eggs = "Yes"                                     #����, ������� ����������, ����� �� � ������ ������ ������� ���� � ���������

  def collect_eggs (self):                         #�������, � ������ ������� �� �������� ����
    if self.eggs == "Yes":
      print ("�� ������� ���� � " + self.name)
      self.eggs = "No"
    else:
      print ("� ����� ��������� ���� ��� �������")

class Chicken (Poultry):                           #����� �����
  
  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight
  
class Goose (Poultry):                             #����� �����
  
  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight

class Duck (Poultry):                              #����� ����
  
  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight

class Sheep (Animals):                             #����� ����, ������������ ������ �� Animals

  wool = "Yes"                                     #����, �������� ����������, ����� �� ������� ����� � ��������� � ������ ������

  def to_cut (self):                               #�������, � ������� ������� �� ������� ����
    if self.wool == "Yes":
      print ("�� ������� ������ � " + self.name)
      self.wool = "No"
    else:
      print ("� ����� ��������� ������ ��� �������")

  def __init__ (self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight


l_an = []                                          #������ �� ����� ��������� ������ Animals

goose_1 = Goose ("goose_1", "������!", 3)
l_an.append(goose_1)
goose_1.feed()
goose_1.collect_eggs()

goose_2 = Goose ("goose_2", "������?!", 2.5)
l_an.append(goose_2)
goose_2.feed()
goose_2.collect_eggs()

cow = Cows ("cow", "����", 500)
l_an.append(cow)
cow.feed()
cow.milk_an_animal()

sheep_1 = Sheep ("sheep_1", "���", 60)
l_an.append(sheep_1)
sheep_1.feed()
sheep_1.to_cut()

sheep_2 = Sheep ("sheep_2", "���", 50)
l_an.append(sheep_2)
sheep_2.feed()
sheep_2.to_cut()

chicken_1 = Chicken ("chiken_1", "����� ��� ���", 1.5)
l_an.append(chicken_1)
chicken_1.feed()
chicken_1.collect_eggs()

chicken_2 = Chicken ("chiken_2", "��������!", 2)
l_an.append(chicken_2)
chicken_2.feed()
chicken_2.collect_eggs()

goat_1 = Goat ("goat_1", "������", 40)
l_an.append(goat_1)
goat_1.feed()
goat_1.milk_an_animal()

goat_2 = Goat ("goat_2", "����", 55)
l_an.append(goat_2)
goat_2.feed()
goat_2.milk_an_animal()

duck = Duck ("duck", "��� ���", 1)
l_an.append(duck)
duck.feed()
duck.collect_eggs()

max_weight = 0                                               #����������, � ������� ������������� ��� ������ �������� ���������
max_weight_name = "noon"                                     #����������, � ������� ������������� ��� ������ �������� ���������
all_weight = 0                                               #����������, � ������� ������������� ����� ��� ���� ��������
for animal in l_an:
  all_weight += animal.weight
  if animal.weight > max_weight:
    max_weight = animal.weight
    max_weight_name = animal.name
print ("����� ������� ��������: " + max_weight_name)
print ("��� ���� �������� �����: " + str(all_weight))