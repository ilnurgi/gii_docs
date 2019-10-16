.. title:: html datalist

.. meta::
    :description: 
        Описание html элемента datalist
    :keywords: 
        html datalist,
        datalist

datalist
========

Содержит определнные опции для элементов input_.

.. code-block:: html

    <input
        id="animals"
        type="text"
        placeholder="animals and sounds"
        list="animalnames"
        name="animals"
        required />

    <datalist id="animalnames">
        <option value="quack">duck</option>
        <option value="banana slug" label="sssss"/>
        <option value="sheep" label="bah"/>
        <option value="horse" label="neigh"/>
    </datalist>