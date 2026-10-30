from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:
	permitted = dark_spell_allowed_ingredients()

	for item in permitted:
		if item in ingredients.lower():
			return f"{ingredients} - VALID"

	return f"{ingredients} - INVALID"