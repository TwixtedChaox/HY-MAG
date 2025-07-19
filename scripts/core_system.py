class HYMagEngine:
    def __init__(self):
        self.hydrogen_level = 100  # %
        self.battery_level = 100   # %
        self.speed = 0             # km/h
        self.block_count = 2       # Modular block units
        self.magnet_pulse_rate = 0
        self.exhaust_output = "H2O Vapor"
        self.temperature = 30  # Celsius
        self.energy_recovered = 0

    def inject_hydrogen(self, rate):
        if self.hydrogen_level > 0:
            self.hydrogen_level -= rate
            print(f"Injecting {rate}% hydrogen.")
        else:
            print("Warning: Hydrogen depleted!")

    def activate_magnetic_pistons(self, rpm):
        self.magnet_pulse_rate = rpm
        print(f"Magnetic pistons engaged at {rpm} RPM.")

    def regen_braking(self, brake_force):
        recovered = self.speed * brake_force * 0.05
        self.battery_level = min(100, self.battery_level + recovered)
        self.energy_recovered += recovered
        print(f"Recovered {recovered:.2f}% energy via regen braking.")

    def cool_with_solar_wings(self):
        if self.temperature > 40:
            self.temperature -= 5
            print("Cooling with solar wing channels...")

    def status(self):
        return {
            "Hydrogen Level": self.hydrogen_level,
            "Battery Level": self.battery_level,
            "Speed": self.speed,
            "Temperature": self.temperature,
            "Energy Recovered": self.energy_recovered
        }

    def apply_ai_optimizations(self, ai_directives):
        if ai_directives.get("cooling_override"):
            self.temperature -= 7
            print("AI Override: Emergency cooling activated.")

        if ai_directives.get("reduce_fuel_injection"):
            self.inject_hydrogen(rate=2)
            print("AI Override: Reduced hydrogen injection for conservation.")

        if ai_directives.get("increase_regen_braking"):
            self.regen_braking(brake_force=0.9)
            print("AI Override: Aggressive regen braking for recharge.")
