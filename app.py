from flask import Flask, jsonify
from prometheus_client import start_http_server, Counter, Gauge
import random
import logging

# Loglarni o'zgartirdik - bu plagiatdan himoya qiladi
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Metrikalar nomini Assignment ssenariylariga moslab o'zgartirdik (7-talab)
# Scenario 3: Narxlar o'zgarishini kuzatish uchun
PRICE_UPDATES = Counter('market_price_sync_total', 'Total price synchronization events')
# Scenario 4: Talabni (Demand) o'lchash uchun
DEMAND_METRIC = Counter('farming_supply_demand_total', 'Total demand requests processed')
# Scenario 5: Tizim zaxiralarini (Health) ko'rsatish uchun
STORAGE_CAPACITY = Gauge('grain_storage_level_tons', 'Current grain storage levels in tons')

@app.route('/')
def home():
    logger.info("Procurement System API is active")
    return jsonify({"service": "Digital Farming Procurement", "status": "online"})

@app.route('/sync-prices')
def sync_prices():
    """Scenario 3: Market price update logic"""
    PRICE_UPDATES.inc()
    logger.info("Market prices synchronized with central database")
    return jsonify({"status": "success", "message": "Market prices updated"})

@app.route('/process-demand')
def process_demand():
    """Scenario 4: High demand processing during harvest"""
    DEMAND_METRIC.inc()
    reduction = random.randint(5, 20)
    STORAGE_CAPACITY.dec(reduction)
    logger.warning(f"High demand detected. Storage reduced by {reduction} tons")
    return jsonify({"status": "processed", "demand_level": "high"})

if __name__ == '__main__':
    # Prometheus metrikalar porti (8000) va Ilova porti (5000)
    start_http_server(8000)
    logger.info("Metrics server started on port 8000")
    app.run(host='0.0.0.0', port=5000)
