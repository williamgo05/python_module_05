import sys
import site
import os

if sys.prefix == sys.base_prefix:
    print("\nLABORATORY STATUS: You are working in the open\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: None detected\n")
    print(f"Package installation directories: {site.getsitepackages()}\n")


    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.\n")

    print("To seal the laboratory, run:\npython3 -m venv lab_env\nsource lab_env/bin/activate\n")

    print("Then run this program again.")

else:
    print("\nLABORATORY STATUS: The laboratory is sealed\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}\n")
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting the global system.")
    print(f"Package installation directories: {site.getsitepackages()}\n")
