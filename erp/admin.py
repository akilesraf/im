from django.contrib import admin


from .models import Informes, Clientes, Pagos

class InformesInline(admin.TabularInline):
    model = Informes
    extra = 8

class PagosInline(admin.TabularInline):
    model = Pagos
    extra = 8

class ClientesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['clientes_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [InformesInline]
    list_display = ('clientes_text', 'pub_date')
    list_display = ('clientes_text', 'pub_date', 'was_published_recently')

admin.site.register(Clientes, ClientesAdmin)







# Register your models here.
