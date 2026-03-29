import psutil
import time
import os

THRESHOLD = 75

while True:
    cpu = psutil.cpu_percent(interval=5)
    print(f"CPU Usage: {cpu}%")

    if cpu > THRESHOLD:
        print("Threshold exceeded! Triggering GCP deployment...")
        os.system("bash ../cloud/deploy_to_gcp.sh")
        break

    time.sleep(5)
