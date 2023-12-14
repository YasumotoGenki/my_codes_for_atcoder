k, g, m = map(int, input().split())

glass_water = 0
mag_water = 0

for _ in range(k):
    if glass_water == g:
        glass_water = 0
    elif mag_water == 0:
        mag_water = m
    else:
        if mag_water > g - glass_water:
            mag_water -= g - glass_water
            glass_water = g
        else:
            glass_water += mag_water
            mag_water = 0

print(glass_water, mag_water)