# 🤖 chatbot_ai

![Chatbot](https://img.shields.io/badge/Chatbot-AI-blue)
![Language](https://img.shields.io/badge/Language-Swedish-yellow)
![Framework](https://img.shields.io/badge/Framework-Streamlit-orange)
![Model](https://img.shields.io/badge/Model-GPT--4-green)

## 🌐 [Live Demo](https://chatbot-web.streamlit.app/)

## 📚 Overview

A “chatbot_ai” is a Swedish-speaking application designed to provide native Swedish speakers with a fast and informative interaction. The client aimed to offer a platform that fluently understands and responds in Swedish and only answers relevant to construction engineering questions.

Using **LlamaIndex** and  **GPT-4** LLM as well as Swedish-trained **SpaCy** model to make sure that the conversation is relevant to construction engineering and is in Swedish. The application was constructed using **Streamlit**. Other training information is provided in TXT and CSV files containing companies reports and other relevant documents.

The user-friendly interface was achieved with **Lottie** animation.

![Examaple screenshot](https://imgur.com/c8w8T7r.png)

## 📂 Supported Data Formats
The chatbot supports various data formats for its knowledge base:
- Text Files (`.txt`)
- CSV Files (`.csv`)
- URLs

Simply ingest the data, and `chatbot_ai` will convert it into documents that form the knowledge base.

## 🔐 Security
Credentials required for the application are securely stored in the `secrets.toml` file, which is excluded from the version control system using `.gitignore` 

## ☁️ Deployment
`chatbot_ai` is deployed on **Streamlit Community Cloud**.

## 🔗 Access the Web App
The application is accessible online. Visit [chatbot-web.streamlit.app](https://chatbot-web.streamlit.app/) to interact with `chatbot_ai`.

## 🚀 Quick Start
1. Clone the repository
2. Install dependencies
3. Set up your `secrets.toml` file with the necessary credentials
4. Run the Streamlit app

