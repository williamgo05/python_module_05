from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    permitted = light_spell_allowed_ingredients()

    for item in permitted:
        if item in ingredients.lower():
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
