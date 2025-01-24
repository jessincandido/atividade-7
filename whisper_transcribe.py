import whisper

def transcribe_audio(file_path: str) -> str:
    """Transcreve o áudio fornecido usando o modelo Whisper."""
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result['text']

if __name__ == "__main__":
    # Código para teste direto do arquivo (apenas para debug)
    test_audio = r"C:\CABOCLO SONHADOR.mp3"
    print(transcribe_audio(test_audio))
