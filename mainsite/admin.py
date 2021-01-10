from django.contrib import admin
from mainsite.models import Post, AccessInfo, Branch, StoreIncome, FiveMountain

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post, PostAdmin)
admin.site.register(AccessInfo)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('title', 'name')
admin.site.register(Branch, BranchAdmin)

class StoreIncomeAdmin(admin.ModelAdmin):
    list_display = ('branch', 'income_year', 'income_month', 'income')
admin.site.register(StoreIncome, StoreIncomeAdmin)

class FiveMountainAdmin(admin.ModelAdmin):
    list_display = ('mountain_name','mountain_high')
admin.site.register(FiveMountain, FiveMountainAdmin)