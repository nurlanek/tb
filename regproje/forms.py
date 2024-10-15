from django import forms
from .models import (Dolboor, Negizgimaalymat, Kenenmaalymat, Iskeashyruuplany,
                     Dolboordundudjeti, Dolboordunkomandasy, Baaloo_turuktuuluk, Tirkemeler, Project_confirmation)

class DolboorForm(forms.ModelForm):
    class Meta:
        model = Dolboor
        fields = [
            'dolboordun_atalyshy',
            'prioritettu_bagyty',
            'dolboordun_moonotu',
            'dolboordun_geografiyalyk_ordu',
            'maksathtalgan_auditoriya',
            'dolboordun_byudzheti',
            'onoktoshtorunuz_maalymat'
        ]
        widgets = {
            'dolboordun_atalyshy': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'prioritettu_bagyty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'dolboordun_moonotu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'dolboordun_geografiyalyk_ordu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'maksathtalgan_auditoriya': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'dolboordun_byudzheti': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'onoktoshtorunuz_maalymat': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'style': 'height: 160px;'}),
        }
        labels = {
            'dolboordun_atalyshy': 'Долбоордун аталышы:',
            'prioritettu_bagyty': 'Приоритеттүү багыты:',
            'dolboordun_moonotu': 'Долбоордун ишке ашуу мөөнөтү: (6 ай, 1 жыл):',
            'dolboordun_geografiyalyk_ordu': 'Долбоордун ишке аша турган географиялык ордун же аймагын жазыңыз:',
            'maksathtalgan_auditoriya': 'Максатталган аудитория:',
            'dolboordun_byudzheti': 'Долбоордун бюджети:',
            'onoktoshtorunuz_maalymat': 'Долбоорду ишке ашырууда колдоо көрсөтө турган өнөктөштөрүңүз жөнүндө маалымат бериңиз:',
        }

class NegizgimaalymatForm(forms.ModelForm):
    class Meta:
        model = Negizgimaalymat
        fields = [
            'dolboor',
            'yuridikalyk_jekekishi',
            'aty_jonu',
            'mekmenin_atalyshy',
            'mekmenin_zhetekchisi',
            'pozitsiyasi',
            'baylanysh_telefonu',
            'mobildik_telefonu',
            'email'
        ]

        widgets = {
            'dolboor': forms.Select(attrs={'class': 'form-control'}),
            'yuridikalyk_jekekishi': forms.Select(attrs={'class': 'form-control'}),
            'aty_jonu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'mekemenin_atalyshy':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'mekemenin_zhetekchisi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'pozitsiyasi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'baylanysh_telefonu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'mobildik_telefonu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }
        labels = {
            'dolboor': 'Долбоор:',
            'yuridikalyk_jekekishi': 'Юридикалык жак/Жеке киши:',
            'aty_jonu': 'Эгер жеке жак болсо Кайрылуучунун аты-жөнү:',
            'mekemenin_atalyshy': 'Мекеменин аталышы',
            'mekemenin_zhetekchisi': 'Мекеменин жетекчиси',
            'pozitsiyasi': 'Позициясы',
            'baylanysh_telefonu': 'Байланыш телефону',
            'mobildik_telefonu': 'Мобилдик телефону',
            'email': 'Email',
        }

class KenenmaalymatForm(forms.ModelForm):
    class Meta:
        model = Kenenmaalymat
        fields = [
            'dolboor',
            'koygoi_zhana_negizdeme',
            'maksat_zhana_mildetteri',
            'maksathtalgan_auditoriya',
            'kutulgozh_zhyintyk',
            'tobokelchilikter',
        ]
        widgets = {
            'dolboor': forms.Select(attrs={'class': 'form-control'}),
            'koygoi_zhana_negizdeme': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'style': 'height: 160px;'}),
            'maksat_zhana_mildetteri': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'style': 'height: 160px;'}),
            'maksathtalgan_auditoriya': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'style': 'height: 160px;'}),
            'kutulgozh_zhyintyk': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'style': 'height: 160px;'}),
            'tobokelchilikter': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'style': 'height: 160px;'}),
        }
        labels = {
            'dolboor': 'Долбоор:',
            'koygoi_zhana_negizdeme': 'Көйгөй жана негиздеме: Сиз сунуштаган долбоор кайсы көйгөйдү чечет жана долбооруңуз эмнеге манилүү?',
            'maksat_zhana_mildetteri': 'Максат жана милдеттери: Долбоор алкагында кандай конкреттүү максаттарга жетүүнү пландап жатасыз?',
            'maksathtalgan_auditoriya': 'Максатталган аудитория: Сунуштаган долбооруңуздун пайдалануучулары ким? (Мисалы, окуучулар, студенттер, мугалимдер, мүдүрлөр... алардын саны канча болорун жазыңыз).',
            'kutulgozh_zhyintyk': 'Күтүлгөн жыйынтык: Долбоордон кандай натыйжа менен ийгилик критерийлери күтүлөт? ',
            'tobokelchilikter': 'Тобокелчиликтер: Сиздин оюңузча, демилгелеген долбооруңузду кандай тобокелчиликтер күтүп турат?',
        }

