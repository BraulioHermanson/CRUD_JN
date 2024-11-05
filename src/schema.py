from pydantic import BaseModel

class PokemonSchame(BaseModel): # contrato de dados, schema de dados, a view da API
    name: str
    type: str

    class Config:
        from_attributes = True