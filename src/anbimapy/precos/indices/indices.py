from typing import TYPE_CHECKING

from anbimapy.module import Module
from anbimapy.precos.indices.carteiras import CarteirasModule
from anbimapy.precos.indices.resultados import ResultadosModule

if TYPE_CHECKING:
    from anbimapy.anbima import Anbima


class IndicesModule(Module):
    def __init__(self, http: "Anbima") -> None:
        super().__init__(http)

        self.carteiras = CarteirasModule(http)
        self.resultados = ResultadosModule(http)
