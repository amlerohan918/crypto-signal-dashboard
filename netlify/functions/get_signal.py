import json
import random

def handler(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Content-Type": "application/json"
    }
    
    signals = ["STRONG BUY 🚀", "BUY 📈", "STRONG SELL 📉", "SELL 🔻", "WAIT ⏳"]
    chosen_signal = random.choice(signals)
    
    body = {
        "status": "success",
        "signal": chosen_signal,
        "message": "Signal fetched successfully!"
    }
    
    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps(body)
    }
    
