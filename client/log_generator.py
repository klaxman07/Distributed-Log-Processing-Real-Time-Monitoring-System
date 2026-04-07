import socket
import time
import random

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9999

messages = ["Login Success", "Login Failed", "File Access", "Unauthorized Access"]
levels = ["INFO", "ERROR", "WARNING"]

def generate_log():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    level = random.choice(levels)
    ip = f"192.168.1.{random.randint(1,50)}"
    message = random.choice(messages)
    #ip = "192.168.1.100"   # fixed attacker IP
    #message = "Login Failed"  # always fail
    return f"{timestamp} | {level} | {ip} | {message}"

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((SERVER_HOST, SERVER_PORT))
        print("✅ Connected to server")
    except:
        print("❌ Connection failed (server not running yet)")
        return

    while True:
        log = generate_log()
        client.send((log + "\n").encode())
        print(f"📤 Sent: {log}")
        time.sleep(1)

if __name__ == "__main__":
    start_client()