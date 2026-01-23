import os
import sys
import site

location = sys.prefix
base_location = sys.base_prefix
xxx = sys.executable

if location != base_location:
    # --- INSIDE THE CONSTRUCT ---
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    env_name = os.environ.get('VIRTUAL_ENV', location.split(os.sep)[-1])
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {location}\n")
    print("SUCCESS: You're in an isolated environment!\n"
          "Safe to install packages without affecting\n"
          "the global system.\n")
    print("Package installation path:")
    paths = site.getsitepackages()
    if paths:
        print(paths[0])
    else:
        print(site.getusersitepackages())

else:
    # --- OUTSIDE THE MATRIX ---
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!\n"
          "The machines can see everything you install.")
    print("To enter the construct, run:\n"
          "python -m venv matrix_env\n"
          "source matrix_env/bin/activate # On Unix\n"
          "matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")
