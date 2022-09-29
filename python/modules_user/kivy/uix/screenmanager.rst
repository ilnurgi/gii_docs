.. py:module:: kivy.uix.screenmanager

screenmanager
=============

Screen()
--------

.. py:class:: Screen()


ScreenManager()
---------------

.. py:class:: ScreenManager()

	.. code-block:: py

		screen_manager = ScreenManager()

		screen_main = Screen(name='MainScreen')
		screen_info = Screen(name='InfoScreen')

		screen_manager.add_widget(screen_main)

		screen_manager.current = screen_main.name
		screen_manager.transition.direction = 'left'

		screen_manager.current = screen_info.name
		
	.. py:attribute:: transition

		* :py:class:`kivy.uix.screenmanager.CardTransition`
		* :py:class:`kivy.uix.screenmanager.FallOutTransition`
		* :py:class:`kivy.uix.screenmanager.FadeTransition`
		* :py:class:`kivy.uix.screenmanager.NoTransition`
		* :py:class:`kivy.uix.screenmanager.RiseInTransition`
		* :py:class:`kivy.uix.screenmanager.SlideTransition`
		* :py:class:`kivy.uix.screenmanager.SwapTransition`
		* :py:class:`kivy.uix.screenmanager.WipeTransition`


CardTransition()
----------------

.. py:class:: CardTransition()

	:py:class:`kivy.uix.screenmanager.SlideTransition`

	.. py:attribute:: mode

		* push
		* pop


FadeTransition()
----------------

.. py:class:: FadeTransition()

	:py:class:`kivy.uix.screenmanager.ShaderTransition`


FallOutTransition()
-------------------

.. py:class:: FallOutTransition()

	:py:class:`kivy.uix.screenmanager.ShaderTransition`

	.. py:attribute:: duration


NoTransition()
--------------

.. py:class:: NoTransition()

	:py:class:`kivy.uix.screenmanager.TransitionBase`


RiseInTransition()
------------------

.. py:class:: RiseInTransition()

	:py:class:`kivy.uix.screenmanager.ShaderTransition`

	.. py:attribute:: duration


Screen()
--------

.. py:class:: Screen(**kwargs)

	:py:class:`kivy.uix.relativelayout.RelativeLayout`

	.. py:attribute:: manager

		Ссылка на менеджер окон, в котором зарегистрировано окно

		:py:class:`kivy.uix.screenmanager.ScreenManager`


	.. py:attribute:: name

		наименование окно


	.. py:attribute:: transition_progress
	.. py:attribute:: transition_state

	.. py:method:: on_pre_enter()
	.. py:method:: on_enter()
	.. py:method:: on_pre_leave()
	.. py:method:: on_leave()


ScreenManager()
---------------

.. py:class:: ScreenManager(**kwargs)

	:py:class:`kyvy.uix.floatlayout.FloatLayout`


	.. py:attribute:: current

		название текущего скрина, который отображаем на экране

	.. py:method:: add_widget(screen)

	.. py:method:: clear_widgets(screens=None)


.. warning:: дополнить