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
    if historicos:
        return historicos[-1]['resposta']

    # fallback: buscar na pasta ./respostas
    nome_arquivo = f"respostas/{cliente.lower().replace(' ', '_')}.md"
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r") as f:
            return f.read()

    return None
