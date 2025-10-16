from django import forms
from Users.models import *
'''
===============================================================================================================
                            Slider Form
===============================================================================================================
'''

class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['title_small', 'title_large', 'description', 'image', 'logo', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            # Apply bootstrap form-control class to all fields
            if visible.field.widget.__class__.__name__ not in ['CheckboxInput', 'ClearableFileInput']:
                visible.field.widget.attrs['class'] = 'form-control'
            # Checkbox / file input ke liye alag class
            elif visible.field.widget.__class__.__name__ == 'CheckboxInput':
                visible.field.widget.attrs['class'] = 'form-check-input'
            elif visible.field.widget.__class__.__name__ == 'ClearableFileInput':
                visible.field.widget.attrs['class'] = 'form-control'

'''
===============================================================================================================
                            Gallery Form
===============================================================================================================
'''

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.widget.__class__.__name__ not in ['CheckboxInput', 'ClearableFileInput']:
                visible.field.widget.attrs['class'] = 'form-control'
            elif visible.field.widget.__class__.__name__ == 'CheckboxInput':
                visible.field.widget.attrs['class'] = 'form-check-input'
            elif visible.field.widget.__class__.__name__ == 'ClearableFileInput':
                visible.field.widget.attrs['class'] = 'form-control'

'''
===============================================================================================================
                           Certificate Form
===============================================================================================================
'''

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['title', 'image', 'button_text', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            widget_name = visible.field.widget.__class__.__name__
            if widget_name not in ['CheckboxInput', 'ClearableFileInput']:
                visible.field.widget.attrs['class'] = 'form-control'
            elif widget_name == 'CheckboxInput':
                visible.field.widget.attrs['class'] = 'form-check-input'
            elif widget_name == 'ClearableFileInput':
                visible.field.widget.attrs['class'] = 'form-control'


'''
===============================================================================================================
                          Awards Form
===============================================================================================================
'''
class AwardsForm(forms.ModelForm):
    class Meta:
        model = Awards
        fields = [ 'award_image','title','description', 'years', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            widget_name = visible.field.widget.__class__.__name__
            if widget_name not in ['CheckboxInput', 'ClearableFileInput']:
                visible.field.widget.attrs['class'] = 'form-control'
            elif widget_name == 'CheckboxInput':
                visible.field.widget.attrs['class'] = 'form-check-input'
            elif widget_name == 'ClearableFileInput':
                visible.field.widget.attrs['class'] = 'form-control'     

'''
===============================================================================================================
                          Ourteam Form
===============================================================================================================
'''
class OurteamForm(forms.ModelForm):
    class Meta:
        model = Ourteam
        fields = ['name', 'role', 'organization', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            widget_name = visible.field.widget.__class__.__name__
            if widget_name not in ['CheckboxInput', 'ClearableFileInput']:
                visible.field.widget.attrs['class'] = 'form-control'
            elif widget_name == 'CheckboxInput':
                visible.field.widget.attrs['class'] = 'form-check-input'
            elif widget_name == 'ClearableFileInput':
                visible.field.widget.attrs['class'] = 'form-control'  
   


'''
===============================================================================================================
                            Managementmember Form
===============================================================================================================
'''

class ManagementmembertForm(forms.ModelForm):
    class Meta:
        model = ManagementMember
        fields = ['name', 'designation', 'organization','is_active']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            widget_name = visible.field.widget.__class__.__name__
            if widget_name not in ['CheckboxInput', 'ClearableFileInput']:
                visible.field.widget.attrs['class'] = 'form-control'
            elif widget_name == 'CheckboxInput':
                visible.field.widget.attrs['class'] = 'form-check-input'
            elif widget_name == 'ClearableFileInput':
                visible.field.widget.attrs['class'] = 'form-control'  
   

'''
===============================================================================================================
                            Missionvision Form
===============================================================================================================
'''

class MissionvisionForm(forms.ModelForm):
    class Meta:
        model = MissionVision
        fields = ['title', 'description', 'icon','is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            widget_name = visible.field.widget.__class__.__name__
            if widget_name not in ['CheckboxInput', 'ClearableFileInput']:
                visible.field.widget.attrs['class'] = 'form-control'
            elif widget_name == 'CheckboxInput':
                visible.field.widget.attrs['class'] = 'form-check-input'
            elif widget_name == 'ClearableFileInput':
                visible.field.widget.attrs['class'] = 'form-control'  

'''
===============================================================================================================
                           AboutUs Form
===============================================================================================================
'''   

class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ['title', 'description', 'logo', 'button_text', 'is_active']
        widgets = {
            'section_type': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'button_text': forms.TextInput(attrs={'class': 'form-control'}),
            'is_deleted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

