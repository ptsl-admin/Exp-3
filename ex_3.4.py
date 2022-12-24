import json
import math
from tabulate import tabulate

# Data from the experiment
data = {
    "1":{ # car 1
        "pulse_min":{
            "first_try" : [0.348],
            "second_try" : [0.347],
            "average_time" : []
        },
        "pulse_mid":{
            "first_try" : [0.219],
            "second_try" : [0.219],
            "average_time" : []
        },
        "pulse_max":{
            "first_try" : [0.167],
            "second_try" : [0.161],
            "average_time" : []
        },
    },
    "1+2":{
        "pulse_min":{
            "first_try" : [0.632],
            "second_try" : [0.614],
            "average_time" : []            
        },
        "pulse_mid":{
            "first_try" : [0.412],
            "second_try" : [0.414],
            "average_time" : []
        },
        "pulse_max":{
            "first_try" : [0.322],
            "second_try" : [0.310],
            "average_time" : []
        },
    },
}

# calculate average_time for each car and each pulse (min, mid and max)
for car in data.items(): # get each car
    for pulse in car[1].items(): # get each pulse
        average_time = [round((f + pulse[1]["second_try"][i])/2,3) for i,f in enumerate(pulse[1]["first_try"])]
        data[car[0]][pulse[0]]["average_time"] = average_time # update average_time for each car and pulse in the experiment data

print(json.dumps(data, indent=4))

# display experiment data in tabular form as required in experiment sheet
data_table = {
    "Car":["1","1+2"],
    "Pulse Min dt[s]": [data["1"]["pulse_min"]["average_time"][0],data["1+2"]["pulse_min"]["average_time"][0]],
    "Pulse Mid dt[s]":[data["1"]["pulse_mid"]["average_time"][0],data["1+2"]["pulse_mid"]["average_time"][0]],    
    "Pulse Max dt[s]": [data["1"]["pulse_max"]["average_time"][0],data["1+2"]["pulse_max"]["average_time"][0]],
}
print ("\n\nExperiment Data Table: \nDetermining average the time for calculating the instantaneous velocity:")
print(tabulate(data_table, headers="keys", tablefmt="grid"))

# calculation of velocity, momemtum and kinetic energy for each pulse
LENGTH_APERTURE = 0.1 # in meter
MASS_CART_1 = 0.397 # in kg
MASS_CART_2 = 0.383 # in kg
TOTAL_MASS = MASS_CART_1 + MASS_CART_2

# calculations for cart1
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

    key = item[0].replace(" dt[s]","")
    data_table_calculations_cart1[key] = [velocity, momentum, kinetic_energy]

print ("\n\nCalculation of velocity v, momentum p and kinetic energy by pulse min, mid and max :\n", "-"*85 , "\n")
print("\nFor cart 1:")
print(tabulate(data_table_calculations_cart1, headers="keys", tablefmt="grid"))

# for cart 1 and 2 combined
data_table_calculations_cart1_2 ={
    "Calculations" :["v[m/s]","p[kg*m/s]","E[kg*m²/s²]"],
}
for item in data_table.items():
    if item[0] == "Car":
        continue
    dt = round(item[1][1],3) # delta t with index 1 is for cart 2
    velocity = round(LENGTH_APERTURE / dt,3) # velocity of cart 1 while pulse min
    momentum = round(TOTAL_MASS * velocity,3)
    kinetic_energy = round(0.5 * TOTAL_MASS * velocity**2,3)

    key = item[0].replace(" dt[s]","")
    data_table_calculations_cart1_2[key] = [velocity, momentum, kinetic_energy]

print("\n\nFor cart 1 and 2 Combined:")
print(tabulate(data_table_calculations_cart1_2, headers="keys", tablefmt="grid"))

# calculate the percentage error in the conservation of momentum
data_table_momentum_error = {
    "Pulse":["Min", "Mid","Max"],
    "Momentum Car1":[
        data_table_calculations_cart1["Pulse Min"][1],
        data_table_calculations_cart1["Pulse Mid"][1],
        data_table_calculations_cart1["Pulse Max"][1],
    ],
    "Momentum Car 1 + 2":[
        data_table_calculations_cart1_2["Pulse Min"][1],
        data_table_calculations_cart1_2["Pulse Mid"][1],
        data_table_calculations_cart1_2["Pulse Max"][1],
    ],
    "Percentage Error" : [] # will be calculated below
}

for index,p_1 in enumerate(data_table_momentum_error["Momentum Car1"]):
    p_2 = data_table_momentum_error["Momentum Car 1 + 2"][index]
    PERCENTAGE_ERROR = str(round(abs(p_1 - p_2)/p_1 * 100,3 )  )+ " %"
    data_table_momentum_error["Percentage Error"].append(PERCENTAGE_ERROR)

print("\n\nPercentage Error in the conservation of Momentum:")
print(tabulate(data_table_momentum_error, headers="keys", tablefmt="grid"))

# calculation of dissipated mechanical energy during inelastic collision
data_table_energy_dissipated = {
    "Pulse" : ["Min", "Mid", "Max"],
    "Energy Before": [
        data_table_calculations_cart1["Pulse Min"][2],
        data_table_calculations_cart1["Pulse Mid"][2],
        data_table_calculations_cart1["Pulse Max"][2],       
    ],
    "Energy After": [
        data_table_calculations_cart1_2["Pulse Min"][2],
        data_table_calculations_cart1_2["Pulse Mid"][2],
        data_table_calculations_cart1_2["Pulse Max"][2],        
    ],
    "Energy Dissipated E[J]": []
}

# now calculate energy dissipated
for index, energy_before in enumerate(data_table_energy_dissipated["Energy Before"]):
    energy_after = data_table_energy_dissipated["Energy After"][index]

    ENERGY_DISSIPATED = energy_before - energy_after
    data_table_energy_dissipated["Energy Dissipated E[J]"].append(ENERGY_DISSIPATED)

print("\n\nMechanical Energy Dissipated:")
print(tabulate(data_table_energy_dissipated, headers="keys", tablefmt="grid"))