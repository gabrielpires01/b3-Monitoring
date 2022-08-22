from django.core.mail import send_mail

def send_email_task(symbol, closed_data, from_email, do):
    send_mail(
            f'{do} Actives',
            f'Is time to sell yours actives from {symbol}: it value is {closed_data}',
            f'{from_email}',
            [f'{from_email}'],
            fail_silently=False,
        )
    
    