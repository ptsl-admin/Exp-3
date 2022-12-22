import json
from tabulate import tabulate

# Data from the experiment
data = {
    "pulse_min" : {
        "first_run" : [0.361,0.355,0.347,0.349],
        "second_run" : [0.363,0.357,0.351,0.351]
    },
    "pulse_mid" : {
        "first_run" : [0.218,0.218,0.216,0.216],
        "second_run" : [0.218,0.218,0.216,0.216]
    },
    "pulse_max" : {
        "first_run" : [0.163,0.164,0.163,0.164],
        "second_run" : [0.164,0.166,0.164,0.164]
    }
}

# Update Average Time from first and second run
for pulse in data.items():
    average_run = []
    for index, first_run in enumerate(pulse[1]["first_run"]):
        second_run = pulse[1]["second_run"][index]
        average_run.append(round((first_run+second_run)/2,3))

    data[pulse[0]]["average_run"] = average_run    



# Displaying data
print (" \n\nExperiment Data with Average Run Calculated\n", "-"*45)
print(json.dumps(data, indent = 4))

# generate data for table view
data_table_time = {
    "Distance s(m)" : [0.10, 0.40, 0.70, 1.0],
    "Pulse Min t(s)" : data["pulse_min"]["average_run"],
    "Pulse Mid t(s)" : data["pulse_mid"]["average_run"],
    "Pulse Max t(s)" : data["pulse_max"]["average_run"]
}
print (" \n\nExperiment Data Table With Average Run Time\n", "-"*45 , "\n")
print(tabulate(data_table_time, headers="keys",tablefmt="grid"))

# calculate velocity and append to data_table
# in this case we use the formula v = l / dt, where l = 0.1m 
# and dt is the average time required to move 0.1 m distance

LENGTH_APERTURE = 0.1

data_table_velocity = dict()

for pulse in data_table_time.items():
    key = pulse[0]
    if key == "Distance s(m)":
        data_table_velocity["Distance s(m)"] = data_table_time["Distance s(m)"]
        continue
    
    key = key.replace("t(s)","v[m/s]")
    velocity = [round(LENGTH_APERTURE / dt,3) for dt in pulse[1]] # we are looking for 3 significant figures only
    data_table_velocity[key] = velocity


print(" \n\nVelocity calculated from above table\n LENGTH_APERTURE(l) = 0.1 \t formula, v = l / dt \n", "-"*45 , "\n")
print(tabulate(data_table_velocity, headers="keys",tablefmt="grid"))