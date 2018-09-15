from abc import ABCMeta

class FarmingAnimal:
  __metaclass__ = ABCMeta
  species = 'animal'
  voice = 'none'
  feed_acc = 0

      
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def feed(self, value):
    if self.feed_acc < 5: #считаем что животное не требуется кормить, если feed_acc превышает значение 5
      self.feed_acc += value
    else:
      self.feed_acc = 'not hungry'

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

# Гуси
animal_01 = Birds('Серый', 1.5)
animal_02 = Birds('Белый', 1.8)
# Корова
animal_03 = MilkProducing('Манька', 350)
# Овцы
animal_04 = WoolProducing('Барашек', 90) 
animal_05 = WoolProducing('Кудрявый', 94)
# Куры
animal_06 = Birds('Ко-ко', 0.8)
animal_07 = Birds('Кукареку', 0.67)
# Козы
animal_08 = MilkProducing('Копыта', 58)
animal_09 = MilkProducing('Рога', 53)
# Утка
animal_10 = Birds('Кряква', 1.4)


animal_01.feed(1)
animal_01.collect_eggs(3)
animal_01.distinguish('ga-ga')

animal_02.feed(1)
animal_02.collect_eggs(2)
animal_02.distinguish('ga-ga')

animal_03.feed(6)
animal_03.distinguish('mu-mu')
animal_03.milk(7)

animal_04.feed(2)
animal_04.distinguish('be-be')
animal_04.shear(10)

animal_05.feed(2)
animal_05.distinguish('be-be')
animal_05.shear(16)

animal_06.feed(1)
animal_06.distinguish('zyp-zyp')
animal_06.collect_eggs(10)

animal_07.feed(1)
animal_07.distinguish('zyp-zyp')
animal_07.collect_eggs(7)

animal_08.feed(3)
animal_08.distinguish('me-me')
animal_08.milk(3)

animal_09.feed(3)
animal_09.distinguish('me-me')
animal_09.milk(2)

animal_10.feed(2)
animal_10.distinguish('krya-krya')
animal_10.collect_eggs(4)


animal_register = [animal_01.__dict__, animal_02.__dict__, animal_03.__dict__, animal_04.__dict__, animal_05.__dict__, animal_06.__dict__, animal_07.__dict__, animal_08.__dict__, animal_09.__dict__,  animal_10.__dict__,]
print(animal_register)

print('______________________________________________')

weight_list = []
n = 0
for weight in animal_register:
  weight_list.append(animal_register[n]['weight'])
  n += 1
print('Самое тяжелое животное на ферме: ', max(weight_list), animal_register[weight_list.index(max(weight_list))]['species'])
print('Общий вес животных на ферме: ', round(sum(weight_list), 2))

print('______________________________________________')

animal_type = []
animal_name = []
for species in animal_register:
  animal_type.append(species.get('species'))
  animal_name.append(species.get('name'))
  type_name_reg = list(zip(animal_type, animal_name))
print('Всего животных:', len(type_name_reg))
print('Список животных: ', type_name_reg)
