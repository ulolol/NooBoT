


# Importing chatterbot
from chatterbot import ChatBot
# Create object of ChatBot class
bot = ChatBot('NooBoT')
# Create object of ChatBot class with Storage Adapter
bot = ChatBot(
    'NooBoT',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)
# Create object of ChatBot class with Logic Adapter
bot = ChatBot(
    'NooBoT',  
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation'],
)



#Testing with Phrases
# Import ListTrainer
import logging
 
from chatterbot.trainers import ListTrainer
 
from chatterbot.trainers import ChatterBotCorpusTrainer
 
from chatterbot.trainers import UbuntuCorpusTrainer
 
logging.basicConfig(level=logging.INFO)
 
trainer = ChatterBotCorpusTrainer(bot)
 
trainer = UbuntuCorpusTrainer(bot)
 
trainer.train()
 
trainer.train("chatterbot.corpus.english")
 
trainer = ListTrainer(bot)
 
trainer.train([
'Hi',
'Hello',
'hey there',
'hey!',
'yo',
'Yo!',
'How are you?',
'Im great!',
'Whats your name?',
'The name\'s Bot, NooBoT, Coz im a Noooob and im a Bot',
'You suck',
'Not as much as you, coz you suck, and you swallow',
'you\'re great!',
'Thx!',
'How old are you?',
'Bots dont have an Age, you Dumbass!', 
'Can you help me?',
'Nope. No one can help a retard like you. You\'re a lost cause ',
'What can you do?',
'A lot more stuff than you !',
'Tell me more',
'Im a chatbot, a noob chatbot :\'(',
'Bye',
'See ya!',
'--info',
'NooBoT v0.001-alpha // Fri-02-04-21 // build.Local '
])



#Input Loop
name=input("Enter Your Name: ")
print("Welcome "+name +" ! Im a basic bot so dont expect a lot from me. Ok? thx byee! I mean you can enter whatever you want now .......")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye, See ya!')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)