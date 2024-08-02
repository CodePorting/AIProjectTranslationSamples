from django.core.exceptions import ValidationError

class PetValidator:
    @staticmethod
    def validate(pet):
        errors = {}
        name = pet.name
        
        # Name validation
        if not name:
            errors['name'] = 'This field is required.'
        
        # Type validation
        if pet.is_new() and not pet.type:
            errors['type'] = 'This field is required.'
        
        # Birth date validation
        if not pet.birth_date:
            errors['birth_date'] = 'This field is required.'
        
        if errors:
            raise ValidationError(errors)

    @staticmethod
    def supports(clazz):
        return issubclass(clazz, Pet)
