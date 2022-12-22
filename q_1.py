import json
import pandas as pd

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
for pulse in data.keys():
    first_run = data[pulse]["first_run"]
    second_run = data[pulse]["second_run"]
    average_run = []
    for index, time_first in enumerate(first_run):
        time_second = second_run[index]
        time_avg = round((time_first + time_second)/2,3) # don't require more than 3 significant figures
        average_run.append(time_avg)
    
    data[pulse]["average_run"] = average_run
    
distances = [0.10, 0.40, 0.70, 1.0]

data_frame = pd.DataFrame(data, index = distances)

print (data_frame)

#print (" Experiment Data with Average Run Calculated:\n", "-"*45)
#print (json.dumps(data, sort_keys=True, indent = 4))
