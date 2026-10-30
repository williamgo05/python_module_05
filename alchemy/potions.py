from .elements import create_air, create_earth
from elements import create_water, create_fire


def healing_potion() -> str:
    return (f"Healing potion brewed "
            f"with '{create_earth()}' and '{create_air()}'")


def strength_potion() -> str:
    return (f"Strength potion brewed "
            f"with '{create_fire()}' and '{create_water()}'")
