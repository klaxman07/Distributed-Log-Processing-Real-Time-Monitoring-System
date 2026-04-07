from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

from state import logs, alerts, metrics

def add_log(entry):
    logs.append(entry)
    if len(logs) > 50:
        logs.pop(0)

def add_alert(alert):
    alerts.append(alert)
    if len(alerts) > 20:
        alerts.pop(0)

@app.route("/logs")
def get_logs():
    return jsonify(logs)

@app.route("/metrics")
def get_metrics():
    return jsonify(metrics)

@app.route("/alerts")
def get_alerts():
    return jsonify(alerts)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Log Dashboard</title>
        <style>
            body { font-family: Arial; background: #0f172a; color: white; }
            h1 { text-align: center; }
            .container { display: flex; gap: 20px; padding: 20px; }
            .box {
                flex: 1;
                background: #1e293b;
                padding: 15px;
                border-radius: 10px;
                height: 400px;
                overflow-y: scroll;
            }
            .log { font-size: 14px; margin: 5px 0; }
            .alert { color: red; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>🚀 Real-Time Log Dashboard</h1>
        <div class="container">
            <div class="box">
                <h2>Logs</h2>
                <div id="logs"></div>
            </div>
            <div class="box">
                <h2>Alerts</h2>
                <div id="alerts"></div>
            </div>
        </div>
            <h2 style="text-align:center;">📊 Performance (Logs/sec)</h2>
            <canvas id="chart" width="600" height="200"></canvas>

        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

        <script>
            async function fetchData() {
                const logsRes = await fetch('/logs');
                const alertsRes = await fetch('/alerts');

                const logs = await logsRes.json();
                const alerts = await alertsRes.json();

                document.getElementById('logs').innerHTML =
                    logs.map(l => `<div class="log">${l}</div>`).join("");

                document.getElementById('alerts').innerHTML =
                    alerts.map(a => `<div class="alert">${a}</div>`).join("");
            }

            setInterval(fetchData, 1000); // refresh every 1 sec
        let chart;

async function updateChart() {
    const res = await fetch('/metrics');
    const data = await res.json();

    const ctx = document.getElementById('chart').getContext('2d');

    if (!chart) {
        chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.map((_, i) => i),
                datasets: [{
                    label: 'Logs/sec',
                    data: data,
                    borderColor: 'cyan',
                    borderWidth: 2
                }]
            }
        });
    } else {
        chart.data.labels = data.map((_, i) => i);
        chart.data.datasets[0].data = data;
        chart.update();
    }
}

setInterval(updateChart, 1000);
        </script>
    </body>
    </html>
    """)

def run_dashboard():
    app.run(port=5000)

if __name__ == "__main__":
    run_dashboard()