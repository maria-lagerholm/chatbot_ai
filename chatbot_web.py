import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader
from llama_index import BeautifulSoupWebReader
from llama_index.memory import ChatMemoryBuffer
from langdetect import detect

from pathlib import Path
from llama_index import download_loader

from llama_index import ServiceContext, LLMPredictor, OpenAIEmbedding, PromptHelper
from llama_index import StorageContext, load_index_from_storage
from llama_index.llms import OpenAI
from llama_index.text_splitter import TokenTextSplitter
from llama_index.node_parser import SimpleNodeParser
from spacy.matcher import PhraseMatcher

import os 

# Check if spacy is installed
try:
    import spacy
except ModuleNotFoundError:
    os.system("pip install spacy")

# Download the model if not already installed
try:
    nlp = spacy.load("sv_core_news_sm")
except IOError:
    os.system("python -m spacy download sv_core_news_sm")

# Read terms from file into a list
with open('construction_terms.txt', 'r', encoding='utf-8') as file:
    terms = [line.strip() for line in file]

# Create pattern objects for each term
patterns = [nlp.make_doc(text) for text in terms]

# Initialize PhraseMatcher
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

# Add the patterns to the matcher
matcher.add("TerminologyList", patterns)


st.markdown("""
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
    .reportview-container h1 {
        font-size: 1.5em;
        color: #0e3b62; 
        text-align: center;
        padding: 1em;
        background: #f1f1f1; 
        border-radius: 10px;
        border: 1px solid #ccc;
        box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)


st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)







memory = ChatMemoryBuffer.from_defaults(token_limit=1024)

# Initialize message history
openai.api_key = st.secrets.openai_key





# Suggested questions
suggested_questions = [
    "Vilka typer av besiktningar erbjuder ni?",
    "Vad är en statusbesiktning?"
    
]


st.header("Chatta med vår AI-assistent")
cols = st.columns(2)
for idx, question in enumerate(suggested_questions):
    if idx % 2 == 0:
        col = cols[0]
    else:
        col = cols[1]
    
    if col.button(question, key=f"main_{idx}"):
        st.session_state.messages.append({"role": "user", "content": question})


if "messages" not in st.session_state.keys(): # Initialize the chat message history

    st.session_state.messages = [
        {"role": "assistant", "content": "Hej! Hur kan jag hjälpa dig?"}
    ]


@st.cache_resource(show_spinner=False)
def load_data():
    print("Debug: Inside load_data function")
    with st.spinner(text="Vänligen vänta"):
        try:
            print("Debug: Before loading data")
            
            # Initialize SimpleDirectoryReader
            reader_txt = SimpleDirectoryReader(input_dir="./data", recursive=True)
            docs = reader_txt.load_data()
            print("Debug: Loaded docs from directory")
            
            # Initialize BeautifulSoupWebReader for URLs
            reader_url = BeautifulSoupWebReader()
          
            
            docs_with_urls = []
            for url in urls_data:
                url_docs = reader_url.load_data(urls=[url])
                for doc in url_docs:
                    doc.metadata = {"source_url": url}
                    docs_with_urls.append(doc)
            print("Debug: Loaded docs from URLs")
            
            # Initialize SimpleCSVReader
            SimpleCSVReader = download_loader("SimpleCSVReader")
            loader_csv = SimpleCSVReader(encoding="utf-8")
            csvs = loader_csv.load_data(file=Path('./data/2023-Provtryckning-och-fukt-planering-2022-PLANERING.csv'))
            print("Debug: Loaded CSV data")
            
            # Setting up the chat engine components
            system_prompt = "You are a friendly chatbot assistant for a Swedish construction company website."
            llm = OpenAI(model="gpt-4", temperature=0, max_tokens=512, system_prompt=system_prompt)
            embed_model = OpenAIEmbedding()
            node_parser = SimpleNodeParser.from_defaults(text_splitter=TokenTextSplitter(chunk_size=512, chunk_overlap=128))
            service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model, node_parser=node_parser)
            
            # Combining documents and creating the index
            index = VectorStoreIndex.from_documents(docs + docs_with_urls + csvs, service_context=service_context)
            print("Debug: Data loaded successfully, index created")
            
            return index
        except Exception as e:
            st.error(f"Ett fel inträffade: {e}")
            print("Debug: Exception occurred in load_data:", e)
            return None





index = load_data()

# rebuild storage context
#storage_context = StorageContext.from_defaults(persist_dir='./storage')
# load index
#index = load_index_from_storage(storage_context)

chat_engine = index.as_chat_engine(chat_mode="context", verbose=True, temperature=0, memory=memory)

def validate_response(response):
    default_response = "Hej, jag är en AI-assistent. Hur kan jag hjälpa dig?"

    if response.startswith(default_response):
        response = response[len(default_response):] 

    if any(char.isdigit() for char in response):  
        response += " Observera: Jag är en AI-chatbot som ger en grundläggande översikt över företaget. Informationen kan variera och vara opålitlig."

     #Check if the response is in Swedish
    if detect(response) != 'sv':
        response = "Jag kan tyvärr endast svara på frågor på svenska. Vänligen ställ din fråga på svenska."

    # Check the presence of construction terms in the response using the PhraseMatcher
    response_doc = nlp(response)
    matches = matcher(response_doc)
    if not matches:
        response = "Jag är här för att svara på frågor som rör bygg och konstruktion. Vänligen ställ en relevant fråga."

    return response

#animation
import json
import requests
from streamlit_lottie import st_lottie

# Fetch the animation JSON
url = requests.get("https://lottie.host/822ac1bc-dc68-4c90-92f3-73ae9700ab52/WP9AChIbpE.json")
url_json = dict()
if url.status_code == 200:
    url_json = url.json()
else:
    print("Error in URL")

# Initialize columns
left_column, right_column = st.columns([1, 1])

# Display the lottie animation with dynamic height and width in the center column
# Move the animation code to the right column

with right_column:
    url = requests.get("https://lottie.host/5ac21fad-dc31-4f5a-be50-2ff04beefeb5/cXDavOrqiu.json")
    url_json = dict()
    if url.status_code == 200:
        url_json = url.json()
    else:
        print("Error in URL")

    st_lottie(url_json,
              reverse=True,
              height='50%',  
              width='50%',
              speed=1,
              loop=True,
              quality='high',
              key='Car'
              )

# Move your chat history to the left column
with left_column:

    # Display the chat history
    for message in st.session_state.messages: 
        with st.spinner("Vänligen vänta..."):
            with st.chat_message(message["role"]):
                st.write(message["content"])

# Place the chat input outside the columns to avoid the error
if prompt := st.chat_input("Din fråga"):
    with st.spinner("Vänligen vänta..."): 
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.experimental_rerun()  

# Pass query to chat engine and display response
if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Vänligen vänta..."):
            response = chat_engine.chat(st.session_state.messages[-1]["content"])
            validated_response = validate_response(response.response)
            st.write(validated_response)
            message = {"role": "assistant", "content": validated_response}
            st.session_state.messages.append(message)
