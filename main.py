def getSpaces(num):
  return " "*num

def appendSpaces(base, targetLength):
  return str(base) + getSpaces(targetLength - len(str(base)))

class Table:
  spacing = []
  def __init__(self, spacing):
    self.spacing = spacing

  def printRow(self, items):
    for index, item in enumerate(items):
      print(f"{appendSpaces(item, self.spacing[index])}", end="")
    print()

def sqrt(target, margin=0, maxIterations=1000, printSteps=False):
  increment = 1
  estimate = 0
  prevToLarge = False

  index = 0

  if (printSteps):
    table = Table([7, 24, 24, 24])
    table.printRow(["index", "estimate", "error", "increment"])

  while(index < maxIterations):
    error = (estimate+increment)**2 - target

    if(printSteps):
      table.printRow([index, estimate, error, increment])

    if(error > 0):
      increment /= 2.0
      prevToLarge = True
    elif (error < 0):
      estimate += increment
      if(prevToLarge):
        increment /= 2.0
      else:
        increment *= 2.0
    else:
      break
    
    if(abs(error) < margin):
      break
    index += 1
  return estimate + increment, index

square = float(input("Please enter the number you want to find the sqaure root of: "))
print()

table = Table([10, 22, 22, 7]);
table.printRow(["Margin", "Root", "Square", "Steps"])

for i in range(0, -10, -1):
  margin = 10**i
  root, steps = sqrt(square, margin)
  table.printRow([margin, root, root**2, steps])

root, steps = sqrt(square, 0, 100)
table.printRow(["0", root, root**2, steps])

