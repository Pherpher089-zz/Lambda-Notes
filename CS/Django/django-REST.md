# Django with REST and Users

**onDelete=CASCADE** as a parameter for a foreignKey field will cause it to be deleted when the connected key is deleted.

You have to register your models for them to show up in the admin interface.

In admin.py

```python
from djangocontrib import admin
from .models import model_to_reg

admin.sight.register(model_to_reg)
```

You can show read only fields by defining an admin class for a model class. Pass that class in as a parameter in the register function and remember to add a comma in the readonly_field because it takes a tuple

```python
from djangocontrib import admin
from .models import model_to_reg

class model_to_regAdmin(admin.ModelAdmin):
    readonly_fields = ('Name of field',)

admin.sight.register(model_to_reg, model_to_regAdmin)
```
