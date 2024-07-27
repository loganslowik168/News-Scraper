#!/bin/bash

# Path to the virtual environment
VENV_PATH="/home/slowikl/PythonPrograms/Environments/NewsScraper"

# Activate the virtual environment
source "$VENV_PATH/bin/activate"

# Check if the virtual environment was activated successfully
if [[ "$?" != 0 ]]; then
  echo "Failed to activate virtual environment: $VENV_PATH"
  exit 1
fi

# Run the Python script
python /home/slowikl/PythonPrograms/NewsScraper/News-Scraper/dataSearch.py

# Deactivate the virtual environment
deactivate

