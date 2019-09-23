React
=====

Глобальный объект, доступен после подключения модуля

.. toctree::
    :maxdepth: 2

    Component


.. code-block:: js

    import React, { Component } from 'react'


cloneElement
------------

.. js:function:: cloneElement(react_elem, props)

    .. code-block:: js

        React.cloneElement(child, { item })

        
createElement
-------------

.. js:function:: createElement(tag, attributes, content)

    Создает и возвращает элемент документ

    .. code-block:: js

        const h2 = React.createElement("h2", {"class": "some-class"}, "Hello World")


.. code-block:: js

    const App = () => {
        return (
            <h2>Hello World</h2>
        )
    }


    const SomeComponent = (props) => {
        return (
            <SomeComponent1 />
            <SomeComponent2 />
            <div onClick={() => console.log(this, '${props.item}')}>
            </div>
            {props.books.map(book => <Book />)}
        )
    }
