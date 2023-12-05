@echo off
call .venv\Scripts\activate
cd faceTracker
start /high call ..\.venv\Scripts\python.exe main.py
pause