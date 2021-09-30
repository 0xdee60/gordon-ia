from django.contrib import admin
from .models import User, PreguntaBeck, RespuestaBeck, ResultadoBeck

admin.site.register(User)
admin.site.register(PreguntaBeck)
admin.site.register(RespuestaBeck)
admin.site.register(ResultadoBeck)
