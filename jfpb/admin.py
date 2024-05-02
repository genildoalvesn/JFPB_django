from django.contrib import admin
from .models import Login,Author
# Register your models here.

from .models import Heroe
@admin.register(Heroe)
class HeroeAdmin(admin.ModelAdmin):
      verbose_name = 'Heroe'

from .models import Villain
@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
      verbose_name = 'Villain'

from .models import Author
@admin.register(Author)
class VillainAdmin(admin.ModelAdmin):
      verbose_name = 'Author'

from .models import Joinha
@admin.register(Joinha)
class JoinhaAdmin(admin.ModelAdmin):
      verbose_name = 'Joinha'



