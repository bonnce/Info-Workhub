from django.core.exceptions import PermissionDenied

class PasajeMixin:
    campos=[]
    modelo=None
#Redefinicion del post para asignarle el trabajador y stalker antes de guardarlo en la bd cuando ya
#se completo el formulario
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instancia=form.save()

            if 'objeto' in self.campos:
                trabajador=self.modelo.objects.get(pk=kwargs['pk'])
                instancia.trabajador=trabajador

            if 'perfil' in self.campos:
                stalker=request.user.Stalker
                instancia.stalker=stalker
            
            form.save(commit=True)
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

  


class PermisosMixin:
	rol = None
	def dispatch(self,request,*args,**kwargs):
		if check(request,self.rol):
			return super().dispatch(request,*args,**kwargs)
		else:
			raise PermissionDenied

def check(request,rol):
	u = request.user
	if u.Trabajador and rol == 'trabajador':
		return True
	elif not (u.Trabajador) and rol == 'stalker':
		return True
	else:
		return False