.. title:: python celery

.. meta::
    :description:
        Справочная информация по python модулю celery.
    :keywords:
        python celery

celery
======

http://docs.celeryproject.org/en/latest/


.. code-block:: py

    # celery.py

    import os

    import celery

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

    app = Celery('proj')

    app.config_from_object('django.conf:settings', namespace='CELERY')

    app.autodiscover_tasks()

    @app.task(bind=True, default_retry_delay=10*60)
    def debug_task(self):
        print(self.request)


.. code-block:: py

    from celery.schedulers import crontab

    CELERY_BEAT_SCHEDULE = {
        'task-name': {
            'task': 'project.apps.statistics.tasks.task',
            'schedule': crontab(day_of_week=1, hour=7),
        }
    }