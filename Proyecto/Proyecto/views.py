from django.http import HttpResponse

#importing loading from django template
from django.template import loader

#our view which is a function named index
def inicio(request):

    #getting our template
    template = loader.get_template('index.html')

    #creating the values to pass
    context = {
        'nom':'Accesible',
        'autor':'Megaman',

    }

    #rendering the template in HttpResponse
    #but this time passing the context and request
    return HttpResponse(template.render(context, request))
