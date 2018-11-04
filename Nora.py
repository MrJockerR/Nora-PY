#importa o chatterbot 
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

#Leitor de voz
import speech_recognition as sr

#speech synthesis
import pyttsx3
voz = pyttsx3.init('sapi5')

def Speak(text):
    voz.say(text)
    voz.runAndWait()
bot = ChatBot('Nora')

conv = ['Oi', 'Olá', 'Tudo bem ?', 'Sim, é você está bém ?', 'Qual o seu nome ?', 'Meu nome é Nora, e o seu ?']

bot.set_trainer(ListTrainer)#Lista os treinos
bot.train(conv)#Treinar

r = sr.Recognizer() #Dando valor do Recognizer a variavel r

with sr.Microphone() as s: #Microfone 
    r.adjust_for_ambient_noise(s) #ajusta a ruidos
    while True:
        print('Fale Algo: ')
        audio = r.listen(s) # lista o audio
        fala = r.recognize_google(audio, language='pt') #converte para texto
        print('Você: ', fala)
        resposta = bot.get_response(fala)
        if float(resposta.confidence) > 0.5: #Confia de resposta do bot > 0.5%      
            print('Nora: ', resposta)
            Speak(resposta)
        else:#Caso não tenha respota
            print('Nora: Não sei!')
            Speak('Não sei!')