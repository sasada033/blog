from django import forms


class PostSearchForm(forms.Form):
    key_word = forms.CharField(
        label='検索...', required=False, widget=forms.TextInput(attrs={
            'type': 'search',
            'class': 'form-control mr-sm-2',
            'placeholder': '検索...',
            'aria-label': '検索...',
        }),
    )
