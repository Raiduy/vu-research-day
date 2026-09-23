# VU Nebula Gateway Integrations

This repository provides configuration files, guides, and code examples to connect your favorite apps and scripts to **Nebula**, a secure AI service hosted at Vrije Universiteit Amsterdam (`https://nebula.cs.vu.nl/api/`). It works similarly to ChatGPT or Claude, allowing you to use advanced AI directly within your own tools.

## Repository Structure

The repository is divided into three main areas based on the type of integration:

### 1. `ai-agents/`
*(Primarily for users who write code or scripts)*
Contains configuration files and launch scripts to point popular AI coding assistants at the Nebula gateway. Supported tools include:
*   **opencode** (`opencode/opencode.json`)
*   **Claude Code** (`claudecode/launch-claude.sh`)
*   **pi** (`pi/models.json`)
*   **oh-my-pi** (`oh-my-pi/models.yml`)

See the [`ai-agents/README.md`](./ai-agents/README.md) for tool-specific setup instructions.

### 2. `obsidian/`
A guide for integrating Nebula into your Obsidian vault. It walks you through setting up the **Copilot Community Plugin** to enable quick chats, inline completions, and knowledge-graph queries directly within Obsidian. It also covers linking OpenCode to Obsidian for advanced file creation and editing.

See the [`obsidian/README.md`](./obsidian/README.md) for the setup guide.

### 3. `programatic-prompts/`
A minimal, ready-to-run Python example demonstrating how to interact with the Nebula API programmatically. It uses the modern `openai` Python SDK (v1) and `.env` files to securely manage credentials and make chat completion requests.

See the [`programatic-prompts/README.md`](./programatic-prompts/README.md) for instructions on running the script.

---

## Prerequisites

To use any of the integrations in this repository, you will need:

1.  **Access to Nebula**: Ensure your network can reach `https://nebula.cs.vu.nl/api/`.
2.  **Nebula API Key**: You must obtain a personal API key. 
    *   *Request access:* [Nebula Access Guide](https://nebula.cs.vu.nl/welcome/gettingAccess/)
    *   *Generate key:* [API Key Guide](https://nebula.cs.vu.nl/welcome/generatingApiKey/)

> **⚠️ Security Warning:** Never commit your API key to version control or share it publicly. Use environment variables or local, untracked configuration files (like `.env`) to manage your key.

---

## Next Steps: Evolving Your Setup

Once you are comfortable with the basic setups provided in this repository, you can start customizing your AI assistants to better fit your specific research or workflow needs:

### 1. Give Your Agents Custom "Skills"
Many AI agents (like **pi** or **Claude Code**) allow you to define custom skills or tools. If you find yourself repeatedly asking the AI to perform the same task (e.g., formatting references, analyzing a specific type of dataset, or querying an external API), you can write a short script and register it as a "skill." This allows the AI to run that script on your behalf whenever needed.

### 2. Extend with System Prompts and Rules
You can shape how your AI assistants behave by using custom instructions. 
- **In Obsidian (Copilot):** You can modify the system prompt in the plugin settings to tell Nebula exactly how it should answer (e.g., "Always reply in academic Dutch" or "Always cite your sources using APA format").
- **In AI Agents:** Tools like **opencode** and **Claude Code** allow you to create project-specific rules (like a `.cursorrules` or `.clauderc` file) that teach the AI about your project's context, naming conventions, and preferred workflows.

### 3. Chain Prompts Programmatically
If you are using the **Programmatic Prompts** example, you can evolve your script from a simple chat into a complex pipeline. For example, you can write a Python script that:
1. Reads all the PDFs in a folder.
2. Asks Nebula to summarize each one.
3. Asks Nebula to find common themes across all the summaries.
4. Saves the final report automatically to your Obsidian vault.

By combining these integrations, you can build a highly personalized, automated research assistant powered entirely by the secure Nebula gateway!
