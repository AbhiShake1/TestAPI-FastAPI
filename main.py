import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello():
    data = [
        {
            'data': 'hello world again'
        }
    ]
    return data


@app.get('/api/{req}')
def handle(req):
    return {'data': req}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
