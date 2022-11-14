from fastapi import FastAPI, Request
from settings import db, printable

from random import sample
import pickle

app = FastAPI()



@app.get("/generate")
def generate_code(request: Request):
    body = request.query_params
    if 'text' in body and 'secret-phrase' in body:
        secret_key = ''.join(sample(printable, 16))

        data = {'text': body.get('text'), "secret-phrase": body.get('secret-phrase')}
        pickled_object = pickle.dumps(data)
        try:
            db.setex(name=secret_key, value=pickled_object, time=60 * 60 * 24 * 7)
        except Exception as s:
            return {'Error': 'message wasn`t created'}

        return {'secret_key': secret_key}
    return {"Hello": "World"}


@app.get("/secrets/{secret_key}")
def check(request: Request, secret_key):
    body = request.query_params
    if 'secret-phrase' not in body:
        return {'Error': 'didn`t accept &secret-phrase='}
    try:
        data = pickle.loads(db.get(secret_key))
        if data['secret-phrase'] == body['secret-phrase']:
            text = data['secret-phrase']
            db.delete(secret_key)
            return {"text": text}
        return {'Error': 'wrong secret-phrase'}
    except:
        return {"Error": 'Unknown'}


