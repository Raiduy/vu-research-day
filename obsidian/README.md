# Integrating Nebula with Obsidian (Copilot Community Plugin)

This guide walks you through adding **Nebula**—the AI‑augmented knowledge‑graph engine—to your Obsidian vault using the **Copilot** community plugin.

---

## Prerequisites

| Requirement | Version / Details |
|-------------|-------------------|
| **Obsidian** | v1.5.0 or newer |
| **Copilot Community Plugin** | Latest release (install from Obsidian's Community Plugins marketplace) |
| **Nebula Account** | Request your Nebula account [here](https://nebula.cs.vu.nl/welcome/gettingAccess/) |
| **Nebula API Key** | Follow [these instructions](https://nebula.cs.vu.nl/welcome/generatingApiKey/) to generate your API Key |

---

## 1. Install the Copilot Plugin

1. Open Obsidian → **Settings → Community plugins → Browse**.  
2. Search **“Copilot”** (by *Logan Yang*).  
3. Click **Install**, then **Enable**.  

---

## 2. Add Nebula as a Custom Provider

Copilot can talk to any OpenAI‑compatible backend via a **custom provider**.

1. Go to the Copilot settings -> BYOK.
2. Click **+ Add Provider** and **+ Add Custom Provider**.
3. Give it a name (e.g., *Nebula*), and set the **Base URL** to your Nebula endpoint (e.g., `https://nebula.cs.vu.nl/api`), paste your **API key**, and add the models you would like to use from Nebula (e.g., `FAST.gemma4:31b`).
4. Save the new provider.

---

## 3. [Highly Recommended] Add OpenCode as agent

Copilot can optionally use OpenCode agents to automatically create and edit files for you in your vault. If you only want to chat with the AI, you can skip this step.

1. Go to the Copilot settings -> Basic.
2. Modify `Default Backend` to opencode.
3. Scroll down to the opencode configuration and click on `Configure`.
4. Click Auto-detect if you have it installed, otherwise install it (See [setup guide](../ai-agents/README.md)).
5. Now you should be able to see all the models that you configured in OpenCode below the `Default effort` setting tagged as `Agent Provided`.

---

## 4. Using Nebula Inside Obsidian

### 4.1 Quick Chat (Command Palette)

1. Press `Ctrl+P` (or `Cmd+P` on macOS) → type **“Copilot: New Chat”**.  
2. Choose **Nebula** as the provider (or rely on the default).  
3. Type your question, e.g., *“What are the key take‑aways from my meeting notes on 2024‑09‑10?”*.

### 4.2 Inline Completion (Selection)

1. Highlight a portion of text (or place the cursor where you want a continuation).  
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) → **“Copilot: Complete Selection”**.
3. Nebula will generate completions using the prompt template, automatically including relevant vault notes.

### 4.3 Knowledge‑Graph Queries

You can ask structured questions to interact with your vault:

- *“Show me all notes that reference ‘quantum entanglement’ and were created last month.”*  
- *“Create a mind‑map of my research on ‘AI safety’ linking to related papers.”*

Nebula will respond with markdown that includes Obsidian wikilinks (`[[Note Title]]`), which you can click to navigate instantly.

---

### 🎉 You’re ready!

With the steps above, Nebula is now a first‑class AI assistant inside your Obsidian vault. Ask questions, generate content, and let the knowledge graph power your workflow. Happy note‑taking!
