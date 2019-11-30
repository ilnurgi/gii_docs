.. title:: css clip-path

.. meta::
    :description: 
        Описание стиля формы объектов
    :keywords: 
        css clip-path

clip-path
=========

circle
------

.. code-block:: css

    clip-path: circle();

.. raw:: html
    
    <div style="width:100px;height:100px;border:1px solid black;">
        <div style="width:100px;height:100px;background:red;clip-path:circle();"></div>
    </div>

.. code-block:: css

    clip-path: circle(25%);

.. raw:: html

    <div style="width:100px;height:100px;border:1px solid black;">
        <div style="width:100px;height:100px;background:red;clip-path:circle(25%);"></div>
    </div>

.. code-block:: css

    clip-path: circle(50% at 0 50%);

.. raw:: html

    <div style="width:100px;height:100px;border:1px solid black;">
        <div style="width:100px;height:100px;background:red;clip-path:circle(50% at 0 50%);"></div>
    </div>


ellipse
-------

.. code-block:: css

    clip-path: ellipse();

.. raw:: html

    <div style="width:300px;height:100px;border:1px solid black;">
        <div style="width:300px;height:100px;background:red;clip-path:ellipse();"></div>
    </div>

.. code-block:: css

    clip-path: ellipse(150px 50px);

.. raw:: html

    <div style="width:300px;height:100px;border:1px solid black;">
        <div style="width:300px;height:100px;background:red;clip-path:ellipse(150px 50px);"></div>
    </div>

.. code-block:: css

    clip-path: ellipse(farthest-side closest-side at 25% 25%);

.. raw:: html

    <div style="width:100px;height:100px;border:1px solid black;">
        <div style="width:100px;height:100px;background:red;clip-path:ellipse(farthest-side closest-side at 25% 25%);"></div>
    </div>

.. code-block:: css

    clip-path: ellipse(farthest-side closest-side at 25% 25%);

.. raw:: html

    <div style="width:100px;height:100px;border:1px solid black;">
        <div style="width:100px;height:100px;background:red;clip-path:ellipse(farthest-side closest-side at 25% 25%);"></div>
    </div>


inset
-----

.. code-block:: css

    clip-path: inset();

.. raw:: html

    <div style="width:100px;height:100px;border:1px solid black;">
        <div style="width:100px;height:100px;background:red;clip-path:inset();"></div>
    </div>

.. code-block:: css

    clip-path: inset(40px);

.. raw:: html
    
    <div style="width:100px;height:100px;border:1px solid black;">
        <div style="width:100px;height:100px;background:red;clip-path:inset(40px);"></div>
    </div>

.. code-block:: css

    clip-path: inset(10px round 10px);

.. raw:: html
    
    <div style="width:100px;height:100px;border:1px solid black;">
        <div style="width:100px;height:100px;background:red;clip-path:inset(10px round 10px);"></div>
    </div>


polygon
-------

.. code-block:: css

    clip-path: polygon(0 0, 0 50px, 95px 95px);

.. raw:: html
    
    <div style="width:100px;height:100px;border:1px solid black;">
        <div style="width:100px;height:100px;background:red;clip-path:polygon(0 0, 0 50px, 95px 95px);"></div>
    </div>