#!/usr/bin/env python3
"""
NASA Environmental Hotspot Activity Forecast & Emergency Dispatch Platform
Root Application Entry Point (app.py) for Cloud Platforms (Render, Railway, Heroku)
"""

import os
import sys

# Ensure backend directory is in python search path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(ROOT_DIR, 'backend')
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from server import run_server

if __name__ == '__main__':
    run_server()
