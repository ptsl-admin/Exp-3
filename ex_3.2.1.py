import json
from tabulate import tabulate

# Data from the experiment
data = {
    10:{
        "first_run" : [1.373,2.856,3.821,4.613],
        "second_run" : [1.375,2.822,3.776,4.560],
        "average_run" : [] # will be calculated later
    },
    18:{
        "first_run" : [1.052, 2.189,2.926,3.528],
        "second_run" : [1.078,2.256,3.012,3.625],
        "average_run" : [] # calculated later
    },
    31:{
        "first_run" : [0.943, 1.829, 2.400, 2.864],
        "second_run" : [0.883, 1.770, 2.343, 2.807],
        "average_run" : [] # will be calculated later
    },        
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
print (" \n\nExperiment Data Table With Average Run Time\n", "-"*45 , "\n")
print(tabulate(data_table_time, headers="keys",tablefmt="grid"))
# printing coordinates (t1,s1),(t2,s2),.. for each height
#temp = ""
#for i,t in enumerate(data[31]["average_run"]):
#    s = data_table_time["Distance s(m)"][i]
#    temp += "({0},{1}),".format(t,s)
#print(temp)