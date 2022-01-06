mkdir "Virtualios aplinkos"
cd "Virtualios aplinkos"
py -m venv venv
venv\Scripts\activate
pip list
pip install pyinstaller
pip list
pip freeze
pip freeze > requirements.txt
pip install -r requirements.txt