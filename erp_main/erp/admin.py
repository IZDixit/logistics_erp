from django.contrib import admin
from .models import Job_Information, File_Ref_No, Client, Cargo_Type, Cargo_Classification, From_Location, To_Location, Route, Supplier_Information, Loose_Cargo_Information, Container_Details

# Register your models here.
# Register all my models to my admin account


admin.site.register(Job_Information)
admin.site.register(File_Ref_No)
admin.site.register(Client)
admin.site.register(Cargo_Type)
admin.site.register(Cargo_Classification)
admin.site.register(From_Location)
admin.site.register(To_Location)
admin.site.register(Route)
admin.site.register(Supplier_Information)
admin.site.register(Loose_Cargo_Information)
admin.site.register(Container_Details)