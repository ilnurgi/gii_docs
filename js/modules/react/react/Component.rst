Component
=========

.. js:class:: Component

    React компонент

    .. code-block:: js

        import React, { Component } from 'react'

        export default SomeComponent extends Component {

            render(){
                return <h1>Hello World</h1>
            }

        }

    .. js:function:: componentDidCatche()
    
    .. js:function:: componentDidMount()

        Вызывается когда компонент уже подключен на страницу и все элементы настроены

        constructor() => render() => componentDidMount()


    .. js:function:: componentDidUpdate(prevProps, prevState)

        Вызывается после того как компонент обновился

        render() => componentDidUpdate()


    .. js:function:: componentWillUnmount()


    .. js:function:: render()

        Должен возвращать разметку для компонента
