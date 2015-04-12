from django.contrib import admin

# Register your models here.
from playtime.models import FieldLocation, Field, FieldSlot


class FieldLocationAdmin(admin.ModelAdmin):
  list_display = ('name', 'address')


class FieldAdmin(admin.ModelAdmin):
  pass


class FieldSlotAdmin(admin.ModelAdmin):
  pass


admin.site.register(FieldLocation, FieldLocationAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(FieldSlot, FieldSlotAdmin)
