from django import forms


class ContactForm(forms.Form):
  
  full_name = forms.CharField()
  email = forms.EmailField()
  content = forms.CharField(widget=forms.Textarea)

  def clean_email(self, *args, **kwargs):
    email = self.cleaned_data.get('email')
    if email.endswith(".edu"):
      raise forms.ValidationError("this is not a valid email")
    return email