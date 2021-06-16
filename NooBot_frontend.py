import streamlit as st


#get_text is a simple function to get user input from text_input
def get_text():
    input_text = st.text_input("You: ","So, what's in your mind")
    return input_text


st.sidebar.title("NLP Bot")
st.title("""
NLP Bot  
NLP Bot is an NLP conversational chatterbot. Initialize the bot by clicking the "Initialize bot" button. 
""")

if st.sidebar.button('Initialize bot'):
    st.title("Your bot is ready to talk to you")


user_input = get_text()

st.text_area("Bot:", value="Welcome! Im a basic bot so dont expect a lot from me. Ok? thx byee! I mean you can enter whatever you want now .......", height=200, max_chars=None, key=None)

if True:
    if user_input=='Bye' or user_input =='bye':
        st.text_area("Bot:", value="OK ! See ya !", height=200, max_chars=None, key=None)
        break
    st.text_area("Bot:", value=bot.get_response(user_input), height=200, max_chars=None, key=None)
    
else:
    st.text_area("Bot:", value="Please start the bot by clicking sidebar button", height=200, max_chars=None, key=None)