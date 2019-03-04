dataclass
=========

.. code-block:: py

    @dataclass
    class MyClass:

        var_a: str
        var_b: str
        
    @dataclass(
        init=True, 
        repr=True, 
        eq=True, 
        order=False, 
        unsafe_hash=False, 
        frozen=False,
    )
    class MyClass:
        """"""

        def __post_init__(self):
            """
            выполнится после основного init
            """

.. code-block:: py

    from dataclasses import field

    @dataclass
    class Student:
        marks: List[int] = field(
            # default_factory=get_random_marks,
            default_factory=False,
            init=False,
            repr=False,
        )
        
    s = Student()
    s.marks
    # [1,4,2,6,9]

.. code-block:: py

    @dataclass(order = True)
    class User:        
        name:str = field(compare = False)
        age: int
        weight: float
        height: float
            

    user_1 = User("John Doe", 23, 70, 1.70)
    user_2 = User("Adam", 24, 65, 1.60)

    user_1 < user_2
    # True