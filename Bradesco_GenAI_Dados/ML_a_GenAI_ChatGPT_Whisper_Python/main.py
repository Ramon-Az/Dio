# cSpell:ignore wavfile dotenv

language = "pt"

import sounddevice as sd
import scipy.io.wavfile as wav
import os
import whisper
from openai import OpenAI
from dotenv import load_dotenv
from gtts import gTTS
import winsound

load_dotenv()

# Função para gravar áudio do microfone e salvar como WAV
def record(seconds=5):
    sample_rate = 44100
    print(f"Gravando por {seconds} segundos...")
    audio_data = sd.rec(int(seconds * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    
    os.makedirs('./data', exist_ok=True)
    file_name = './data/request_audio.wav'
    wav.write(file_name, sample_rate, audio_data)
    print("Gravação concluída!")
    return file_name

# Função para transcrever áudio local usando Whisper
def transcribe_audio_local(audio_file_path):
    print("Carregando modelo Whisper (primeira vez pode demorar)...")
    model = whisper.load_model("small")
    
    print("Transcrevendo...")
    result = model.transcribe(audio_file_path, fp16=False, language=language)
    return result['text']

# Função para obter resposta do ChatGPT usando a API da OpenAI. Requer chave de API configurada. Se não estiver configurada, a função retorna None. O programa continua normalmente, mas sem a resposta do ChatGPT.

def get_chatgpt_response(text):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Aviso: OPENAI_API_KEY não configurada. Pulando ChatGPT.")
        return None
    
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}]
    )
    return response.choices[0].message.content

# Função para converter texto em fala (TTS) usando gTTS e salvar como wav. O arquivo é salvo em ./data/resposta_audio.mp3. O programa continua normalmente, mesmo que haja falha na conversão de texto para fala, mas a reprodução do áudio será pulada.
def text_to_speech(text, output_file):
    gtts_objeto = gTTS(text, lang=language, slow=False)
    gtts_objeto.save(output_file)
    print(f"Áudio salvo em: {output_file}")

# Função para reproduzir áudio usando winsound (Windows)
def play_audio(audio_file):
    winsound.PlaySound(audio_file, winsound.SND_FILENAME)

# Fluxo principal do programa
if __name__ == "__main__":
    # 1. Gravar áudio
    recorded_audio = record()
    print(f"Áudio salvo em: {recorded_audio}")
    
    # 2. Transcrever áudio
    transcricao_texto = transcribe_audio_local(recorded_audio)
    print(f"\nTranscrição: {transcricao_texto}")
    
    # 3. Obter resposta do ChatGPT (opcional, depende da configuração da chave de API)
    chat_response = get_chatgpt_response(transcricao_texto)
    
    if chat_response:
        print(f"\nResposta do ChatGPT: {chat_response}")
        
        # 4. Sintetizar resposta em áudio
        response_audio = "./data/resposta_audio.wav"
        text_to_speech(chat_response, response_audio)
        
        # 5. Reproduzir áudio
        print("\nReproduzindo resposta...")
        play_audio(response_audio)