from django.db.models.enums import TextChoices

class StudentGenderChoices(TextChoices):
    male = "male", "Male"
    female = "female", "Female"

class FacultyChoices(TextChoices):
    FKPI = "FKPI", "FKPI"
    NKLP = "NKLP", "NKLP"
    FPK = "FPK", "FPK"
    FRDCP = "FRDCP", "FRDCP"