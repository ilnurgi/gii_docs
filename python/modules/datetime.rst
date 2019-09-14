.. py:module:: datetime

datetime
========

Модуль для работы с датой и временем


.. py:attribute:: MAXYEAR

    максимальный год

    .. code-block:: py

        datetime.MAXYEAR
        # 9999



.. py:attribute:: MINYEAR

    минимальный год

    .. code-block:: py

        datetime.MINYEAR
        # 1


date
----

.. py:class:: date(year, month, day)

    дата


    .. py:attribute:: day

        возвращает день

        .. code-block:: py

            date.today().day
            # 3


    .. py:attribute:: max

        возвращает :py:class:`date` максимально возможную дату

        .. code-block:: py

            date.max
            # date(9999, 12, 31)


    .. py:attribute:: min

        .. code-block:: py

            date.min
            # date(1, 1, 1)


    .. py:attribute:: month

        возвращает месяц

        .. code-block:: py

            date.today().month
            # 5


    .. py:attribute:: resolution

        .. code-block:: py

            date.resolution
            # timedelta(days=1)


    .. py:attribute:: year

        возвращает год

        .. code-block:: py

            date.today().year
            # 2017


    .. py:staticmethod:: fromisoformat(date_string)

        .. versionadded:: 3.7


    .. py:staticmethod:: fromordinal(dates)

        возвращает дату :py:class:`date`, соответствующую количеству дней,
        прошедших с 1 года

        .. code-block:: py

            date.max.toordinal()
            # 3652059

            date.fromordinal(3652059)
            # date(9999, 12, 31)

            date.fromordinal(1)
            # date(1, 1, 1)


    .. py:staticmethod:: fromtimestamp(seconds)

        возвращает дату :py:class:`date`, соответствующую количеству секунд,
        прошедших с начала эпохи

        .. code-block:: py

            datetime.date.fromtimestamp(time.time())
            # date(2014, 8, 24)

            datetime.date.fromtimestamp(1233368623.0)
            # date(2009, 1, 31)


    .. py:staticmethod:: isoformat(date)

        Возвращает строку, дату в исо формате

        .. code-block:: py

            date.isoformat(date.today())
            # '2017-03-05'


    .. py:method:: ctime()

        возвращает строку специального формата

        .. code-block:: py

            date.ctime()
            # 'Sun Jun 5 00:00:00 2011'


    .. py:method:: isocalendar()

        возвращает кортеж из 3х элементов (год, номер недели и порядковый номер дня в неделе)

        .. code-block:: py

            date.today().isocalendar()
            # (2019, 37, 4)


    .. py:method:: isoformat()

        возвращает дату в формате ГГГГ-ДД-ММ

        .. code-block:: py

            date.today().isoformat()
            # '2019-09-12'


    .. py:method:: isoweekday()

        возвращает порядковый номер дня недели (начинается с 1)

        .. code-block:: py

            date.today().isoweekday()
            # 4


    .. py:method:: replace(year, month, day)

        возвращает дату с обновленными значемниями

        .. code-block:: py

            date.today()
            # date(2019, 9, 12)

            date.today().replace(2020)
            # date(2020, 9, 12)


    .. py:method:: strftime(dt_format)

        возвращает отформатированную строку

        .. code-block:: py

            date.today().strftime('%Y-%m-%d')
            # '2019-09-12'


    .. py:method:: timetuple()

        возвращает :py:class:`time.struct_time` с датой и временем

        .. code-block:: py

            date.today().timetuple()
            # time.struct_time(tm_year=2019, tm_mon=9, tm_mday=12, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=255, tm_isdst=-1)


    .. py:staticmethod:: today()

        Возвращает :py:class:`datetime.date`, текущую дату

        .. code-block:: py

            date.today()
            # datetime.date(2017, 5, 3)


    .. py:method:: toordinal()

        возвращает количесвто дней, прошедших с 1 года

        .. code-block:: py

            date.today().toordinal()
            # 737314


    .. py:method:: weekday()

        возвращает порядковый номер дня в недели (начинается с 0)

        .. code-block:: py

            date.today().weekday()
            # 3


