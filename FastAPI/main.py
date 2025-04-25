#https://www.borntodev.com/2021/10/08/%E0%B8%A1%E0%B8%B2%E0%B8%97%E0%B8%B3%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B8%88%E0%B8%B1%E0%B8%81%E0%B8%81%E0%B8%B1%E0%B8%9A-fast-api/
from fastapi import FastAPI,Form,File, UploadFile

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/result/{score}")
async def result_exam(score):
    score = int(score)
    if(score >= 50):
        result = "Pass"
    else:   
        result = "No pass"
    return {"your result is": result}

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


###calculator exercise 
@app.get("/sum/{num1}+{num2}")
async def login(num1:int,num2:int):
    x = num1 + num2
    return {"sum": x}