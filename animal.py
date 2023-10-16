class Animal:
  def __init__(self, name, classification, size, color, weight):  #constructor
    self.name = name
    self.classification = classification
    self.size = size
    self.color = color
    self.weight = weight

  
  def __str__(self): #returns the given string, if not there, return memory address
    detail = f"name: {self.name}, classification: {self.classification}, size: {self.size}, color: {self.color}, weight: {self.weight}"
    return detail

  def __eq__(self, other)  :  #comparison method
    if self.classification == other.classification and self.size == other.size:
      return True
    else:
      return False
  def __repr__(self):  #returns class name if nothing is given in str method. backup for str method
    return f"{self.__class__.__qualname__}"

  def __ne__(self, other):
    if self.weight < other.weight or self.weight > other.weight:
      return True
    else:
      return False
  #def __hash__(self):
    #return hash((self.color, self.weight))

  def __lt__(self, other):
    if self.weight <= other.weight:
      return True
    else: 
      return False

  def __ge__(self, other):
    if self.weight >= other.weight:
      return True
    else:
      return False

  def moves(self):
    return f"{self.name} moves perfectly"

  def eats(self):
    return f"{self.name} eats well"

  def barks(self):
    return f"This {self.name} barks so loud"
    
  @staticmethod
  def moving(legs):
    x = f"Animals walk on {legs}"
    return x


class FourLegged():
  def __init__(self,name):
    self.name = name

  def walkson(self):  
   return f"{self.name} walks on four legs"

class Child(Animal, FourLegged):
  pass
elephant = Child("Elephant", "Mammal", "Big", "Black", 100) 
#print(elephant.moves(), elephant.walkson())

  

animal_details = [Animal("German Shephard", "Mammal", "Medium", "Brown", 70), Animal("Domestic Cat", "Mammal", "Small", "Cream", 60), Animal("Red Fox", "Mammal", "Small", "Red", 96) ]
#animals = [dog, cat, fox]
animals = ["Dog", "Cat", "Fox"]
dog = Animal("German Shephard", "Mammal", "Medium", "Brown", 70)
cat = Animal("Domestic Cat", "Mammal", "Small", "Cream", 60)
fox = Animal("Red Fox", "Mammal", "Small", "Red", 96)

#for x,y in zip(animals, animal_details):
  #print(f"{x} is {y}")

#def __del__(self):   #destructor method
  #x = "deleted"
  #return x
#print(dog.hash(color))  
print(dog.moving("4 legs"))  
print(dog < cat or dog > cat)  
print(dog <= cat)
print(dog >= cat)
#print(type(animals))
#print(animals[0])
#print(cat.classification)
#print(dog.barks())
print(dog)
#print(animals[0]==animals[1])
print(cat == fox)
    
  