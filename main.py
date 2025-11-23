from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.post("/post")
def test_post(data: dict):
    return {"received": data}

@app.put("/put")
def test_put(data: dict):
    return {"updated": data}

@app.patch("/patch")
def test_patch(data: dict):
    return {"patched": data}

@app.delete("/delete")
def test_delete():
    return {"status": "deleted"}
