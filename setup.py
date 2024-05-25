"""Basic setup for the project."""

import os

os.system("pdm run pre-commit install")
os.system("pdm run playwright install")
