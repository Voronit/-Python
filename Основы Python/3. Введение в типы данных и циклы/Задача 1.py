girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']

if len(girls) == len(boys):
  girls.sort ()
  boys.sort ()
  print("Perfect couples:")
  for i, j in zip(girls, boys):
    print(i + " è " + j)

else:
  print("Someone may not have enough pair, the program will not run")