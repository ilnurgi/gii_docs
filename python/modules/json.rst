.. title:: python json

.. meta::
    :description:
        Справочная информация по python модулю json.
    :keywords:
        python json


.. py::module:: json

json
====

Модуль для работы с JSON.


.. code-block:: py

    import json

    class ComplexEncoder(json.JSONEncoder):

        def default(self, z):
            if isinstance(z, complex):
                return (z.real, z.imag)
            else:
                super().default(self, z)

    json.dumps(2 + 5j, cls=ComplexEncoder)
    # '[2.0, 5.0]'

    encoder = ComplexEncoder()
    encoder.encode(3 + 6j)
    # '[3.0, 6.0]'


.. code-block:: py

    json.dumps({'date': date(1987, 1, 28)}, default=)