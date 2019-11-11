.. title:: matplotlib pyplot

.. meta::
    :description:
        Описание python модуля matplotlib.pyplot.
    :keywords:
        python matplotlib pyplot

.. py:module:: matplotlib.pyplot

pyplot
======

Оснвные методы для построения:

    * :py:func:`bar` - диаграмма вертикальная
    * :py:func:`barh` - диаграмма горизонтальная
    * :py:func:`boxplot`
    * :py:func:`broken_barh`
    * :py:func:`contour`
    * :py:func:`contourf`
    * :py:func:`errorbar` - графики с ошибками
    * :py:func:`hist` - гистограммы
    * :py:func:`hist2d`
    * :py:func:`hlines`
    * :py:func:`pie` - круги, куски пирога
    * :py:func:`plot` - графики, ломаная линия
    * :py:func:`polar` - полярная система координат
    * :py:func:`scatter` - нанесение маркера в точке
    * :py:func:`semilogy` - график логарифметический
    * :py:func:`text` - нанесение текста


acorr()
-------

.. py:function:: acorr()


angle_spectrum()
----------------

.. py:function:: angle_spectrum()


annotate()
----------

.. py:function:: annotate(text, xy, *args, **kwargs*)

    Добавляет аннотацию указанных точек, аналогично :py:meth:`matplotlib.axes.Axes.annotate()`, возвращает :py:class:`matplotlib.text.Text`.

    * **text** : str - сообщение

    * **xy** : tuple(x, y) - координата точки

    * **annotation_clip** : bool

        * **True** - аннотация будет отрисовываться, если xy попадает в результирующую ось
        * **False** - аннотация будет отрисовываться всегда
        * **None** - аннотация будет отрисовываться, если ху попадает в результирующую ось и xycoords == 'data'

    * **arrowprops** : dict - описание свойств указателя, стрелки на точку для объекта :py:class:`matplotlib.patches.FancyArrowPatch()`

        Если задан параметр **arrowstyle**, то остальные ключи игнорируются

        * **arrowstyle** : str - стиль стрелки
            * **-** - None
            * **|-|** - widthA=1.0, widthB=1.0
            * **-[** - widthB=1.0, lengthB=0.2, angleB=None
            * **->** - head_length=0.4, head_width=0.2
            * **<-** - head_length=0.4, head_width=0.2
            * **<->** - head_length=0.4, head_width=0.2
            * **-|>** - head_length=0.4, head_width=0.2
            * **<|-** - head_length=0.4, head_width=0.2
            * **<|-|>** - head_length=0.4, head_width=0.2
            * **fancy** - head_length=0.4, head_width=0.4, tail_width=0.4
            * **simple** - head_length=0.5, head_width=0.5, tail_width=0.2
            * **wedge** - tail_width=0.3, shrink_factor=0. 5
        * **connectionstyle** - стиль соединения с точкой
            * **arc** -> angleA=0, angleB=0, armA=None, armB,=None, rad=0.0
                * arc,angleA=10,armA=30,rad=15
            * **arc3** -> rad=0.0
                * arc3,rad=.2
                * arc3,rad=-.2
            * **angle** -> angleA=90, angleB=0, rad=0.0
            * **angle3** -> angleA=90, angleB=0
            * **bar** -> armA=0.0,armB=0.0,fraction=0.3,angle=None
        * **headlength**
        * **headwidth**
        * **mutation_aspect**
        * **mutation_scale**
        * **patchA**
        * **patchB**
        * **relpos**
        * **shrink** - отступ от точки
        * **shrinkA**
        * **shrinkB**
        * **width**

    * **textcoords**: str, :py:class:`matplotlib.artist.Artist()`, :py:class:`matplotlib.transform.Transform()`, callbal, tuple

        система координат, для укзанной позиции сообщения

        * **offset points**
        * **offset pixels**

    * **xycoords**: str, :py:class:`matplotlib.artist.Artist()`, :py:class:`matplotlib.transform.Transform()`, callbal, tuple

        система координат, для указанной позиции точек

        * **figure points**
        * **figure pixels**
        * **figure fraction**
        * **axes points**
        * **axes pixels**
        * **axes fraction**
        * **data**
        * **polar**

    * **xytext** : tuple(x, y) - координата где отображать текст, если не задан, то отображается на указанной точке

    * :py:class:`matplotlib.text.Text` параметры

    .. code-block:: py

        pyplot.annotate(
            'message on (0.3, 0.3), point on (0.2, 0.2)',
            (0.2, 0.2),
            xytext=(0.3, 0.3),
            arrowprops={
                'facecolor': 'black',
                'shrink': 0.05
            }
        )

    .. figure:: images/annotate_1.png


arrow()
-------

.. py:function:: arrow(x, y, dx, dy, **kwargs)

    Рисует стрелку на графике и возвращает :py:class:`matplotlib.patches.FancyArrow()`

    * **head_length** : float or None = 1.5*head_width
    * **head_width** : float or None = 3*width
    * **head_starts_at_zero** : bool = False
    * **length_includes_head** : bool = False
    * **overhang** : float  = 0
    * **shape** : ['full', 'left', 'right'] = full
    * **width** : float = 0.001
    * :py:class:`matplotlib.patches.FancyArrow()` параметры

    .. code-block:: py

        pyplot.arrow(
            0.2, 0.2, 0.2, 0.2,
            fc='r',
            ec='g',
            head_width=0.1,
        )

    .. figure:: images/arrow_1.png

autoscale()
-----------

.. py:function:: autoscale()


autumn()
--------

.. py:function:: autumn()


axes()
------

.. py:function:: axes(arg=None, **kwargs)

    Создает новую ось в текущей фигуре и возвращает :py:class:`matplotlib.axes.Asxes()`

    * **arg** - None, tuple(l, b, w, h)
    * **label** - str
    * **polar** - bool
    * **projection** - None, 'aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear', str
    * **sharex** - :py:class:`matplotlib.axes.Axes()`
    * **sharey** - :py:class:`matplotlib.axes.Axes()`
    * :py:class:`matplotlib.axes.Axes()` параметры

    .. code-block:: py

        axes()
        # AxesSubplot(0.125, 0.11; 0.775x0.77)

    .. code-block:: py

        axes([0, 0, 0.5, 0.5], facecolor='r')

    .. figure:: images/axes_1.png


axhline()
---------

.. py:function:: axhline(y=0, xmin=0, xmax=1, **kwargs)

    Добавляет линию для оси Х и возвращает :py:class:`matplotlib.lines.Line2D()`

    * :py:class:`matplotlib.lines.Line2D()` параметры

    .. code-block:: py

        axhline()
        axhline(linewidth=4, color='r')
        axhline(y=1)
        axhline(y=.5, xmin=0.25, xmax=0.75)

    .. figure:: images/axhline_1.png


axvline()
---------

.. py:function:: axvline(x=0, ymin=0, ymax=1, **kwargs)

    Добавляет линию для оси Х и возвращает :py:class:`matplotlib.lines.Line2D()`

    * :py:class:`matplotlib.lines.Line2D()` параметры

    .. code-block:: py

        axvline()
        axvline(linewidth=4, color='r')
        axvline(y=1)
        axvline(y=.5, xmin=0.25, xmax=0.75)

    .. figure:: images/axvline_1.png


axhspan()
---------

.. py:function:: axhspan(ymin, ymax, xmin=0, xmax=1, **kwargs)

    Добавляет горизонтальную область и возвращает :py:class:`matplotlib.patches.Polygone()`

    * :py:class:`matplotlib.patches.Polygone()` параметры

    .. code-block:: py

        axhspan(0, 0.3, 0, 10, color='r')

    .. figure:: images/axhspan_1.png

bar()
-----

.. py:function:: bar(x, height, **kwargs)

    Рисует вертикальную диаграмму, столбцы и возвращает :py:class:`matplotlib.container.BarContainer()`

    * **x** : iterable - координаты по оис х
    * **height** : scalar | iterable - высота столбцов
    * **align** : 'center' | 'edge' - выравнивание столбцов относительно значения
    * **bottom** : scalar | iterable = 0 - у координата столбцов
    * **capsize** : scalar | iterable
    * **color** : scalar | iterable  - цвета столбцов
    * **ecolor** : scalar | iterable
    * **edgecolor** : scalar | iterable - цвета границ столбцов
    * **error_kw**: dict
    * **linewidth** : scalar | iterable - ширина границ столбцов
    * **log** : bool - устанавливает логарифмическую ось У
    * **tick_label** : scalar | iterable - подписи для значений оси х
    * **xerr**, **yerr** : scalar | iterable -
    * **width** : scalar | iterable = 0.8 - ширина столбцов

    .. code-block:: py

        pyplot.bar([1, 2, 3], [5, 8, 3])

    .. figure:: images/bar_1.png


barbs()
-------

.. py:function:: barbs()

barh()
------

.. py:function:: barh()

    Диаграмма горизонтальная, аналогичная :py:func:`matplotlib.pyplot.bar`

    .. code-block:: py

        pyplot.barh([1, 2, 3], [5, 8, 3])

    .. figure:: images/barh_1.png


bone()
------

.. py:function:: bone()

    Устанавливает цветовую схему bone


box()
-----

.. py:function:: box(on: bool = None)


boxplot()
---------

.. py:fun:: boxplot()


broken_barh()
-------------

.. py:function:: broken_barh()


cla()
-----

.. py:function:: cla()

    Очищает область осей


clabel()
--------

.. py:function:: clabel()


clf()
-----

.. py:function:: clf()

    Очищает область фигуры


clim()
------

.. py:function:: clim(vmin=None, vmax=None)


close()
-------

.. py:function:: close(fig=None)

    Закрывает окно фигуры


cohere()
--------

.. py:function:: cohere()


colorbar()
----------

.. py:function:: colorbar()


connect()
---------

.. py:function:: connect(event_name, callback)

    Добавляет обработчики событий и возвращет его идентификатор, 
    который можно исползоват для удаления обработчика через :py:func:`matplotlib.pyplot.disconnect()`.

    * **button_press_event**
    * **button_release_event**
    * **draw_event**
    * **key_press_event**
    * **key_release_event**
    * **motion_notify_event**
    * **pick_event**
    * **resize_event**
    * **scroll_event**
    * **figure_enter_event**,
    * **figure_leave_event**,
    * **axes_enter_event**,
    * **axes_leave_event**
    * **close_event**

    .. code-block:: py

        close_id = pyplot.connect('close_event', lambda event: pass)


contour()
---------

.. py:function:: contour()


contourf()
----------

.. py:function:: contourf()


cool()
------

.. py:function:: cool()

    Устанавливает цветовую схему **cool**.


cooper()
--------

.. py:function:: cooper()

    Устанавливает цветовую схему **cooper**.


csd()
-----

.. py:function:: csd()


delaxes()
---------

.. py:function:: delaxes(ax=None)

    Удаляет область рисования из фигуры


disconnect()
------------

.. py:function:: disconnect(cid)

    Удаляет обработчик событий, назначенный через :py:func:`matplotlib.pyplot.connect()`


draw()
------

.. py:function:: draw()

    Перерисовывает фигуру


errorbar()
----------

.. py:function:: errorbar(x, y, yerr, xerr, fmt, ecolor, elinewidth, capsize)

    Строит какой то график

    .. code-block:: py

        errorbar(
            numpy.arange(0, 4, 0.2),
            numpy.exp(-x),
            0.1 * numpy.abs(
                numpy.random.randn(len(y))),
            fmt=".-"
        )

        errorbar(x, y, yerr=e1, xerr=e2)
        errorbar(x, y, yerr=[e1, e2])


eventplot()
-----------

.. py:function:: eventplot()


figtext()
---------

.. py:function:: figtext()

     Возвращает :py:class:`matplotlib.text.Text`


figure()
--------

.. py:function:: figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)

    Возвращает объект области рисования, :py:class:`matplotlib.figure.Figure` и назначает размер области рисования

    * figsize - кортеж с размерами окна диаграммы в дюймах, по умобчанию 80 пискелей на дюйм


    .. code-block:: py

        fig = plt.figure(figsize=(3, 3))

        fig = plt.figure(dpi=128, figsize=(3, 3))

        fig = plt.figsize(figsize=(8, 6), facecolor='pink', frameon=True)


