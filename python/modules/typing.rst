.. title:: python typing

.. meta::
    :description: 
        Справочная информация по python модулю typing.
    :keywords: 
        python typing

.. py:module:: typing

typing
======

final()
-------

.. py:function:: final()

    .. versionadded:: 3.8

    .. code-block:: py

        # от этого класса нельзя наследоваться
        @final
        class SomeClass:
            pass

    .. code-block:: py

        # нельзя переопределять метод
        class SomeClass:

            @final
            def foo(self):
                pass


Final()
-------

.. py:class:: Final()

    .. code-block:: py

        # переменную нельзя переприсвоить
        ID: FINAL[float] = 1
        ID = 2  # error: Cannot assign to final name "ID"

        STR: Final = 'final'
        STR = "oops"  # error: Cannot assign to final name "STR"

        letters: Final = []
        letters.append('c')  # ok

        class ImmutablePoint:
            x: Final[int]
            y: Final[int]  # error: Final name must be initialized with a value

            def __init__(self) -> None:
                self.x = 1  # ok

        ImmutablePoint().x = 2 # error: Cannot assign to final attribute "x"


Iterable()
----------

.. py:class:: Iterable()


Literal()
---------

.. py:class:: Literal()

    .. code-block:: py

        def give_me_four(x: Literal[4]):
            pass

        give_me_four(4)  
        # ok
        
        give_me_four(4.0) 
        # error: Argument 1 to "give_me_four" has incompatible type "float"; expected "Literal[4]"
        
        give_me_four(42)  
        # error: Argument 1 to "give_me_four" has incompatible type "Literal[42]"; expected "Literal[4]"



Protocol()
----------

.. py:class:: Protocol()

    .. versionadded:: 3.8

    Протокол

    .. code-block:: py

        from abc import abstractmethod
        from typing import Protocol, Iterable


        class SupportsRoar(Protocol):
            @abstractmethod
            def roar(self) -> None:
                raise NotImplementedError

        class Lion(SupportsRoar):
            def roar(self) -> None:
                print("roar")

        class Cat:
            def meow(self) -> None:
                print("meow")

        def roar_all(bigcats: Iterable[SupportsRoar]) -> None:
            for t in bigcats:
                t.roar()

        roar_all([Lion(), Tiger()])  # ok
        
        roar_all([Cat()])  
        # error: List item 0 has incompatible type "Cat"; expected "SupportsRoar"


TypedDict()
-----------

.. py:class:: TypedDict()

    .. versionadded:: 3.8

    .. code-block:: py

        class Book(TypedDict):
            title: str
            author: str

        Book = TypedDict(
            'Book', 
            {
                'title': str,
                'author': str,
            }
        )

        book: Book = {
            'title': 'title',
            'author': 'author'
        }

        book: Book = {
            'title': 'title',
            'artist': 'artist'
        }
        # error: Extra key 'artist' for TypedDict "Book"

        book: Book = {
            'title': 'Fareneheit 481'
        }  
        # error: Key 'author' missing for TypedDict "Book"

    .. code-block:: py

        # total=False - не обязательное заполнение всех полей
        class Book(TypedDict, total=False):
            title: str
            artist: str

        book: Book = {
            'title': 'Fareneheit 481'
        }  
        # ok