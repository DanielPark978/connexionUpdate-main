from django import forms
from .models import Post, Category 

#choices = [('AI', 'AI'), ('FinTech', 'FinTech'), ('Block Chain', 'Block Chain')]


choices = Category.objects.all().values_list('name', 'name')
choice_list = []
 
for item in choices:
    choice_list.append(item)

print(choice_list)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'size', 'budget', 'terms', 'category', 'category2', 'category3', 'snippet', 'description', 'header_image')
        #fields = ('title', 'author', 'size', 'budget', 'category', 'snippet', 'description', 'header_image')
        #add more fields for tags, images, etc ltr


        widgets = { 
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title your idea here'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'user', 'type':'hidden'}),
            'size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How many people are in your team so far?'}),
            'budget': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is the budget for this idea?'}),
            'terms': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is the budget for this idea?'}),
            
            'category': forms.Select(choices = choice_list, attrs={'class': 'form-control ', 'placeholder': 'What are some specific keywords for this idea?'}),
            'category2': forms.Select(choices = choice_list, attrs={'class': 'form-control ', 'placeholder': 'What are some specific keywords for this idea?'}),
            'category3': forms.Select(choices = choice_list, attrs={'class': 'form-control ', 'placeholder': 'What are some specific keywords for this idea?'}),
           
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Summarizes your idea here'}), 
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Desrcibe your idea in detail here'}),
        }
          #add more fields for tags, images, etc ltr
          #vid#5 8:20 might use TextSelect for tags later likewise to the author in the vid