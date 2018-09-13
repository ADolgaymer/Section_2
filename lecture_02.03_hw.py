from pprint import pprint
from collections import Counter

#==========JSON==========
print('=============JSON=============')
import json
with open('files/newsafr.json') as datafile:
  json_data = json.load(datafile)
  description_list = list()
  word_list = list()
  n = 0
  k = 0
  for news in json_data['rss']['channel']['items']:
    description_list.append(json_data['rss']['channel']['items'][n]['description'])
    n += 1
  for items in description_list:
    word_list += (description_list[k].split())
    k += 1

six_letters = list()
for word in word_list:
  if len(word) > 6:
    six_letters.append(word)
counts_list = []
for items in Counter(six_letters).items():
  counts_list.append(items)
top_10 = sorted(counts_list, key=lambda item: item[1], reverse=True)
print(top_10[:10])
# print(Counter(six_letters))

#==========XML==========
print('=============XML=============')
import xml.etree.ElementTree as ET
tree = ET.parse('files/newsafr.xml')
descriptions = []
root = tree.getroot()
# print(root.tag)
# print(root.attrib)
xml_title = root.find('channel/title')
# print(xml_title.text)
xml_items = root.findall('channel/item')
# print('Всего новостей в ленте:', len(xml_items))
# print(xml_items)

for desc in xml_items:
  description = desc.find('description')
  descriptions += description.text.split(' ')
  # print(description.text)

def sortByLength(inputStr):
  return len(inputStr)

descriptions.sort(key=sortByLength, reverse=True)
# print(descriptions)

six_letters_xml = list()

for word in descriptions:
  if len(word) > 6:
    six_letters_xml.append(word)
counts_list = []
for items in Counter(six_letters_xml).items():
  counts_list.append(items)
top_10 = sorted(counts_list, key=lambda item: item[1], reverse=True)
print(top_10[0:10])

print('=============ПРИМЕЧАНИЕ=============')
print('''В новостях три слова, которые встречаются три раза:
- природы: 13,
- долларов: 13,
- Safaris: 13.
Списки топ-10 отличаются последним словом, поскольку Python случайным образом выбирает одно из трёх слов, встретившихся 13 раз.''')