grid()
------

.. py:function:: grid(bool)

    Включает отображение сетки по значениям осей

    .. code-block:: py

        grid(True)


hist()
------

.. py:function:: hist(values, bin=10, color, edgecolor, )

    Строит гистограмму для входящих данных.

    По умолчанию делит данные на 10 отрезков

    .. code-block:: py

        hist([1, 1, 1, 0])
        hist([1, 1, 1, 0], color='blue', edgecolor='black', bins=30)


hold()
------

.. py:function:: hold(bool)

    Отображает пустое окно

    .. code-block:: py

        hold(True)


interactivity()
---------------

.. py:function:: interactivity(bool)

    Включает интерактинвый режим, изображение перерисовывается
    при каждом вызове метода :py:func:`plot`.

    Смотрите также:

        * :py:func:`ioff`
        * :py:func:`ion`
        * :py:func:`isinteractive`

    .. code-block:: py

        interactivity(True)


ioff()
------

.. py:function:: ioff()

    Выключает интерактинвый режим

    Смотрите также:

        * :py:func:`ion`
        * :py:func:`interactivity`
        * :py:func:`isinteractive`

    .. code-block:: py

        ioff()


ion()
-----

.. py:function:: ion()

    Включает интерактинвый режим

    Смотрите также:

        * :py:func:`ioff`
        * :py:func:`interactivity`
        * :py:func:`isinteractive`

    .. code-block:: py

        ion()


