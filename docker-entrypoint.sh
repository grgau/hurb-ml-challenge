#!/bin/bash
GREEN='\033[0;32m'
RESET='\033[0m' # Color Reset

# Run tests
echo -e "${GREEN} [+] Running tests... ${RESET}"
pytest tests/

# Train and save model to be served with bentoml
echo -e "${GREEN} [+] Training and saving model... ${RESET}"
python src/save_serve_model.py

# Serve model
echo -e "${GREEN} [+] Serving model... ${RESET}"
bentoml serve