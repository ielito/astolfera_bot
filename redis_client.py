import redis
import json
import os

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def save_history(cliente, prompt, resposta):
    historico = {
        "cliente": cliente,
        "prompt": prompt,
        "resposta": resposta
    }
    r.set(cliente.lower().replace(" ", "_"), json.dumps(historico))

def get_history(cliente):
    key = cliente.lower().replace(" ", "_")
    data = r.get(key)
    if data:
        return json.loads(data)
    return None