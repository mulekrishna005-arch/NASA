#!/usr/bin/env python3
"""
NASA Environmental Hotspot Activity Forecast
Unified Full-Stack Launcher (run.py)

Connects and orchestrates:
- Python virtual environment (venv)
- Backend data science pipeline (backend/model_pipeline.py)
- Backend HTTP & REST API server (backend/server.py)
- Frontend client web application (frontend/)
- Automatic browser launcher
"""

import os
import sys
import time
import subprocess
import webbrowser
import urllib.request
import urllib.error

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(ROOT_DIR, 'backend')
FRONTEND_DIR = os.path.join(ROOT_DIR, 'frontend')

def find_venv_python():
    """Finds the virtual environment Python interpreter."""
    candidates = [
        os.path.join(ROOT_DIR, 'venv', 'Scripts', 'python.exe'),
        os.path.join(ROOT_DIR, '.venv', 'Scripts', 'python.exe'),
        os.path.join(BACKEND_DIR, 'venv', 'Scripts', 'python.exe'),
        os.path.join(ROOT_DIR, 'venv', 'bin', 'python'),
        os.path.join(ROOT_DIR, '.venv', 'bin', 'python'),
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return sys.executable

def verify_environment(python_exec):
    """Verifies that numpy and pandas are available in the Python runtime."""
    print(f"[*] Checking Python runtime: {python_exec}")
    req_file = os.path.join(BACKEND_DIR, 'requirements.txt')
    
    check_code = "import numpy, pandas; print('DEPS_OK')"
    try:
        proc = subprocess.run([python_exec, "-c", check_code], capture_output=True, text=True)
        if "DEPS_OK" in proc.stdout:
            print("[+] Dependencies verified: NumPy and Pandas are ready.")
            return True
    except Exception as e:
        print(f"[-] Dependency check error: {e}")

    # If missing, try installing
    if os.path.exists(req_file):
        print("[!] Installing missing dependencies from backend/requirements.txt...")
        subprocess.run([python_exec, "-m", "pip", "install", "-r", req_file])
    return True

def ensure_initial_forecast(python_exec):
    """Ensures forecast_data.json exists before launching server."""
    backend_json = os.path.join(BACKEND_DIR, 'forecast_data.json')
    frontend_json = os.path.join(FRONTEND_DIR, 'forecast_data.json')
    
    if not os.path.exists(backend_json) or not os.path.exists(frontend_json):
        print("[*] Generating initial forecast data & model benchmarks...")
        pipeline_script = os.path.join(BACKEND_DIR, 'model_pipeline.py')
        subprocess.run([python_exec, pipeline_script], cwd=BACKEND_DIR)
    else:
        print("[+] Existing forecast telemetry dataset found.")

def wait_for_server(url, timeout=10):
    """Polls server until ready."""
    start = time.time()
    while time.time() - start < timeout:
        try:
            with urllib.request.urlopen(f"{url}api/status", timeout=1) as response:
                if response.status == 200:
                    return True
        except (urllib.error.URLError, ConnectionResetError, OSError):
            time.sleep(0.3)
    return False

def main():
    print("==================================================================")
    print("       NASA Environmental Hotspot Activity Forecast System       ")
    print("                  Full-Stack Environment Launcher                ")
    print("==================================================================")
    
    python_exec = find_venv_python()
    verify_environment(python_exec)
    ensure_initial_forecast(python_exec)

    server_script = os.path.join(BACKEND_DIR, 'server.py')
    port = 8000

    print(f"\n[*] Launching Backend Server on port {port}...")
    server_proc = subprocess.Popen([python_exec, server_script], cwd=BACKEND_DIR)

    base_url = f"http://localhost:{port}/#d:24hrs;@83.3,1.5,3.2z"
    if wait_for_server(f"http://localhost:{port}/", timeout=8):
        print(f"[+] Full-Stack Application is ONLINE at: {base_url}")
        print("[+] API Status Endpoint:     http://localhost:8000/api/status")
        print("[+] API Forecast Endpoint:   http://localhost:8000/api/forecast")
        print("[+] Opening web browser automatically...\n")
        webbrowser.open(base_url)
    else:
        print(f"[!] Server started. Open your browser at: {base_url}")

    print("==================================================================")
    print("  Application running. Press Ctrl+C in this terminal to shut down.")
    print("==================================================================")

    try:
        server_proc.wait()
    except KeyboardInterrupt:
        print("\n[*] Shutting down backend server...")
        server_proc.terminate()
        server_proc.wait()
        print("[+] Server stopped. Goodbye!")

if __name__ == '__main__':
    main()
