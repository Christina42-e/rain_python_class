batteries = [50,30,4,45,12,18,30]  ##battery basket

minimum_battery_power = 20    ## battery use minimum 20% charge

usable_battery_power = 0    ## battery 0 power 0
usable_battery_count = 0    ## usable battery 0

for battery in  batteries:   ## check  every battery
    if battery > minimum_battery_power:   # check if battery is over charge 20% to use
        usable_battery_power += battery    # if yes use power added
        usable_battery_count += usable_battery_count + 1  # if yes use battery   count add

print(f"There are {usable_battery_count} batteries which can be used to generate {usable_battery_power}")