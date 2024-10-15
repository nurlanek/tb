from django.db import models
from django.contrib.auth.models import User


class Dolboor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  verbose_name='User')
    dolboordun_atalyshy = models.CharField(max_length=255, verbose_name='Долбоордун аталышы')
    prioritettu_bagyty = models.CharField(max_length=255, verbose_name='Приоритеттүү багыты')
    dolboordun_moonotu = models.CharField(max_length=100, verbose_name='Долбоордун мөөнөтү')
    dolboordun_geografiyalyk_ordu = models.CharField(max_length=255, verbose_name='Долбоордун географиялык орду')
    maksathtalgan_auditoriya = models.CharField(max_length=255, verbose_name='Максатталган аудитория')
    dolboordun_byudzheti = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Долбоордун бюджети')
    onoktoshtorunuz_maalymat = models.TextField(verbose_name='Өнөктөштөрүңүз маалымат')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    def __str__(self): return self.dolboordun_atalyshy

class Project_confirmation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_confirmation_user', verbose_name='Кайрылуучу')
    applicant_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_confirmation_confirmer',
                             verbose_name='Тастыктоочу')
    dolboor = models.ForeignKey(Dolboor, on_delete=models.CASCADE, verbose_name="Долбоор")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    confirmation = models.BooleanField(default=False, verbose_name='Макулдук')
    comment = models.CharField(max_length=255, verbose_name='Коментарий')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    def __str__(self):
        return f"{self.user} - {self.dolboor.dolboordun_atalyshy}"

class Negizgimaalymat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='negizgimaalymat', verbose_name='User')
    dolboor = models.ForeignKey(Dolboor, on_delete=models.CASCADE, related_name='negizgimaalymat', verbose_name='Долбоор')
    yuridikalyk_jekekishi = models.CharField(max_length=20, choices=[('Юридикалык жак', 'Юридикалык жак'), ('Жеке киши', 'Жеке киши')], verbose_name='Юридикалык жак/Жеке киши')
    aty_jonu = models.CharField(max_length=255, blank=True, null=True, verbose_name='Аты-жөнү')
    mekmenin_atalyshy = models.CharField(max_length=255, blank=True, null=True, verbose_name='Мекеменин аталышы')
    mekmenin_zhetekchisi = models.CharField(max_length=255, blank=True, null=True, verbose_name='Мекеменин жетекчиси')
    pozitsiyasi = models.CharField(max_length=255, blank=True, null=True, verbose_name='Позициясы')
    baylanysh_telefonu = models.CharField(max_length=20, blank=True, null=True, verbose_name='Байланыш телефону')
    mobildik_telefonu = models.CharField(max_length=20, verbose_name='Мобилдик телефону')
    email = models.EmailField(verbose_name='Email')

    def __str__(self): return f"{self.yuridikalyk_jekekishi} - {self.mekemenin_atalyshy or 'N/A'}"

class Kenenmaalymat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kenenmaalymat', verbose_name='User')
    dolboor = models.ForeignKey(Dolboor, on_delete=models.CASCADE, related_name='kenenmaalymat', verbose_name='Долбоор')
    koygoi_zhana_negizdeme = models.TextField(verbose_name='Көйгөй жана негиздеме')
    maksat_zhana_mildetteri = models.TextField(verbose_name='Максат жана милдеттери')
    maksathtalgan_auditoriya = models.TextField(verbose_name='Максатталган аудитория')
    kutulgozh_zhyintyk = models.TextField(verbose_name='Күтүлгөн жыйынтык')
    tobokelchilikter = models.TextField(verbose_name='Тобокелчиликтер')

    def __str__(self): return self.koygoi_zhana_negizdeme[:50]

class Iskeashyruuplany(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='iskeashyruuplany', verbose_name='User')
    dolboor = models.ForeignKey(Dolboor, on_delete=models.CASCADE, related_name='iskeashyruuplany',
                                verbose_name='Долбоор')
    etap = models.CharField(max_length=255, verbose_name='Этап')
    ish_araket = models.TextField(verbose_name='Иш-аракет')
    ishke_ashyruu_moonotu = models.CharField(max_length=100, verbose_name='Ишке ашыруу мөөнөтү')
    kutulgozh_zhyintyk = models.TextField(verbose_name='Күтүлгөн жыйынтык')

    def __str__(self): return f"{self.etap} - {self.ish_araket[:30]}..."

class Dolboordundudjeti(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dolboordundudjeti', verbose_name='User')
    dolboor = models.ForeignKey(Dolboor, on_delete=models.CASCADE, related_name='dolboordundudjeti',
                                verbose_name='Долбоор')
    komanda_sunushtalgan_budjet = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Команда сунушталган бюджет')
    komanda_bayandama = models.TextField(verbose_name='Команда баяндама')
    ischara_sunushtalgan_budjet = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Ишчара сунушталган бюджет')
    ischara_bayandama = models.TextField(verbose_name='Ишчара баяндама')
    tuzchygymdar_sunushtalgan_budjet = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Түзчүгүңдөр сунушталган бюджет')
    tuzchygymdar_bayandama = models.TextField(verbose_name='Түз чыгымдөр баяндама')
    ozduksalym_bayandama = models.TextField(verbose_name='Өздүк салым баяндама')
    ozduksalym_sunushtalgan_budjet = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Өздүк салым сунушталган бюджет')

    def __str__(self): return f"Бюджет - {self.komanda_sunushtalgan_budjet}"


class Dolboordunkomandasy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dolboordunkomandasy', verbose_name='User')
    dolboor = models.ForeignKey(Dolboor, on_delete=models.CASCADE, related_name='dolboordunkomandasy',
                                verbose_name='Долбоор')
    negizgi_katyshuuchular = models.TextField(verbose_name='Негизги катышуучулар')

    def __str__(self): return f"Команда - {self.negizgi_katyshuuchular[:30]}..."

class Baaloo_turuktuuluk(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='baaloo_turuktuuluk', verbose_name='User')
    dolboor = models.ForeignKey(Dolboor, on_delete=models.CASCADE, related_name='baaloo_turuktuuluk',
                                verbose_name='Долбоор')
    baaloo_metoddoru = models.TextField(verbose_name='Баалоо методдору')
    turuktuluk_plany = models.TextField(verbose_name='Туруктуулук планы')

    def __str__(self): return f"Баалоо жана Туруктуулук - {self.baaloo_metoddoru[:30]}..."

class Tirkemeler(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tirkemeler', verbose_name='User')
    dolboor = models.ForeignKey(Dolboor, on_delete=models.CASCADE, related_name='tirkemeler',
                                verbose_name='Долбоор')
    name = models.CharField(max_length=255, verbose_name='Name')
    file = models.FileField(upload_to='uploads/', verbose_name='File')

    def __str__(self): return self.name

