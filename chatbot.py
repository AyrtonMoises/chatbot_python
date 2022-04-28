# corrigir bug do erro conflito entre chatterbot e spacy
# from spacy.cli import download

# download("en_core_web_sm")

# class ENGSM:
#     ISO_639_1 = 'en_core_web_sm'

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#chatbot = ChatBot('MeuBot', tagger_language=ENGSM)
chatbot = ChatBot('MeuBot')

# Cria dialogo que bot ira treinar para responder de acordo com resposta
# Bot e inteligente e vai aprender a responder mesmo que a mensagem não seja exatamente aquilo 

conversa = [
    "Olá",
    "Oi, tudo bem ?",
    "Tudo certo",
    "Qual a boa de hoje?",
    "a Hashtag ta ensinando python até com chatbot",
    "Nossa, que legal",
    "Legal mesmo",
    "Sim"
]

# cria objeto ListTrainer
trainer = ListTrainer(chatbot)

# Informa o dialogo de conversa para aprender, ele cria um arquivo sqlite com historico
trainer.train(conversa)

while True:
    mensagem = input('Usuário: ')
    if mensagem == 'parar':
        break
    resposta = chatbot.get_response(mensagem)

    # checa 
    if float(resposta.confidence) > 0.5:
        print('Bot: ', resposta)
    else:
        print('Bot: Ainda não sei responder esta pergunta')
    

# Limpa arquivo de dados (não exclui)
#chatbot.storage.drop()