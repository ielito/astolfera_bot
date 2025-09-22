from redis_client import save_history
from history_client import get_last_history, salvar_historico_json
import os
from gemini_client import generate_discovery

def main():
    """Main function for refining an existing client discovery report.

    This function prompts the user for a client name, retrieves the last
    discovery report for that client, and then asks for new meeting notes.
    It then sends the previous report and the new notes to the Gemini model
    to generate a refined report. The new report is then saved and displayed.
    """
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
    salvar_historico_json(cliente, prompt, nova_resposta)

    with open(f"respostas/{cliente.lower().replace(' ', '_')}.md", "w") as f:
        f.write(nova_resposta)
    print("✅ Nova resposta salva em ./respostas/")

if __name__ == "__main__":
    main()