from alchemy.grimoire.light_spellbook import light_spell_record

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
print(f"Testing record light spell: "
      f"{light_spell_record('Fantasy', 'Earth, wind and fire')}")
print(f"Testing invalid spell: "
      f"{light_spell_record('Darkness', 'poison and shadows')}")
