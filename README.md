# Model to prod tutorial
## Run local server
``` bash
cp .env.example .env
python app.py
```

## Run client
``` bash
python client.py
```
## Run production server
``` bash
zip -r model2prod.zip . -x venv\* -x .git\* -x .idea\* -x __pycache__\*
scp model2prod.zip user@server:projects/model2prod.zip
ssh user@server
cd /projects
unzip model2prod.zip -d model2prod
cd model2prod
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
waitress-serve --port=2023 app:app
```