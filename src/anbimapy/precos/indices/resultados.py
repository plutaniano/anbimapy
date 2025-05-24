import datetime as dt

from anbimapy.module import Module


class ResultadosModule(Module):
    def pu_intradiario(self, data: dt.date) -> ...:
        response = self.http.get(
            url="/v1/indices-mais/pu-intradiario",
            params={
                "data": f"{data:%Y-%m-%d}",
            },
        )
        response.raise_for_status()
        return response.json()

    def ida_fechado(self, data: dt.date) -> ...:
        response = self.http.get(
            url="/v1/indices/resultados-ida-fechado",
            params={
                "data": f"{data:%Y-%m-%d}",
            },
        )
        response.raise_for_status()
        return response.json()

    def ida_mais(self, data: dt.date) -> ...:
        response = self.http.get(
            url="/v1/indices-mais/resultados-ida",
            params={
                "data": f"{data:%Y-%m-%d}",
            },
        )
        response.raise_for_status()
        return response.json()

    def idka(self, data: dt.date) -> ...:
        response = self.http.get(
            url="/v1/indices/resultados-idka",
            params={
                "data": f"{data:%Y-%m-%d}",
            },
        )
        response.raise_for_status()
        return response.json()

    def idka_mais(self, data: dt.date) -> ...:
        response = self.http.get(
            url="/v1/indices-mais/resultados-idka",
            params={
                "data": f"{data:%Y-%m-%d}",
            },
        )
        response.raise_for_status()
        return response.json()

    def ihfa_fechado(self, data: dt.date) -> ...:
        response = self.http.get(
            url="/v1/indices/resultados-ihfa-fechado",
            params={
                "data": f"{data:%Y-%m-%d}",
            },
        )
        response.raise_for_status()
        return response.json()

    def ihfa_mais(self, data: dt.date) -> ...:
        response = self.http.get(
            url="/v2/indices-mais/resultados-ihfa",
            params={
                "data": f"{data:%Y-%m-%d}",
            },
        )
        response.raise_for_status()
        return response.json()

    def ima(self, data: dt.date) -> ...:
        response = self.http.get(
            url="/v1/indices/resultados-ima",
            params={
                "data": f"{data:%Y-%m-%d}",
            },
        )
        response.raise_for_status()
        return response.json()

    def ima_mais(self, data: dt.date) -> ...:
        response = self.http.get(
            url="/v1/indices-mais/resultados-ima",
            params={
                "data": f"{data:%Y-%m-%d}",
            },
        )
        response.raise_for_status()
        return response.json()

    def ima_intradiario(self, data: dt.date) -> ...:
        response = self.http.get(
            url="/v1/indices-mais/resultados-intradiarios-ima",
            params={
                "data": f"{data:%Y-%m-%d}",
            },
        )
        response.raise_for_status()
        return response.json()
