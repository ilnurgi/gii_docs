.. py:module:: matplotlib.figure

.. title:: matplotlib.figure

.. meta::
    :description lang=ru: описание модуля matplotlib.figure, языка программирования python
    :description lang=en: python matplotlib.figure module description
    :keywords lang=ru: python matplotlib figure
    :keywords lang=en: python matplotlib figure

figure
======

Figure()
--------

.. py:class:: Figure(figzie=None, dpi=None, facecolor=None, edgecolor=None, linewidth=0.0, frameon=None, subplotpars=None, tight_layout=None, constrained_layout=None)

    Фигура, которая может иметь несколько областей рисования :py:class::`matplotlib.axes.Axes`

    * figsize - кортеж размера фигуры, по умолчанию задано в
      :py:attr:`matplotlib.rcParams` -> figure.figsize и равно [6.4, 4.8], т.е. 640х480 пикселей

    * dpi - количесвто точек на дюйм, по умолчанию задано в
      :py:attr:`matplotlib.rcParams` -> figure.dpi, по умолчанию 100.0

    * facecolor - цвет фона фигуры, по умолчанию задано в
      :py:attr:`matplotlib.rcParams` -> figure.facecolor, white

    * edgecolor - цвет границ фигуры, по умолчанию задано в
      :py:attr:`matplotlib.rcParams` -> figure.edgecolor, white

    * linewidth - ширина линии фигуры

    * frameon - отрисовка сетки

    * subplotpars - настройки для subplot, :py:class:`SubplotParams()`

    * tight_layout - по умолчанию задано в
      :py:attr:`matplotlib.rcParams` -> figure.autolayout

    .. code-block:: py

        fig = matplotlib.pyplot.figure()

    .. py:attribute:: axes

        Список текущих областей рисования

        .. code-block:: py

            fig = plt.figure()

            print(fig.axes())
            # []



    .. py:method:: add_artist(artist, clip=False)

        * artist - :py:class:`matplotlib.artist.Artist`

        Добавляет артиста и возвращает его.


    .. py:method:: add_axes(rect, projection=None, polar=False, **kwargs)
    .. py:method:: add_axes(ax)

        Добавляет область рисования в фигуру и возвращает её :py:class:`matplotlib.axes.Axes`

        * rect - [left, bottom, width, height] для новой области

        * projection - None, aitoff, hammer, lambert, mollweide, polar, rectilinear, :py:class:`matplotlib.projection`

        * polar - круговая диаграмма, projection='polar'

        * sharex, sharey - :py:class:`matplotlib.axes.Axes`

        * label - заголовок области рисования

        * kwargs - остальные параметры из :py:class:`matplotlib.axes.Axes`

        .. code-block:: py

            fig.add_axes((l, b, h, w), label='label', projection='polar')

            fig.add_axes((l, b, h, w), frameon=False, facecolor='g')
            
            ax = fig.add_axes((l, b, h, w), polar=True)


    .. py:method:: add_axobserver(func)

        Устанавливает обработчик для изменения состояния области

        .. code-block:: py

            def notify_axes_change(fig):
                """"""

            fig.add_axobserver(notify_axes_change)


    .. py:method:: add_subplot(numrows, numcols, fignum)

        Добавляет объект для рисования графика по укзанным координатам

        Вовзвращает :py:class:`matplotlib.axes.Axes`, объект для рисования графиков.

        .. code-block:: py

            ax = fig.add_subplot(111)
            ax1 = fig.add_subplot(1, 1, 1)
            ax2 = fig.add_subplot(1, 1, 1, axisbg='r', projection='polar')


    .. py:method:: text()

        Аналог :py:func:`matplotlib.pyplot.figtext`


    .. py:method:: suptitle()

        Аналог :py:func:`matplotlib.pyplot.suptitle`


SubplotParams()
---------------

.. py:class:: SubplotParams(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)

    Настройки для subplot

    .. py:method:: update(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)

        Обновляет параметры
