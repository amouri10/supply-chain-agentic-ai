# 🛒 Enterprise Supply Chain & Procurement Engine

An autonomous, multi-agent AI procurement system designed to intercept critical warehouse inventory deficits, calculate restocking parameters under strict margin thresholds, and autonomously negotiate B2B bulk purchase contracts.

![Python](https://shields.io)
![Framework](https://shields.io)
![UI](https://shields.io)
![License](https://shields.io)

## 🏢 System Architecture Overview

This application bridges the gap between raw data parsing and operational execution. It converts raw system log anomalies into complete, structured business workflows without human intervention.


**The Parameter Layer:** A responsive Streamlit UI dashboard lets managers configure supplier names, retail anchors, and wholesale cost margins on the fly.
2. **The Logistics Core (Agent 1):** Parses unstructured text log streams, calculates unfulfilled backlogs, and establishes mathematically safe wholesale target budgets.
3. **The B2B Negotiation Layer (Agent 2):** Takes the analytical output and constructs an institutional-grade, formal wholesale purchase order contract proposal.

## 🛠️ Tech Stack & Dependencies

- **Orchestration Framework:** CrewAI (Sequential Process Management)
- **Local Model Engine:** Ollama running an isolated `llama3.1` model
- **Data Validation & Integrity:** Pydantic (Strict typing constraint models)
- **User Interface Framework:** Streamlit (Dark-mode corporate dashboard UI)
- **Data Structuring Core:** Python 3.10+ & Pandas

## 💻 Local Installation & Setup

To run this full-stack suite entirely on your own hardware for free, follow these installation rules:

1. **Clone the repository space:**
   ```bash
   git clone https://github.com
   cd supply-chain-agentic-ai
   ```

2. **Initialize and activate an isolated virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate.ps1 # On Windows PowerShell
   ```

3. **Install the required package dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your local environment keys (`.env`):**
   Create a `.env` file in the root folder and point it to your active Ollama instance:
   ```env
   OPENAI_API_BASE="http://localhost:11434/v1"
   OPENAI_API_KEY="ollama"
   OPENAI_MODEL_NAME="llama3.1"
   ```

5. **Fire up the local host web server:**
   ```bash
   streamlit run run_ecommerce_suite.py
   ```

## 📊 Core Features & Implementation Details

- **Deterministic Typing Constraints:** Uses strict `Pydantic` data structures ensuring numbers are managed as data entries rather than basic text strings, preventing calculation hallucinations.
- **Asynchronous Loop Safe Handling:** Wrapped natively inside Python's `asyncio` framework loop parameters to ensure stability across core Windows operating systems.
- **Dynamic Variable Injection:** Allows operational parameters to shift in real time without restarting the backend multi-agent pipeline threads.
