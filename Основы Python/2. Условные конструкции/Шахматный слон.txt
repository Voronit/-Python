Vertical1 = int(input ("Enter the vertical number of the cell where the elephant stands: "))
Horizontal1 = int(input ("Enter the horizontal cell number where the elephant stands: "))
Vertical2 = int(input ("Enter the vertical number of the cell where you want to place the elephant: "))
Horizontal2 = int(input ("Enter the horizontal cell number where you want to place the elephant: "))

if ((Vertical1 - Vertical2 == Horizontal1 - Horizontal2) or (Vertical1 - Vertical2 == Horizontal2 - Horizontal1)):
  print("YES")
else:
  print("NO")