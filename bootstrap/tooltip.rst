Подсказки
=========

* data-toggle="tooltip"
* data-placement="left/right/top/bottom"
* title="tooltip text"

.. code-block:: js

    $(function(){
        $('[data-toggle="tooltip"]').tooltip();
    });


Popover
=======

* data-toggle="popover"
* data-placement="left/right/top/bottom"
* title="popover text"

.. code-block:: js

    $(function(){
        $('[data-toggle="popover"]').popover();
    });


Collapse
========

* data-toggle="collapse"
* data-target="#ID"
* collapse, id задать для блока


Аккордеон
=========

* data-toggle="collapse"
* data-parent="#ID"
* href="#ID2"

Контент панели:

* id="ID2"
* class="panel-collapse collapse"
* in - для активной панели