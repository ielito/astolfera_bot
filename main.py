from pdf_loader import extract_text_from_pdf
from gemini_client import generate_discovery

# Caminhos dos PDFs
pdf1_path = "docs/proof_plan_prints.pdf"
pdf2_path = "docs/proof_plan_ppt.pdf"

# Extração de texto
texto1 = extract_text_from_pdf(pdf1_path)
texto2 = extract_text_from_pdf(pdf2_path)

texto_completo = f"{texto1}\n\n{texto2}"

# Geração com Gemini
resposta = generate_discovery(texto_completo)

print("\n===== RESPOSTA DO GEMINI =====\n")
print(resposta)
