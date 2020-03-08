import requests

'''
people = requests.get('http://api.open-notify.org/astros.json')

people_json = people.json()
print(people_json)

#number of people 
print("Number of people in space:",people_json['number'])

#pritning elements 
for p in people_json['people']:
    #rint(p['name'])
'''

# rhyming words
parameter = {"rel_rhy":"simple"}
request = requests.get('https://api.datamuse.com/words',parameter)

rhyme_json = request.json()
for i in rhyme_json[0:3]:
    print(i['word'])