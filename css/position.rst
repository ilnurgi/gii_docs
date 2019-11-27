.. title:: css position

.. meta::
    :description:
        Описание css стиля position
    :keywords:
        css position

position
========

Позиционирование элементов

.. raw:: html

    <div style="background-color:#aff1b6; width:30px; padding:5px; box-sizing:border-box;">
        <div style="background-color:#ffcca5; width:20px; height:20px;">1</div>
        <div style="background-color:#9cdbff; width:20px; height:20px;">2</div>
        <div style="background-color:#e1e8fa; width:20px; height:20px;">3</div>
    </div>

* **absolute**

    Элемент исключается из потока документа.

    Позиционируется относительно всего документа,
    если заданы смещения top, left, ...

    Если не заданы смещения top, left, ... то остается на своем месте.

    При скроле документа будет уходить из области видимости.

    .. code-block:: css

        .absolute-lt {
            position: absolute;
            top: 150px;
            left: 100px;
        }
        .absolute {
            position: absolute;
        }

    .. raw:: html

        <div style="background-color:#aff1b6; width:30px; padding:5px; box-sizing:border-box;">
            <div style="background-color:#ffcca5; width:20px; height:20px; position:absolute;">absolute</div>
            <div style="background-color:#9cdbff; height:20px; position:absolute; left:100px; top:150px;">absolute-lt</div>
            <div style="background-color:#e1e8fa; height:20px; width:20px; top:20px;"></div>
        </div>

* **fixed**

    Элемент исключается из потока документа.

    Позиционируется относительно всего документа,
    если заданы смещения top, left, ...

    Если не заданы смещения top, left, ... то пропадает из области видимости.

    При скроле документа будет оставаться на месте относительно окна просмотра.

    .. code-block:: css

        .fixed-lt {
            position: fixed;
            top: 170px;
            left: 100px;
        }
        .fixed {
            position: fixed;
        }

    .. raw:: html

        <div style="background-color:#aff1b6; width:100px; padding:5px; box-sizing:border-box;">
            <div style="background-color:#ffcca5; height:20px; position:fixed;">fixed</div>
            <div style="background-color:#9cdbff; height:20px; position:fixed; left: 100px; top:170px;">fixed-lt</div>
            <div style="background-color:#e1e8fa; height:20px;"></div>
        </div>

* **relative**

    Элемент НЕ исключается из потока документа,
    т.е. его место остается пустым.

    Позиционируется относительно своего родителя,
    если заданы смещения top, left, ...

    Если не заданы смещения top, left, ... то остается на месте.

    При скроле документа будет оставаться на месте относительно окна просмотра.

    .. code-block:: css

        .relative-lt {
            position: relative;
            left: 20px;
        }
        .relative {
            position: relative;
        }

    .. raw:: html

        <div style="background-color:#aff1b6; width:100px; padding:5px; box-sizing:border-box;">
            <div style="background-color:#ffcca5; height:20px; position:relative;">relative</div>
            <div style="background-color:#9cdbff; height:20px; position:relative; left: 20px;">relative-lt</div>
            <div style="background-color:#e1e8fa; height:20px;"></div>
        </div>

* **static** - по умолчанию, нормальный поток документов

* **sticky** - закрепленное, комбинация относительного и фиксированного

    .. code-block:: css

        .sticky-lt {
            position: sticky;
            left: 20px;
        }
        .sticky {
            position: sticky;
        }

    .. raw:: html

        <div style="background-color:#aff1b6; width:100px; padding:5px; box-sizing:border-box;">
            <div style="background-color:#ffcca5; height:20px; position:sticky;">sticky</div>
            <div style="background-color:#9cdbff; height:20px; position:sticky; left: 20px;">sticky-lt</div>
            <div style="background-color:#e1e8fa; height:20px;"></div>
        </div>
