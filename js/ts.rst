.. title:: type script

.. meta::
    :description: type script
    :keywords: type script

TypeScript
==========

.. code-block:: js

    var identifier: Type = value;
    let identifier: Type = value;
    const IDENTIFIER: Type = value;

    var identifier: any = value;
    
    var v1: number = 1;
    let binary: number = 0b101;
    let octal: number = 0o5;
    let decimal: number = 5;
    let hex: number = 0x5;

    let v1: string = 'ilnurgi';

    let v1: boolean = false;

    let v1: symbol = Symbol('ilnurgi');

    let v: null = null;
    let v: undefind = undefind;

    let k: int = 1;
    let v: typeof k = 2;

.. code-block:: js

    function identifier(param1: Type, param2: Type): ReturnedType {}
    function identifier <T, U>(): ReturnedType {}
    function func(): void {}

    <T, U>( param: Type, param: Type ): Type => value

    class A(){}
    class B(){}
    class C(){}
    function move(animal: A | B | C): void {
      animal.method_a() // ERROR
      animal.method_b() // ERROR
      animal.method_c() // ERROR
      
      animal.method_abc() // Ok
    }

    function start(port: 80 | 42) {}
    function animate(name: "easy-in" | "easy-out") {}

    var animalAll: (A | B | C)[] = [new A(), new B(), new C()]

    // tuple
    let lion: [string, number] = [1, 'Simba']

.. code-block:: js

    function identifier(p1: T1, p2: T2): T3;
    function identifier(p1: T4, p2: T5): T6;
    function identifier(p1: T, p2: T): T {
      return 'value';
    }

    function f( ..rest: [number, string, boolean]): void {}
    // function f( ..rest: [number, string?, boolean]): void {}
    // string? - ? - необязательный

    let f2: Function = f;

    let tuple: [ number, string, boolean ] = [ 5, '', true ];
    let array = [ 5, '', true ];

    f( 5 ); // Error
    f( 5, '' ); // Error
    f( 5, '', true ); // Ok
    f( ...tuple ); // Ok
    f( tuple[0], tuple[1], tuple[2] ); // Ok
    f(...array); // Error
    f( array[0], array[1], array[2] ); 
    // Error, 
    // все элементы массива принадлежат к типу string | number | boolean, 
    // в то время как первый элемент кортежа принадлежит к типу number

    class Identifier {
      constructor(p1: T1, p2: T2);
      constructor(p1: T3, p2: T4);
      constructor(p1: T, p2: T) {}

      identifier(p1: T1, p2: T2): T3
      identifier(p1: T4, p2: T5): T6;
      identifier(p1: T, p2: T): T {
          return 'value';
      }
    }

.. code-block:: js

    class Identifier<T> {
      static staticField: Type = value; // member
      
      static get staticProperty(): Type { // member
          return value;
      }
      static set staticProperty(value: Type) { // member
         
      }

      static staticMethod <T, U>(param: Type, param: Type): Type { } // member

      [indexSignature: Type]: Type; // member

      [computedProp]: Type = value; // member

      field: Type = value; // member

      get property(): Type { // member
          return value;
      }
      set property(value: Type) { // member
         
      }

      constructor(param0: Type, param1: Type){}

      method <T, U>(param: Type, param: Type): Type { } // member
    }

.. code-block:: js

  enum Fruits {
    Apple,  // 0
    Pear,  // 1
  }
  Fruits[Fruits.Apple] 
  // Apple

  // такие энамы инлайнятся значениями сразу в код
  const enum Fruits {
    Apple = 2,
    Pear = 4,
  }

.. code-block:: js

  interface IAnimal {
    nicknameL string;
    execute(command: string): void;
  }

  class Bird implements IAnimal, IAnimal2 {
    nicknameL string;
    execute(command: string): void;
  }

  class Eagle extends Bird implements IFlyable {}

  interface IAnimal3 extends IAnimal, IAnimal2 {}
  
  interface IAnimal3 extends Animal {}
