﻿# Agentic_Ai_Ecommerce
## Agentic AI-Based E-commerce Price Tracker and Smart Buyer

This project implements an Agentic AI system that acts as a smart e-commerce assistant capable of understanding and acting on user-defined purchase rules through natural language.

With a simple instruction like:

“Track iPhone 15 on Amazon. Buy if price < $800 and seller rating > 4.”

the AI agent performs the following tasks:

Natural Language Understanding: Utilizes OpenAI's LLM to parse commands and extract structured rules.

Web Scraping: Leverages Selenium to fetch live data such as price and seller rating from platforms like Amazon.

Rule-Based Decision Making: Evaluates real-time data against extracted rules and simulates a buy action if criteria are met.

User Interface: A Streamlit app for seamless interaction and real-time feedback.

💻 Tech Stack: Python, OpenAI LLM, Selenium, Streamlit
🧩 Key Features:

Agentic AI agent that links perception (scraping) and reasoning (rule application)

Natural language interface for task delegation

Simulated autonomous decision-making

Modular architecture to support multiple platforms and products
