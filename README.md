# 🧠 Mixture of Agents — LLM Aggregator App

This project demonstrates how to build a **Mixture of Agents** app using open-source language models and the [Together API](https://api.together.xyz). It takes a user query, collects responses from multiple reference models, and synthesizes a final answer using an aggregator model — all through a simple Streamlit interface.

> 🔍 Inspired by a Telegram post that sparked curiosity — could multiple LLMs really be orchestrated in under 50 lines of code? Turns out, yes.

---

## 🚀 Live Demo

🌐 **App**: [mixture-of-agents-01.streamlit.app](https://mixture-of-agents-01.streamlit.app/)  
🔑 **Get API Key**: [Together API Keys](https://api.together.xyz/settings/api-keys)

---

## 🧰 Features

- 🔄 Runs multiple open-source LLMs in parallel
- 🧠 Aggregates responses using a separate LLM with a custom system prompt
- 💬 Simple, interactive interface built with Streamlit
- ⚙️ Works with **Together AI**'s hosted models

---

## 🧪 Models Used

### Reference Models:
- `Qwen/Qwen2-72B-Instruct`
- `mistralai/Mistral-7B-Instruct-v0.1`

### Aggregator Model:
- `mistralai/Mistral-7B-Instruct-v0.1`  
  > Uses a system prompt to synthesize a clear, unified answer.

---

## 🔧 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/PrathamPatel-01/mixture-of-agents.git
cd mixture-of-agents



