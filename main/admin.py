from django.contrib import admin
from .models import Freelancer
from .models import Client
from .models import Job_Detail
from .models import Job_Bid
from .models import Job_Awarded
from .models import Blog , Blog_Comment


admin.site.register(Freelancer)
admin.site.register(Client)
admin.site.register(Job_Detail)
admin.site.register(Job_Bid)
admin.site.register(Job_Awarded)
admin.site.register(Blog)
admin.site.register(Blog_Comment)
# Register your models here.
