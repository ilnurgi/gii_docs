.. py:module:: jinja2

jinja2
======

.. code-block:: html

    <body>
        {{ content }}
        {% %} - statements
        {{ }} - expressions to print to the template output
        {# #} - comments which are not included in the template output
        # ## - line statements

        {% raw %}
        His name is {{ name }}
        {% endraw %}

        {% for person in persons -%}
            {{ person.name }} {{ person.age }}
        {% endfor %}

        Сумма {{ objects | sum(attribute='price') }}

        {% extends 'base.html' %}
        
        {% block content%}
    
        {% endblock %}
    </body>

Template
--------

.. py:class:: Template()

    Шиблонизатор

    .. code-block:: py

        from jinja2 import Template

        Template('Hello {{ name }}').render(name='ilnurgi')
        # Hello ilnurgi

        Template('{{ data | e}}).render(data='<a>Today is a sunny day</a>')
        # 


    .. py:method:: render(**kwargs)

        Рендеринг шаблона

        .. code-block:: py

            Template('Hello {{ name }}').render(name='ilnurgi')
            # Hello ilnurgi


FileSystemLoader
----------------

.. py:class:: FileSystemLoader(root)

    Загрузчик шаблонов из файла

    .. code-block:: py

        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)

        template = env.get_template('index.html')


Environment
-----------

.. py:class:: Environment(loader)

    Окружение/контекст для работы

    .. code-block:: py

        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)

        template = env.get_template('index.html')

    .. py:attribute:: trim_blocks
    .. py:attribute:: lstrip_blocks
    .. py:attribute:: rstrip_blocks

    .. py:method:: get_template(name)

        Возвращает :py:class:`Template`, шаблон из окружения
