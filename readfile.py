from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:/home/itsoftware/StudentsPerformance.csv}")
async def read_file(file_path: str):
    return {"file_path": file_path}