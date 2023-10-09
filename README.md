# 🤖 chatbot_ai

![Chatbot](https://img.shields.io/badge/Chatbot-AI-blue)
![Language](https://img.shields.io/badge/Language-Swedish-yellow)
![Framework](https://img.shields.io/badge/Framework-Streamlit-orange)
![Model](https://img.shields.io/badge/Model-GPT--4-green)

## 🌐 [Live Demo](https://chatbot-web.streamlit.app/)

## 📚 Overview

A “chatbot_ai” is a Swedish-speaking application designed to provide native Swedish speakers with a fast and informative interaction experiences. The client aimed to offer an intuitive platform that fluently understands and responds in Swedish and only answers relevant to construction engineering questions.

Utilising **LlamaIndex** and  **GPT-4** LLM, this chatbot effectively grasped the nuances of the Swedish language while delivering accurate responses. It also uses the Swedish-trained **SpaCy** model to make sure that the conversation is relevant to construction engineering. I integrated these technologies, with a focus on optimising LlamaIndex for precision and leveraging GPT-4 LLM for enhanced conversational capabilities. The application was constructed using **Streamlit**, selected for its lightweight properties and straightforward deployment process, a smooth launch and reliable performance. It accesses webpages like hitta.se and allabolag.se to provide the customer with the most recent information about the company in question. Other training information is provided in TXT and CSV files containing companies reports and other relevant documents.

Upon completion, “chatbot_ai” received positive feedback for its user-friendly interface with a friendly **Lottie** animation and accurate language processing, meeting the client’s objective of creating a tool that resonates with Swedish speakers by providing fast and engaging interactions.

![Examaple screenshot](https://imgur.com/c8w8T7r.png)

## 📂 Supported Data Formats
The chatbot supports various data formats for its knowledge base:
- Text Files (`.txt`)
- CSV Files (`.csv`)
- URLs

Simply ingest the data, and `chatbot_ai` will convert it into documents that form the knowledge base.

## 🔐 Security
Credentials required for the application are securely stored in the `secrets.toml` file, which is excluded from the version control system using `.gitignore` to ensure security and privacy.

## ☁️ Deployment
`chatbot_ai` is deployed on **Streamlit Community Cloud**. The application's secrets are managed and used in compliance with the Community Cloud modal, ensuring a secure and stable deployment environment.

## 🔗 Access the Web App
The application is accessible online. Visit [chatbot-web.streamlit.app](https://chatbot-web.streamlit.app/) to interact with `chatbot_ai`.

## 🚀 Quick Start
1. Clone the repository
2. Install dependencies
3. Set up your `secrets.toml` file with the necessary credentials
4. Run the Streamlit app


## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

## 🌟 Show your support
Give a ⭐️ if this project helped you!