isinteractive()
---------------

.. py:function:: isinteractive()

    Возвращает :py:class:`bool`, включен интерактинвый режим

    Смотрите также:

        * :py:func:`ioff`
        * :py:func:`ion`
        * :py:func:`interactivity`

    .. code-block:: py

        isinteractive()
        # True


legend()
--------

.. py:function:: legend(**kwargs)

    Возвразает или отображаем легенду :py:class:`matplotlib.legend.Legend`

    * borderaxespad - величина зазора между осями и легендой

    * legend_names - список названии легенд, лучше задавать при построении графика

    * loc - местоположение вывода данных легенды, можно задачть как числом так и строкой,
      а также кортежом позиции

        * 0 - best
        * 1 - upper right
        * 2 - upper left
        * 3 - lower left
        * 4 - lower right
        * 5 - right
        * 6 - center left
        * 7 - center right
        * 8 - lower center
        * 9 - upper center
        * 10 - center



    .. code-block:: py

        legend()
        legend(['Legend1', 'Legend2'])
        legend(loc=(-0.1, 0.9))
        legend(loc='best')
        legend(loc=3)

    * mode

        * expand - растянуть легенду по всей ширине

    * ncol - количество столбцов для легенды


pie()
-----

.. py:function:: pie(x, **kwargs)

    Кусок пирога

    * colors - цвета секторов
    * explode - список уровней выдвижения секторов
    * labels - список заголовков секторов
    * shadow - булево, добавить тень
    * labeldistance
    * autopct
    * pctdistance

    .. code-block:: py

        pie([10, 30, 60], ['Red', 'Green', 'Blue'])
        pie(
            x,
            labels,
            explode=[0.2, 0.1, 0.0],
            autopct="%1.1f%%",
        )