datetime
--------

.. py:class:: datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None,*, fold=0)

    дата и время


    .. py:attribute:: year

        год


    .. py:attribute:: month

        месяц


    .. py:attribute:: day

        день


    .. py:attribute:: fold

        .. versionadded:: 3.6


    .. py:attribute:: hour

        часы


    .. py:attribute:: max

        .. code-block:: py

            datetime.max
            # datetime(9999, 12, 31, 59, 59, 999999)


    .. py:attribute:: microsecond

        микросекунды


    .. py:attribute:: min

        .. code-block:: py

            datetime.min
            # datetime(1, 1, 1)


    .. py:attribute:: minute 

        минуты 


    .. py:attribute:: resolution

        .. code-block:: py

            datetime.resolution
            # timedelta(microsecond=1)


    .. py:attribute:: second

        секунды 


    .. py:attribute:: tzinfo

        временная зона


    .. py:classmethod:: combine(date, time)

        создает экземпляр класса в соответствии со значениями экземпляров класса date и time

        .. code-block:: py

            datetime.combine(date.today(), time(11, 10))
            # datetime(2019, 9, 12, 11, 10)


    .. py:staticmethod:: fromisoformat(date_string)

        .. versionadded:: 3.7


    .. py:classmethod:: fromordinal(days)

        возвращает дату, соответсвующую количесвту дней, прошедших с 1 года

        .. code-block:: py

            datetime.fromordinal(1)
            # datetime(1, 1, 1, 0, 0)


    .. py:classmethod:: fromtimestamp(seconds, tz=None)

        возвращает дату, соотвествующую количесвтоу секунд с начала эпохи

        .. code-block:: py

            datetime.fromtimestamp(time.time())
            # datetime(2014, 8, 24, 0, 0)

            datetime.fromtimestamp(1233368623.0)
            # datetime(2009, 1, 31, 0, 0)


    .. py:classmethod:: now(tz)

        возвращает текущую дату и время

        .. code-block:: py

            datetime.now()
            # datetime(2019, 9, 12, 0, 0)


    .. py:classmethod:: strptime(date_str, date_format)

        разбирает строку с датой в соответсвии со строкой формата

        .. code-block:: py

            datetime.strptime('2019-09-12', '%Y-%m-%d')
            # datetime(2019, 9, 12, 0, 0)


    .. py:classmethod:: today()

        возвращает текущую дату и время

        .. code-block:: py

            datetime.today()
            # datetime(2019, 9, 12, 6, 54, 47, 320298)


    .. py:classmethod:: utcfromtimestamp(seconds)

        dозвращает дату, соответствующую количесвту секунд, прошедших с начала эпохи в универсальном времени (UTC)

        .. code-block:: py

            datetime.utcfromtimestamp(1)
            # datetime(1970, 1, 1, 0, 0, 1)


    .. py:classmethod:: utcnow()

        возвращает текущее универсальное время (UTC) 

        .. code-block:: py

            datetime.utcnow()
            # datetime(2019, 9, 12, 3, 55, 59, 579073)


    .. py:method:: astimezone(tz=None)

        Возвращает новый экземпляр даты с измененной таймзоной


    .. py:method:: ctime()

        возвращает строку специального формата

        .. code-block:: py

            datetime.now().ctime()
            # 'Fri Sep 13 06:57:23 2019'


    .. py:method:: date()

        возврашает дату в формате :py:class:`date`

        .. code-block:: py

            datetime.now().date()
            # date(2019, 9, 13)


    .. py:method:: dst()


    .. py:method:: isocalendar()

        возвращает кортеж из трех элементов (год, номер недели в году и порядковый номер дня в неделе)

        .. code-block:: py

            datetime.now().isocalendar()
            # (2019, 37, 5)


    .. py:method:: isoformat(sep='T', timespec='auto')

        dозвращает дату в формате ISO 8601

        .. code-block:: py

            datetime.now().isoformat()
            # '2019-09-13T06:57:23.687795'


    .. py:method:: isoweekday()

        возвращает порядковый номер дня недели (начинается с 1)

        .. code-block:: py

            datetime.now().isoweekday()
            # 5


    .. py:method:: replace(year, month, day, hour, minute, second, microsecond, tzinfo, fold=0)

        .. versionadded:: 3.6

            добален параметр fold

        возвращает дату с обновленными значениями

        .. code-block:: py

            datetime.now()
            # datetime(2019, 9, 12, 0, 0)

            datetime.now().replace(2020)
            # datetime(2020, 9, 12, 0, 0)


    .. py:method:: strftime(format_sr)

        возвращает отформатированную строку

        .. code-block:: py

            datetime.now().strftime('%d-%m-%Y')
            # '12-09-2019'

        
    .. py:method:: time()

        возвращает время в формате :py:class:`time`

        .. code-block:: py

            datetime.now().time()
            # time(6, 57, 23, 687795)

        
    .. py:method:: timestamp()


    .. py:method:: timetuple()

        возвращает дату и время в формате :py:class:`struct_time`

        .. code-block:: py

            datetime.now().timetuple()
            # time.struct_time(tm_year=2019, tm_mon=9, tm_mday=13, tm_hour=6, tm_min=57, tm_sec=23, tm_wday=4, tm_yday=256, tm_isdst=-1)


    .. py:method:: timetz()

        возвращает время в формате :py:class:`time` с учетом временной зоны

        .. code-block:: py

            datetime.now().timetz()
            # time(6, 57, 23, 687795)


    .. py:method:: toordinal()

        возвращает количесвто дней с 1 года

        .. code-block:: py

            datetime.now().toordinal()
            # 737315


    .. py:method:: tzname()


    .. py:method:: utcoffset()


    .. py:method:: utctimetuple()

        возвращает дату и время в формате :py:class:`struct_time` в универсальном времене

        .. code-block:: py

            datetime.now().utctimetuple()
            # time.struct_time(tm_year=2019, tm_mon=9, tm_mday=13, tm_hour=6, tm_min=57, tm_sec=23, tm_wday=4, tm_yday=256, tm_isdst=0)


    .. py:method:: weekday()

        возвращает порядковый номер дня в недели (начинается с 0)

        .. code-block:: py  

            datetime.now().weekday()
            # 4


