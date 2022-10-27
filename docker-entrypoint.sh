#!/bin/bash

# Train and save model to be served with bentoml
python src/save_serve_model.py

# Serve model
bentoml serve