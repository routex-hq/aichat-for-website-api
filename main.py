from fastapi import FastAPI
from getWeb import crawl_start
from chat import chat

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/crawl/{url:path}", status_code=200)
def crawl(url: str):
    crawl_start(url)
    return {"result": "done", "url": url}


@app.get("/question/{domain:str}/{question:str}", status_code=200)
def result(domain: str, question: str):
    result = chat(domain, question)
    return {"question": question, "result": result}
