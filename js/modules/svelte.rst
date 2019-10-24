.. title:: js svelte

.. meta::
    :description:
        Описание js модуля svelte.
    :keywords:
        js svelte

svelte
======

.. code-block:: html

    <style>
        button {
            border-radius: 0;
            background-color: aqua;
        }
        :global(.noscroll) {
            overflow: hidden;
        }
    </style>

    <button>
        <slot/>
    </button>


.. code-block:: html

    <script>
        export let big = false;
        export let ghost = false;
    </script>

    <style>
        .big {
            font-size: 20px;
            display: block;
            width: 100%;
        }

        .ghost {
            background-color: transparent;
            border: solid currentColor 2px;
        }
    </style>

    <button class:big class:ghost>
        <slot/>
    </button>

    <!-- использование -->

    <Button big ghost>Click Me</Button>


.. code-block:: html

    <script>
        export let primary = false;
        export let secondary = false;
    </script>

    <button
        class:c-btn--primary={primary}
        class:c-btn--secondary={secondary}
        class="c-btn">
        <slot></slot>
    </button>

    <!--
        использование
        итоговый html будет выглядеть следующим образом
        <button class="c-btn c-btn--primary">Click Me</button>
    -->
    <Button primary>Click Me</Button>


.. code-block:: html

    <script>
        let class_name = '';
        export { class_name as class };
    </script>

    <button class="c-btn {class_name}">
        <slot />
    </button>

    <!-- использование -->
    <Button class="mt40">Click Me</Button>


.. code-block:: html

    <script>
        export let cols = 4;
    </script>

    <style>
        ul {
            display: grid;
            width: 100%;
            grid-column-gap: 16px;
            grid-row-gap: 16px;
            grid-template-columns: repeat({cols}, 1fr);
        }
    </style>

    <ul>
        <slot />
    </ul>

.. code-block:: html

    <script>
        export let cols = 4;
    </script>

    <style>
        ul {
            display: grid;
            width: 100%;
            grid-column-gap: 16px;
            grid-row-gap: 16px;
            grid-template-columns: repeat(var(--columns), 1fr);
        }
    </style>

    <ul style="--columns:{cols}">
        <slot />
    </ul>