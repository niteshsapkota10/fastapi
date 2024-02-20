from typing import Union,Any
from typing_extensions import Self
from pydantic import BaseModel,SecretStr,UUID4,field_serializer,model_validator

class User(BaseModel):
    user_id: int
    uuid: Union[UUID4,None]=None
    username: str
    email: str
    password: SecretStr
    is_active: bool

    @field_serializer('password',when_used='json')
    def dump_secret(self,v):
        return v.get_secret_value()

    @model_validator(mode='after')
    def validatepassword(self)->Self:
        if len(self.password)<8:
            raise ValueError("Password Length Should be Greater than or Equal to 8")
        return self