.. title:: python typing

.. meta::
    :description: 
        Справочная информация по python модулю typing.
    :keywords: 
        python typing

.. py:module:: typing

typing
======

.. versionadded:: 3.5

TYPE_CHECKING
-------------

.. py:attribute:: TYPE_CHECKING

    Булево, в runtime'е будет False
    

cast()
------

.. py:function:: cast()


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


get_args()
----------

.. py:function:: get_args()

    .. code-block:: py

        get_origin(Dict[str, int]) is dict
        get_args(Dict[int, str]) == (int, str)

        get_origin(Union[int, str]) is Union
        get_args(Union[int, str]) == (int, str)


get_origin()
------------

.. py:function:: get_origin(tp)


get_type_hints()
----------------

.. py:function:: get_type_hints(obj, globals, locals)


no_type_check()
---------------

.. py:function:: no_type_check()


no_type_check_decorator()
-------------------------

.. py:function:: no_type_check_decorator()


overload()
----------

.. py:function:: overload()

    .. code-block:: py

        @overload
        def process(response: None) -> None: ...

        @overload
        def process(response: int) -> Tuple[int, str]: ...
        
        @overload
        def process(response: bytes) -> str: ...
        
        def process(response):
            # implementation    


runtime_checkable()
-------------------

.. py:function:: runtime_checkable()

    .. versionadded:: 3.8

        .. code-block:: py

            @runtime_checkable
            class Closable(Protocol):
                
                def close(self):
                    pass

            assert isinstance(open(path), Closable)


type_check_only()
-----------------

.. py:function:: type_check_only()

    .. code-block:: py
    
        @type_check_only
        class Response: 
            pass

        def fetch() -> Response:
            pass



AbstractSet()
-------------

.. py:class:: AbstractSet(Sized, Collection)

    Generic версия :py:class:`collections.abc.Set`


Any()
-----

.. py:class:: Any()

    .. code-block:: py

        def func(item: Any):
            pass


AnyStr()
--------

.. py:class:: AnyStr()

    .. code-block:: py

        AnyStr == TypeVar('AnyStr', str, bytes)
    

AsyncContextManager()
---------------------

.. py:class:: AsyncContextManager(Generic[T_co])

    Generic версия :py:class:`collections.AbstractAsyncContextManager`


AsyncGenerator()
----------------

.. py:class:: AsyncGenerator(AsyncIterator[T_co], Generic[T_co, T_contra])

    .. code-block:: py

        # AsyncGenerator[YieldType, SendType]

        async def func() -> AsyncGenerator[int, float]:

            sent = yield =0
            while sent >= 0.0:
                rounded = await round(sent)
                sent = yield rounded


AsyncIterable()
---------------

.. py:class:: AsyncIterable(Generic[_coT])

    .. versionadded:: 3.5.2

    Generic версия :py:class:`collections.abc.AsyncIterable`


AsyncIterator()
---------------

.. py:class:: AsyncIterator(AsyncIterable[T])

    Generic версия :py:class:`collections.abc.AsyncIterator`


Awaitable()
-----------

.. py:class:: Awaitable(Generic[T_co])

    .. versionadded:: 3.5.2

    Generic версия :py:class:`collections.abc.Awaitable`


BinaryIO()
----------

.. py:class:: BinaryIO()


ByteString()
------------

.. py:class:: ByteString(Sequence[T])

    Generic версия :py:class:`collections.abc.ByteString`


Callable()
----------

.. py:class:: Callable([ArgTypes, ...], ReturnValue)

    .. code-block:: py

        def func(get_next_item: Callable[[], str]):
            pass

    
ChainMap()
----------

.. py:class:: ChainMap(collections.ChainMap, MutableMapping[KT, VT])

    Generic версия :py:class:`collections.ChainMap`


ClassVar()
----------

.. py:class:: ClassVar()

    .. code-block:: py
    
        class Starship:
            stats: ClassVar[Dict[str, int]] = {}

        ship = Starship()

        ship.stats = {}
        # Error, setting class variable on instance

        Starship.stats = {}     
        # ok


