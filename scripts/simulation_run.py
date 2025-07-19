from core_system import HYMagEngine

engine = HYMagEngine()

engine.inject_hydrogen(rate=5)
engine.activate_magnetic_pistons(rpm=3000)
engine.speed = 80
engine.regen_braking(brake_force=0.7)
engine.cool_with_solar_wings()

print(engine.status())
