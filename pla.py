import math

DIAMETER = 0.175  # cm
DENSITY = 1.25  # g/cm3

REEL_WEIGHT = 300  # g


def get_pla_net_weight(gross_weight, reel_weight=REEL_WEIGHT):
    return gross_weight - reel_weight


def calc_pla_in_mts(pla_net_weight, pla_diameter=DIAMETER, pla_density=DENSITY):
    filament_area = math.pi * (pla_diameter/2)**2  # cm2

    lenght_cm = pla_net_weight / (filament_area * pla_density)
    lenght_mts = round(lenght_cm / 100, 2)

    return lenght_mts


def main():
    gross_weight = float(input('Insert filament weight in grams: '))

    net_weight = get_pla_net_weight(gross_weight)

    print(f'REEL is usually {REEL_WEIGHT}g, so you have {net_weight}g of PLA.')

    pla_mts = calc_pla_in_mts(net_weight)

    print(f'You have about {pla_mts}m of PLA left')


if __name__ == '__main__':
    main()
