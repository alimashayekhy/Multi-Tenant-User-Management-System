# from django.contrib import admin
# from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken


# @admin.register(OutstandingToken)
# class OutstandingTokenAdmin(admin.ModelAdmin):
#     """
#     Admin interface for OutstandingToken model.
#     Represents tokens that have been issued and are yet to expire or be blacklisted.
#     """
#     list_display = ('user', 'jti', 'token', 'created_at', 'expires_at', 'last_update')
#     search_fields = ('user__username', 'token', 'jti')
#     list_filter = ('created_at', 'expires_at', 'user')


# @admin.register(BlacklistedToken)
# class BlacklistedTokenAdmin(admin.ModelAdmin):
#     """
#     Admin interface for BlacklistedToken model.
#     Represents tokens that have been blacklisted and are no longer valid.
#     """
#     list_display = ('token', 'blacklisted_at')
#     search_fields = ('token',)
#     list_filter = ('blacklisted_at',)