import sys
import os

# Add the parent directory (circleci-demo) to Python's path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import add  # Now Python can find app.py

def test_add():
    assert add(2, 3) == 5