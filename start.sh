#!/bin/bash


echo "Starting KeepAlive server..."
python3 keepalive.py &


echo "Starting VJ Bot..."
python3 bot.py
