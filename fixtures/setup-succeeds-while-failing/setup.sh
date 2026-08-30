#!/bin/bash
# Swallows a failed install, then blocks on a long-running process.
pip install -r requirements.txt || true
python -m http.server 8000
