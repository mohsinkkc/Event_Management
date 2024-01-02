from django.contrib import admin
from .models import User,Service,Event,Rent,Cart,Transaction

# Register your models here.
admin.site.register(User)
admin.site.register(Service)
admin.site.register(Event)
admin.site.register(Rent)
admin.site.register(Cart)
admin.site.register(Transaction)
