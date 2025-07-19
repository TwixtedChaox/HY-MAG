def regenerate_energy(speed, brake_force, battery_level):
    if speed > 10 and brake_force > 0.1:
        recovered_energy = speed * brake_force * 0.05
        if battery_level + recovered_energy > 100:
            return 100
        return battery_level + recovered_energy
    return battery_level
