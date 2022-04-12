from django.contrib import admin
from .models import Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('user_profile', 'volunteer')

    fields = ('volunteer', 'review_text',
              'approved', 'user_profile',)

    list_display = ('volunteer', 'review_text',
                    'approved',
                    'date')

    ordering = ('-date',)


admin.site.register(Review, ReviewAdmin)
