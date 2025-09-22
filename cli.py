from gemini_client import generate_discovery
from web_search import search_company
from prompts.system_prompt import build_prompt
from redis_client import save_history  # ✅ Assumindo que você quer usar Redis
import argparse
import json
import os
from datetime import datetime


# ✅ Função complementar para salvar também localmente como backup ou log
def salvar_historico_local(cliente, prompt, resposta):
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
    parser = argparse.ArgumentParser(description="Astolfo: Discovery Assistant")
    parser.add_argument("cliente", type=str, help="Nome do cliente")
    parser.add_argument("--output", type=str, default=None, help="Nome do arquivo Markdown de saída")
    args = parser.parse_args()

    cliente = args.cliente.strip()

    print("=== ASTOLFO: CLIENT DISCOVERY ASSISTANT ===")
    print(f"🔍 Buscando informações públicas sobre '{cliente}'...")
    info_web = search_company(cliente)

    print("🧠 Construindo prompt...")
    nota_adicional = "NOTE: The documents provided are internal sales templates and not specific to the client. Use public information as the primary source."
    referencia_texto = ""  # removido PDF loader
    full_prompt = build_prompt(cliente, info_web, referencia_texto, nota_adicional)

    print("\n===== 🔍 PROMPT COMPLETO ENVIADO AO GEMINI =====\n")
    print(full_prompt)

    print("💬 Enviando para o modelo Gemini...")
    resposta = generate_discovery(full_prompt)

    # ✅ Salva no Redis
    save_history(cliente, full_prompt, resposta)

    # ✅ Salva localmente também (opcional, mas útil)
    salvar_historico_local(cliente, full_prompt, resposta)

    # ✅ Salva resposta como .md
    output_filename = args.output or f"respostas/{cliente.lower().replace(' ', '_')}.md"
    os.makedirs("respostas", exist_ok=True)
    with open(output_filename, "w") as f:
        f.write(resposta)
    print(f"✅ Resposta salva em ./{output_filename}")


if __name__ == "__main__":
    main()