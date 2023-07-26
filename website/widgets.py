from django.forms.widgets import TextInput

class GenderIconWidget(TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        icon_class = 'pink-text' if value == 'female' else 'blue-text'  # Customize based on the value
        attrs['class'] = icon_class
        return super().render(name, value, attrs, renderer)