plot()
------

.. py:function:: plot(*args, **kwargs)

    Создает график

    * color - цвет линии

    * label - строка легенды

    * line_format - идет сразу после координат,
      тип линии, цвет линии, маркер точек, задается строкой

        Типы линии

        * - - сплошная линия
        * -- - пунктирная линия
        * -. - пнутирная с точкой
        * : - точечный график

        Цвета

        * b - синий
        * c - голубой
        * g - зеленый
        * k - черный
        * m - фиолетовый
        * r - красный
        * w - белый
        * y - желтый
        * 'red'
        * '#ff00ff' - hex
        * (1, 0, 1, 1) - RGBA
        * '0.7' - оотенки серого

        Маркеры точек

        * ., , - точка
        * \*, +, \|, - -
        * V, ^, <, > - треуголник
        * 1, 2, 3, 4 -
        * o - круг
        * D - ромбик
        * d -
        * H -
        * h -
        * s - квадрат
        * p - пятиуголник
        * X -
        * x -

    * linestyle  - стиль линии

    * linewidth - ширина линии

    * marker - маркер точек

    * markeredgecolor - цвет граней маркера

    * markeredgewidth - ширина грней маркера

    * markerfacecolor - цвет заливки маркера

    * markersize - размер маркера



    .. code-block:: py

        # строит график по указанным у координатам
        # каждой у соответсвует х от 0
        plot([1, 3, 2, 4])

        # строит график по указанным x, y координатам
        x = range(6)
        y = [i**2 for i in x]
        plot(x, y)

    .. code-block:: py

        # строит график по указанным x, y координатам
        x = range(6)
        y = [i**2 for i in x]
        y1 = [i*3 for i in x]
        plot(x, y, x, y1)

    .. code-block:: py

        # график с красной линией
        plot([1, 3, 2, 4], 'r')

        # графики с цветами
        plot(
            x, y, 'r',
            x, y1, 'y')

        # типы линии
        plot(
            x, y, '--',
            x, y1, '-.')

        plt.plot(

            # голубой, пунктирный, маркеры - х
            y, 'cx--',

            # фиолетовый, точечный, маркер - круг
            y+1, 'mo:',

            # черный, тире и точка, маркер - пятиуголник
            y+2, 'kp-.')

        plt.plot(
            y,
            color='blue',
            linestyle='dashdot',
            linewidth=4,
            marker='o',
            markerfacecolor='red',
            markeredgecolor='black',
            markeredgewidth=3,
            markersize=12);


