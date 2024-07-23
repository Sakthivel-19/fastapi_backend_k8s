from fastapi import FastAPI
from fastapi_backend_k8s_sub_module.submodule.test import Test

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/try")
def read_root_copy():
    return {"Hello": "Try"}

@app.get("/test")
def read_test():
    res = Test.test_function()
    return res

@app.get("/testone")
def read_test_copy():
    res = Test.test_function_copy()
    return res