Collection()
------------

.. py:class:: Collection(Sized, Iterable, Container)

    .. versionadded:: 3.6

    Generic версия :py:class:`collections.abc.Collection`


Container()
-----------

.. py:class:: Container()

    Generic версия :py:class:`collections.abc.Container`


ContextManager()
----------------

.. py:class:: ContextManager(Generic[T_co])

    Generic версия :py:class:`collections.AbstractContextManager`


Coroutine()
-----------

.. py:class:: Coroutine(Awaitable[V_co], Generic[T_co T_contra, V_co])

    .. versionadded:: 3.5.3

    Generic версия :py:class:`collections.abc.Coroutine`

    .. code-block:: py

        c = None  # type: Coroutine[List[str], str, int]
        x = c.send('hi)  # type: List[str]

        async def bar() -> None:
            x = await c  # type: int


Counter()
---------

.. py:class:: Counter(collections.Counter, Dict[T, int])

    Generic версия :py:class:`collections.Counter`


DefaultDict()
-------------

.. py:class:: DefaultDict(collections.defaultdict, MutableMapping[KT, VT])

    Generic версия :py:class:`collections.defaultdict`


Deque()
-------

.. py:class:: Deque(deque, MutableSequence[T])

    .. versionadded:: 3.5.4

    Generic версия :py:class:`collections.deque`


Dict()
------

.. py:class:: Dict(dict, MutableMapping[KT, VT])

    .. code-block:: py

        def func(item: Dict[str, str]):
            pass
    

Final()
-------

.. py:class:: Final()

    .. versionadded:: 3.8

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


ForwardRef()
------------

.. py:class:: ForwardRef()


FrozenSet()
-----------

.. py:class:: FrozenSet(frozenset, AbstractSet[T_co])

    Generic версия :py:class:`frozenset`


Generator()
-----------

.. py:class:: Generator(Iterator[T_co], Generic[T_co, T_contra, V_co])

    .. code-block:: py

        # Generator[YieldType, SendType, ReturnType]
    
        def func() -> Generator[int, float, str]:
            sent = yield 0
            while send > 0:
                sent = yield round(sent)
            return 'Done'


Generic()
---------

.. py:class:: Generic()

    .. code-block:: py

        T = TypeVar('T')

        def func(item: Generic[T]):
            pass
    

Hashable()
------------

.. py:class:: Hashable()

    Generic версия :py:class:`collections.abc.Hashable`


KeysView()
----------

.. py:class:: KeysView(MappingView[KT_co], AbstractSet[KT_co])

    Generic версия :py:class:`collections.abc.KeysView`


IO()
----

.. py:class:: IO()


ItemsView()
-----------

.. py:class:: ItemsView(MappingView, Generic[KT_co, VT_co])

    Generic версия :py:class:`collections.abc.ItemsView`


Iterable()
----------

.. py:class:: Iterable()

    Generic версия :py:class:`collections.abc.Iterable`


Iterator()
----------

.. py:class:: Iterator()

    Generic версия :py:class:`collections.abc.Iterator`


Literal()
---------

.. py:class:: Literal()

    .. versionadded:: 3.8

    .. code-block:: py

        def give_me_four(x: Literal[4]):
            pass

        give_me_four(4)  
        # ok
        
        give_me_four(4.0) 
        # error: Argument 1 to "give_me_four" has incompatible type "float"; expected "Literal[4]"
        
        give_me_four(42)  
        # error: Argument 1 to "give_me_four" has incompatible type "Literal[42]"; expected "Literal[4]"


List()
------

.. py:class:: List(list, MutableSequence[T])
    
    .. code-block:: py

        def func(items: List[str]):
            pass

        Vector = List[float]
        def func(items: Vector):
            pass
    

Mapping()
---------

.. py:class:: Mapping(Sized, Collection, Generic)

    Generic версия :py:class:`collections.abc.Mapping`

    .. code-block:: py

        overrides = Mapping[str, str]


MappingView()
-------------

.. py:class:: MappingView(Sized, Iterable[T_col])

    Generic версия :py:class:`collections.abc.MappingView`


Match()
-------

.. py:class:: Match()


MutableMapping()
----------------

.. py:class:: MutableMapping(Mapping[KT, VT])

    Generic версия :py:class:`collections.abc.MutableMapping`


MutableSequence()
-----------------

.. py:class:: MutableSequence(Sequence[T])

    Generic версия :py:class:`collections.abc.MutableSequence`


MutableSet()
------------

.. py:class:: MutableSet(AbstractSet)

    Generic версия :py:class:`collections.abc.MutableSet`


NamedTuple()
------------

.. py:class:: NamedTuple()

    Типизированная версия :py:class:`collections.namedtuple`

    .. code-block:: py

        class Employee(NamedTuple):
            name: str
            id: int

        People = NamedTuple('People', [('name', str), ('id', int)])


NewType()
---------

.. py:class:: NewType()

    .. code-block:: py

        UserId = NewType('UserId', int)
        some_id = UserId(12345)


NoReturn()
----------

.. py:class:: NoReturn()

    .. code-block:: py
    
        def func() -> NoReturn:
            raise RuntimeError('no way')

Optional()
----------

.. py:class:: Optional()



OrderedDict()
-------------

.. py:class:: OrderedDict(collections.OrderedDict, MutableMapping[KT, VT])

    Generic версия :py:class:`collections.OrderedDict`


Pattern()
---------

.. py:class:: Pattern()


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


Reversible()
------------

.. py:class:: Reversible()

    Generic версия :py:class:`collections.abc.Reversible`


Sequence()
----------

.. py:class:: Sequence(Reversible[T], Collection[T])

    Generic версия :py:class:`collections.abc.Sequence`

    .. code-block:: py

        Address = Tuple[str, int]
        ConnectionOptions = Dict[str, str]
        Server = Tuple[Address, ConnectionOptions]
        
        def func(servers: Sequence[Server]):
            pass


Set()
-----

.. py:class:: Set(set, MutableSet[T])

    Generic версия :py:class:`set`


Sized()
-------

.. py:class:: Sized()

    Алиас :py:class:`collections.abc.Sized`


SupportsAbs()
-------------

.. py:class:: SupportsAbs()

    ABC класс с абстрактынм методом __abs__.


SupportsBytes()
---------------

.. py:class:: SupportsBytes()

    ABC класс с абстрактынм методом __bytes__.


SupportsComplex()
-----------------

.. py:class:: SupportsComplex()

    ABC класс с абстрактынм методом  __complex__.


SupportsFloat()
---------------

.. py:class:: SupportsFloat()

    ABC класс с абстрактынм методом __float__.


SupportsIndex()
---------------

.. py:class:: SupportsIndex()

    .. versionadded:: 3.8

    ABC класс с абстрактынм методом __index__.


SupportsInt()
-------------

.. py:class:: SupportsInt()

    ABC класс с абстрактынм методом __int__.


SupportsRound()
---------------

.. py:class:: SupportsRound()

    ABC класс с абстрактынм методом __round__.


Text()
------

.. py:class:: Text()

    Алиас :py:class:`str`


TextIO()
--------

.. py:class:: TextIO()


Type()
------

.. py:class:: Type(Generic[])

    .. versionadded:: 3.5.2

    .. code-block:: py

        class User:
            pass

        def func(user: Type[User]):
            pass


TypeVar()
---------

.. py:class:: TypeVar()

    # любой тип
    T = TypeVar('T')  

    # стркоа или байты
    A = TypeVar('A', str, bytes)

    def func(l: Sequence[T]) - > T:
        pass


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


Tuple()
-------

.. py:class:: Tuple()

    .. code-block:: py

        def func(item: Tuple[str, int]):
            pass


Union()
-------

.. py:class:: Union()

    ... code-block:: py

        Union[Union[int, str], float] == Union[str, int, float]
        Union[int] == int
        Union[int, str, float] == Union[int, str]


ValuesView()
-----------

.. py:class:: ValuesView(MappingView[VT_co])

    Generic версия :py:class:`collections.abc.ValuesView`