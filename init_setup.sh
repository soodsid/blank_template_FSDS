echo [$(date)]: "Start"
echo [$(date)]: "creating an env"

python -m venv env

echo [$(date)]: "activating an env"
source env/Scripts/activate

echo [$(date)]: "installing the requirements"
pip install -r requirements.txt

echo [$(date)]: "end"
