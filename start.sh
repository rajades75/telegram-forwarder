#!/bin/bash
chmod +x start.sh
uvicorn server:app --host 0.0.0.0 --port 10000 &
python3 main.py
