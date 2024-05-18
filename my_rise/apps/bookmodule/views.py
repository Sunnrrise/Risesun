from django.shortcuts import redirect, render
from .models import ProseModel

def index(request):
# render the appropriate template for this request
 return render(request, 'bookmodule/index.html')
def cato(request):
    return   render(request, 'bookmodule/cato.html')

def poetry(request):
    return render(request, 'bookmodule/poetry.html')

def prose(request):
    return render(request, 'bookmodule/prose.html')

def thoughts(request):
    return render(request, 'bookmodule/thoughts.html')

def save_prose(request):
    if request.method == 'POST':
        prose_text = request.POST.get('prose_input')
        ProseModel.objects.create(prose_text=prose_text)
        return redirect('index')
    else:
        return redirect('poetry')

#return redirect( '/')
#def numcato(request , bId):
    cato1 = {'id': 11, 'title': 'Reflections'}
    cato2 = {'id': 22, 'title': 'prose' }
    cato3 = {'id': 33, 'title': 'Poetry' }
#targercato = None
#if cato1['id'] == bId: targetcato = cato1
#context = {'numcato': targetcato}
#def some_view(request):
    # Your view logic here
    return render(request, 'bookmodule/numcato.html', context)

