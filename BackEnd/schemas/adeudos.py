from typing import List,Union
from pydantic import BaseModel
from datetime import datetime

from models.Adeudos import MyDetalle

class AdeudoBase(BaseModel):
    
    Area:str
    Cliente: str
    Descripcion: str
    Fecha_Registro:datetime
    Fecha_Actualizacion:datetime
    Estatus:bool
    Tipo: str
    Detalle: MyDetalle
    
       
    
class AdeudoCreate(Base):
    pass
class AdeudoUpdate(AdeudoBase):
    pass
class Adeudo(AdeudoBase):
    ID: int

    class Config:
        orm_mode = True