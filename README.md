# Bot
## Instalación
Creando el entorno
```
$ cd bot/
$ virtualenv -p python3.9 venv && source venv/bin/activate
```
Instalando dependencias y el paquete ```bot/```
```
(venv)$ pip install -r requirements.txt && python setup.py install
```
## Corriendo
```
(venv)$ uvicorn bot.main:app
```

## Curl
```
curl -X 'POST' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://google+.com/?res=dario&res=dario,dario"
}'

------------
Response 200
{
  "url": "https://google+.com/?res=dario&res=dario,dario",
  "words": {
    "https": 1,
    "google": 1,
    "com": 1,
    "res": 2,
    "dario": 3
  }
}
```