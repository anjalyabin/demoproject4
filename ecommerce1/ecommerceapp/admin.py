from django.contrib import admin

# Register your models here.
from . models import category,Product
class cadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,cadmin)


class padmin(admin.ModelAdmin):
    list_display = ['name', 'price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
admin.site.register(Product,padmin)
