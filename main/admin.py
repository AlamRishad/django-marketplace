from django.contrib import admin
from .models import Freelancer
from .models import Client
from .models import Job_Detail
from .models import Job_Bid
from .models import Job_Awarded


admin.site.register(Freelancer)
admin.site.register(Client)
admin.site.register(Job_Detail)
admin.site.register(Job_Bid)
admin.site.register(Job_Awarded)

# Register your models here.
