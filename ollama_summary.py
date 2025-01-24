import requests


def summarize_text(text: str, api_url: str, api_key: str) -> str:
    """
    Envia o texto transcrito para o Ollama e retorna os pontos-chave.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {"text": text}
    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("summary", "Resumo indisponível")
    else:
        raise Exception(f"Erro na API Ollama: {response.status_code}")