class IskeAshyruUplanyForm(forms.ModelForm):
    class Meta:
        model = Iskeashyruuplany
        fields = [
            'dolboor',
            'etap',
            'ish_araket',
            'ishke_ashyruu_moonotu',
            'kutulgozh_zhyintyk'
        ]
        widgets = {
            'dolboor': forms.Select(attrs={'class': 'form-control'}),
            'etap': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'ish_araket': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'rows': 4}),
            'ishke_ashyruu_moonotu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'kutulgozh_zhyintyk': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'rows': 4}),
        }
        labels = {
            'dolboor': 'Долбоор',
            'etap': 'Этап',
            'ish_araket': 'Иш-аракет',
            'ishke_ashyruu_moonotu': 'Ишке ашыруу мөөнөтү',
            'kutulgozh_zhyintyk': 'Күтүлгөн жыйынтык',
        }

class DolboordundudjetiForm(forms.ModelForm):
    class Meta:
        model = Dolboordundudjeti
        fields = [
            'dolboor',
            'komanda_sunushtalgan_budjet',
            'komanda_bayandama',
            'ischara_sunushtalgan_budjet',
            'ischara_bayandama',
            'tuzchygymdar_sunushtalgan_budjet',
            'tuzchygymdar_bayandama',
            'ozduksalym_bayandama',
            'ozduksalym_sunushtalgan_budjet'
        ]
        widgets = {
            'dolboor': forms.Select(attrs={'class': 'form-control'}),
            'komanda_sunushtalgan_budjet': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'komanda_bayandama': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'rows': 4}),
            'ischara_sunushtalgan_budjet': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'ischara_bayandama': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'rows': 4}),
            'tuzchygymdar_sunushtalgan_budjet': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'tuzchygymdar_bayandama': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'rows': 4}),
            'ozduksalym_bayandama': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'rows': 4}),
            'ozduksalym_sunushtalgan_budjet': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }
        labels = {
            'dolboor': 'Долбоор',
            'komanda_sunushtalgan_budjet': 'Командага сунушталган бюджет: ',
            'komanda_bayandama': 'Командага баяндама: Долбоорду ишке ашыруу үчүн жооптуу Персонал боюнча кыскача маалымат киргизиңиз.',
            'ischara_sunushtalgan_budjet': 'Ишчарага сунушталган бюджет:',
            'ischara_bayandama': 'Ишчарага сунушталган бюджеттик баяндама: Долбоордун алкагында ишке ашырылчу иш-чаралар чыгымы тууралуу кененирээк маалымат жазыңыз',
            'tuzchygymdar_sunushtalgan_budjet': 'Түз чыгымдарга сунушталган бюджет:',
            'tuzchygymdar_bayandama': 'Түз чыгымдарга сунушталган бюджеттик баяндама: Жогоруда саналбаган башка чыгымдарды бул жерге киргизиңиз.',
            'ozduksalym_bayandama': 'Өздүк салымга сунушталган бюджеттик баяндама: Кошумча каржылоо булактары жана өздүк салым тууралуу жазыңыз',
            'ozduksalym_sunushtalgan_budjet': 'Өздүк салымга сунушталган бюджет:',
        }

class DolboordunkomandasyForm(forms.ModelForm):
    class Meta:
        model = Dolboordunkomandasy
        fields = ['dolboor', 'negizgi_katyshuuchular']
        widgets = {
            'dolboor': forms.Select(attrs={'class': 'form-control'}),
            'negizgi_katyshuuchular': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'rows': 4}),
        }
        labels = {
            'dolboor': 'Долбоор',
            'negizgi_katyshuuchular': 'Негизги катышуучулар: Долбоорду ишке ашыра турган команда жөнүндө маалымат бериңиз (Билим деңгээли, жөндөмдөрү, жалпы тажрыйбасы, билим берүү тармагындагы тажрыйбасы, билим берүү тармагында долбоорлорду ишке ашыруу тажрыйбасы)',
        }

class BaalooTuruktuulukForm(forms.ModelForm):
    class Meta:
        model = Baaloo_turuktuuluk
        fields = ['dolboor', 'baaloo_metoddoru', 'turuktuluk_plany']
        widgets = {
            'dolboor': forms.Select(attrs={'class': 'form-control'}),
            'baaloo_metoddoru': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'rows': 4}),
            'turuktuluk_plany': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'rows': 4}),
        }
        labels = {
            'dolboor': 'Долбоор',
            'turuktuluk_plany': 'Туруктуулук планы: Финансылык колдоо бүткөндөн кийин долбоор кантип уланат?',
            'baaloo_metoddoru':'Баалоо методдору: Долбоордун ийгилигин кантип баалайсыз? '
        }

class TirkemelerForm(forms.ModelForm):
    class Meta:
        model = Tirkemeler
        fields = ['dolboor', 'name', 'file']
        labels = {
            'dolboor': 'Долбоор:',
            'name': 'Документтин аты:',
            'file': 'Документти жүктөө:'
        }
        widgets = {
            'dolboor': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Документтин атын жазыңыз'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ProjectConfirmationForm(forms.ModelForm):
    class Meta:
        model = Project_confirmation
        fields = ['confirmation', 'comment']
        widgets = {
            'comment': forms.TextInput(attrs={'id': 'comment', 'required': True}),
            'confirmation': forms.CheckboxInput(attrs={'id': 'approval', 'required': True}),
        }