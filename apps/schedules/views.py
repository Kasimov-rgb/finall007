from django.shortcuts import render, redirect
from apps.schedules.models import Schedule
from apps.schedules.forms import ScheduleForm


def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'salud/schedule_list.html', {'schedules': schedules})


def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm()
    return render(request, 'salud/add_schedule.html', {'form': form})
