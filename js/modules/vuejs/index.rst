vuejs
=====

Mustache

.. code-block:: html

    <-- отображаем данные в элементе -->
    <div id='todos' data-title='{{title}}'></div>

.. code-block:: text

    <-- отображаем элементы из списка -->
    <ul>
        <li v-repeat='tasks'>{{title}}</li>
        <-- внутри цикла достцпны перменные $index, $key, $value -->
    </ul>
    <ul>
        <li v-repeat='task: tasks'>{{title}}</li>
        <-- внутри цикла достцпны перменные $index, $key, $value -->
        <span v-show='task != editTask' v-on='dblclick: editTask = task' v-class='text-primary : task.done'>{{ task.title }}</span>
        <input v-show='task == editTask' type='text' v-model='editTask.title' v-on='keyup: editTask = null | key "enter"'>
    </ul>

.. code-block:: text

    <-- обработка формы -->
    <form v-on='submit: addTask'>
        <input lazy v-model='newTask'>
        <-- lazy - данные попадут в модель после события change -->

        <span v-on='click: removeTask($index)'>
    </form>

    <-- фильтр, выводим значение переменной в json формате -->
    <pre>
        {{ $data | json }}
    </pre>

.. code-block:: js

    var Todos = Vue.extend({
        name: 'todos'
    });

    var vm = new Todos({
        el: '#todos', // элемент внутри которого работаем
        data: {
            title: 'todos'
        },
        ready: function(){
            console.log('viewmodel ready!');
        }
    });

    var vm2 = new Todos({

        // элемент внутри которого работаем, селектор или сам элемент
        el: '#todos',

        // данные вьюхи
        data: {
            tasks: [
                {
                    title: '1',
                    done: true
                }, {
                    title: '2',
                    done: false
                }
            ],
            newTask: '',
            editTask: ''
        },
        // фильтры
        filters: {
            openTasks: function(){
                return this.tasks.filter(function(item){
                    return item.done;
                });
            }
        },
        // методы
        methods: {
            addTask: function(event){
                // обработчик сабмита формы

                e.preventDefault();
                console.log('Task added');
                this.tasks.push({title: this.newTask, done: false})
                this.newTask = '
            },
            removeTask: function(index){
                this.tasks.$remove(index);
            }
        }
        ready: function(){
            console.log('viewmodel ready!');
        }
    });

    // познеесвязывание представления с вьюмоделью
    vm.$mount('todos');

    // изменение данных в ВМ
    vm.$data.title = '123'

    // добавление данных в ВМ
    vm.$data.$add('title', 'NewTitle);

Директивы
=========

* v-text - текстовое содержимое элемента, textContent

    .. code-block:: html

        <span v-text='variable'></span>

* v-html - innerHTML

    .. code-block:: html

        <span v-html='html'></span>

* v-attr - attributes

    .. code-block:: html

        <img v-attr="width: '100px', height: '100px'"/>

* v-class - добавляет классы

    .. code-block:: html

        <span v-class="red: true"></span>

* v-style - css-style

    .. code-block:: html

        <span v-style="css.string, css.object">

* v-show, v-if - display

    .. code-block:: html

        <span v-show="true">
        <span v-if="false">

* v-on - добавляет обработчик событий

    .. code-block:: html

        <span v-on="click: callback, blur: red = !red">
        <form v-on="submit: callback($event)">
        <textarea v-on="keyup: callback($event) | key 13"> // enter
        <textarea v-on="keyup: callback($event) | key 'enter'"> // enter

* v-el - задает идентификатор элементу

    .. code-block:: html

        <textarea v-el="comment" v-on="submit: callback($event)">
        <script>
            callback: function(event){
                this.$$.comment.value;
            }
        </script>

* v-pre - элемент не используется для дата биндинга

* v-repeat - цикл, track-by - ключ, идентификатор, для того чтобы не перерисовывать объект

* v-model- lazy, debounce - таймер для синхронизации, number - преобразовать к числу если возможно

.. code-block:: html

    <script>
        Vue.directive('test', {
            bind: function(){
                // привязываем элемент к директиве

            },
            unbind: function(){
                // удаляем директиву из элемента
            },
            update: function(newValue, oldValue){
                // значение будет изменено
            }
        })
        Vue.directive('test', function(){
                // удаляем директиву из элемента
            }
        })
    </script>
    
    <span v-test=''/>

.. code-block:: html

    <script>
        Vue.elementDirective('like', {
            bind: function(){
            },

        });
    </script>
    <like/>


Фильтры
=======

.. code-block:: js

    Vue.filter('filter-name', {
        read: function(value){
        },
        write: function(newValue, oldValue){
        }
    })
    Vue.filter('filter-name', function(value, ends){
        },
    })

- json
- capitalize
- uppercase
- lowercase
- currence 'RUB'
- pluralize 'item'
- pluralize 'ый' 'ой'
- filterBy 't' - поиск во всех свойствах
- filterBy 't' in 'title' - поиск в указанных свойствах
- orderBy 'id' true


Вычисляемые поля
================

.. code-block:: js

    var vm = new Vue({
        el: '#container',
        data: {},
        computed: {
            full_name: {
                get: function(){},
                set: function(value){},
            },
            initials: function(){
                // сеттер нам не нужен
            },

        }
    });
