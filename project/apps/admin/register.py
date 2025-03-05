class MenuItem:
    @classmethod
    def get_fields(cls):
        fields = []
        for key, value in cls.__dict__.items():
            fields.append({
                'name': key,
                'f_type': value.f_type,
                'description': value.description,
                'allow_null': value.allow_null,
            })
        return fields
