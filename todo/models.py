from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        'auth.User',
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        related_name='tasks',
        blank=True, null=True,
    )
    tittle=models.CharField(blank=True,null=True,verbose_name=_('Task Tittle'),max_length=50)
    description=models.TextField(blank=True,null=True,verbose_name=_('Task Description'),max_length=4000)
    class STATUS(models.TextChoices):
        TODO= '0',_('todo')
        IN_PROGRESS = '1',_('In Progress')
        DONE = '2', _('Done')

    status=models.CharField(
        max_length=1,
        choices=STATUS.choices,
        default=STATUS.TODO,
    )

    due_Date=models.DateField(verbose_name=_('Due Date'),blank=True, null=True,)

    class Meta:
        ordering = ['due_Date']

    def __str__(self):
        return self.tittle