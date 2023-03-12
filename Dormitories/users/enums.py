from django.db.models.enums import TextChoices

class StudentGenderChoices(TextChoices):
    male = "Male", "Male"
    female = "Female", "Female"

class FacultyChoices(TextChoices):
    FKPI = "FKPI", "FKPI"
    NKLP = "NKLP", "NKLP"
    FPK = "FPK", "FPK"
    FRDCP = "FRDCP", "FRDCP"

