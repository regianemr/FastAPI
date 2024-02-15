import uvicorn
import contas_a_pagar_e_receber_router
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def oi_eu_sou_programador() -> str:
    return "Oi, eu sou programadora!"


app.include_router(contas_a_pagar_e_receber_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
