# worm_simulation.py
import random

NUM_HOSTS = 20
ATTEMPTS_PER_INFECTED = 3
INFECTION_PROBABILITY = 0.4   # 40% chance per contact
MAX_STEPS = 20

def simulate_worm():
    hosts = list(range(NUM_HOSTS))
    infected = set([0])  # start with host 0 infected
    step = 0

    print(f"Starting infection. Initial infected hosts: {infected}")

    while len(infected) < NUM_HOSTS and step < MAX_STEPS:
        step += 1
        newly_infected = set()

        for host in infected:
            for _ in range(ATTEMPTS_PER_INFECTED):
                target = random.choice(hosts)
                if target not in infected and random.random() < INFECTION_PROBABILITY:
                    newly_infected.add(target)

        infected.update(newly_infected)
        print(f"Step {step}: Infected {len(infected)}/{NUM_HOSTS} hosts. New this step: {len(newly_infected)}")

        if not newly_infected:
            print("No new infections this step – worm has stalled.")
            break

    print("\nFinal infected hosts:", sorted(infected))

if __name__ == "__main__":
    simulate_worm()
