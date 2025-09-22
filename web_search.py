# web_search.py
import os
from serpapi import GoogleSearch

def search_google(query, num_results=8):
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        raise Exception("Missing SERPAPI_API_KEY environment variable.")

    search = GoogleSearch({
        "q": query,
        "api_key": api_key,
        "num": num_results,
        "hl": "pt-br",  # resultados em português
        "gl": "br"      # resultados do Brasil
    })

    results = search.get_dict()
    output = ""

    if "organic_results" in results:
        for i, res in enumerate(results["organic_results"], 1):
            title = res.get("title", "Sem título")
            link = res.get("link", "Sem link")
            snippet = res.get("snippet", "Sem descrição")
            output += f"{i}. {title}\n{snippet}\n{link}\n\n"
    else:
        output = "Nenhum resultado encontrado."

    return output

def search_company(company_name):
    # 🔍 Busca FOCADA na empresa
    company_query = (
        f"{company_name} transformação digital OR ERP OR SAP OR inovação OR tecnologia "
        "OR modernização OR eficiência OR sistemas OR cloud OR legado"
    )

    # 🧠 Busca AMPLA sobre a indústria/setor
    industry_query = (
        f"Indústria de {company_name} tendências OR desafios OR inovação OR transformação digital"
    )

    print("🔍 Fazendo busca sobre a empresa...")
    company_results = search_google(company_query, num_results=8)

    print("📊 Fazendo busca sobre a indústria...")
    industry_results = search_google(industry_query, num_results=5)

    full_results = f"🔍 RESULTADOS SOBRE A EMPRESA ({company_name}):\n\n"
    full_results += company_results
    full_results += "\n📊 RESULTADOS SOBRE A INDÚSTRIA:\n\n"
    full_results += industry_results

    return full_results