# importa o chatterbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

#importes diversos
import sys

# Leitor de voz
import speech_recognition as sr

# speech synthesis
import pyttsx3
voz = pyttsx3.init('sapi5')

# Voz do bot
def Speak(text):
    voz.say(text)
    voz.runAndWait()
bot = ChatBot('Nora')  # Criando Bot
                            
conv = ['Oi', 'Olá', 'Tudo bem ?', 'Sim, é você está bém ?',
        'Qual o seu nome ?', 'Meu nome é Nora, e o seu ?']

convMetodos = ['Modo de cálculos', 'Escolha qual operação deseja: adição, subtração, multiplicação e divisão', 'Fecha progragrama', 'Deseja finalizar minha execução? ', 'Fizalizar', 'Programa sendo encerrado!', 'Encerrar', 'Programa sendo encerrado!']

convMethMathep = ['adição', 'Me diga quantos números vão ser somados?', '', 'subtração', 'Me diga quantas números irão ser subtraidos?', '', 
        'Multiplicação', 'Mé diga quantos números vão ser multiplicados?', '', 'Divisão', 'Me diga qual é o dividendo', '']

bot.set_trainer(ListTrainer)  # Lista os treinos
#bot.train(conv)  # Treinar
bot.train(convMetodos)
#bot.train(convMethMathep)
r = sr.Recognizer()  # Dando valor do Recognizer a variavel r

with sr.Microphone() as s:  # Microfone
    while True:
        print('Nora: Insira a senha: ')
        Speak('Insira a senha')
        r.adjust_for_ambient_noise(s)  # ajusta a ruidos
        audioS = r.listen(s)
        falaS = r.recognize_google(audioS, language='pt')
        print(falaS)
        if(falaS == 'nora' or falaS == 'Nora' or falaS == 'a senha é nora' or falaS == 'a senha é Nora' or falaS == 'a senha e Nora'):
            print('Nora: Acesso aceito!')
            Speak('Acesso aceito')
            print('Nora: Vamos conversa! Pergunte-me algo!')
            Speak('Vamos conversa! Pergunte-me algo')
            while True:
                audio = r.listen(s)  # lista o audio
                fala = r.recognize_google(audio, language='pt')  # converte para texto
                resposta = bot.get_response(fala)
                if(fala == "adição" or fala == 'soma' or fala == 'subtração' or fala == 'multiplicação' or fala == 'divisão'):
                    if(fala == 'adição' or fala == 'soma'):
                        print('Você: ', fala)
                        print('Nora: ', resposta)
                        Speak(resposta)
                        #capturando novo audio
                        audio = r.listen(s)  # lista o audio
                        fala = r.recognize_google(audio, language='pt')  # converte para texto
                        print('Você: ', fala)
                        quantNum = int(fala)
                        soma = 0
                        print('Nora: ', quantNum, 'números serão somados, me diga o 1º número: ')
                        Speak(str(fala) + 'º números serão somados, me diga o 1º número: ')
                        for i in range(quantNum):
                            audio = r.listen(s)  # lista o audio
                            fala = r.recognize_google(audio, language='pt')  # converte para texto
                            print('Você: ', fala)
                            print('Nora: Próximo!')
                            Speak('Próximo!')
                            soma = soma + int(fala)
                        print('Nora: A soma foi', soma)
                        Speak('O resultado da soma foi: ' + str(soma))
                    elif(fala == 'subtração'):  
                        print('Você: ', fala)
                        print('Nora: ', resposta)
                        Speak(resposta)
                        audio = r.listen(s)  # lista o audio
                        fala = r.recognize_google(audio, language='pt')  # converte para texto
                        quantNum = int(fala)
                        print('Nora: ' + str(quantNum) + ' números serão subtraidos, me diga o 1º número: ')
                        Speak(str(quantNum) + ' números serão subtraidos, me diga o 1º número: ')
                        sub = 0
                        for i in range(quantNum):
                            audio = r.listen(s)  # lista o audio
                            fala = r.recognize_google(audio, language='pt')  # converte para texto
                            print('Você: ', fala)
                            if(i < quantNum -1):
                                print('Nora: Próximo!')
                                Speak('Próximo')
                            sub = float(fala) - sub  
                        print('Nora: O resultado da subtração foi: ', sub * -1)
                        Speak('O resultado da subtração foi: ' +  str(sub * -1))
                    elif(fala == 'multiplicação'):
                        print('Você: ', fala)
                        print('Nora: ', resposta)
                        Speak(resposta)
                        audio = r.listen(s)  # lista o audio
                        fala = r.recognize_google(audio, language='pt')  # converte para texto
                        quantNum = int(fala)
                        print('Nora: ' + str(quantNum) + ' números serão multiplicados, me diga o 1º número: ')
                        Speak(str(quantNum) + ' números serão multiplicados, me diga o 1º número: ')
                        mult = 1
                        for i in range(quantNum):
                            audio = r.listen(s)  # lista o audio
                            fala = r.recognize_google(audio, language='pt')  # converte para texto
                            print('Você: ', fala)
                            if(i < quantNum -1):
                                print('Nora: Próximo!')
                                Speak('Próximo')
                            mult = mult * float(fala)
                        print('Nora: O resultado da multiplicação foi: ', mult)
                        Speak('O resultado da multiplicação foi: ' + str(mult))
                    else:
                        print('Você: ', fala)
                        print('Nora: ', resposta)
                        Speak(resposta)
                        audio = r.listen(s)  # lista o audio
                        fala = r.recognize_google(audio, language='pt')  # converte para texto
                        print('Você: ', str(fala))
                        dividendo = float(fala)
                        print('Nora: Me diga quem é o divisor!' )
                        Speak('Me diga quem é o divisor!')
                        audio = r.listen(s)  # lista o audio
                        fala = r.recognize_google(audio, language='pt')  # converte para texto
                        print('Você: ', str(fala))
                        div = float( dividendo/float(fala))
                        print('Nora: O resultado da divisão foi: ', str(div))
                        Speak('O resultado da divisão foi: ' + str(div))
                elif float(resposta.confidence) > 0.8:  # Confia de resposta do bot > 0.5%
                        print('Você: ', fala)
                        if(fala == 'Fechar programa' or fala == 'Fecha programa' or fala == 'Fechar programar' or fala == 'Fizalizar' or fala == 'encerrar' or fala == 'finalizar' or fala == 'Encerrar'):
                            fechar = True
                            print('entrou')
                            while fechar:
                                if(fala == 'Fechar programa' or fala == 'Fecha programa' or fala == 'Fechar programar'):
                                    print('Nora: ', resposta)
                                    Speak(resposta)
                                    audio = r.listen(s)  # lista o audio
                                    fala = r.recognize_google(audio, language='pt')  # converte para texto
                                    if(fala == 'Sim' or fala == 'sim'):
                                        print('Programa sendo encerrado!')
                                        Speak('Programa sendo encerrado!')
                                        sys.exit(0)
                                    else:
                                        print('Nora: Então vamos conversa!')
                                        Speak('Nora: Então vamos conversa!')
                                        fechar = False
                                elif(fala == 'Finalizar' or fala == 'encerrar' or fala == 'finalizar' or fala == 'Encerrar'):
                                    print('Nora: ', resposta)
                                    Speak(resposta)
                                    sys.exit(0)
                        else:
                            print('Nora: ', resposta)
                            Speak(resposta)
                else:
                    print('Você: ', fala)
                    print('Nora: Não sei!')
                    Speak('Não sei!')
        else:
            print('Nora: Acesso negado!')
            Speak('Acesso negado!')
