from django.shortcuts import render
def index(request):
# render the appropriate template for this request
 return render(request, 'bookmodule/index.html')
def cato(request):
    return   render(request, 'bookmodule/cato.html')
#return redirect('/')
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

