from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="DAJE Atende API", version="1.0.0")


class SolicitacaoOrcamento(BaseModel):
    cliente_nome: str
    telefone: str
    tipo_piso: str
    largura: float
    comprimento: float


def calcular_quebra_tecnica(largura: float, comprimento: float) -> float:
    area_base = largura * comprimento

    # Aplica 10% de margem técnica (RF02)
    return round(area_base * 1.10, 2)


@app.get("/")
def status():
    return {"sistema": "DAJE Atende", "status": "operacional"}


@app.post("/orcamentos/")
def criar_orcamento(dados: SolicitacaoOrcamento):
    metragem_total = calcular_quebra_tecnica(
        dados.largura,
        dados.comprimento
    )

    return {
        "cliente": dados.cliente_nome,
        "tipo_piso": dados.tipo_piso,
        "area_real_m2": round(dados.largura * dados.comprimento, 2),
        "area_com_quebra_10_m2": metragem_total,
        "status": "Em Análise"
    }
class AgendamentoVisita(BaseModel):
    orcamento_id: int
    data_visita: str
    turno: str  # Manhã ou Tarde
    endereco: str


@app.post("/visitas/")
def agendar_visita(dados: AgendamentoVisita):
    return {
        "mensagem": "Visita técnica confirmada com sucesso!",
        "data": dados.data_visita,
        "turno": dados.turno,
        "status": "Confirmado"
    }
