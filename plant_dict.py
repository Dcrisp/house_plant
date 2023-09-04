#creating a log to enter plants into

#plant name
#quantity
#hydration range, upper_limit, lower_limit
#input log to check last water
#real time date tracker
#water frequency
import pandas as pd #for working with data
from pathlib import Path #working with file paths
import csv

data_file_path = Path( "data", "house_plant_inventory.csv")
plant_list = pd.read_csv(data_file_path)
house_plant_dict = [

]
import datetime #working with live date/time
current_time = datetime.datetime.now()
print("Hi Daniel, the time now is:",current_time)


def plant_id(house_plant_inventory):
    plant_name = input('What is the name of your new plant? ')
    print(f'A {plant_name}! good choice')
    water_sched = input('How frequently (days) does your mew plant require water? ')
    print((f'okay I will remind you every {water_sched} days to water your {plant_name}'))
    house_plant_inventory[plant_name] = water_sched
    print(f'I have added your {plant_name} to your list of house plants, here is your full plant list!')
    house_plant_dict[plant_name, water_sched]
    file = open("house_plant_inventory.csv", 'a', newline='')
    writer = csv.writer(file)
    writer.writerows(house_plant_dict)
    file.close()
    print(house_plant_inventory)



plant_id(plant_list)



# adds a plant to the list but need to figure out how to save this addition
# need to add lines to rows not columns


