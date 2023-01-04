from django.db import models


class Space(models.Model):
    name = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def add_slots(self, total_slots):
        self.space_slots.all().delete()
        for i in range(total_slots):
            Slot.objects.create(space=self)
        return total_slots


class Slot(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE, related_name="space_slots")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.space.name} - {self.id}"


class SlotBook(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name="slot_bookings")
    duration = models.PositiveIntegerField(default=0)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    payment = models.PositiveIntegerField(default=0)