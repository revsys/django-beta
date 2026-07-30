from django.contrib import admin

from beta.models import BetaSignup


class BetaSignupAdmin(admin.ModelAdmin):
    model = BetaSignup
    list_filter = ("contacted", "registered")
    search_fields = ("email", "first_name", "last_name")


admin.site.register(BetaSignup, BetaSignupAdmin)
