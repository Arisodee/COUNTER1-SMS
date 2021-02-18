from django.db import models
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

# Create your models here.
class Count(models.Model):
    username = models.CharField(max_length=80)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.username)


class Invitation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    code = models.CharField(max_length=20)
    sender = models.ForeignKey(User)

  
    def __unicode__(self):
        return u'%s, %s' % (self.sender.username, self.email)

    def send(self):
        subject = u'Invitation to join Django Bookmarks'
        link = 'http://%s/friend/accept/%s/' % (
        settings.SITE_HOST,
        self.code
            )
        template = get_template('invitation_email.txt')
        context = Context({
        'name': self.name,
        'link': link,
        'sender': self.sender.username,
             })
        message = template.render(context)
        send_mail(
        subject, message,
        settings.DEFAULT_FROM_EMAIL, [self.email]    )    