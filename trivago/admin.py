from django.contrib import admin
from trivago.models import RoomType, Room, Visitor, Worker, Scedule, Checkout, Checkin

admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Visitor)
admin.site.register(Worker)
admin.site.register(Scedule)
admin.site.register(Checkin)
admin.site.register(Checkout)

