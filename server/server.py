import socket
import threading
from queue import Queue
from processor import process_log
from dashboard import run_dashboard
import threading

HOST = '0.0.0.0'
PORT = 9999

log_queue = Queue()

def handle_client(client_socket, addr):
    print(f"✅ Connected: {addr}")

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break

            logs = data.decode().split("\n")

            for log in logs:
                if log.strip():
                    log_queue.put(log)

        except:
            break

    print(f"❌ Disconnected: {addr}")
    client_socket.close()


def worker():
    while True:
        log = log_queue.get()
        process_log(log)
        log_queue.task_done()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"🚀 Server running on port {PORT}...")

    # 🔥 Start dashboard in same process
    dashboard_thread = threading.Thread(target=run_dashboard, daemon=True)
    dashboard_thread.start()

    # Start worker threads
    for _ in range(3):  # you can increase later
        t = threading.Thread(target=worker, daemon=True)
        t.start()

    while True:
        client_socket, addr = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, addr)
        )
        thread.start()


if __name__ == "__main__":
    start_server()