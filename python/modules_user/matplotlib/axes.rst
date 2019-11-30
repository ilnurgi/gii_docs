.. py:module:: matplotlib.axes

.. title:: matplotlib.axes

.. meta::
    :description lang=ru: описание модуля matplotlib.axes, языка программирования python
    :description lang=en: python matplotlib.axes module description
    :keywords lang=ru: python matplotlib axes
    :keywords lang=en: python matplotlib axes

axes
====

Axes()
------

.. py:class:: Axes()

    Область рисования

    .. py:method:: annotate()

        Аналог :py:func:`matplotlib.pyplot.annotate()`


    .. py:method:: get_xticklabels()

        Возвращает список :py:class:`matplotlib.text.Text`, текстовые элементы объекта


    .. py:method:: plot()

        Аналог :py:func:`matplotlib.pyplot.plot`


    .. py:method:: set_title(label, fontdict=None, loc='center', pad=None, **kwargs)

        Устанавливает заголовок для области рисования и возвращает :py:class:`matplotlib.text.Text`, аналогично :py:func:`matplotlib.pyplot.title`

        * label - заголовок окна

        * fontdict - настройка шрифта

            .. code-block:: py

                {
                    'fontsize': rcParams['axes.titlesize'],
                    'fontweight' : rcParams['axes.titleweight'],
                    'verticalalignment': 'baseline',
                    'horizontalalignment': loc,
                }

        * loc - center, left, right

        * pad - величина отступа

        * kwargs - доп.параметры :py:class:`matplotlib.text.Text`

        .. code-block:: py

            ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

            ax.set_title('Voltage vs. time chart', color='0.7')

        .. code-block:: py

            from matplotlib import font_manager as fm, rcParams
            
            ax.set_title(
                'Using a ttf font file in Matplotlib', 
                fontproperties=fm.FontProperties(
                    fname=os.path.join(rcParams["datapath"], "fonts/ttf/cmr10.ttf")
                ),
            )


    .. py:method:: set_xlabel(label)

        Аналог :py:func:`matplotlib.pyplot.xlabel`


    .. py:method:: set_ylabel(label)

        Аналог :py:func:`matplotlib.pyplot.ylabel`


    .. py:method:: set_xlim((max, min))

        Задает макисмальные и маинимальные знаяения для оси


    .. py:method:: set_ylim((max, min))

        Задает макисмальные и маинимальные знаяения для оси


    .. py:method:: suptitle()

        Аналог :py:func:`matplotlib.pyplot.suptitle()`


    .. py:method:: text()

        Аналог :py:func:`matplotlib.pyplot.text`


    .. py:method:: twinx()

        Добавляет новую ось координат и возвращает объект для рисования


    .. py:method:: twiny()

        Добавляет новую ось координат и возвращает объект для рисования

