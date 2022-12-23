import json
import math
from tabulate import tabulate

# Data from the experiment
data = {
    1:{ # car 1
        "pulse_min":{
            "first_try" : [0.348],
            "second_try" : [0.351],
            "average_time" : []
        },
        "pulse_mid":{
            "first_try" : [0.214],
            "second_try" : [0.217],
            "average_time" : []
        },
        "pulse_max":{
            "first_try" : [0.163],
            "second_try" : [0.163],
            "average_time" : []
        }
    },
    2:{ # car 2
        "pulse_min":{
            "first_try" : [0.442],
            "second_try" : [0.415],
            "average_time" : []
        },
        "pulse_mid":{
            "first_try" : [0.287],
            "second_try" : [0.291],
            "average_time" : []
        },
        "pulse_max":{
            "first_try" : [0.225],
            "second_try" : [0.225],
            "average_time" : []
        }
    }
}

# calculate average_time for each car and each pulse (min, mid and max)
for car in data.items(): # get each car
    for pulse in car[1].items(): # get each pulse
        average_time = [round((f + pulse[1]["second_try"][i])/2,3) for i,f in enumerate(pulse[1]["first_try"])]
        data[car[0]][pulse[0]]["average_time"] = average_time # update average_time for each car and pulse in the experiment data

print(json.dumps(data, indent=4))

# display experiment data in tabular form as required in experiment sheet
data_table = {
    "Car":[1,2],
    "Pulse Min dt[s]": [data[1]["pulse_min"]["average_time"][0],data[2]["pulse_min"]["average_time"][0]],
    "pulse Mid dt[s]":[data[1]["pulse_mid"]["average_time"][0],data[2]["pulse_mid"]["average_time"][0]],    
    "pulse Max dt[s]": [data[1]["pulse_max"]["average_time"][0],data[2]["pulse_max"]["average_time"][0]],
}
print ("\n\n Experiment Data Table: \n Determining the time for calculating the instantaneous velocity:\n", "-"*65 , "\n")
print(tabulate(data_table, headers="keys", tablefmt="grid"))

# calculation of velocity, momemtum and kinetic energy for each pulse
LENGTH_APERTURE = 0.1 # in meter
MASS_CART_1 = 0.397 # in kg
MASS_CART_2 = 0.382 # in kg


data_table_calculations_cart1 ={
    "Calculations" :["v[m/s]","p[kg*m/s]","E[kg*m²/s²]"],
}

for item in data_table.items():
    if item[0] == "Car":
        continue
    dt = round(item[1][0],3) # delta t
    velocity = round(LENGTH_APERTURE / dt,3) # velocity of cart 1 while pulse min
    momentum = round(MASS_CART_1 * velocity,3)
    kinetic_energy = round(0.5 * MASS_CART_1 * velocity**2,3)

    key = item[0].replace("dt[s]","")
    data_table_calculations_cart1[key] = [velocity, momentum, kinetic_energy]

print ("\n\n Calculation of velocity v, momentum p and kinetic energy Ekin by pulse min. pulse mid and pulse max.:\n", "-"*85 , "\n")
print("\n\n For cart 1:\n", "-"*15 , "\n")
print(tabulate(data_table_calculations_cart1, headers="keys", tablefmt="grid"))


# for cart 2
data_table_calculations_cart2 ={
    "Calculations" :["v[m/s]","p[kg*m/s]","E[kg*m²/s²]"],
}
for item in data_table.items():
    if item[0] == "Car":
        continue
    dt = round(item[1][1],3) # delta t with index 1 is for cart 2
    velocity = round(LENGTH_APERTURE / dt,3) # velocity of cart 1 while pulse min
    momentum = round(MASS_CART_2 * velocity,3)
    kinetic_energy = round(0.5 * MASS_CART_2 * velocity**2,3)

    key = item[0].replace("dt[s]","")
    data_table_calculations_cart2[key] = [velocity, momentum, kinetic_energy]

print("\n\n For cart 2:\n", "-"*15 , "\n")
print(tabulate(data_table_calculations_cart2, headers="keys", tablefmt="grid"))