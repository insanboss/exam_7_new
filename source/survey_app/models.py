from django.db import models

# Create your models here.


class Poll(models.Model):
    question = models.TextField(max_length=200, null=False, blank=False, verbose_name="Вопрос")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Questions'
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return "{}. {}".format(self.created_at, self.question)


class AnswerOption(models.Model):
    option_text = models.TextField(max_length=300, null=False, blank=False, verbose_name="Вариант ответа")
    poll = models.ForeignKey('survey_app.Poll', related_name='Опрос-ответы', on_delete=models.CASCADE,
                                verbose_name='Опрос')

    def __str__(self):
        return "{}. {}".format(self.poll, self.option_text)
