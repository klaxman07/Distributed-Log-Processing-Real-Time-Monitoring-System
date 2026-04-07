import threading
import subprocess

NUM_CLIENTS = 20 # increase later

def start_client():
    subprocess.run(["python", "client/log_generator.py"])

threads = []

for i in range(NUM_CLIENTS):
    t = threading.Thread(target=start_client)
    t.start()
    threads.append(t)

for t in threads:
    t.join()