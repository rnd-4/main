from django.db.models.enums import TextChoices

class RoomTypeChoices(TextChoices):
    duo_room = "duo_room", "Duo Room"
    squad_room = "squad_room", "Squad Room"