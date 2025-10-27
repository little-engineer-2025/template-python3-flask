from prometheus_client import Counter, generate_latest
"""Metrics package hold the different metrics that use the
application."""

# Define here the metrics
view_metric = Counter("view", "Product view", ["product"])
buy_metric = Counter("buy", "Product buy", ["product"])


# Call this function from the /metrics endpoint
def generate_metrics():
    generate_latest()
