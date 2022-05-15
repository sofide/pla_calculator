import math

DIAMETER = 0.175  # cm
DENSITY = 1.25  # g/cm3

FILAMENT_SUP = math.pi * (DIAMETER/2)**2  # cm2

REEL_WEIGHT = 300  # g

weight = float(input('Insert filament weight in grams: '))

pla_weight = weight - REEL_WEIGHT

print(
    'REEL is usually {}g, so you have {}g of PLA.'.format(
        REEL_WEIGHT,
        pla_weight
    )
)

lenght = pla_weight / (FILAMENT_SUP * DENSITY)

print('You have about {}m of PLA left'.format(round(lenght/100, 2)))
