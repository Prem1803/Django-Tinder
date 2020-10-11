from django.contrib import admin
from core.models import Tinder_Account,Facebook,Location,Instagram_Account,Like,Super_Like,Match,Message,UnMatch,ReportUser
# Register your models here.
admin.site.register(Tinder_Account)
admin.site.register(Facebook)
admin.site.register(Location)
admin.site.register(Instagram_Account)
admin.site.register(Like)
admin.site.register(Super_Like)
admin.site.register(Match)
admin.site.register(Message)
admin.site.register(UnMatch)
admin.site.register(ReportUser)
