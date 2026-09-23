# Configuring Coding Agents against the Nebula Gateway

This folder contains the configuration files that point four different coding agents at the
same internal model gateway — **Nebula**, an OpenAI/Anthropic-compatible API hosted at
`https://nebula.cs.vu.nl/api/`.

Each file configures a different tool, but they all do the same job: tell the agent
*where* the models live (the Nebula base URL), *how* to authenticate (an API key), and
*which* models are available.

| File | Configures | Format | Endpoint style | Link |
|------|------------|--------|----------------|------|
| [`opencode.json`](./opencode/opencode.json)     | **opencode** | JSON | OpenAI-compatible | [https://opencode.ai/](https://opencode.ai/) |
| [`launch-claude.sh`](./claudecode/launch-claude.sh)  | **Claude Code** | Bash / env vars | Anthropic-compatible | [https://claude.com/product/claude-code](https://claude.com/product/claude-code) |
| [`models.json`](./pi/models.json)    | **pi** coding agent | JSON | OpenAI-compatible | [https://pi.dev/](https://pi.dev/) |
| [`models.yml`](./oh-my-pi/models.yml) | **Oh-My-Pi** | YAML | OpenAI-compatible | [https://omp.sh/](https://omp.sh/) |

---

## The Nebula gateway

All four configurations target the same host:

- **Base URL:** `https://nebula.cs.vu.nl/api/`
- **API style:** OpenAI-compatible chat/completions (pi and oh-my-pi declare `api: openai-completions`;
  opencode uses the `@ai-sdk/openai-compatible` adapter; Claude Code connects through its Anthropic-compatible
  client, pointed at the same base URL).

---

## Prerequisites

1. **Get your API key from Nebula.** Every file contains the placeholder
   `REPLACE_WITH_YOUR_API_KEY`. Replace it with your real Nebula API key in each file
you want to use. Please check the [API Key guide](https://nebula.cs.vu.nl/welcome/generatingApiKey/) for instructions on how to obtain your key.
2. **Make sure you can reach the gateway** (`https://nebula.cs.vu.nl/api/`).

> **WARNING**: keep your API key to yourself, and yourself only. Watch out for files that you commit to public repos, or share with others. If you think your key has been compromised, generate a new one.

---

## 1. opencode — [`opencode.json`](./opencode/opencode.json)

### How to install
Compatible with: macOS / Linux / WSL

```bash
curl -fsSL https://opencode.ai/install | bash
```

This file configures **opencode** (opencode.ai) with a custom provider named `Nebula`
using the OpenAI-compatible SDK adapter.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "Nebula": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Nebula API",
      "options": {
        "baseURL": "https://nebula.cs.vu.nl/api/",
        "apiKey": "REPLACE_WITH_YOUR_API_KEY"
      },
      "models": {
        "FAST.gpt-oss:120b": { "name": "FAST.gpt-oss:120b" },
        "FAST.gemma4:31b": { "name": "FAST.gemma4:31b" },
        "SURF.gpt-oss-120b": { "name": "SURF.gpt-oss-120b" },
        "SURF.Mistral-Small-3.2-24B-Instruct-2506": { "name": "SURF.Mistral-Small-3.2-24B-Instruct-2506" },
        "SURF.Qwen3.8-27B-FP8": { "name": "SURF.Qwen3.8-27B-FP8" }
      }
    }
  }
}
```

**How to configure:**

1. Replace `REPLACE_WITH_YOUR_API_KEY` in the `options.apiKey` field.
2. Place `opencode.json` where opencode looks for config:
   - **Project level:** in the project root (the file is already named `opencode.json`), or
   - **User level:**
     - macOS / Linux / WSL: `~/.config/opencode/opencode.json`
     - Windows: `%APPDATA%\opencode\opencode.json`
3. Start `opencode` and select a Nebula model from the model list.

Note: opencode's provider block keys models by their full id and the `npm` field
(`@ai-sdk/openai-compatible`) is what makes it speak the OpenAI-compatible API. Keep both
when editing.


---

## 2. Claude Code — [`launch-claude.sh`](./claudecode/launch-claude.sh)

### How to install
Compatible with: macOS / Linux / WSL

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

This is a launcher script rather than a config file. It exports a set of
`ANTHROPIC_*` environment variables that redirect Claude Code at Nebula, then runs `claude`.

```bash
export ANTHROPIC_API_KEY="REPLACE_WITH_YOUR_API_KEY"          # your Nebula key
export ANTHROPIC_BASE_URL=https://nebula.cs.vu.nl/api/        # the gateway
export ANTHROPIC_DEFAULT_OPUS_MODEL="SURF.Qwen3.8-27B-FP8"
export ANTHROPIC_DEFAULT_SONNET_MODEL="FAST.gpt-oss:120b"
export ANTHROPIC_DEFAULT_FABLE_MODEL="FAST.gemma4:31b"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="SURF.Mistral-Small-3.2-24B-Instruct-2506"

claude
```

**How the tiers map to models:**

| Claude tier | Meaning | Nebula model |
|-------------|---------|--------------|
| `OPUS`  | most capable | `SURF.Qwen3.8-27B-FP8` |
| `SONNET` | balanced default | `FAST.gpt-oss:120b` |
| `FABLE`  | mid | `FAST.gemma4:31b` |
| `HAIKU`  | fast / cheap | `SURF.Mistral-Small-3.2-24B-Instruct-2506` |

**To configure:**

1. Edit `launch-claude.sh` and replace `REPLACE_WITH_YOUR_API_KEY` with your key.
2. (Optional) Adjust the `ANTHROPIC_DEFAULT_*_MODEL` values to point the tiers at different
   models, or add the unused `SURF.gpt-oss-120b` if you want it available.
3. Run it: `./launch-claude.sh`.

> The script makes the exports apply only to that one invocation. To make them permanent, add all the lines containing `export` to your shell profile (a hidden configuration file for your terminal):
> - **macOS:** Open terminal and edit `~/.zshrc` (e.g., using `nano ~/.zshrc`)
> - **Linux / WSL:** Open terminal and edit `~/.bashrc`
> - **Windows:** Open PowerShell and edit `$PROFILE`
> 
> If you are uncomfortable editing these files, you can just run the export commands directly in your terminal every time before you run `claude`.

---

## 3. pi — [`models.json`](./pi/models.json)

### How to install
Compatible with: macOS / Linux / WSL

```bash
curl -fsSL https://pi.dev/install.sh | sh
```

Compatible with Windows (PowerShell):

```powershell
powershell -c "irm https://pi.dev/install.ps1 | iex"
```

This file configures the **pi** coding agent's compatible-endpoint models. It matches pi's
`models.json` schema exactly.

```json
{
  "providers": {
    "Nebula": {
      "baseUrl": "https://nebula.cs.vu.nl/api/",
      "api": "openai-completions",
      "apiKey": "REPLACE_WITH_YOUR_API_KEY",
      "models": [
        { "id": "FAST.gpt-oss:120b" },
        { "id": "FAST.gemma4:31b" },
        { "id": "SURF.gpt-oss-120b" },
        { "id": "SURF.Mistral-Small-3.2-24B-Instruct-2506" },
        { "id": "SURF.Qwen3.8-27B-FP8" }
      ]
    }
  }
}
```

**How to configure:**

1. Replace `REPLACE_WITH_YOUR_API_KEY` (or use `apiKey: "$NEBULA_API_KEY"` and export
   `NEBULA_API_KEY` in your shell).
2. Move and rename the file to where pi reads models:
   - **User level:**
     - macOS / Linux / WSL: `~/.pi/agent/models.json`
     - Windows: `%USERPROFILE%\.pi\agent\models.json`
   - **Project level:** `<project-dir>/.pi/models.json` (loads after the project is trusted)

   So copy `models.json` to the appropriate location, or use it
   as a template for that file.
3. Run `pi` in your working directory. Opening `/model` reloads the file, so new or
   changed models appear there without a restart.

All five models are listed, so any of them can be selected/cycled with pi's model picker.

---

## 4. oh-my-pi — [`models.yml`](./oh-my-pi/models.yml)

### How to install
Compatible with: macOS / Linux / WSL

```bash
curl -fsSL https://omp.sh/install | sh
```

This is a YAML variant of the same Nebula provider configuration, used by the
**oh-my-pi** setup.

```yaml
providers:
  nebula:
    baseUrl: https://nebula.cs.vu.nl/api
    api: openai-completions
    apiKey: REPLACE_WITH_YOUR_API_KEY
    models:
      - id: FAST.gpt-oss:120b
        name: FAST.gpt-oss:120b
      - id: FAST.gemma4:31b
        name: FAST.gemma4:31b
      - id: SURF.gpt-oss-120b
        name: SURF.gpt-oss-120b
      - id: SURF.Mistral-Small-3.2-24B-Instruct-2506
        name: SURF.Mistral-Small-3.2-24B-Instruct-2506
      - id: SURF.Qwen3.8-27B-FP8
        name: SURF.Qwen3.8-27B-FP8
```

**How to configure:**

1. Replace `REPLACE_WITH_YOUR_API_KEY` in the `apiKey` field.
2. Copy `models.yml` to the configuration directory and start `oh-my-pi` using the `omp` command:
   - **User level:**
     - macOS / Linux / WSL: `~/.omp/agent/models.yml`
     - Windows: `%USERPROFILE%\.omp\agent\models.yml`
   - **Project level:** `<project-dir>/.omp/models.yml`
3. To use more models, add more entries under `models:` using the ids from the model
   catalog above (e.g. `SURF.Qwen3.8-27B-FP8`, `SURF.Mistral-Small-3.2-24B-Instruct-2506`,
   or `SURF.gpt-oss-120b`).

---

## Common gotchas
- **Model ids must match exactly**, including the `:` in `gpt-oss:120b` and the version
  suffix in `Mistral-Small-3.2-24B-Instruct-2506`. Note that `FAST.gpt-oss:120b` and
  `SURF.gpt-oss-120b` are *different* models, not duplicates.
- **Reload after editing:** pi reloads on `/model`; Claude Code picks up new env vars only
  in a new invocation (re-run the script or re-export in the shell); opencode and oh-my-pi
  read the file on start.

## Quick checklist

- [ ] Replaced `REPLACE_WITH_YOUR_API_KEY` in each file you use (or switched to an env var).
- [ ] opencode: place `opencode.json` (project root or `~/.config/opencode/`).

- [ ] Claude Code: edited `launch-claude.sh` and ran `./launch-claude.sh` or placed the lines containing `export` to the shell profile.
- [ ] pi: installed `models.json` (`~/.pi/agent/` or project `.pi/`).
- [ ] oh-my-pi: installed `models.yml` (`~/.omp/agent/` or project `.omp/`).
- [ ] Can reach `https://nebula.cs.vu.nl/api/`.
