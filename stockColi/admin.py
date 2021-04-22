from django.contrib import admin
from .models import Envoi
from .models import Client
from .models import Employer
from .models import Depot
from .models import Coli

admin.site.register(Envoi)
admin.site.register(Client)
admin.site.register(Employer)
admin.site.register(Depot)
admin.site.register(Coli)