from core_system import HYMagEngine
from ai_controller import HYMagAIController

engine = HYMagEngine()
ai = HYMagAIController()

# Simulate one full cycle
engine.speed = 25
engine.hydrogen_level = 18
engine.temperature = 65
engine.battery_level = 25

state = engine.status()
directives = ai.analyze_state(state)
engine.apply_ai_optimizations(directives)

print(engine.status())
