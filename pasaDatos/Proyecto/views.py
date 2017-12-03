from django.http import HttpResponse

#importing loading from django template
from django.template import loader
from django.views.decorators.csrf import csrf_exempt



#our view which is a function named index
def inicio(request):

    #getting our template
    template = loader.get_template('indexBootstrap.html')

    #creating the values to pass
    context = {
        'nom':'Accesible',
        'autor':'Megaman',

    }

    #rendering the template in HttpResponse
    #but this time passing the context and request
    return HttpResponse(template.render(context, request))

@csrf_exempt


def pregunta(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        #adding the values in a context variable
        context = {
            'name': name,
            'email': email,
            'phone': phone
        }

        #getting our showdata template
        template = loader.get_template('showdata.html')

        #returing the template
        return HttpResponse(template.render(context, request))
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('forma.html')
        return HttpResponse(template.render())