polar()
-------

.. py:function:: polar()

    Полярная система координат

    .. code-block:: py

        # окружность от 0 до 2pi
        theta = numpy.arange(0., 2., 1./180.)*numpy.pi

        # спираль
        plt.polar(3*theta, theta/5);

        # цветок
        plt.polar(theta, numpy.cos(4*theta));

        # круг
        plt.polar(theta, [1.4]*len(theta));


rgrid()
-------

.. py:function:: rgrid([radii, labels, angle=22.5])

    Используется для полярных систем :py:func:`polar`

    Настройка круговых линии

    Возвращает два занчения, линии окружности и их заголовки или соответственно задает

    * radii - растояние между радиальных окружностей сетки

    * labels - заголовки

    * angle - шаг отображения градусов

    .. code-block:: py

        # отображаем радиальные углы
        plt.rgrids(np.arange(0.2, 3.1, .7), angle=0)


savefig()
---------

.. py:function:: savefig(fname, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None, metadata=None)

    Сохраняет график в файл или любой другой записываемый объект,
    с параметрами по умолчанию

    * dpi - количество точек на дюйм
    * bbox_inches - отсечь пропуски

    .. code-block:: py

        savefig("some_plot.png", bbox_inches='tight')
        savefig(open("some_plot.png", 'w'))


scatter()
---------

.. py:function:: scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, plotnonfinite=False, data=None, **kwargs)

    Добавляет точки, маркеры на область рисования и возвращает коллекцию точек :py:class:`matplotlib.collections.PathCollection`

    * s - размер маркера, как для 1 значения так и для списка

    * c - цвет маркера, как для 1 значения так и для списка

    * marker - :py:class:`matplotlib.markers.MarkerStyle`

    * cmap - :py:class:`matplotlib.colors.Colormap`

    * norm - :py:class:`matplotlib.colors.Normalize`

    * kwargs - :py:class:`matplotlib.collections.Collection`

    .. code-block:: py

        scatter(1, 1, edgecolors='none', c='red', s=40)
        scatter(1, 1, edgecolors='none', c=(0, 0, 0.8), s=40)

        scatter([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], cmap=plt.cm.Blues)


semilogy()
----------

