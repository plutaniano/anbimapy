import datetime as dt
from anbimapy.module import Module


class CarteirasModule(Module):
    def ida(self, mes: dt.date) -> ...:
        response = self.http.get(
            url="/v1/indices/carteira-teorica-ida",
            params={
                "ano": mes.year,
                "mes": mes.month,
            },
        )
        response.raise_for_status()
        body: ... = response.json()
        return body["referencias"]

    def ida_mais(self, mes: dt.date) -> ...:
        response = self.http.get(
            url="/v1/indices-mais/carteira-teorica-ida",
            params={
                "ano": mes.year,
                "mes": mes.month,
            },
        )
        response.raise_for_status()
        body: ... = response.json()
        return body["referencias"]

    def ida_mais_previa(self, mes: dt.date) -> ...:
        response = self.http.get(
            url="/v1/indices-mais/previa-carteira-teorica-ida",
            params={
                "ano": mes.year,
                "mes": mes.month,
            },
        )
        response.raise_for_status()
        body: ... = response.json()
        return body["referencias"]

    def ihfa(self, mes: dt.date) -> ...:
        response = self.http.get(
            url="/v2/indices/carteira-teorica-ihfa",
            params={
                "ano": mes.year,
                "mes": mes.month,
            },
        )
        response.raise_for_status()
        body: ... = response.json()
        return body["componentes"]

    def ihfa_mais(self, mes: dt.date) -> ...:
        response = self.http.get(
            url="/v2/indices-mais/carteira-teorica-ihfa",
            params={
                "ano": mes.year,
                "mes": mes.month,
            },
        )
        response.raise_for_status()
        body: ... = response.json()
        return body["componentes"]

    def ima(self, mes: dt.date) -> ...:
        response = self.http.get(
            url="/v1/indices/carteira-teorica-ima",
            params={
                "ano": mes.year,
                "mes": mes.month,
            },
        )
        response.raise_for_status()
        return response.json()

    def ima_mais(self, mes: dt.date) -> ...:
        response = self.http.get(
            url="/v1/indices-mais/carteira-teorica-ima",
            params={
                "ano": mes.year,
                "mes": mes.month,
            },
        )
        response.raise_for_status()
        return response.json()

    def ima_mais_previa(self, mes: dt.date) -> ...:
        response = self.http.get(
            url="/v1/indices-mais/previa-carteira-teorica-ima",
            params={
                "ano": mes.year,
                "mes": mes.month,
            },
        )
        response.raise_for_status()
        return response.json()
