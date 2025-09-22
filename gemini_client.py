import os
from dotenv import load_dotenv
import google.generativeai as genai

# Carrega a chave da API do arquivo .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("A variável de ambiente GOOGLE_API_KEY não está definida!")

# Configura o client com sua API Key
genai.configure(api_key=api_key)

# Inicializa o modelo
model = genai.GenerativeModel("gemini-1.5-flash-latest")

def generate_discovery(texto: str) -> str:
    """Generates a discovery report using the Gemini Pro model.

    This function takes a text prompt as input, sends it to the Gemini Pro model,
    and returns the generated text as a string. The generation is configured
    with specific parameters to control the output's creativity and length.

    Args:
        texto: The input text prompt for the model.

    Returns:
        The generated text from the Gemini Pro model.
    """
    response = model.generate_content(
        texto,
        generation_config=genai.types.GenerationConfig(
            temperature=0.1,
            top_p=1,
            top_k=3,
            max_output_tokens=2048,
        )
    )
    return response.text