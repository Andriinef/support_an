from django.contrib import admin
from repairs.models.car import Car
from repairs.models.parts import Parts
from repairs.models.places import PlacesToWork
from repairs.models.repairs import Repair
from repairs.models.type_repair import TypeRepair
from repairs.models.work import Works

admin.site.register(Car)
admin.site.register(Parts)
admin.site.register(PlacesToWork)
admin.site.register(TypeRepair)
admin.site.register(Repair)
admin.site.register(Works)
