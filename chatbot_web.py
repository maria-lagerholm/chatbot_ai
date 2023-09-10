
hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Style the header
st.markdown("""
<style>
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
from llama_index.llms import OpenAI
from llama_index.text_splitter import TokenTextSplitter
from llama_index.node_parser import SimpleNodeParser


memory = ChatMemoryBuffer.from_defaults()#token_limit=1024)

# Initialize message history
openai.api_key = st.secrets.openai_key



# Suggested questions
suggested_questions = [
    "Kan ni berätta mer om de tjänster ni erbjuder?",
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
    with st.spinner(text="Vänligen vänta"):
        try:
            reader_txt = SimpleDirectoryReader(input_dir="./data", recursive=True)
            docs = reader_txt.load_data()
            reader_url = BeautifulSoupWebReader()
            
            urls_data = [
                'https://www.allabolag.se/5569418576/byggok-ab', 
                'https://www.merinfo.se/foretag/Byggok-AB-5569418576/2k3vyvk-1ahbo', 
                'https://www.hitta.se/byggok+ab/kinna/llguyantu', 
                'https://www.bolagsfakta.se/5569418576-Byggok_AB', 
                'https://www.ratsit.se/5569418576-Byggok_AB'
            ]
            
            docs_with_urls = []
            for url in urls_data:
                url_docs = reader_url.load_data(urls=[url])
                for doc in url_docs:
                    doc.metadata = {"source_url": url}
                    docs_with_urls.append(doc)
            
            SimpleCSVReader = download_loader("SimpleCSVReader")

            loader_csv = SimpleCSVReader(encoding="utf-8") #input_dir="./data", 
            csvs = loader_csv.load_data(file=Path('./data/2023-Provtryckning-och-fukt-planering-2022-PLANERING.csv'))


            system_prompt=("You are a friendly chatbot assistant for a Swedish construction company website.")
            llm = OpenAI(model="gpt-4", temperature=0, max_tokens=1024, system_prompt=system_prompt)
            
            embed_model = OpenAIEmbedding()
            node_parser = SimpleNodeParser.from_defaults(
              text_splitter=TokenTextSplitter(chunk_size=4096, chunk_overlap=248)
            )
            prompt_helper = PromptHelper(
              context_window=4096, 
              num_output=2048, 
              chunk_overlap_ratio=0.1, 
              chunk_size_limit=None
            )

            service_context = ServiceContext.from_defaults(
              llm=llm,
              embed_model=embed_model,
              node_parser=node_parser,
              prompt_helper=prompt_helper
            )



            index = VectorStoreIndex.from_documents(docs + docs_with_urls + csvs, service_context=service_context)
            return index
        except Exception as e:
            st.error(f"Ett fel inträffade: {e}")
            return None



index = load_data()
chat_engine = index.as_chat_engine(chat_mode="context", temperature=0, memory=memory, verbose=True)

def validate_response(response):
    default_response = "Hej, jag är en AI-assistent. Hur kan jag hjälpa dig?"

    if response.startswith(default_response):
        response = response[len(default_response):]  # Remove the default message from the response

    if any(char.isdigit() for char in response):  
        response += " Observera: Jag är en AI-chatbot som ger en grundläggande översikt över företaget. Informationen kan variera och vara opålitlig."

    # Check if the response is in Swedish
    if detect(response) != 'sv':
        response = "Jag kan tyvärr endast svara på frågor på svenska. Vänligen ställ din fråga på svenska."

    return response





# Display the chat history
for message in st.session_state.messages: 
    with st.spinner("Vänligen vänta..."):
        with st.chat_message(message["role"]):
            st.write(message["content"])


if prompt := st.chat_input("Din fråga"):
    with st.spinner("Vänligen vänta..."): 
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.experimental_rerun()  # Force a rerun to update the chat history

# Pass query to chat engine and display response
if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Vänligen vänta..."):
            response = chat_engine.chat(st.session_state.messages[-1]["content"])
            validated_response = validate_response(response.response)
            st.write(validated_response)
            message = {"role": "assistant", "content": validated_response}
            st.session_state.messages.append(message)

