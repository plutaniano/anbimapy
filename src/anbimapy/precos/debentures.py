import datetime as dt
from typing import TypedDict

from anbimapy.module import Module


class CurvaDeCredito(TypedDict):
    a: float
    aa: float
    aaa: float
    data_referencia: str
    vertice_anos: float


class MercadoSecundario(TypedDict):
    codigo_ativo: str
    data_referencia: str
    data_vencimento: str
    desvio_padrao: float
    duration: float
    emissor: str
    grupo: str
    percent_vne: float
    percent_pu_par: float
    percent_reune: str
    percentual_taxa: str
    pu: float
    referencia_ntnb: str
    taxa_compra: float
    taxa_indicativa: float
    taxa_venda: float
    val_max_intervalo: float
    val_min_intervalo: float


class Projecao(TypedDict):
    data_coleta: str
    data_validade: str
    indice: str
    mes_referencia: str
    tipo_projecao: str
    variacao_projetada: float


class DebenturesModule(Module):
    def curvas_de_credito(self, data: dt.date) -> list[CurvaDeCredito]:
        response = self.http.get(
            url="/v1/debentures/curvas-credito",
            params={
                "data": f"{data:%Y-%m-%d}",
            },
        )
        response.raise_for_status()
        return response.json()

    def mercado_secundario(self, data: dt.date) -> list[MercadoSecundario]:
        response = self.http.get(
            url="/v1/debentures/mercado-secundario",
            params={
                "data": f"{data:%Y-%m-%d}",
            },
        )
        response.raise_for_status()
        return response.json()

    def projecoes(self, mes: dt.date) -> list[Projecao]:
        response = self.http.get(
            url="/v1/debentures/projecoes",
            params={
                "ano": mes.year,
                "mes": mes.month,
            },
        )
        response.raise_for_status()
        return response.json()
