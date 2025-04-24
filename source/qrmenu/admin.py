from django.contrib import admin

from .models import Category, Meal

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ('name',)
    # prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10
    # list_editable = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )

class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ('categories',)
    # prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10
    # list_editable = ('price',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'categories')
        }),
    )
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('categories')
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if form.cleaned_data.get('categories'):
            obj.categories.set(form.cleaned_data['categories'])
        else:
            obj.categories.clear()

    def delete_model(self, request, obj):
        obj.categories.clear()
        super().delete_model(request, obj)
        
admin.site.register(Category, CategoryAdmin)
admin.site.register(Meal, MealAdmin)

admin.site.site_header = "QR Menu Admin"
admin.site.site_title = "QR Menu Admin Portal"
admin.site.index_title = "Welcome to the QR Menu Admin Portal"
admin.site.empty_value_display = '-empty-'
admin.site.site_url = None  # Disable the admin site URL in the header
