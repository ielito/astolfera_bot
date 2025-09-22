import redis
import json
import os

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def save_history(cliente, prompt, resposta):
    """Saves the history of a client interaction to Redis.

    This function takes the client's name, the prompt, and the response,
    and saves them as a JSON object in Redis. The key is the client's name,
    lowercased and with spaces replaced by underscores.

    Args:
        cliente (str): The name of the client.
        prompt (str): The prompt that was sent to the model.
        resposta (str): The response received from the model.
    """
    historico = {
        "cliente": cliente,
        "prompt": prompt,
        "resposta": resposta
    }
    r.set(cliente.lower().replace(" ", "_"), json.dumps(historico))

def get_history(cliente):
    """Gets the history of a client interaction from Redis.

    This function retrieves the history for a given client from Redis.
    The key is the client's name, lowercased and with spaces replaced by
    underscores.

    Args:
        cliente (str): The name of the client.

    Returns:
        dict: A dictionary containing the client's history, or None if no history
        is found.
    """
    key = cliente.lower().replace(" ", "_")
    data = r.get(key)
    if data:
        return json.loads(data)
    return None