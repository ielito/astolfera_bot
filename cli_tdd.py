from redis_client import save_history, get_history
import os
import json
from datetime import datetime
from gemini_client import generate_discovery

# Nova função para tentar recuperar o último histórico no Redis
# ou no arquivo .md local

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

def main():
    print("=== ASTOLFO: REFINAR RESPOSTA COM NOVAS INFORMAÇÕES ===")
    cliente = input("🟡 Nome do cliente para refinar resposta: ").strip()

    anterior = get_last_history(cliente)
    if not anterior:
        print("❌ Nenhuma resposta anterior encontrada para este cliente.")
        return

    print("✍️ Cole as novas anotações da reunião (digite 'FIM' para encerrar):")
    novas_anotacoes = []
    while True:
        linha = input()
        if linha.strip().upper() == "FIM":
            break
        novas_anotacoes.append(linha)
    nova_info = "\n".join(novas_anotacoes)

    print("🧠 Gerando nova versão da resposta com base nas anotações...")

    prompt = f"""
Seu nome é Astolfo e você é meu assistente de descoberta de clientes. Você já gerou uma resposta para o cliente '{cliente}', mas agora estou te passando novas anotações e informações obtidas em uma reunião.

Por favor, revise e atualize sua resposta anterior com base nas novas informações. Mantenha o formato e a estrutura original. Apenas complemente, refine ou corrija partes do texto anterior conforme necessário.

---
📄 RESPOSTA ANTERIOR:
{anterior}

---
🆕 NOVAS ANOTAÇÕES:
{nova_info}

---
✅ NOVA VERSÃO (atualizada, completa e formatada):
"""

    nova_resposta = generate_discovery(prompt)

    print("\n===== 🔵 RESPOSTA REFINADA DO ASTOLFO =====\n")
    print(nova_resposta)

    save_history(cliente, prompt, nova_resposta)

    with open(f"respostas/{cliente.lower().replace(' ', '_')}.md", "w") as f:
        f.write(nova_resposta)
    print("✅ Nova resposta salva em ./respostas/")

if __name__ == "__main__":
    main()