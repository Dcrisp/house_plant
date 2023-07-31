#creating a log to enter plants into

#plant name
#quantity
#hydration range, upper_limit, lower_limit
#input log to check last water
#real time date tracker
#water frequency
import datetime
current_time = datetime.datetime.now()
print("Hi Daniel, the time now is:",current_time)
house_plant_inventory = {

}
def plant_id():
    plant_name = input('What is the name of your new plant? ')
    print(f'A {plant_name}! good choice')
    water_sched = input('How frequently (days) does your mew plant require water? ')
    print((f'okay I will remind you every {water_sched} days to water your {plant_name}'))
    house_plant_inventory[plant_name] = water_sched
    print(f'I have added your {plant_name} to your list of house plants, here is your full plant list!')
    print(house_plant_inventory)
plant_id()
# adds a plant to the list but need to figure out how to save this addition
