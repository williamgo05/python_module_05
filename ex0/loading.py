try:
    import pandas
    print(f"\n[OK] pandas ({pandas.__version__}) - Data manipulation ready")
except ImportError:
    print("[MISSING] pandas - Data manipulation unavailable")
    print("Install with pip: pip install pandas")
    print("Install with Poetry: poetry add pandas")

try:
    import numpy
    print(f"[OK] numpy ({numpy.__version__}) - Numerical computation ready")
except ImportError:
    print("\n[MISSING] numpy - Numerical computation unavailable")
    print("Install with pip: pip install numpy")
    print("Install with Poetry: poetry add numpy")

print("\npip vs Poetry:\n")
print("pip: requirements.txt declares which packages to install, "
      "but it does not guarantee identical versions across installations.\n")

print("Poetry: pyproject.toml declares dependencies, while "
      "poetry.lock records resolved versions to ensure more consistent "
      "and reproducible environments.")
