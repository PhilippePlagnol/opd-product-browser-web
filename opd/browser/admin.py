from django.contrib import admin
from django.db import models

from .models import Gtin, Nutrition, Brand, Brand_type, Brand_owner, Search
from django.conf import settings

class BrandTypeAdmin(admin.ModelAdmin):
    actions = None

    # Never delete a brand, update its BSIN
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Brand_type, BrandTypeAdmin)

class BrandAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('BSIN', 'BRAND_NM', 'FLAG_DELETE')
    fields_add = (
        (None, {
            'classes': ('wide',),
            'fields': ('BSIN', 'BRAND_NM',
                       # Postponed in ticket #58
                       #'owner_cd',
                       'BRAND_TYPE_CD', 'BRAND_LINK','COMMENTS', 'LAST_MODIFIED')
        }),
    )
    fields_change = (
        (None, {
            'classes': ('wide',),
            'fields': ('BSIN', 'BRAND_NM',
                       # Postponed in ticket #58
                       #'owner_cd',
                       'BRAND_TYPE_CD', 'BRAND_LINK', ('FLAG_DELETE', 'COMMENTS'),'LAST_MODIFIED')
        }),
    )
    readonly_fields_su = ('BSIN', 'LAST_MODIFIED')
    readonly_fields_moderator = ('BSIN', 'LAST_MODIFIED', 'BRAND_NM')
    search_fields = ['BSIN', 'BRAND_NM',
                     # Postponed in ticket #58
                     #'owner_cd__owner_nm'
                     ]
    list_filter = ('FLAG_DELETE', )

    # Never delete a brand, update its BSIN
    def has_delete_permission(self, request, obj=None):
        return False

    def get_fieldsets(self, request, obj=None):
        # if editing
        if obj:
            return self.fields_change
        return self.fields_add

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields_su
        return self.readonly_fields_moderator

admin.site.register(Brand, BrandAdmin)
