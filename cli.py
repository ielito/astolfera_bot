from pdf_loader import extract_text_from_pdf
from gemini_client import generate_discovery
from web_search import search_company
from prompts.system_prompt import build_prompt
from redis_client import save_history

import json
import os
from datetime import datetime

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

def main():
    print("=== ASTOLFO: CLIENT DISCOVERY ASSISTANT ===")
    cliente = input("🟡 Qual o nome do cliente? ").strip()

    print(f"🔍 Buscando informações públicas sobre '{cliente}'...")
    info_web = search_company(cliente)

    print("📄 Lendo documentos de referência internos...")
    # Por enquanto, deixando vazio se você decidiu não usar os PDFs
    referencia_texto = ""

    print("🧠 Construindo prompt...")
    nota_adicional = (
        "NOTE: The documents provided are internal sales templates and not specific to the client. "
        "Use public information as the primary source."
    )
    full_prompt = build_prompt(cliente, info_web, referencia_texto, nota_adicional)

    print("\n===== 🔍 PROMPT COMPLETO ENVIADO AO GEMINI =====\n")
    print(full_prompt)

    print("💬 Enviando para o modelo Gemini...")
    resposta = generate_discovery(full_prompt)

    save_history(cliente, full_prompt, resposta)
    salvar_historico_json(cliente, full_prompt, resposta)

    print("\n===== 🔵 RESPOSTA DO ASTOLFO =====\n")
    print(resposta)

    # Salvar resposta em markdown
    os.makedirs("respostas", exist_ok=True)
    filename = f"respostas/{cliente.lower().replace(' ', '_')}.md"
    with open(filename, "w") as f:
        f.write(resposta)
    print(f"✅ Resposta salva em ./{filename}")

if __name__ == "__main__":
    main()