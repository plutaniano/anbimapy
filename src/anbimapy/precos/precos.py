from typing import TYPE_CHECKING

from anbimapy.module import Module
from anbimapy.precos.debentures import DebenturesModule
from anbimapy.precos.indices import IndicesModule

if TYPE_CHECKING:
    from anbimapy.anbima import Anbima


class PrecosModule(Module):
    def __init__(self, http: "Anbima") -> None:
        super().__init__(http)

        self.debentures = DebenturesModule(http)
        self.indices = IndicesModule(http)
