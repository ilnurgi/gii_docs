.. title:: css box-sizing

.. meta::
    :description: 
        Описание каскадных стилей описания веб документов.
    :keywords: 
        css box-sizing

box-sizing
==========

Порядок измерения высоты и ширины элемента

context-box
-----------

Обычный порядок

.. code-block:: css
    
    box-sizing: context-box;
    
    width: 200px;
    height: 100px;
    background: red;
    padding: 20px;
    margin: 20px;

.. raw:: html

    <div style="width:200px;height:100px;background:red;padding:20px;box-sizing:context-box;margin:20px;">
        Text
    </div>


padding-box
-----------

Включить в расчет значение padding

.. code-block:: css
    
    box-sizing: padding-box;
    
    width: 200px;
    height: 100px;
    background: red;
    padding: 20px;
    margin: 20px;

.. raw:: html

    <div style="width:200px;height:100px;background:red;padding:20px;box-sizing:padding-box;margin:20px;">
        Text
    </div>


border-box
----------

Включить в расчет значение border

.. code-block:: css
    
    box-sizing: border-box;
    
    width: 200px;
    height: 100px;
    background: red;
    padding: 20px;
    margin: 20px;

.. raw:: html
    
    <div style="width:200px;height:100px;background:red;padding:20px;box-sizing:border-box;margin:20px;">
        Text
    </div>
