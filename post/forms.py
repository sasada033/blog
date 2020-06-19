from django import forms
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


class PostSearchForm(forms.Form):
    key_word = forms.CharField(
        label='検索...', required=False, widget=forms.TextInput(attrs={
            'type': 'search',
            'class': 'form-control mr-sm-2',
            'placeholder': '検索...',
            'aria-label': '検索...',
        }),
    )


class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=50)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名', max_length=100)
    message = forms.CharField(label='本文', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = '例) 山田太郎'

        self.fields['email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder'] = '例) yamadataro@example.com'

        self.fields['title'].widget.attrs['class'] = 'form-control col-11'
        self.fields['title'].widget.attrs['placeholder'] = '例) ××についてのご連絡'

        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = '本文をここに入力してください。'

    def send_email(self, request):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        context = {
            'name': name,
            'email': email,
            'title': title,
            'message': message,
        }

        subject = '[SASA*SITE] お問い合わせ受付完了のお知らせ'
        body = render_to_string('post/email/noreply.txt', context, request)
        form_email = 'SASA*SITE <noreply@sasasite.net>'
        to_list = [
            email
        ]
        bcc_list = [
            'sasada@email.sasasite.net'
        ]

        info_mail = EmailMessage(subject=subject, body=body, from_email=form_email, to=to_list, bcc=bcc_list)
        info_mail.send()
