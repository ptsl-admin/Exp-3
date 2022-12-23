import json
from tabulate import tabulate

# Data from the experiment
data = {
    10:{
        "first_run" : [0.635,0.361,0.280,0.239],
        "second_run" : [0.636,0.362,0.280,0.239],
        "average_run" : [] # will be calculated later
    },
    18:{
        "first_run" : [0.505,0.280,0.214,0.181],
        "second_run" : [0.477,0.275,0.212,0.180],
        "average_run" : [] # calculated later
    },
    31:{
        "first_run" : [0.366, 0.213, 0.164, 0.138],
        "second_run" : [0.373,0.213,0.163,0.138],
        "average_run" : [] # will be calculated later
    }
}

# calculate average time taken from first and second run for each height
for roll in data.items():
    average = [round((f+roll[1]["second_run"][i])/2,3) for i, f in enumerate(roll[1]["first_run"])]
    data[roll[0]]["average_run"] = average

# Displaying data
print (" \n\nExperiment Data with Average Time Calculated\n", "-"*45)
print(json.dumps(data, indent = 4))

# generate data for table view
data_table_time = {
    "Distance s(m)" : [0.10, 0.40, 0.70, 1.0],
    "Wood height \nh=10mm, t(s)" : data[10]["average_run"],
    "Wood height \nh=18mm, t(s)" : data[18]["average_run"],
    "Wood height \nh=31mm, t(s)" : data[31]["average_run"]
}

print ("\n\n Experiment Data Table: Average Time wrt to Height and Distance\n", "-"*65 , "\n")
print(tabulate(data_table_time, headers="keys",tablefmt="grid"))

# calculate velocity and append to data_table
# in this case we use the formula v = l / dt, where l = 0.1m 
# and dt is the average time required to move 0.1 m distance

LENGTH_APERTURE = 0.1

data_table_velocity = dict()

for roll in data_table_time.items():
    key = roll[0]
    if key == "Distance s(m)":
        data_table_velocity["Distance s(m)"] = data_table_time["Distance s(m)"]
        continue
    
    key = key.replace("t(s)","v[m/s]")
    velocity = [round(LENGTH_APERTURE / dt,3) for dt in roll[1]] # we are looking for 3 significant figures only
    data_table_velocity[key] = velocity

print ("\n\n Experiment Data Table: Velocity at Each distance for variuos height\n", "-"*65 , "\n")
print(tabulate(data_table_velocity, headers="keys",tablefmt="grid"))


# printing coordinates (t1,v1),(t2,v2),.. for each height
#temp = ""
#for i,t in enumerate(data[31]["average_run"]):
#    s = data_table_time["Distance s(m)"][i]
#    temp += "({0},{1}),".format(t,s)
#print(temp)
#data_table_time = {
#    10: [1.374,2.839,3.798,4.587],
#    18: [1.065,2.223,2.969,3.577],
#    31: [0.913,1.8,2.372,2.835]
#}

#temp = ""
#for i,t in enumerate(data_table_time[31]):
#    v = data_table_velocity["Wood height \nh=31mm, v[m/s]"][i]
#    temp += "({0},{1}),".format(t,v)

#print(temp)