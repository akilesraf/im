from django.contrib import admin

from .models import Cliente, Informe

class InformeInline(admin.TabularInline):
    model = Informe
    extra = 8


class ClienteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['cliente_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [InformeInline]
    list_display = ('cliente_text', 'pub_date')
    list_display = ('cliente_text', 'pub_date', 'was_published_recently')

admin.site.register(Cliente, ClienteAdmin)