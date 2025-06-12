from django.contrib import admin # type: ignore
from django.apps import apps # type: ignore
from django.contrib.admin.sites import AlreadyRegistered # type: ignore

app = apps.get_app_config('cms')  

for model_name, model in app.models.items():
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