time
----

.. py:class:: time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, fold=0)

    время

    
    .. py:attribute:: fold


    .. py:attribute:: hour

        часы


    .. py:attribute:: max

        .. code-block:: py

            time.max
            # time(23, 59, 59, 999999)


    .. py:attribute:: microsecond

        микросекунды


    .. py:attribute:: min

        .. code-block:: py

            time.min
            # time(0, 0, 0, 0)


    .. py:attribute:: minute

        минуты


    .. py:attribute:: second

        секунды


    .. py:attribute:: tzinfo

        информаиця о временной зоне


    .. py:method:: dst()


    .. py:method:: fromisoformat(time_str)


    .. py:method:: isoformat(timespec='auto')

        возвращает время в формате ISO 8601

        * auto - по умолчанию
        * hours - HH
        * minutes - HH:MM
        * seconds - HH:MM:SS
        * milliseconds - HH:MM:SS.sss
        * microseconds - HH:MM:SS.ffffff

        .. code-block:: py

            time(23, 12, 38, 375000).isoformat()
            # '23:12:38.375000'

            time(23, 12, 38, 375000).isoformat('hours')
            # '23'

            time(23, 12, 38, 375000).isoformat('minutes')
            # '23:12'

            time(23, 12, 38, 375000).isoformat('seconds')
            # '23:12:38'

            time(23, 12, 38, 375000).isoformat('milliseconds')
            # '23:12:38.000'

            time(23, 12, 38, 375000).isoformat('microseconds')
            # '23:12:38.000001'


    .. py:method:: replace(hour, minute, second, microsecond, tzinfo)

        возвращает время с обновленными значениями


    .. py:method:: strftime(format_str)

        возвращает отформатированную строку
    

    .. py:method:: tzname()


    .. py:method:: utcoffset()


