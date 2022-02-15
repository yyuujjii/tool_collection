from random import choice
from django import forms


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "

    subject = forms.fields.ChoiceField(choices=(("選択してください", "選択してください"), ("アプリケーション作成依頼", "アプリケーション作成依頼"), (
        "アプリケーション使用方法", "アプリケーション使用方法"), ("その他", "その他")), label='お問い合わせ種別', required=True, widget=forms.widgets.Select)
    name = forms.CharField(label="名前")
    tell = forms.CharField(label="電話番号")
    sender = forms.EmailField(label='メールアドレス', help_text='※ご確認の上、正しく入力してください。')
    message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea)
    myself = forms.BooleanField(label='同じ内容を受け取る', required=False)
