from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from navigation.models import BlogPost,Emailinput

@receiver(post_save, sender=BlogPost)
def send_email_to_subscribers(sender, instance, created, **kwargs):
    if created:
        # Retrieve all subscriber emails
        subscriber_emails = Emailinput.objects.values_list('email', flat=True)

        # Compose email content
        email_subject = 'New Blog Post: {}'.format(instance.title)
        email_message = 'A new blog post has been published!\n\n'
        email_message += 'Title: {}\n'.format(instance.title)
        email_message += 'Content: {}\n'.format(instance.summary)
        email_message += 'Author: {}\n'.format(instance.Postauthor)

        # Send email to each subscriber
        for email in subscriber_emails:
            send_mail(email_subject, email_message, 'dolikemathewalex@gmail.com', [email], fail_silently=False)