timedelta
---------

.. py:class:: timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

    дата  в виде количесвта дней, секунд и микросекунд

    .. code-block:: py

        timedelta(days=2) + timedelta(days=7)
        # timedelta(9)

        timedelta(days=7) - timedelta(days=2)
        # timedelta(5)

        timedelta(days=7) / timedelta(days=2)
        # 3.5

        timedelta(days=2) * 2
        # datetime.timedelta(4)
        
        timedelta(days=7) * 2
        # timedelta(14)

        timedelta(days=2) / 2, 
        # datetime.timedelta(1)
        
        timedelta(days=2) / 2.5
        # datetime.timedelta(2, 69120)

        timedelta(days=7) // timedelta(days=2)
        # 3

        timedelta(days=2) // 2
        # timedelta(1)
        
        timedelta(days=7) // 2
        # timedelta(3, 43200)

        timedelta(days=7) % timedelta(days=2)
        # timedelta(1)

    .. code-block:: py

        timedelta(days=2) == timedelta(days=7)
        # False

        timedelta(days=7) == timedelta(weeks=1)
        # True

        timedelta(days=2) != timedelta(days=7)
        # True

        timedelta(days=7) != timedelta(weeks=1)
        # False

        timedelta(days=2) < timedelta(days=7)
        # True

        timedelta(days=7) <= timedelta(weeks=1)
        # True

        timedelta(days=2) > timedelta(days=7)
        # False

        timedelta(days=7) <= timedelta(weeks=1)
        # True


    .. py:attribute:: days

        количество дней


    .. py:attribute:: min

        .. code-block:: py

            timedelta.max
            # timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)


    .. py:attribute:: min

        .. code-block:: py

            timedelta.min
            # timedelta(-999999999)


    .. py:attribute:: microseconds

        количесвто микросекунд


    .. py:attribute:: resolution

        .. code-block:: py

            timedelta.resolution
            # timedelta(microseconds=1)


    .. py:attribute:: seconds

        количесвто секунд


    .. py:method:: total_seconds()

        возвращает результат в секундах 

        .. versionadded:: 3.2

        .. code-block:: py

            timedelta(days=365).total_seconds()
            # 31536000.0


tzinfo
------

.. py:class:: tzinfo

    зона времени

    .. py:method:: dst(dt)
    

    .. py:method:: fromutc(dt)


    .. py:method:: tzname(dt)


    .. py:method:: utcoffset(dt)


timezone
--------

.. versionadded:: 3.2

.. py:class:: timezone(offset, name=None)

    зона времени

    .. py:attribute:: utc


    .. py:method:: fromutc(dt)


    .. py:method:: dst(dt)


    .. py:method:: tzname(dt)


    .. py:method:: utcoffset(dt)


Форматирование
--------------

* a - день недели сокращенный, Sun - Sat
* A - день недели полный, Sunday - Saturday
* w - день недели в числовом виде, 0 - 6
* d - день недели с ноликом, 01 - 31
* b - месяц сокращенный, Jan - Dec
* B - месяц полный, January - December
* m - месяц в числовом виде, 01 - 12
* y - год бес тысячелетия, 01 - 99
* Y - год с тысячелетием, 0001 - 9999
* H - часы в 24 часовом формате, 01 - 23
* I - часы в 12 часовм формате, 01 - 12
* p - am/pm
* M - минуты, 00 - 59
* S - секунды, 00 - 59
* f - микросекунды, 00000 - 999999
* z - utc офсет, +0000, -0400, +1030
* Z - название таймзоны, UTC, EST, CST
* j - номер дня недели в году, 001 - 366
* U - номер недели в году, из расчета воскресенье первый день недели, 00 - 53
* W - номер недели в году, из расчета понедельник первый день недели, 00 - 53
* c - локальное представление время, Tue Aug 16 21:30:00 1988
* x - локальное представление даты, 08/16/1988
* X - локальное представление времени, 21:30:00
