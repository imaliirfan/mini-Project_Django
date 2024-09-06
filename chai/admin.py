from django.contrib import admin
from .models import ChaiVarity , ChaiReview, ChaiCertificate, Store
from .models import Post 
# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',)
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)

class ChaicertAdmin(admin.ModelAdmin):
    list_display = ('chai',)

admin.site.register(ChaiVarity, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register( ChaiCertificate, ChaicertAdmin )

