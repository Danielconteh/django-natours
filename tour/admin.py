from django.contrib import admin

from .models import Location, Tour,Images,User_Image,Review

 
class ImagesAdmin(admin.StackedInline):
    model = Images
 
@admin.register(Tour)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImagesAdmin]
    prepopulated_fields = {"slug":("name",)}
    
 
    class Meta:
       model = Tour
 
admin.site.register(Location)
admin.site.register(Images)
admin.site.register(User_Image)
admin.site.register(Review)
