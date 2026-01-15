import speech_recognition as sr # type: ignore
import os

print("testando...")


#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone para ouvir o usuÃ¡rio
    microfone = sr.Recognizer()

    #usando o microfone
    with sr.Microphone() as source:
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Avisa o usuario que esta pronto para ouvir
        print("Diga alguma coisa: ")
        
        #Armazena a informacao de audio na variavel
        audio = microfone.listen(source)

    try:
        #Passa a variavel para o algoritmo reconhecedor de padroes
        print("Reconhecendo...")
        frase = microfone.recognize_google(audio, language='pt-BR')
        
        #Retorna a frase pronunciada
        print("Você disse: " + frase)

        if "navegador" in frase:
            os.system("start chrome.exe")
            return False
        
        elif "Excel" in frase:
            os.system("start excel.exe")
            return False
        
        elif "PowerPoint" in frase:
            os.system("start POWERPONT.exe")
            return False
        
        elif "Edge" in frase:
            os.system("start msedge.exe")
            return False
        
        elif "Fechar" in frase:
            print("Encerrando...")
            return True
    
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnknownValueError:
        print("Não entendi o que você disse")
    
    except sr.RequestError as e:
        print(f"Erro ao conectar com o serviço de reconhecimento: {e}")
    
    return False
    
while True:
    if ouvir_microfone():
        break