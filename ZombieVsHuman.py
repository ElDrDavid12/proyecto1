import random
import time

human = 100  # Initial human population
zombis = 50   # Initial zombi population
day = 0

# Simulation
while True:
    print("=" * 10)
    print(f"DAY {day}")
    print(f"Population of human: {human}")
    print(f"Population of zombis: {zombis}")
    print("=" * 10)

    # Encounter Probability
    if random.randrange(1, 10) <= 3:  # 30% chance of Encounter
        human_strength = random.randrange(1, 10)
        zombis_strength = random.randrange(1, 10)
        
        if human_strength > zombis_strength:
            zombis -= human
            if zombis < 0:
                zombis = 0
            human *= 2
        elif zombis_strength > human_strength:
            human -= zombis
            if human < 0:
                human = 0
            zombis *= 2
        else:
            human -= zombis
            zombis -= human
            if human < 0:
                human = 0
            if zombis < 0:
                zombis = 0

    # Survival
    if random.randrange(1, 10) >= 7:  # 70% chance of Survival
        human *= 2

    # Mutation
    if random.randrange(1, 10) <= 3:  # 30% chance of Mutation
        zombis *= 2

    day += 1

    if human <= 0:
        print("The zombis have won")
        break
    elif zombis <= 0:
        print("The human have won")
        break

    time.sleep(1)
