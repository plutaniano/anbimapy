from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from anbimapy.anbima import Anbima


class Module:
    def __init__(self, http: "Anbima") -> None:
        self.http = http
