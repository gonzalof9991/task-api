from marshmallow import Schema, fields


class PlainTaskSchema(Schema):
    id = fields.Str(dump_only=True)  # No se va a usar para la validación
    name = fields.Str(required=True)
    status = fields.Boolean()
    is_active = fields.Boolean()
    expected_time = fields.Float()
    time_finished = fields.Float()


class PlainCategorySchema(Schema):
    id = fields.Str(dump_only=True)  # No se va a usar para la validación
    name = fields.Str(required=True)
    description = fields.Str()  # No se va a usar para la validación
    is_active = fields.Boolean()


class TaskSchema(PlainTaskSchema):
    category_id = fields.Int(required=True, load_only=True)
    category = fields.Nested(PlainCategorySchema(), dump_only=True)


class CategorySchema(PlainCategorySchema):
    tasks = fields.List(fields.Nested(PlainTaskSchema()), dump_only=True)
