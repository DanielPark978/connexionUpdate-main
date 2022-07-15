from django import forms
from .models import Post, Category

#choices = [('AI', 'AI'), ('FinTech', 'FinTech'), ('Block Chain', 'Block Chain')]
choices = Category.objects.all().values_list('name', 'name')
choice_list = []
 
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'size', 'budget', 'category', 'snippet', 'description', 'header_image')
        #add more fields for tags, images, etc ltr


        widgets = { #mayhe add default=shit or smth fuck it
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title your idea here'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'user', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How many people are in your team so far?'}),
            'budget': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is the budget for this idea?'}),
            'category': forms.Select(choices = choice_list, attrs={'class': 'form-control', 'placeholder': 'What are some specific keywords for this idea?'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Summarizes your idea here'}), 
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Desrcibe your idea in detail here'}),
        }
          #add more fields for tags, images, etc ltr
          #vid#5 8:20 might use TextSelect for tags later likewise to the author in the vid