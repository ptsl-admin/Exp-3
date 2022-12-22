import json
from tabulate import tabulate

# Measurements of time take to reach various distances in various pulses while
#  device timing is switched to Mode 1
data = {
    "pulse_max" : {
            "first_run" : [0.162,0.661,1.155, 1.656], # first run
            "second_run" : [0.164,0.665,1.162, 1.665]  # second run
        },
    "pulse_mid" : {
            "first_run" : [0.220,0.904,1.578,2.259],  # first run
            "second_run" : [0.210,0.880,1.541,2.210]   # second run
        },
    "pulse_min" : {
            "first_run" : [0.358,1.440,2.494,3.558], # first run
            "second_run" : [0.345,1.408,2.438,3.479]  # second run
        }
}

# calculate average run for each pulse
for pulse in data.items():    
    average_run = []
    for index, time_first in enumerate(pulse[1]["first_run"]):
        time_second = pulse[1]["second_run"][index]
        time_avg = round((time_first + time_second)/2,3) # don't require more than 3 significant figures
        average_run.append(time_avg)
    
    data[pulse[0]]["average_run"] = average_run


print (" \n\nExperiment Data with Average Run Calculated\n", "-"*45)
print (json.dumps(data, indent = 4))

print (" \n\nExperiment Data Table With Average Run Time\n", "-"*45 , "\n")
# construct new data for table
table_data = {
    "Distance s(m)" : [0.10, 0.40, 0.70, 1.0],
    "Pulse Min t(s)" : data["pulse_min"]["average_run"],
    "Pulse Mid t(s)" : data["pulse_mid"]["average_run"],
    "Pulse Max t(s)" : data["pulse_max"]["average_run"]
}

print(tabulate(table_data, headers="keys",tablefmt="grid"))