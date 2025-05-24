from typing import Literal, TypedDict

import httpx

from anbimapy.precos.precos import PrecosModule


class AccessToken(TypedDict):
    access_token: str
    token_type: Literal["access_token"]
    expires_int: int


class Anbima(httpx.Client):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        *,
        host: Literal[
            "api.anbima.com.br",
            "api-sandbox.anbima.com.br",
        ] = "api.anbima.com.br",
    ) -> None:
        super().__init__(base_url=f"https://{host}")

        self.client_id = client_id
        self.client_secret = client_secret

        self.precos = PrecosModule(self)

    def autenticar(self) -> None:
        response = super().post(
            url="/oauth/access-token",
            auth=(self.client_id, self.client_secret),
            json={
                "grant_type": "client_credentials",
            },
        )
        response.raise_for_status()
        body: AccessToken = response.json()
        self.headers["Authorization"] = f"Bearer {body['access_token']}"
