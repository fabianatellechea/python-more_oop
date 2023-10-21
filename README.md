# Python OOP - Abtract Class, Interface, Subclassing 

## Introduction:
Welcome to this set of exercises aimed at honing your understanding and application of Object-Oriented Programming (OOP) concepts in Python. Through these exercises, you will delve into abstract classes, interfaces, duck typing, and subclassing standard base classes among other crucial OOP concepts. By the end of these exercises, you should be proficient in employing OOP principles to design, implement, and test Python programs.

## Learning Objectives:
1. **Abstract Classes:** Understand and apply abstract classes to define common interfaces while enforcing certain levels of class completeness.
2. **Interfaces and Duck Typing:** Grasp the concept of interfaces and duck typing to ensure that objects adhere to a specific contract or protocol.
3. **Subclassing Standard Base Classes:** Learn to extend standard base classes like lists, dictionaries, and iterators to create custom data structures with specialized behavior.
4. **Method Overriding:** Employ method overriding to alter or enhance the behavior of base class methods.
5. **Multiple Inheritance:** Understand and apply multiple inheritance to form complex relationships between classes.
6. **Mixins:** Utilize mixins to compose behavior across unrelated classes.

## Resources:

- [Python 3 Object-Oriented Programming](https://docs.python.org/3/tutorial/classes.html)
- [ABC — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Real Python - Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [Corey Schafer - OOP Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
- [sentdex - Python OOP Tutorial](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfhTF3Zfyzc_yD-Mq9iTp4G)

The above resources provide a mix of reading material, interactive exercises, and video tutorials to cater to different learning styles. 
It's recommended to go through these resources to build a solid understanding of OOP concepts in Python before attempting the exercises.

## Basic Exercises

### Exercise 1: Create an Abstract Class
- Use the `ABC` package to create an abstract class named `Animal` with an abstract method `sound`.
- Create two subclasses, `Dog` and `Cat`, and implement the `sound` method to return "Bark" and "Meow" respectively.

### Exercise 2: Interface and Duck Typing
- Create an abstract class named `Shape` with abstract methods `area` and `perimeter`.
- Create two classes, `Circle` and `Rectangle`, and implement the `area` and `perimeter` methods.
- Write a function `shape_info` that takes a `Shape` object and prints the area and perimeter. Test it with `Circle` and `Rectangle` objects.

### Exercise 3: Extend a Base Class
- Extend the Python `list` class to create a class `VerboseList` that prints a message every time an item is added or removed.

### Exercise 4: Subclassing and Method Overriding
- Create a class `CountedIterator` that extends the `iter` class and keeps track of the number of items iterated.
- Override the `__next__` method to increment the count each time an item is iterated.

### Exercise 5: Multiple Inheritance
- Create a class `FlyingFish` that inherits from both a `Fish` class and a `Bird` class.
- Implement methods in `FlyingFish` that override methods from `Fish` and `Bird` to demonstrate multiple inheritance and method resolution order.

### Exercise 6: Mixins
- Create a `SwimMixin` and a `FlyMixin` with methods `swim` and `fly` respectively.
- Create a class `Dragon` that inherits from both `SwimMixin` and `FlyMixin`, and demonstrate how a `Dragon` object can both swim and fly.

These exercises provide a structured way to explore various OOP concepts in Python. They start from understanding abstract classes and move towards more complex ideas like subclassing standard base classes, method overriding, multiple inheritance, and mixins. Each exercise builds upon the previous one, allowing students to apply what they have learned in a progressive manner.

## Advanced Exercises

Let's add more complexity and deepen the understanding of the OOP concepts involved:

### Exercise 7: Advanced Abstract Classes
- Create an abstract class `Vehicle` using the `ABC` package with abstract methods `fuel_efficiency` and `top_speed`. 
- Create two subclasses, `Car` and `Motorcycle`, and implement the abstract methods. Each subclass should have additional attributes like `make`, `model`, and `year`.

### Exercise 8: Interfaces, Duck Typing, and Composition
- Create an abstract class `Storage` with abstract methods `store` and `retrieve`.
- Create two classes, `Warehouse` and `Vault`, to implement the `Storage` interface. 
- Create a third class `InventorySystem` that accepts objects of type `Storage` and manages items through the `store` and `retrieve` methods of the passed in `Storage` objects, showcasing duck typing.

### Exercise 9: Extending and Overriding Base Class Functionality
- Extend the Python `dict` class to create a class `VerboseDict` that prints a message every time an item is added, updated or removed.
- Override methods like `__setitem__`, `__delitem__` and provide additional method `get_history` to track all changes in the dictionary.

### Exercise 10: Custom Iterators and Generators
- Create a class `Fibonacci` that extends the `Iterator` class to generate Fibonacci numbers.
- Override the `__iter__` and `__next__` methods to generate Fibonacci numbers, and include a method to reset the iterator.

### Exercise 11: Multiple Inheritance and Method Resolution
- Create classes `Aquatic` and `Aerial` with methods `swim` and `fly` respectively.
- Create a class `FlyingFish` that inherits from both `Aquatic` and `Aerial` classes. Override the `swim` and `fly` methods to print unique messages and demonstrate method resolution order.

### Exercise 12: Mixins and Dynamic Attribute Access
- Create a `FlightMixin` with methods `take_off`, `fly`, and `land`.
- Create a `Bird` class with a `species` attribute and methods for `sing` and `nest`.
- Create a class `Airplane` with attributes for `model` and `airline`.
- Create a class `FlyingMachine` that inherits from `Bird`, `Airplane`, and `FlightMixin`. Use dynamic attribute access and method calls to interact with the mixed-in behavior and inherited attributes.
