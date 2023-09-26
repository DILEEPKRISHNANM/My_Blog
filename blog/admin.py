from django.contrib import admin

# Register your models here.


from .models import Tag,Author,Post



class PostAdmin(admin.ModelAdmin):
    list_display=("title","author","date")
    list_filter = ("author","tags","date")
    prepopulated_fields ={"slug":("title",)}


admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post,PostAdmin)