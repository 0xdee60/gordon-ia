from django.shortcuts import render, redirect
from django.views.generic import View
from .models import PreguntaBeck, User
from .forms import UsuarioCreateForm

class HomeView(View):
    def get(self,request,*args,**kwargs):
        form = UsuarioCreateForm()
        context = {
            'form':form
        }
        return render(request, 'home.html',context)


    def post(self,request,*args,**kwargs):
        if request.method == "POST":
            form = UsuarioCreateForm(request.POST)
            if(form.is_valid()):
                nombres = form.cleaned_data.get('nombres')
                apellidos = form.cleaned_data.get('apellidos')
                dni = form.cleaned_data.get('dni')
                fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
                sexo = form.cleaned_data.get('sexo')
                #crear usuario
                us, created = User.objects.get_or_create(nombres = nombres,apellidos = apellidos,dni = dni,fecha_nacimiento = fecha_nacimiento,sexo = sexo)
                us.save()
               
                return redirect(f'{us.id}/')
        context = {
            'form': form
        }
        return render(request, 'home.html',context)
    

class PreguntasIView(View):
    def get(self,request,*args,**kwargs):
        context = {
            'preguntas_beck': PreguntaBeck.objects.all()
        }
        return render(request, 'preguntas_beck.html',context)
    


