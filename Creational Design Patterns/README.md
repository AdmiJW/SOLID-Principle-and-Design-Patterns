# ⚙️ Creational Design Patterns ⚙️

---
## 1.0 - __Factory__ 🏭

---

__Reference [HERE](https://www.youtube.com/watch?v=EcFVTgRHJLM)__

For the formal definition,

> __Factory__ design pattern defines an interface for creating an object, but let subclasses (factories) decide which and how each class will be instantiated. Factory method let classes defer instantiation to subclasses (factories)

To put simply, __Factory__ encapsulates object creation. Factory is an object specializing in creating other objects.

In Layman's term, Factory can be thought as functions that create and return objects based on user input, or internal program state. It can return object of different classes. Eg: it can create instances of both `Dog` and `Cat`

From the book, there is 3 types of factories stated:

* Simple factory - Only one single concrete factory. Think of it as a function that helps you create different objects 
* Factory method - A family of factories, able to create different objects
* Abstract factory - Discussed as separate topic

We can say __Factory__ design pattern can be applied to implementing __Strategy__ design pattern. In the example of __Strategy__, we only have a single concrete `Duck` class, but yet there should be multiple types of `Duck` like `CityDuck` and `WildDuck`.Therefore, instead of passing the methods like `quack()` and `fly()` into `Duck`'s constructor, we could use __Factory__ to help us do just that.

---

### Problem:
* Uncertainties in types of objects
* Decisions to be made at runtime regarding which classes to use, depending on parameter or even program state
* Instantiation logic is complex and deserves to be separated

Say we are designing a war game. The game consist of 5 levels where the number of `Infantry` and `Tank` would increase by level. Also, there are also difficulty levels that could be chosen. For example, in Normal mode, ratio of `Infantry` should roughly be equal to `Tank`, while in Hard mode, `Tank` should have higher ratio. (Similarly, we could have `Easy` or even `Tutorial` mode)

---


### Solution:

Instead of having an if-else statement checking the game mode and instantiating enemies using `new` statement, we could use __Factory__ here.

First, create an __interface__ like `EnemyFactory` that consist of a `createEnemy()` method that could return an instance of `Enemy`, like `Tank` or `Infantry`.

Then, we would create concrete factories like `NormalModeEnemyFactory` and `HardModeEnemyFactory`. This is because the instantiating algorithm of different game modes shall be different. Say if `NormalModeEnemyFactory.createEnemy()` is called 100 times, the number of `Infantry` and `Tank` created should almost be equal. This is another story for `HardModeEnemyFactory`.

Then finally in our game, we would have a topmost `EnemyFactory` that we would use to add `Enemies` into our battlefield depending on the level and gamemode the game is currently in.

You can see this provides much flexibility for our program to grow. Say if I suddenly want Hardmode `Tank`s to have much higher HP and damage, I can simply modify the instantiating logic in `HardModeEnemyFactory` without changing code at other place!


<br><br>


---
## 2.0 - __Abstract Factory__ 🏭

---

__Reference [HERE](https://www.youtube.com/watch?v=hUE_j6q0LTQ)__

__Abstract Factory__ is defined as:

> Interface for creating __families of related/dependent objects__ without specifying their concrete classes.

In contrast of __Factory__ design pattern, which a factory only responsible for constructing one type of object, an __Abstract Factory__ is capable of constructing multiple related objects, __same type or different type__.

In fact, one can argue that the difference between a __Factory__ and a __Abstract Factory__ is simply that Abstract factory is capable of constructing multiple objects of related families.

Take GUI as an example. Maybe in our program, GUI components are separated according to platforms. Perhaps we have `WindowOSText`, `MacOSText` and `LinuxOSText`. If we want to abstract away the platform dependency and simply get an object of text via something like `getText`, we would use a __Factory__ pattern here, perhaps `TextFactory`.

However, we could take the abstraction a level further. Say *Alert Boxes*, which consist of __MessageBox__, __Buttons__, and __Text__. What we could do is instead of creating 3 separate factories `MessageBoxFactory`, `ButtonFactory` and `TextFactory` that handles the platform dependency, we could just create a `AlertBoxFactory` that handles the instantiation of above 3 objects for us, at once *(We may even use composition, a factory that have 3 factories)*. We create a alertbox by calling `createAlertBox()`, which in turn may call `createMessageBox()`, `createButton()` and `createText()`. This in essence is what __Abstract Factory__ do!

An another example would be to have a `LightModeUIFactory` and `DarkModeUIFactory`, which creates component instances based on what mode the client is applying.

---

### Problem:

Now in our previously mentioned wargame, you decided that the code is messy and needs to modularized. You want to be able to create the enemy team just by a simple `createEnemy()` method, which creates a team consisting of `Infantry`, `Calvary` and `Tank`. Those `Enemy`s are simply abstract class that are to be inherited by concrete `Enemy` like `NormalModeInfantry` and `HardModeCalvary`.

---

### Solution:

To apply __Abstract Factory__, we could have `NormalModeEnemyFactory` and `HardModeEnemyFactory` which inherits a common interface of `createInfantry()`, `createTank()` and `createCalvary()`. The implementation of these methods will vary by factory, creating normal mode and hard mode variations of the `Enemy`. Lastly, we could have a `createEnemies()` method that utilize the above methods to create an enemy army!

<br><br>


---
## 3.0 - __Singleton__ 🦠

---

__Reference [HERE](https://www.youtube.com/watch?v=hUE_j6q0LTQ)__

The definition of __Singleton__:

> __Singleton__ ensures that the class has only one instance, and provides a global point of access to it.

A __Singleton__ is commonly referred as "global variables" across multiple modules/scripts. 

Essentially, a singleton is simply the __ONLY INSTANCE__ that a class will ever create in the program lifecycle. The class will only create THAT SINGLE INSTANCE, and provides a way for other modules to access it. This is useful especially for __information cache__. 


If you've ever used `mongoose` (or other database modules), which is Javascript's library for working with `MongoDB` database, once the connection to the database is established via the singleton object itself, the connection remains when the module is required in other scripts. We wouldn't want to create more than one connection to the database do we?

If you are required to read data from a file and access it in multiple scripts, instead of reading the file over and over again in every script, use a singleton so that the file is only __READ ONCE__.

---

### Controversy:

The __Singleton__ pattern has its controversials among developers that it is a bad practice. Here's why:

* We should avoid globals as much as possible.
* We can never sure that the program will ever need a single instance of the class. Maybe we need a new instance as we add functionailies to our program?
* Add challenges to unit testing, as codes depend on this "global variable"

---

In Python, __Module__ itself is already a singleton. If we have:
* `test1.py` - which have `print("Hello World")`
* `test2.py` - which have `import test1`
* `test3.py` - which have `import test1` and `import test2`

By running `test3.py` you will only see `Hello World` printed once only. This is because modules in Python are singleton.

---

In other languages like Java, creating a Singleton may require the following steps:

* Creating a __static__ variable which holds an instance of itself, which is to be shared
* Making the constructor __private__ to prevent instantiating of the class
* Creating a public method to retrieve the singleton object

```java
class Singleton {
    int value = 123;
    String name = "Hi";

    // Singleton
    static Singleton obj = new Singleton();

    // Make constructor private
    private Singleton(){}

    // Method to retrieve singleton
    public static Singleton retrieve() {
        return obj;
    }
}
```


<br><br>


---
## 2.3 - __Builder__ 🏗

---

__Builder__ is a solution to a anti-pattern called *Telescoping constructor*. 

A *Telescoping constructor* is essentially a constructor of a class that is bloated: maybe it has 10 required parameters to initialize all the fields of the object, which is a lot. Maybe you will work around with having separate setters, but still that isn't very elegant.

A __Builder__'s job is to construct the complex object, but hiding away all the pesty details away from the user. Imagine the original object requires 10 parameters to construct, but using builders, you can choose 3 of them to fill only.

The __Builder__ design pattern usually consist of these main components:

|Components|Description|
|-|-|
|__Director__| In charge of actually building the object via Builders; The class using the builders |
|__Abstract Builder__|The base builder class which will be inherited by __Concrete Builders__ (Eg: `PhoneBuilder`)|
|__Concrete Builders__|The actual builders which will construct the object, making some default assumptions (Eg: `NokiaBuilder`, `SamsungBuilder`)|
|__Product__| The actual object being built (Eg: `Nokia`)|

One way to implement traditionally, is to have a __Abstract Builder__ that has a constructor, that builds the object with required parameters only (or inferred). Through providing setters, other optional fields can be set. Eg:

```java
Phone phone = new NokiaPhoneBuilder("3310").setPrice(100).setColor('blue').getPhone();

// The Abstract Builder will specify constructor, setPrice, setColor, getPhone etc and must be inherited by concrete builders
```

For `Javascript`, things can be done via Javascript Objects to set optional parameters.

```javascript
class Phone {
    constructor(name, { price, color } = {}) {
        ...
    }
}

const phone = new Phone('3310', {
    price: 100,
    color: 'blue'
})
```

<br><br>


---
## 2.4 - __Prototype__ 🧬

---

__Prototype__ clone objects according to a prototypical instance. It is useful when dealing with creating many identical objects individually, where we would prefer cloning instead.

For example, let's say in our forum system, each user comment is an object. Instead of creating each comment object one by one *(which may need to connect to database in the constructor, an expensive operation)*, we can instead apply __Prototype__ design pattern, fetch a bunch of comments from database, create one individual comment object, and clone it for other comments.

The implementation may be ambiguous, but the point remains
* Create a prototypical instance
* Clone it whenever we need a replica