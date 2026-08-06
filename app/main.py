from fastapi import FastAPI

app = FastAPI(title='ATHENA-X', version='1.0.0')

@app.get('/')
def root():
    return {'project':'ATHENA-X','status':'running'}

@app.get('/health')
def health():
    return {'status':'healthy'}
