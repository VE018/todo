from django.shortcuts import render,redirect

from vichu.models import todays

# Create your views here.
def home(request):
    if request.method == 'POST':
        index=request.POST['index']
        task=request.POST['task']
        t= todays(index=index, task=task)
        t.save()
        




    p=todays.objects.all()


    return render(request,'todo.html',{"s":p})

def delete(request,taskid):
    ts = todays.objects.get(id=taskid)   
    ts.delete()

    return redirect(home)