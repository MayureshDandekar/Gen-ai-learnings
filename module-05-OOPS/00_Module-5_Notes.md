# Module 5 — OOP in Python: Revision Notes

---

## 1. Inheritance

**What it is:** A child class reuses everything (attributes + methods) from a parent class, without rewriting it.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):   # Dog inherits from Animal
    pass

d = Dog("Tommy")
d.speak()   # Tommy makes a sound — inherited, not rewritten
```

**Trigger:** Multiple classes share common behavior — pull the shared part into a parent, extend from there.

**Key point:** `Dog(Animal)` means "Dog IS-A Animal." Anything true for `Animal` is automatically true for `Dog` unless overridden.

---

## 2. Polymorphism — 3 types

**Core idea:** Same method call, different behavior depending on what's actually running it.

### a) Method Overriding
Child class redefines a parent's method with the same name.

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):          # overrides parent's version
        print("Woof!")
```

Calling `.speak()` on a `Dog` object runs `Dog`'s version, not `Animal`'s — Python checks the object's **actual class** first.

`super().speak()` lets you call the parent's version too, instead of fully replacing it.

### b) Method Overloading
Same method name, different behavior based on arguments — **Python doesn't support this natively** (unlike Java/C++). Faked using default args or `*args`:

```python
class Calculator:
    def area(self, *args):
        if len(args) == 1:
            return args[0] * args[0]
        elif len(args) == 2:
            return args[0] * args[1]
```

### c) Duck Typing
"If it has the method, call it" — no shared parent class or inheritance required at all.

```python
class Duck:
    def sound(self): print("Quack")

class Car:
    def sound(self): print("Vroom")

def make_it_speak(thing):
    thing.sound()   # works on ANY object with a .sound() method
```

**Key mental model (object passing):** `get_info(Book())` — `Book()` creates an object FIRST, then that object is passed in. The class name is never "passed" — the object just permanently carries its class as internal metadata, which is how Python knows which method version to run.

---

## 3. Encapsulation — Public / Protected / Private

**What it is:** Bundling data + methods in a class, and controlling how much outside code can touch the data directly.

Python has **no real enforced privacy** — it's naming convention (except private, which does one real thing: name-mangling).

| Level | Syntax | Behavior |
|---|---|---|
| Public | `self.name` | Accessible from anywhere, no restriction |
| Protected | `self._name` | Convention only — "internal use," but still accessible |
| Private | `self.__name` | Name-mangled to `_ClassName__name` — inaccessible by the original name from outside the class |

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance   # private

    def get_balance(self):
        return self.__balance      # works FROM INSIDE the class — mangling doesn't apply here
```

**Gotcha:** `acc.__balance = 10` from outside doesn't error — it silently creates a brand new decoy attribute, unrelated to the real mangled one. Not a security hole; the real private value stays untouched.

---

## 4. Getter & Setter — `@property`

**Why it exists:** Lets you keep validation logic (like a private attribute + manual getter/setter) while still using clean, plain-looking attribute syntax (`acc.balance`, not `acc.get_balance()`).

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance     # goes through the setter — validates immediately

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value
```

**Rules:**
- Getter and setter must share the exact same method name.
- `@property` must be defined BEFORE `@propertyname.setter`.
- A property with no setter is **read-only**.

**#1 bug to avoid (hit this 3 times in practice):** Writing `self.__balance = value` directly anywhere — including inside `__init__` — **bypasses the setter completely**, skipping all validation. Always assign through the property name (`self.balance = value`), never the raw private variable, unless you're inside the getter/setter methods themselves.

**Fail loudly, not silently:** Use `raise ValueError(...)` in a setter, not `print(...)`. A `print` lets execution continue with the object left in a broken/incomplete state — errors should surface immediately, at the point of bad input, not later as a confusing `AttributeError` somewhere else.

---

## 5. Abstraction

**What it is:** Defining a contract — "every subclass MUST implement these methods" — without saying how. Hides *implementation*, not code — the caller doesn't need to know or care how a method works internally to use it correctly.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
```

**Enforcement:**
- `Shape()` directly → `TypeError` — abstract classes can't be instantiated.
- If `Circle` forgot to implement `area()`, `Circle()` would ALSO throw `TypeError` — Python won't let a class inherit from an ABC without fulfilling every abstract method.

**Abstraction vs Encapsulation — don't mix these up:**
- **Encapsulation** = controls *who can access data* (private/protected/public).
- **Abstraction** = controls *what the caller needs to know* to use an object (hides the "how," exposes only the "what").

**Abstraction vs Duck Typing:**
- Duck typing = no enforced contract, fails at runtime with `AttributeError` if a method is missing.
- Abstraction (`ABC`) = enforced contract, fails immediately at class-definition/instantiation time if a method is missing.

---

## Quick self-check questions (answer without looking back)

1. What's the difference between overriding and overloading, in one line each?
2. Why does Python fake method overloading instead of supporting it natively?
3. Why does `acc.__balance = 10` from outside a class not throw an error, but also not change the real balance?
4. What's the one bug pattern that breaks `@property` validation almost every time? (Hint: happens most often inside `__init__`.)
5. Why does an abstract class refuse to be instantiated directly?
6. In one sentence: what does "abstraction hides implementation" actually mean for the person CALLING your code?