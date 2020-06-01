# Python program to read 
# json file 
  
  
import json 

# Opening JSON file 
f = open('C:/Users/nitg/DevNet/DevNetTrainingAssignments/data/db.json',) 
  
# returns JSON object as  
# a dictionary 
data1 = json.load(f) 
  
# Iterating through the json 
# list 
#for i in data1:
print("json: ")
print(data1) 
print('\n')
# Closing file 
f.close() 


import xml.etree.ElementTree as ET
tree = ET.parse('C:/Users/nitg/DevNet/DevNetTrainingAssignments/data/db.xml')
root = tree.getroot()
print("xml")
for child in root.iter():
    print(child.tag, child.attrib)
n=0
while(n<3):
    
    for x in root[n]:
        print(x.text)
    n=n+1
print('\n')    

import yaml

print("yaml")
with open(r'C:\Users\nitg\DevNet\DevNetTrainingAssignments\data\db.yml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    accounts_list = yaml.load(file, Loader=yaml.FullLoader)

    print(accounts_list)

