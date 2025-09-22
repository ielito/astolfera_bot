import os
import json
from datetime import datetime
from redis_client import get_history

def salvar_historico_json(cliente, prompt, resposta):
    """Saves the history of a client interaction to a JSON file.

    This function creates a directory named 'history' if it doesn't exist.
    It then saves a JSON file named after the client and the current timestamp.
    The JSON file contains the client's name, the timestamp, the prompt, and the
    response.

    Args:
        cliente (str): The name of the client.
        prompt (str): The prompt that was sent to the model.
        resposta (str): The response received from the model.
    """
    historico_dir = "history"
    os.makedirs(historico_dir, exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{historico_dir}/{cliente}_{now}.json"

    historico = {
        "cliente": cliente,
        "data_hora": now,
        "prompt": prompt,
        "resposta": resposta
    }

    with open(filename, "w") as f:
        json.dump(historico, f, indent=4)

def get_last_history(cliente):
    """Gets the last history entry for a client from Redis.

    This function retrieves the history for a given client from Redis.
    It then returns the 'resposta' field of the last entry in the history.
    If the history is a single dictionary, it returns the 'resposta' field
    directly.

    Args:
        cliente (str): The name of the client.

    Returns:
        str: The last response for the client, or None if no history is found.
    """
    historicos = get_history(cliente)

    # Verifica se é uma lista e se tem itens
    if isinstance(historicos, list) and historicos:
        return historicos[-1]['resposta']
    
    # Se veio um dict direto (ex: só um histórico), acessa direto
    if isinstance(historicos, dict) and 'resposta' in historicos:
        return historicos['resposta']
    
    return None