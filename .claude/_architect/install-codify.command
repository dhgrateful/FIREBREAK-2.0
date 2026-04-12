#!/bin/zsh

# ============================================================
# Codify Vault Installer
# The client double-clicks this file. Everything else is automatic.
# ============================================================

clear
echo ""
echo "  ╔══════════════════════════════════════╗"
echo "  ║     Building Your Business Brain     ║"
echo "  ║                                      ║"
echo "  ║   This takes about 2 minutes.        ║"
echo "  ║   You don't need to do anything.     ║"
echo "  ╚══════════════════════════════════════╝"
echo ""

# --- Configuration ---
# The architect sets these before sending to the client
VAULT_NAME="my-vault"
GITHUB_TEMPLATE="https://github.com/mike-scott-darwin/codify-vault-template.git"
VAULT_PATH="$HOME/Documents/$VAULT_NAME"
# Set by architect — client's Claude API key for the Agent Client plugin
CLAUDE_API_KEY=""

# --- Step 1: Install Homebrew (if needed) ---
if ! command -v brew &> /dev/null; then
    echo "  [1/5] Installing package manager..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" < /dev/null

    # Add brew to PATH for Apple Silicon
    if [[ -f "/opt/homebrew/bin/brew" ]]; then
        eval "$(/opt/homebrew/bin/brew shellenv)"
        echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
    fi
else
    echo "  [1/5] Package manager ready."
fi

# --- Step 2: Install Git (if needed) ---
if ! command -v git &> /dev/null; then
    echo "  [2/5] Installing version control..."
    xcode-select --install 2>/dev/null
    # Wait for xcode-select to finish
    until command -v git &> /dev/null; do
        sleep 5
    done
else
    echo "  [2/5] Version control ready."
fi

# --- Step 3: Install Obsidian (if needed) ---
if [[ ! -d "/Applications/Obsidian.app" ]]; then
    echo "  [3/5] Installing Obsidian..."
    brew install --cask obsidian 2>/dev/null
else
    echo "  [3/5] Obsidian ready."
fi

# --- Step 4: Install Claude Code + ACP Adapter ---
if ! command -v claude &> /dev/null; then
    echo "  [4/5] Installing AI engine..."
    # Install Node.js if needed
    if ! command -v node &> /dev/null; then
        brew install node 2>/dev/null
    fi
    npm install -g @anthropic-ai/claude-code 2>/dev/null
    npm install -g @anthropic-ai/claude-agent-acp 2>/dev/null
else
    # Ensure ACP adapter is installed even if Claude Code already exists
    if ! command -v claude-agent-acp &> /dev/null; then
        npm install -g @anthropic-ai/claude-agent-acp 2>/dev/null
    fi
    echo "  [4/5] AI engine ready."
fi

# --- Step 5: Build the Vault ---
if [[ -d "$VAULT_PATH" ]]; then
    echo "  [5/5] Vault already exists at $VAULT_PATH"
else
    echo "  [5/5] Building your vault..."
    git clone "$GITHUB_TEMPLATE" "$VAULT_PATH" 2>/dev/null

    if [[ $? -ne 0 ]]; then
        mkdir -p "$VAULT_PATH"
        cd "$VAULT_PATH"
        git init -q
    fi
fi

# --- Configure Agent Client plugin with API key ---
ACP_PATH=$(which claude-agent-acp 2>/dev/null || echo "/opt/homebrew/bin/claude-agent-acp")
NODE_PATH=$(which node 2>/dev/null || echo "/opt/homebrew/bin/node")
PLUGIN_CONFIG="$VAULT_PATH/.obsidian/plugins/agent-client/data.json"

if [[ -f "$PLUGIN_CONFIG" && -n "$CLAUDE_API_KEY" ]]; then
    # Update the plugin config with the client's API key and correct paths
    python3 -c "
import json
with open('$PLUGIN_CONFIG') as f:
    config = json.load(f)
config['claude']['apiKey'] = '$CLAUDE_API_KEY'
config['claude']['command'] = '$ACP_PATH'
config['nodePath'] = '$NODE_PATH'
with open('$PLUGIN_CONFIG', 'w') as f:
    json.dump(config, f, indent=2)
" 2>/dev/null
    echo "  ✓ AI chat pane configured"
fi

# --- Open Obsidian ---
echo ""
echo "  Opening your vault..."
echo ""
open "obsidian://open?path=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$VAULT_PATH'))")"

sleep 3

echo "  ╔══════════════════════════════════════╗"
echo "  ║          You're all set.             ║"
echo "  ║                                      ║"
echo "  ║   Your vault is open in Obsidian.    ║"
echo "  ║                                      ║"
echo "  ║   When Obsidian asks to trust        ║"
echo "  ║   plugins, click 'Enable.'           ║"
echo "  ║                                      ║"
echo "  ║   Two ways to use your vault:        ║"
echo "  ║                                      ║"
echo "  ║   1. WhatsApp — message your         ║"
echo "  ║      Pocket Architect anytime         ║"
echo "  ║                                      ║"
echo "  ║   2. Obsidian — open the chat pane   ║"
echo "  ║      (Cmd+P → 'Agent Client')        ║"
echo "  ║      to run skills on your vault     ║"
echo "  ║                                      ║"
echo "  ╚══════════════════════════════════════╝"
echo ""
echo "  You can close this window."
echo ""
