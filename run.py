import sys
import os

# Add the 'files' directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'files'))

# Import the App class from photo_editor.py
from files.photo_editor import App

if __name__ == "__main__":
    App()
