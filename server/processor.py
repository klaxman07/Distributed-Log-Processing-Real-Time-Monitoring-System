import time
from detector import detect_anomaly
from state import logs, metrics

# Performance tracking
count = 0
start_time = time.time()

def process_log(log):
    global count, start_time

    parts = log.split(" | ")
    if len(parts) != 4:
        return

    timestamp, level, ip, message = parts

    # Add to shared logs
    log_entry = f"{timestamp} | {level} | {ip} | {message}"
    logs.append(log_entry)

    # Keep only last 50 logs
    if len(logs) > 50:
        logs.pop(0)

    # Count logs
    count += 1

    # 🔥 FIXED PERFORMANCE BLOCK
    if time.time() - start_time >= 1:
        logs_per_sec = count / 1
        print(f"⚡ Logs/sec: {logs_per_sec:.2f}")

        # Add metric
        metrics.append(logs_per_sec)

        if len(metrics) > 20:
            metrics.pop(0)

        count = 0
        start_time = time.time()

    # Detect anomaly
    detect_anomaly(ip, message)