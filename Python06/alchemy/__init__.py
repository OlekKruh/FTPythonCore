"""The Alchemy package initializer.
Exposes only specific elemental spells (fire and water) to the public interface,
while keeping others (earth and air) internal.
"""

__version__ = "1.0.0"
__author__ = "Master Pythonicus"

from .elements import create_fire, create_water
