import time
import subprocess
import requests
import psutil

def is_process_running(process_name):
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if process_name in proc.info['cmdline']:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def restart_process(process_name):
    print(f"Restarting {process_name}...")
    try:
        subprocess.Popen(["python3", process_name])
        print(f"{process_name} restarted successfully.")
    except FileNotFoundError:
        print(f"Error: {process_name} not found.")
    except Exception as e:
        print(f"Error restarting {process_name}: {e}")

def ping_url():
    try:
        requests.get("https://verbose-eureka-69wx7xpv6vg5f5pg9.github.dev")
    except Exception as e:
        print(f"Error pinging URL: {e}")

if __name__ == "__main__":
    process_to_watch = "stx.py"
    while True:
        if not is_process_running(process_to_watch):
            restart_process(process_to_watch)
        ping_url()
        time.sleep(10)
