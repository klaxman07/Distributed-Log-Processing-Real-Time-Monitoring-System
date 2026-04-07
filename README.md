# 🚀 Distributed Log Processing & Real-Time Monitoring System

## 📌 Overview

A high-performance distributed system designed to process logs from multiple clients in real time, detect anomalies, and visualize system activity through a live dashboard.

This project demonstrates strong concepts in **backend engineering, concurrency, system design, and real-time monitoring**, making it highly relevant for modern software engineering roles.

---

## ⚙️ Features

* 🔄 Real-time log streaming using socket programming
* 🧵 Multi-threaded server for handling concurrent clients
* 📥 Queue-based architecture (Producer–Consumer model)
* 🚨 Anomaly detection (e.g., brute-force login attempts)
* 📊 Live dashboard displaying logs, alerts, and performance graph
* ⚡ Performance monitoring using logs/sec metric
* 🔁 Auto-refreshing UI with real-time updates
* 🧠 Efficient memory handling using shared state

---

## 🧠 System Architecture

```
Clients → Socket Server → Queue → Worker Threads → Processing → Dashboard (Flask)
```

---

## 🛠️ Tech Stack

* **Language:** Python
* **Backend:** Socket Programming, Multithreading
* **Frontend:** HTML, CSS, JavaScript
* **Framework:** Flask
* **Visualization:** Chart.js
* **Concepts:** Distributed Systems, Concurrency, Real-Time Processing

---

## 🚀 How It Works

1. Multiple clients continuously generate logs
2. Logs are sent to the central server via sockets
3. Server pushes incoming logs into a queue
4. Worker threads process logs asynchronously
5. Anomaly detection identifies suspicious activities
6. Dashboard displays logs, alerts, and performance metrics in real time

---

## 📊 Performance

* Supports **10–20 concurrent clients**
* Processes logs in real time with minimal delay
* Displays **live logs/sec performance graph**
* Optimized using multi-threading and queue-based architecture

---

## ▶️ How to Run

### 1️⃣ Start Server (includes dashboard)

```bash
python server/server.py
```

### 2️⃣ Start Clients (multi-client load testing)

```bash
python client/multi_client.py
```

### 3️⃣ Open Dashboard in Browser

```
http://127.0.0.1:5000/
```

---

## 🚨 Sample Output

```
[PROCESSED] 192.168.1.10 → Login Failed
⚡ Logs/sec: 32.50
🚨 Brute-force attack detected from 192.168.1.10
```

---


## 💡 Key Learnings

* Designed a scalable distributed system
* Implemented concurrency using multithreading
* Applied producer-consumer architecture
* Built real-time monitoring dashboards
* Optimized performance under load
* Debugged real-world system issues

---

## 🔥 What Makes This Project Unique

Unlike typical academic projects, this system focuses on:

* Real-time data processing
* Performance monitoring and visualization
* Concurrent architecture for scalability
* End-to-end system (backend + frontend + monitoring)

---
## 📸 Screenshots

### 🖥️ Dashboard UI
![Dashboard](assets/dashboard.png)

### 📄 Logs
![Logs](assets/logs.png)

### 🚨 Alerts
![Alerts](assets/alerts.png)


## 📌 Future Improvements

* Store logs in database (MongoDB / PostgreSQL)
* Add authentication & role-based access
* Deploy on cloud platforms (AWS / Azure)
* Implement WebSockets for ultra-fast updates
* Add filtering, search, and analytics dashboard

---

## 👨‍💻 Author

**K Laxman Reddy*

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

---

## 📣 Keywords

Distributed Systems • Backend Engineering • Multithreading • Real-Time Processing • Flask • System Design • Performance Monitoring • Python
