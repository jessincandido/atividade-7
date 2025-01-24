from utils.whisper_transcribe import transcribe_audio
from utils.ollama_summary import summarize_text


def main(audio_file: str, ollama_api_url: str, ollama_api_key: str):
    # Transcrição do áudio
    print("Transcrevendo o áudio...")
    transcript = transcribe_audio(audio_file)
    print("Transcrição concluída!")

    # Extração de pontos-chave
    print("Extraindo pontos-chave...")
    summary = summarize_text(transcript, ollama_api_url, ollama_api_key)
    print("Resumo extraído com sucesso!")

    # Resultados
    print("\nTranscrição:")
    print(transcript)
    print("\nResumo:")
    print(summary)


if __name__ == "__main__":
    # Configure os parâmetros de entrada aqui
    audio_file = "inputs/sample_audio.mp3"
    ollama_api_url = "https://api.ollama.ai/endpoint"
    ollama_api_key = "sua_api_key"

    main(audio_file, ollama_api_url, ollama_api_key)