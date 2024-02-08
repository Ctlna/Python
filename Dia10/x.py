#import datetime
import json
dici=open("data.json")
pausar=json.load(dici)

#crear
print(pausar["ventas"])
nuevo=str(input("c: "))
nueto = json.loads(nuevo)
pausar["ventas"].append(nueto)
print(pausar["ventas"])

#a