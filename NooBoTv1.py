import streamlit as st
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
# Create object of ChatBot class with PreProcessors
bot = ChatBot(
    'NooBoT',  
    preprocessors=['chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.convert_to_ascii',
        'chatterbot.preprocessors.unescape_html'],
)

#get_text is a simple function to get user input from text_input
def get_text():
    input_text = st.text_input("You: ","So, what's in your mind")
    return input_text

#Define sidebar title and text
st.sidebar.title("NooBoT")
st.title("""
NooBoT  
NooBoT is an NLP conversational chatterbot. Initialize the bot by clicking the "Initialize bot" button. 
""")

#bot training
#use initialize button to train bot
import logging
 
from chatterbot.trainers import ListTrainer
 
from chatterbot.trainers import ChatterBotCorpusTrainer
 
from chatterbot.trainers import UbuntuCorpusTrainer

#enable logging for testing
logging.basicConfig(level=logging.INFO)


if st.sidebar.button('Initialize bot'):
    #define trainers
    trainer = ChatterBotCorpusTrainer(bot)
    #commented ubuntucorpus trainer while testing code to reduce execution time.
    #trainer = UbuntuCorpusTrainer(bot)
    #trainer.train()
 
    trainer.train("chatterbot.corpus.english")
    #train using custom phrases
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
        'NooBoT v1-alpha // Wed-16-06-21 // build.Local '
    ])
 
    st.title("Your bot is ready to talk to you")


user_input = get_text()

st.text_area("Bot:", value="Welcome! Im a basic bot so dont expect a lot from me. Ok? thx byee! I mean you can enter whatever you want now .......", height=200, max_chars=None, key=None)

if True:
    if user_input=='Bye' or user_input =='bye':
        st.text_area("Bot:", value="OK ! See ya !", height=200, max_chars=None, key=None)
       #break
    st.text_area("Bot:", value=bot.get_response(user_input), height=200, max_chars=None, key=None)
    
else:
    st.text_area("Bot:", value="Please start the bot by clicking sidebar button", height=200, max_chars=None, key=None)


