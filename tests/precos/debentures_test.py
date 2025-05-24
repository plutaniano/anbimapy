import datetime as dt
from anbimapy import Anbima


def test_curvas_de_credito(anbima: Anbima):
    anbima.precos.debentures.curvas_de_credito(dt.date(2025, 5, 13))


def test_mercado_secundario(anbima: Anbima):
    anbima.precos.debentures.curvas_de_credito(dt.date(2025, 5, 13))


def test_projecoes(anbima: Anbima):
    anbima.precos.debentures.projecoes(dt.date(2025, 5, 13))
