from collections import defaultdict
from state import alerts

failed_attempts = defaultdict(int)

def detect_anomaly(ip, message):
    if "Login Failed" in message:
        failed_attempts[ip] += 1

        if failed_attempts[ip] > 5:
            print(f"🚨 ALERT: Possible brute-force attack from {ip}")