.. py:function:: semilogy()

    Логарифмическая диаграмма

    Аналогично :py:func:`plot`


setp()
------

.. py:function:: setp()

    Устаналивает свойства для объектов

    .. code-block:: py

        # задаем свойства для текстовых элементов
        setp(text, fontsize=16, color='green')

        # задает свойство для всех текстовых элементов ax элемента
        setp(ax.get_ticklabels(), fontsize=5.)


show()
------

.. py:function:: show()

    Отображает окно с графиком

    .. code-block:: py

        show()


subplot()
---------

.. py:function:: subplot(nrows, ncols, index, **kwargs)
.. py:function:: subplot(pos, **kwargs)
.. py:function:: subplot(ax)

    Добавляет subplot в текущую фигуру и возвращает :py:class:`matplotlib.axes.Axes`.

    При добавлении удаляет все существующие фигуры из области рисования, если такое поведение мешает, можно воспользоваться методом :py:meth:`matplotlib.figure.Figure.add_sublot` или :py:meth:`matplotlib.pyplot.axes`

    * label 

    * polar - (True | False)

    * projection - None, aitoff, hammer, lambert, mollweide, polar, rectilinear, :py:class:`matplotlib.projection`

    * sharex, sharey - :py:class:`matplotlib.axes.Axes`

    * kwargs - параметры из :py:class:`matplotlib.axes.Axes`


    .. code-block:: py

        plt.subplot(211)

        # без сетки
        plt.subplot(211, frameon=False)

        # круговая проекция

    .. code-block:: py

        # добавляем область рисования с сеткой, 2 ряда и 2 колонки
        # область рисования будет в первой ячейке
        ax1 = plt.subplot(2, 2, 1)
        # plt.subplot(221)
        # аналогично

        # добавляем область рисования во вторую ячейку, без границ
        ax2 = plt.subplot(222, frameon=False)

        # добавляем область в третью ячейку, с круговой проекцией
        plt.subplot(223, projection='polar')

        # добавляем обасть рисования, окрашеную в красный фоновый цвет
        plt.subplot(224, sharex=ax1, facecolor='red')

        # удаляем указанную область рисования
        plt.delaxes(ax2)

        # вновь добавляем указанную область рисования
        plt.subplot(ax2)

        plt.show()

    .. figure:: images/subplot_1.png


subplots()
----------

.. py:function:: subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True, subplot_tk=None, gridspec_kw=None, **kwargs)

    Возвращает кортеж:

        фигуру :py:class:`matplotlib.figure.Figure`, которая имеет несколько областей рисования

        область рисования :py:class:`matplotlib.axes.Axes`

    .. code-block:: py

        fig, ax = plt.subplots()

        fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2)

        fig, [ax1, ax2, ax3, ax4] = plt.subplots(1, 4)


suptitle()
----------

.. py:function:: suptitle()

    Возвращает :py:class:`matplotlib.text.Text`, аналогично :py:func:`matplotlib.axes.Axes.suptitle()`


text()
------

