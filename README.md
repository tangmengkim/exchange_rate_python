# exchange_rate_python
## Setup

### 1. Prerequisites

- Python 3.x installed
- [pip](https://pip.pypa.io/en/stable/installation/) installed (Python package installer)

### 2. Create and Activate Virtual Environment

```bash
# Create a new virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On Unix/Linux/macOS
source .venv/bin/activate

# On Windows
source .venv/Scripts/activate

### 3. Install some module
pip install -r requirements.txt

### 4. Create SecretKey Environment
cp .env.example .env
### 4. Run app
python -u app.py
