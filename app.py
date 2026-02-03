from flask import Flask, jsonify
from prometheus_client import start_http_server, Counter, Gauge
import random

app = Flask(__name__)

# Custom Metrics (7-talab)
PRODUCT_UPDATES = Counter('agri_product_updates_total', 'Total product updates')
ORDERS_COUNT = Counter('agri_orders_total', 'Total orders processed')
STOCK_LEVEL = Gauge('agri_stock_level_kg', 'Current stock levels')

@app.route('/update-product')
def update():
    PRODUCT_UPDATES.inc()
    return jsonify({"status": "updated"})

@app.route('/order')
def order():
    ORDERS_COUNT.inc()
    STOCK_LEVEL.dec(random.randint(1, 5))
    return jsonify({"status": "ordered"})

if __name__ == '__main__':
    start_http_server(8000) # Metrikalar porti
    app.run(host='0.0.0.0', port=5000)
