.. title:: js svelte

.. meta::
    :description:
        Описание js модуля svelte.
    :keywords:
        js svelte

svelte
======

https://svelte.dev/

.. code-block:: html

    <!-- App.svelte -->

    <style>
    </style>

    <script>
        import Form from './Form.svelte';
        import {scale} from 'svelte/transition';

        let name = "ilnurgi";
        let items = [];
        const remove = item => {
            items = items.filter(i => i !== item);
        }
        const addItem = () => {
            items = [
                ...items,
                {}
            ]
        }
        // если tasks изменился, message тоже изменится
        $: countTaskMessage = `${tasks.length}`;
        $: console.log(tasks.length);
        function addTask(e){
            tasks = [...tasks, e.detail]
        }
    </script>

    <Form 
        bind:task="{task}"
        on:add="{addTask}"
    >Slot title</Form>

    <!-- короткая форма -->
    <!-- <Form bind:task></Form>-->

    <!-- будет использоваться значение по умолчанию -->
    <!-- <Form></Form>-->

    <!-- quote - Promis -->
    {#await quote}
        loading...
    {:then value}
        {@html value}
    {:catch}
        Error
    {/await}
    <!-- <Form></Form>-->

    <!-- quote - Promis -->
    <!-- краткая форма -->
    {#await quote then value}
        {@html value}
    {/await}

    <button on:click="{() => isVisible = !isVisible }">Toggle</button>
    <div transition:scale="{{duration: 500}}">
        <Quote></Quote>
    </div>
    <button on:click="{() => isVisible = !isVisible }">Toggle</button>
    <div in:scale="{{duration: 500}}" out:fly="{{duration:500, y: 50}}">
        <Quote></Quote>
    </div>

.. code-block:: html

    <!-- Form.selte -->
    <script>
        import {createEventDispatcher} from 'selte';

        export let task = 'Test';
        let dispatch = createEventDispatcher();

        function addTask(){
            dispatch('add', task);
        }

    </script>

    <form on:submit|preventDefault={addItem}>
        <input bind:value={name}>
        <button on:click="{addTask}">+</button>
    </form>
    <h1>Hello {name}!</h1>
    <ul>
        {#each items as item}
            <li class={item.done ? 'done' : ''}>
                <input type="checkbox" bind:checked={item.done} />
                {item.name}
                <button on:click={() => remove(item)}>X</button>
            </li>
            // <li class:done={item.done}><{item.name}/li>
            {:else}
            <li>empty list</li>            
        {/each}
    </ul>
    <slot>Default slot title</slot>

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

    {#if time < 10}
        <p>Good morning</p>
    {:else if time < 20}
        <p>Good day</p>
    {:else}
        <p>Good evening</p>
    {/if}

.. code-block:: js

    <script>
        import {onMount} from 'svelte'

        onMount(() => {})
    </script>

    // onMount, beforeUpdate, afterUpdate, onDestroy, tick