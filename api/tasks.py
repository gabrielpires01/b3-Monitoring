from django.core.mail import send_mail

from api import alpha_api, tasks
from api.models import Pipeline

def send_email_task(symbol, closed_data, from_email, do):
    send_mail(
            subject = f'{do} Actives',
            message = f'Is time to {do} yours actives from {symbol}: it value is {closed_data}',
            from_email = f'{from_email}',
            recipient_list = [f'{from_email}'],
            fail_silently=False,
        )
    
def verify_prices_task(symbol, top_value, bottom_value, email, current_value):
    try:
        if float(current_value) >= float(top_value):
            send_email_task(symbol, current_value, email, 'Sell')
        if float(current_value) <= float(bottom_value):
            send_email_task(symbol, current_value, email, 'Buy')
    except:
        raise SystemExit()
    return

interaval = {
		'1min': 1,
		'5min': 5,
		'15min': 15,
		'30min': 30,
		'60min': 60
	}

def create_job(scheduler, data):
    real_interval = interaval[data['interval']]

    scheduler.add_job(job, args=(
			data['symbol'], 
			data['interval'], 
			data['top_value'], 
			data['bottom_value'],
			data['email']), 
			trigger='interval', 
			minutes=real_interval
		)
    return

def get_jobs(scheduler):
	data = Pipeline.objects.all()
	pipelines = data.values()

	for obj in pipelines:
		real_interval = interaval[obj['interval']]

		scheduler.add_job(job, args=(
			obj['symbol'], 
			obj['interval'], 
			obj['top_value'], 
			obj['bottom_value'],
			obj['email']), 
			trigger='interval', 
			minutes=real_interval
		)

	return

def job(*args):
	data = alpha_api.get_alpha_api_last(args[1], args[0])
	tasks.verify_prices_task(args[0],args[2],args[3], args[4],data['4. close'])
	
	return