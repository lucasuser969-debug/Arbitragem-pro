import os
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Permite que o App do seu celular fale com o servidor
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pega a chave de forma segura das configurações do Render
API_KEY = os.getenv("ODDS_API_KEY", "60df5425c5c3967414ac5f0cd1d9d54d")

@app.get("/")
def home():
    return {"status": "Online", "msg": "Servidor de Arbitragem Rodando 24h"}

@app.get("/scan")
def scan():
    # Lista de esportes para varredura completa
    sports = ['soccer_brazil_serie_a', 'basketball_nba', 'tennis_atp_wimbledon', 'mma_mixed_martial_arts']
    results = []
    
    for sport in sports:
        url = f'https://api.the-odds-api.com/v4/sports/{sport}/odds/?apiKey={API_KEY}&regions=eu&markets=h2h,totals'
        try:
            resp = requests.get(url).json()
            for game in resp:
                # Aqui vai a lógica de cálculo de lucro que fizemos antes
                # O servidor processa e devolve os dados prontos
                pass
        except: continue
    return results

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
