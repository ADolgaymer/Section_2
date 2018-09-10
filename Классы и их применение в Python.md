# Section_2
Работа с файловой системой в Python

class FarmingAnimal:
  species = 'animal'
  voice = 0

      
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def feed(self, feed):
    self.feed = feed

  def distinguish(self, voice):
    if voice == 'ga-ga':
      self.species = 'Goose'
    elif voice == 'mu-mu':
      self.species = 'Cow'
    elif voice == 'be-be':
      self.species = 'Sheep'
    elif voice == 'zyp-zyp':
      self.species = 'Chicken'
    elif voice == 'me-me':
      self.species = 'Goat'
    elif voice == 'krya-krya':
      self.species = 'Duck'
    else:
      self.species = ("Unrecognized")
        
class Birds(FarmingAnimal):
  species = 'bird'
  eggs = 0

  def collect_eggs(self, value):
    self.eggs += value


class Hoofed(FarmingAnimal):
  species = 'hoofed'

class MilkProducing(Hoofed):
  species = 'milk producing'
  milk_yield = 0

  def milk(self, value):
    self.milk_yield += value

class WoolProducing(Hoofed):
  species = 'wool producing'
  wool = 0

  def shear(self, value):
    self.wool += value


animal_01 = Birds('Серый', 1.5)
animal_02 = MilkProducing('Манька', 350)
animal_03 = WoolProducing('Барашек', 90) 
animal_04 = Birds('Ко-ко', 0.8)
animal_05 = MilkProducing('Копыта', 58)
animal_06 = Birds('Кряква', 1.4)


animal_01.feed('yes')
animal_01.collect_eggs(3)
animal_01.distinguish('ga-ga')

animal_02.feed('yes')
animal_02.distinguish('mu-mu')
animal_02.milk(7)

animal_03.feed('yes')
animal_03.distinguish('be-be')
animal_03.shear(10)

animal_04.feed('yes')
animal_04.distinguish('zyp-zyp')
animal_04.collect_eggs(10)

animal_05.feed('yes')
animal_05.distinguish('me-me')
animal_05.milk(3)

animal_06.feed('yes')
animal_06.distinguish('krya-krya')
animal_06.collect_eggs(4)

animal_register = [animal_01.__dict__, animal_02.__dict__, animal_03.__dict__, animal_04.__dict__, animal_05.__dict__, animal_06.__dict__]

print(animal_register)

print('________________________')

weight_list = []
n = 0
for weight in animal_register:
  weight_list.append(animal_register[n]['weight'])
  n += 1
print('Самое тяжелое животное на ферме: ', max(weight_list), animal_register[weight_list.index(max(weight_list))]['species'])
print('Общий вес животных на ферме: ', sum(weight_list))
