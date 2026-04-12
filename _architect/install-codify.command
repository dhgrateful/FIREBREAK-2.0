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

# --- Step 4: Install Claude Code (if needed) ---
if ! command -v claude &> /dev/null; then
    echo "  [4/5] Installing AI engine..."
    # Install Node.js if needed
    if ! command -v node &> /dev/null; then
        brew install node 2>/dev/null
    fi
    npm install -g @anthropic-ai/claude-code 2>/dev/null
    npm install -g @zed-industries/claude-agent-acp 2>/dev/null
else
    # Ensure ACP adapter is installed even if Claude Code already exists
    if ! command -v claude-agent-acp &> /dev/null; then
        npm install -g @zed-industries/claude-agent-acp 2>/dev/null
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
        # If clone fails (private repo), create from scratch
        mkdir -p "$VAULT_PATH"
        cd "$VAULT_PATH"
        git init -q
    fi
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
echo "  ║   Then open the chat pane:           ║"
echo "  ║   Cmd+P → type 'Agent Client'       ║"
echo "  ║                                      ║"
echo "  ║   Your architect will take it        ║"
echo "  ║   from here.                         ║"
echo "  ╚══════════════════════════════════════╝"
echo ""
echo "  You can close this window."
echo ""
