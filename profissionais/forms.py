from django import forms

class BuscarProfissionalForm(forms.Form):

	busca = forms.CharField(required=True)
	
	
	

	def is_valid(self):
		valid = True
		if not super(BuscarProfissionalForm, self).is_valid():
			self.adiciona_erro('Por Favor, Verifique os dados informados')
			valid = False
		
		return valid

	def adiciona_erro(self, message):
		erros = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		erros.append(message)

class BuscarCidadeProfForm(forms.Form):

	busca = forms.IntegerField(required=True)
	
	
	

	def is_valid(self):
		valid = True
		if not super(BuscarCidadeProfForm, self).is_valid():
			self.adiciona_erro('Por Favor, Verifique os dados informados')
			valid = False
		
		return valid

	def adiciona_erro(self, message):
		erros = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		erros.append(message)