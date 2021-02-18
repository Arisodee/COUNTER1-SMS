import datetime
import celery

@celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=5)) # here we assume we want it to be run every 5 mins
def myTask():
    # Do something here
    # like accessing remote apis,
    # calculating resource intensive computational data
    # and store in cache
    # or anything you please
    print 'This wasn\'t so difficult'