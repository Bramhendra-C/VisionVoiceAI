#!/bin/bash

# --- Configuration ---
PYTHON_CMD="python3"
VENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"

# --- Helper Functions ---
echo_info() {
    echo "INFO: $1"
}

echo_success() {
    echo "✅ SUCCESS: $1"
}

echo_error() {
    echo "❌ ERROR: $1" >&2
    exit 1
}

# --- Main Script ---

# 1. Check for Python 3
if ! command -v $PYTHON_CMD &> /dev/null; then
    echo_error "$PYTHON_CMD could not be found. Please install Python 3."
fi
echo_info "Python 3 found."

# 2. Check for pip
if ! $PYTHON_CMD -m pip --version &> /dev/null; then
    echo_error "pip for $PYTHON_CMD could not be found. Please ensure pip is installed."
fi
echo_info "pip found."

# 3. Create requirements.txt
echo_info "Creating $REQUIREMENTS_FILE..."
cat > $REQUIREMENTS_FILE << EOL
opencv-python
speechrecognition
pyaudio
pygame
pywhatkit
pyttsx3
wikipedia
pyjokes
requests
EOL
echo_success "$REQUIREMENTS_FILE created."

# 4. Create Virtual Environment
if [ -d "$VENV_DIR" ]; then
    echo_info "Virtual environment '$VENV_DIR' already exists."
else
    echo_info "Creating virtual environment at '$VENV_DIR'..."
    $PYTHON_CMD -m venv $VENV_DIR
    if [ $? -ne 0 ]; then
        echo_error "Failed to create virtual environment."
    fi
    echo_success "Virtual environment created."
fi

# 5. Install Dependencies into VENV
echo_info "Installing dependencies from $REQUIREMENTS_FILE into $VENV_DIR..."
# Activate the venv and install
source $VENV_DIR/bin/activate
pip install -r $REQUIREMENTS_FILE

if [ $? -ne 0 ]; then
    echo_error "Failed to install dependencies. Please check for errors above."
fi
deactivate
echo_success "All dependencies installed."

# 6. Final Instructions
echo ""
echo "--- 🚀 SETUP COMPLETE 🚀 ---"
echo ""
echo "Your project is almost ready. Just two more steps:"
echo ""
echo "1. CONFIGURE API KEYS:"
echo "   Open 'voice_assistant.py' and set your API key and music folder:"
echo "   - OPENWEATHERMAP_API_KEY = \"your_api_key_here\" (line 20)"
echo "   - MUSIC_DIR = \"/path/to/your/music_folder\" (line 21)"
echo ""
echo "2. RUN THE APPLICATION:"
echo "   First, activate the virtual environment:"
echo "   source $VENV_DIR/bin/activate"
echo ""
echo "   Then, run the main script:"
echo "   python3 start.py"
echo ""