.. py:function:: text(x, y, text, **kwargs)

    Рисует указанный текст на указанной позиции и
    возвращает :py:class:`matplotlib.text.Text` (withdash=False) или
    :py:class:`matplotlib.text.TextWithDash` (withdash=True)

    * alpha - прозрачность

    * background - цвет фона шрифта

        * blue
        * r
        * #11aa55
        * (0.4, 0.5, 0.3)
        * 0.7

    * bbox - словарь, описание рамки вокруг текста

        * edgecolor - цвет рамки
        * facecolor - цвет заливки рамки
        * fill - булево, заливка
        * linestyle - стиль рамки
            * solid - обычная рамка
            * dashed - штрих-пунктир
            * dashdot - штрихпунктир
            * dotted - точечный
        * linewidth - толщина линии рамки
        * hatch - штриховка внутри рамки
            * "/"
            * "\"
            * "|"
            * "-"
            * "+"
            * "x"
            * "o"
            * "O"
            * "."
            * "*"
        * visible - булево, рамка видима
        * boxstyle - внешний вид рамки
            * square
            * sawtooth
            * roundtooth
            * rarrow
            * larrow
            * round64
            * round

    * color - цвет шрифта

        * blue
        * r
        * #11aa55
        * (0.4, 0.5, 0.3)
        * 0.7

    * family - семейство шрифта

        * sans-serif
        * serif
        * fantasy
        * monospace
        * verdana

    * fontdict - словарь, описывающий шрифт

        * family

    * rotation - поворот текста

        * horizontal
        * vertical
        * 45

    * size - размер шрифта

        * xx-small
        * x-small
        * small
        * medium
        * large
        * x-large
        * xx-large

    * style - стиль

        * normal
        * italic
        * oblique

    * weight - толщина шрифта

        * ultralight
        * light
        * normal
        * regular
        * book
        * medium
        * roman
        * semibold
        * demibold
        * demi
        * bold
        * heavy
        * bold
        * black
        * 200

    * withdash - :py:class:`bool`, текст с линией

    .. code-block:: py

        plt.text(0.1, -0.04, 'text', fontsize=26, bbox={'color': 'w'}, rotation=90)

        plt.text(
            0.5, 
            0.5, 
            'Text with borders', 
            fontsize=14,
            # выравнивание по вертикали и по горизонтали по центру
            horizontalalignment='center', 
            verticalalignment='center',
            bbox=dict(facecolor='pink', alpha=0.5)
        )


tick_params()
-------------

.. py:function:: tick_params(axis, which, labelsize)

    Оформление делений на осях

    .. code-block:: py

        tick_params(axis='both', which='major', labelsize=14)


thetagrid()
-----------

.. py:function:: thetagrid([angles, labels, frac])

    Используется для полярных систем :py:func:`polar`

    Настройка линии для углов

    .. code-block:: py

        # отображаем только углы от 45 до 360 с шагом 90
        thetagrids(range(45, 360, 90))


title()
-------

.. py:function:: title(label, fontsize)

    Устанавливает подпись для графика и возвращает :py:class:`matplotlib.text.Text`, аналогично :py:meth:`matplotlib.axes.Axes.set_title()`

    .. code-block:: py

        title("Plot", fontsize=24)


xkcd()
------

.. py:function:: xkcd(scale=1, length=100, randomness=2)

    Включает эффект рисования от руки

    Можно использовать как контекстный процессор

    .. code-block:: py

        with xkcd():
            pass


xlabel()
--------

.. py:function:: xlabel(label, fontsize)

    Устанавливает подпись для оси х и возвращает :py:class:`matplotlib.text.Text`, аналогично :py:meth:`matplotlib.axes.Axes.set_xlabel()`

    .. code-block:: py

        plt.xlabel('X axis', fontsize=24)


xlim()
------

.. py:function:: xlim([new_xlim])

    Аналогично :py:func:`matplotlib.pyplot.axis` возвращает или устанавливает
    предельные значения по оси х

    .. code-block:: py

        xlim()
        # (1.0, 4.0)

        xlim([0, 5])


xticks()
--------

.. py:function:: xticks([locations [, labels]])

    Возвращает или задает настройки для х оси

    .. code-block:: py

        locations, labels = xticks()

        # меняем символы на точках оси
        xticks(
            range(len(x)),
            ['a', 'b', 'c'])

        # отображаем только указанные точки
        xticks(range(len(1, 8, 2)))


yticks()
--------

.. py:function:: yticks([locations [, labels]])

    Возвращает или задает настройки для y оси

    Аналогично :py:func:`xticks`


ylabel()
--------

.. py:function:: ylabel(label, fontsize)

    Устанавливает подпись для оси y и возвращает :py:class:`matplotlib.text.Text`, аналогично :py:meth:`matplotlib.axes.Axes.set_ylabel()`

    .. code-block:: py

        plt.ylabel('Y axis', fontsize=24)


ylim()
------

.. py:function:: ylim([new_ylim])

    Аналогично :py:func:`matplotlib.pyplot.axis` возвращает или устанавливает
    предельные значения по оси y

    .. code-block:: py

        ylim()
        # (0.0, 12.0)

        ylim([-1, 13])
