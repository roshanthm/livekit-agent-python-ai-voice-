# 🔊 LiveKit AI Voice Assistant

**LiveKit AI Voice Assistant** is a futuristic, real-time voice-powered AI built on [LiveKit Agents](https://github.com/livekit/agents), blending powerful speech processing with intelligent task automation. It is designed to **speak, listen, understand, and act** — creating a fully interactive AI experience that goes beyond just text.

Whether you're building smart customer support, personal productivity agents, or voice-first applications, this project shows how to combine **AI + real-time voice + tools** in a unified, scalable solution.

---

## 🚀 What It Does

This voice assistant listens in real time, understands natural language via GPT-based LLMs, and responds with human-like speech — all while being capable of **real-world actions** like:

* 🌦️ **Getting Live Weather** from any city
* 🌐 **Searching the Web** using DuckDuckGo via LangChain
* 📧 **Sending Emails** with your Gmail account
* 🧠 **Conversing Smartly** using GPT-4o-mini or Google Realtime models
* 🗣️ **Real-Time Voice Communication** via Silero STT + TTS
* 🕵️ **Multilingual Turn Detection** for natural conversation flow
* 🔇 **Noise Cancellation** for crisp and clean audio
* 🎤 **Voice Activity Detection** to smartly manage when to speak and listen

---

## 🧹 Core Technologies & Tools

| Feature                        | Tech Used                          |
| ------------------------------ | ---------------------------------- |
| Voice Transmission             | [LiveKit](https://livekit.io)      |
| LLM / Reasoning                | GPT-4o-mini or Google Realtime     |
| Speech-to-Text (STT)           | Silero                             |
| Text-to-Speech (TTS)           | Silero, Google Voices              |
| Noise Cancellation             | LiveKit BVC                        |
| Voice Activity Detection (VAD) | Silero VAD                         |
| Turn Detection                 | LiveKit Multilingual Turn Detector |
| Web Search                     | DuckDuckGo via LangChain           |
| Email Sending                  | Gmail SMTP + App Password          |
| Weather API                    | wttr.in                            |
| Tool Framework                 | LiveKit Function Tools + LangChain |

---

## 💡 Why This Project Matters

This project brings voice interfaces closer to real-world usability by combining **AI reasoning**, **multimodal capabilities**, and **actionable tools**. It's more than just a virtual assistant — it's a **programmable voice agent** you can embed into apps, use for automation, or evolve into a fully custom AI support system.

Ideal for:

* 🌐 Voice-enabled apps & platforms
* 🤖 Virtual agent research
* 📞 Smart call assistants
* 🧑‍💼 Personal AI companions
* 🏢 Voice agents for enterprise workflows

---

## 🌍 Live in Action

Test or extend this voice agent in the [LiveKit Playground](https://playground.livekit.io/agents) — a real-time environment where your agent comes to life through voice.

---

## 🔐 Environment Configuration (Quick Glance)

> While setup steps are not shown here, the project securely uses `.env` for your API keys and credentials including:

* `GMAIL_USER`
* `GMAIL_APP_PASSWORD`
* Any LLM or LiveKit API tokens you might need

---

## 💬 Built by Humans, Powered by AI

This assistant was built with modularity and scale in mind. Every component — from email to search to speech — is a plug-and-play function tool, allowing developers to swap in better APIs or add new capabilities on the fly.

Welcome to the future of voice-native AI.
