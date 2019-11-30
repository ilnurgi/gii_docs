.. title:: python unittest mock

.. meta::
    :description:
        Справочная информация по python модулю unittest.mock

    :keywords:
        python unittest mock

.. py:module:: mock

mock
====

Mock()
------

.. py:class:: Mock(**kwargs)

    Простой мок класс

    * **return_value** - возвращаемое значение

    .. code-block:: py

        mock_obj = Mock()
        mock_obj_foo = mock_obj.foo

    .. py:class:: py

        class A:

            def get_x(self):
                return 100

            def get_y(self):
                return 100

            def compute(self):
                return self.get_x() + self_get_y()

        a = A()
        mock_obj2 = Mock()

        a.get_x = mock_obj2.get_x
        a.get_y = mock_obj2.get_y

        a.get_x.return_value = 200
        a.get_y.return_value = 200

        a.compute()
        # 400

        mock_obj2.mock_calls == [call.get_x(), call.get_y()]

    .. code-block:: py

        def side_effect(arg):
            return {
                'a': 1,
                'b': 2,
            }
        mock.side_effect = side_effect

        mock('a'), mock('b')
        # (1, 2)

    .. code-block:: py

        mock.side_effect = [5, 4, 3]

        mock(), mock()
        # (5, 4)

    .. code-block:: py

        # патчим input
        __builtins__.input = Mock(return_value=100)
        input()
        # 100

        # если какой-то модуль не доступен, мокаем и его
        import sys
        sys.modules['some_module'] = Mock()


    .. py:attribute:::: mock_calls

        Список, который хранит вызванные объекты

        .. code-block:: py

            mock_obj.mock_calls
            # []

            mock_obj_foo()

            mock_obj.mock_calls
            # [call.foo()]

    .. py:attribute:: return_value

        Атрибут хранит значение, которое вернет мок объект при уго вызове


MagicMock()
-----------

.. py:class:: MagicMock()

    Наследник :py:class:`Mock`,
    расширенный реализацией магических методово питона

    .. code-block:: py

        thing = Thing()
        thing.method = MagicMock(return_value=3)

        thin.method2 = MagicMock(side_effect=KeyError('foo')

    .. py:method:: assert_called_with()

        .. code-block:: py

            thing.method(3, 4, 5, key='value')
            # 3

            thing.assert_called_with(3, 4, 5, key='value')




patch()
-------

.. py:method:: patch(**kwargs)

    * target
    * new = DEFAULT
    * spec = None
    * create = False
    * spec_set = None
    * autospec = None
    * new_callable = None

    Возвращает новый патченный объект :py:class:`unittest.mock.MagicMock()`

    .. code-block:: py

        with patch('__main__.A.get_x', new=Mock(return_value=500)):
            pass


        with patch('__main__.A.get_x') as mock_A_get_x:
            mock_A_get_x.return_value = 400


        @patch('myapp.settings.SOME_VALUE', 99)
        def test():
            pass


        @patch('myapp.settings.some_method2')
        @patch('myapp.settings.some_method')
        def test(mock_some_method, mock_some_method2):
            mock_some_method.return_value = '123'
            mock_some_method.assert_called()
            mock_some_method.assert_called_once_with('foo')


        @patch('myapp.settings.Class.property', new_callable=PropertyMock)
        def test(mock_property):
            mock_property.return_value = '123'
