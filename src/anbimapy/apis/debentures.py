import datetime as dt
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from anbimapy.anbima import Anbima


class CurvaCredito(TypedDict):
    a: float
    aa: float
    aaa: float
    data_referencia: str
    vertice_anos: float


class Debentures:
    def __init__(self, http: "Anbima") -> None:
        self.http = http

    def curvas_credito(self, data: dt.date) -> CurvaCredito:
        response = self.http.get(
            url="/precos-indices/v1/debentures/curvas-credito",
            params={
                "data": f"{data:%Y-%m-%d}",
            },
        )
        response.raise_for_status()
        return response.json()

    def mercado_secundario(self, data: dt.date) -> None:
        response = self.http.get(
            url="/precos-indices/v1/debentures/mercado-secundario",
            params={
                "data": f"{data:%Y-%m-%d}",
            },
        )
        response.raise_for_status()
        return response.json()

    def projecoes(self, data: dt.date) -> None:
        response = self.http.get(
            url="/precos-indices/v1/debentures/projecoes",
            params={
                "data": f"{data:%Y-%m-%d}",
            },
        )
        response.raise_for_status()
        return response.json()
