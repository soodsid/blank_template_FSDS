# Project Setup Instructions

This guide outlines the steps to initialize and set up the project environment for a new project.

## 1. Project Initialization

Before generating the project structure, you need to configure the project name and ensure dependencies are defined.

### Step 1: Configure Package Name
Open `template.py` and verify the `package_name` variable matches your desired project name.
```python
# template.py
package_name = "NPI"  # Change "package_name" to your project name (e.g., "NPI")
```

### Step 2: Verify Dependencies
Ensure `requirements.txt` contains all necessary initial libraries. It must include `-e .` to install the package in editable mode.
```text
# requirements.txt
-e .
# Add other dependencies here (e.g., pandas, numpy, etc.)
```

### Step 3: Generate Project Structure
Run the template script to create the standard folder structure (src, notebooks, etc.).
```bash
python template.py
```

## 2. Environment Setup

Once the structure is created, set up the virtual environment and install dependencies.

### Option A: Using Setup Script (Recommended)
Run the initialization script using a bash shell (e.g., Git Bash).
```bash
bash init_setup.sh
```
This script will:
1. Create a virtual environment (`env`).
2. Activate the environment.
3. Install the requirements from `requirements.txt`.

### Option B: Manual Setup
If you prefer to set it up manually:

1. **Create Virtual Environment**
   ```bash
   python -m venv env
   ```

2. **Activate Environment**
   *   **Windows**:
       ```cmd
       env\Scripts\activate
       ```
   *   **Linux/Mac/Git Bash**:
       ```bash
       source env/Scripts/activate
       ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
