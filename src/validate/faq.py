from marshmallow import Schema, fields, validate

class FaqSchema(Schema):
    id_produto = fields.Integer(required=True)
    nome = fields.String(
        required=True, 
        validate=[validate.Length(min=3, max=100, error="Dado inválido.")], 
        error_messages={"required": "Este campo é obrigatório"}
    )
    email = fields.Email(required=True)
    texto = fields.String(
        required=True, 
        validate=[validate.Length(min=3, max=1000, error="Dado inválido.")], 
        error_messages={"required": "Este campo é obrigatório"}
    )
