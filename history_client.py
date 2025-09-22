import os
import json
from datetime import datetime
from redis_client import get_history

def salvar_historico_json(cliente, prompt, resposta):
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
    historicos = get_history(cliente)

    # Verifica se é uma lista e se tem itens
    if isinstance(historicos, list) and historicos:
        return historicos[-1]['resposta']
    
    # Se veio um dict direto (ex: só um histórico), acessa direto
    if isinstance(historicos, dict) and 'resposta' in historicos:
        return historicos['resposta']
    
    return None