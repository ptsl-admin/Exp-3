import math
from tabulate import tabulate


# these are the datas from ex_3.2.1 and 3.2.2 for the velocity and time taken when the car
# reaches 1 meter disance as detected by the photo sensor

BAR_LENGTH = 1 # in meter (the length of roller track)

data = {
    "Height (h[m])" : [10/1000, 18/1000, 31/1000], # converted to m from mm
    "Velocity (v[m/s])" : [0.428, 0.566, 0.762],
}

# we now calculate the distance between two supports (l)
data["Distance (l[m])"] = [(math.sqrt(BAR_LENGTH**2 - h**2)) for h in data["Height (h[m])"]]

# calculate angle for each height
data["Angle (rad)"] = [math.atan((data["Height (h[m])"][i])/l) for i,l in enumerate(data["Distance (l[m])"])]


data["g[m/s²]"] = [] # will be determined below

# calculate the magnitude of acceleration due to gravity
for i, v in enumerate(data["Velocity (v[m/s])"]):
    alpha = data["Angle (rad)"][i]

    # using the formula v² = u² + 2as, for s = 1m, we get, a = v²/2 because is u = 0
    a = (v**2) / (2 * BAR_LENGTH)

    # calculate the g, using a
    g = a/(math.sin(alpha))

    data["g[m/s²]"].append(g)


print(tabulate(data, headers="keys", tablefmt="grid"))

average_acceleration = sum(data["g[m/s²]"]) / len(data["g[m/s²]"])
ACTUAL_ACCELERATION = 9.8
percent_error = round((ACTUAL_ACCELERATION - average_acceleration) / ACTUAL_ACCELERATION * 100,2)
print("\n\nAverage acceleration due to gravity = {0} m/s²".format(round(average_acceleration,3)))
print("\nPercentage Error wrt Actual value (9.8 m/s²) = {0} %".format(percent_error))