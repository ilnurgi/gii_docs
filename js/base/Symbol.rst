Symbol - символ
===============

.. note:: ECMAScript6

.. code-block:: js

    // символы не видимы для циклов
    let s = Symbol('my_symbol');
    let o = {};
    o[s] = 's'
    Object.keys(o);
    // []

    o.s
    // error

    o[s]
    // 's'


.. code-block:: js

    Symbol('1') == Symbol('1')
    // false

    Symbol.for('1') == Symbol.for('1')
    // true



.. js:class:: Symbol()

    .. code-block:: js

        var s = Symbol();
        typeof s;
        // 'symbol'

    .. code-block:: js

        try {
            let s = new Symbol();
        } catch (e) {
            // Symbol is not a constructor
        }


    .. js:attribute:: hasInstance

    .. js:attribute:: isContcatSpreadable

    .. js:attribute:: iterator

        Символ для реализации интерфейса итератора

        .. code-block:: js

            class Users {
                constructor(users) {
                    this.users = users;
                }

                [Symbol.iterator]() {
                    let i = 0;
                    let users = this.users;
                    return {
                        next() {
                            if (i < users.length) {
                                return {
                                    done: false,
                                    value: users[i++],
                                };
                            }
                            return {
                                done: true,
                            }
                        }
                    }
                }
            }

            let users = Users([...])

            users_iterator = users[Symbol.iterator];
            users_iterator.next();

            for (let user of users) {
                ...
            }

            [...users]
            // [...]
            

    .. js:attribute:: match

    .. js:attribute:: replace

    .. js:attribute:: search

        Символ для реализации интерфейса поиска

        .. code-block:: js

            class Product {

                constructor(type) {
                    this.type = type;
                }

                [Symbol.search](string) {
                    return string.indexOf(this.type) >= 0 ? 'FOUND': 'NOT_FOUND'
                }

            }

            let pr = Product('soap');

            pr[Symbol.search]('barsoap');
            // FOUND

            'barsoap'.search(pr);
            // FOUND

            'shampoo'.search(pr);
            // NOT_FOUND


    .. js:attribute:: species

    .. js:attribute:: split

    .. js:attribute:: toPrimitive

    .. js:attribute:: toStringTag
    
    .. js:attribute:: unscopables

    .. py:function:: for(string)

        Создает символ глобально

        .. note:: ECMAScript6