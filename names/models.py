from django.db import models


# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=127)

    def __repr__(self) -> str:
        return f"<Name ({self.id}) - {self.name}>"
