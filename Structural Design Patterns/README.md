# ⚙️ Structual Design Patterns ⚙️

---
## 1.0 - __Decorator__ 🎀

---

__Reference [HERE](https://www.youtube.com/watch?v=GCraGHx6gso)__

__Decorator__ is a design pattern that is defined as:

> Decorator attachs a additional responsibility to an object __dynamically__ (without changing source code). It is an flexible alternative to subclassing for extending functionality

To put in another way, an decorator will manipulate the returning value or any parameters sent to the object, at __runtime__ without changing the code itself.

Traditionally (like __Java__), this is done by wrapping an object with a *Decorator* class, which *(this may sound confusing)*, should be also the subclass of the base class itself.

---

### Problem:

In the book __Head First Design Pattern__, the example provided is that we have a Cafe shop that will have `Beverages` (abstract class) like `Espresso` and `Mocha`.

These `Beverages` will have methods like `getCost` and `description`.

 However, problem arises when we need a way to have optional toppings like `Soy Milk`, `Chocolate`, or `WhippedCream` for those beverages. Initially, we may have some ideas of the implementation:

 * Subclassing for the combinations. Say `ChocolateMocha` or `WhippedCreamEspresso`. However, what if toppings can be mixed? Like `SoyChocolateMocha`? How many combinations will it result in?

 * Implementing boolean/integer variables in the `Beverage` itself, like variables `hasSoy` or `chocolateCount`. However, this will pose a potential __Interface Segregation__ issue. Say we started selling `Tea`. `Tea` should never use `hasChocolate` because it is a absurd combination!

 ---

 ### Solution:

 Instead, the idea is that we first start with two interfaces:

 * `Beverage` - Having `getCost` and `describe` method
 * `BeverageDecorator` - __Extends `Beverage` class__. Also, each `BeverageDecorator` should have an attribute `Beverage` acting as inner object which it decorates.

*(Over here, you can see the Decorator, `BeverageDecorator`, __is a Beverage__ and __has a Beverage__). A decorator should be the same type with the object it is decorating, and has the same type  with the object it is decorating*

Then we can go ahead and create concrete classes of `Beverage` like `Espresso` and `Mocha`, as well as concrete classes of `BeverageDecorator` like `Soy MilkDecorator` and `ChocolateDecorator`.

As you might see where this is going, when we want to add Chocolate to our Mocha, we simply create a `ChocolateDecorator` decorator and pass in our original `Mocha` inside, like:

```java
Beverage myBeverage = new ChocolateDecorator( new Mocha() );
myBeverage.getCost();
```

As we are calling the `getCost()` method, the `ChocolateDecorator` will return the __base price__ of whatever the beverage it is having as attribute (In this case, `Mocha`), and add an additional price to it, if that is what your intention.

You can see, this pattern is similar to recursion - Decorator will recurse until it hits the base case, in this case it's `getCost()` of `Mocha`

---

In Python, using decorator is fairly simple because it is already built in.

For example, using decorators, we can easily create a new function that extends the original function by running code before and after the execution, or modify the return value of the original function.

The subsequent design patterns such as __Adapter__, __Composite__ and __Strategy__, are all related to __Decorator__.

<br><br>


---
## 2.0 - __Proxy__ ⏱️

---

__Reference [HERE](https://www.youtube.com/watch?v=NwaabHqPHeM)__

According to the defintion:

> __Proxy__ provides a surrogate/placeholder for another object to control access to it.

According to the book, __Proxy__ is split into 3 types:

* __Remote__ - Subject to access is from other server, or from other project
* __Virtual__ - Subject to access is potentially expensive, thus you may want to cache it or delay its instantiation until absolutely necessary
* __Protection__ - Subject to access hold credentials and you want to authorize client prior to giving access

The core __intent__ of using a __Proxy__, is to intersect the direct access of a client to a targeted subject, while the Proxy itself still is able to be used as the actual subject itself.

The 3 main idea of proxy is that:

* Proxy control access to the actual subject
* Proxy implements the same interface as the actual subject
* Proxy handles instantiation of the subject.

Perhaps in a multithreaded program, a certain service is frequently accessed. Therefore, between client and the server, a proxy may be used to check whether the service is busy prior to giving access to a particular client. *(Maybe you can change implementation of service itself to check occupied, but maybe you simply can't)*

---

### Problem:

Say we have a website about __Books__. We have a `BookParser` class that takes in a constructor of a `http` link that directs to the full txt of the book. 

In the constructor, it will download the whole book, parses the whole book, and set some fields like `noOfPages`, `noOfWords`, etc.

Say in the `BookParser` consist of `getNoOfPages()`, `getNoOfWords()`, and `toString()` which returns text of whole book as string. 

Note that the constructor operation is expensive (Downloading and Parsing), while the other methods are cheaper. The question arises when there are times where the `BookParser` are instantiated (therefore expensive operation executed), but its method are never accessed?

This is exactly where we would use a `BookParserProxy` to

1. Delay the instantiation of `BookParser` until absolutely necessary
1. Cache the result of method calls (Memoization)

Let's see how it is done in `Proxy.py`

<br><br>

---
## 3.0 - __Adapter__ 🔌

---

__Reference [HERE](https://www.youtube.com/watch?v=2PKQtcJjYvc)__

Definition:

> __Adapter__ converts the interface of a class to another interface the client would expect.
 
> __Adapter__ let classes work together that couldn't otherwise becasue of incompatible interfaces.

__Adapter__, exactly what you think it is. Adapter solves the problem of incompatible interfaces (Different expectation of method names or attributes).

Here are the 4 design patterns that could easily get confused:

* __Adapter__
* __Facade__
* __Proxy__
* __Decorator__

There are two ways of implementing __Adapters__:
* Composition
* Multiple Inheritance

We'll mainly discuss __Composition Adapter__.

Say we have a `Client` (Usually the program that we are writing) that wants to call an `Adaptee`'s (Usually inaccessible code, Eg: libraries) method. However, there are problem faced:

* We do not has access, or does not want to modify the `Adaptee`'s source code.
* The input format coming from the `Client` is incompatible to that of `Adaptee`'s.

For example, we are developing a Stock program that monitors stock movement, presenting different stocks in bars and chart using some third party charting library (Adaptee). However, the stock data providers give data in __XML__ format, and the charting library expects to receive __JSON__ data. 

With this, we could use composition to include a `ChartingAdapter` inside our data fetching class, and pass in our raw XML data into the adapter instead of directly calling `chart(data)` of the Adaptee, which you would expect an error.

```java
// Composition implementation of Adapter
class DataFetcher {
    DataToChartAdapter chartingAdapter = new XMLDataToJSONChartAdapter( library );  // Pass the adaptee into adapter
    XMLData data;
    ...
    void chart() {
        chartingAdapter.chart(data);
    }
}
```

Note in above example, we used `DataToChartAdapter`. Imagine suddenly we changed our stock data provider and the new provider gives __Excel__ data or __csv__ data. Without changing code in our `DataFetcher` class, we would still do fine, just implement a new `CSVDataToJSONChartAdapter` or `ExcelDataToJSONChartAdapter`!

In programming languages like __Python__ where functions are first class citizens, we can build an adapter that maps function calls directly to another function call by magic function `__dict__` and `__getattr__`. This particularly solves the issue of incompatible method names between adaptees.

---

### Problem:

For example, when developing a war based game, we have a `Infantry` class that has `walk_forward()` and `fire_rifle()` method. They are being controlled by a `Commander` that controls them using `unit.interpret_command('walk')` and `unit.interpret_command('fire')`. Now, we added a `Tank` class that has `drive_forward()` and `fire_missle()` method that is called by command `'drive'` and `'missle'` respectively. However, the commander wants to use the `Tank` classes with the same command `'walk'` and `'fire'` as those of `Infantry`'s. A adapter design pattern needs to be used to "translate" the commands!



<br><br>

---
## 4.0 - __Facade__ 🗂

---

__Reference [HERE](https://www.youtube.com/watch?v=K4FkHVO5iac)__

A __Facade__ design pattern, defined:

> __Facade__ pattern provides a unified interface to a set of interfaces in a subsystem.

> __Facade__ defines a higher level interface that makes the subsystem easier to use

__Facade__ isn't too hard to understand. What we are essentially doing is to combined multiple subsystems under one unified interface that is easier to use.

The name of the design pattern does makes sense if you think about it. __Facade__ means the front facing part of the house, which hides away internal, complex implementations like water piping, electrical cabling, foundation etc. Clients doesn't even need to know these internal implementation at all to use the system.

Another important concept that should be introduced in system design, is [__Law of Demeter__](https://en.wikipedia.org/wiki/Law_of_Demeter) *(Aka __Principle of Least Knowledge__)*. It means:

* Each unit should have only limited knowledge about other units: only units "closely" related to the current unit.
* Each unit should only talk to its friends; don't talk to strangers.
* Only talk to your immediate friends.

Conceptually, it discourages code pattern like so: `obj1.obj2.obj3` which involves objects that are not inside the current object.

Applying __Law of Demeter__ will inherently cause more classes, each class having a small responsibility rather than few classes that have large amount of responsibility. However it is cases like this that we are more supposed to use __Facade__ design pattern

---

### Problem:

Let's take an ATM machine as an example. Under the hood, it may have to interact with `SecurityChecker`, `CardReader`, `AccountBalanceChecker` etc. Instead of having to interact with each of these from the client, we should create a `ATM` class that provides an unified interface to perform a significant operation such as `withdraw`.

<br><br>

---
### 5.0 - Bridge 🌉

__Reference [HERE](https://www.youtube.com/watch?v=F1YQ7YRjttI)__

Definition:

> The intent of the bridge pattern is to decouple an abstraction from its implementation so that the two can vary independently

Let's start by looking at the concept of __cartesian product__. The cartesian product of two sets, {A,B,C} and {1,2} would be {(A,1), (A,2), (B,1), (B,2), (C,1), (C,2)}.

Now, imagine those are two set of classes which are related. Set A, will have composition of one of the classes in Set B. If one of these two sets are larger, we would have to implement as many classes as the size of the cartesian product, which is bad.

Some say that the __Bridge__ pattern are extended __Strategy__ pattern due to the similarity of their UML diagram.

Say we are developing an application which has `View` class that controls how a list of contents are displayed. Also, we have `Resource` which holds the contents to be displayed.

For example, `View` can be of type __Detailed__, __Simple__, and __Mobile__. As for `Resource` we have __Book__, __Movie__ and __Music__.. We want to be able to display information about Books, Movies and Musics in our application, while allowing user to choose whatever type of view they want.

Do we make a class for every possible combinations, say `DetailedBookView`, `DetailedMovie`, `DetailedMusic`, `SimpleBook`, `SimpleMovie`, `SimpleMusic` and so on? That would be bad when we decided to suddenly add a new type of `View` or `Resource`!

Instead, using `Bridge` pattern, we decouple the `View` into concrete implementations like `DetailedView`, `SimpleView`, `MobileView`. Each of these views, will contain a resource like `BookResource`, `MovieResource` and `MusicResource`. Those `Resource` will implement a common interface that the `View` may use. For example, each of the `Resource` will implement `getTitle()`, `getAuthor()`, `getDescription()` according to the interface. This way, the classes we made are much less compared to cartesian product method.

<br><br>

---

### 6.0 - General Comparison

__Comparison [HERE](https://www.youtube.com/watch?v=lPsSL6_7NBg)__


<br><br>

---

### 7.0 - Template Method 🔩

__Reference [HERE](https://www.youtube.com/watch?v=7ocpwK9uesw)__

The definition is as follows:

> The __Template Method__ pattern defines the skeleton of an algorithm in an operation, deferring some steps to subclasses. __Template Method__ let subclasses define certain steps of the algorithm without changing the algorithm structure. 

In other words, __Template Methods__ will require us to first implement a incomplete method (algorithm) with some pieces missing. Those pieces shall be implemented in the subclasses. This prevents duplicating core algorithm that does not vary, yet providing freedom for the code that should vary by subclasses.

For example, we are creating a method for `pdf`, `txt` and `csv` files that reads the file, processes accordingly and output to the user screen. Perhaps we will implement 3 classes, `PdfParser`, `TxtParser`, and `CsvParser`. However, we soon realize that the `parse()` method of three classes have some duplicate codes, mainly on the reading file and printing part. In this case, we could utilize the __Template Method__ to create an abstract class `Parser` and have the template method inside.

This pattern can be applied to the following example situations:

* __Sorting algorithm with Custom comparator__ - The core sorting algorithm is the same, just that the comparator varies depending on use case and the datatype to sort
* __Hooks__ - Before and after the data is processed, hooks must be called.
* __ORM__ - When we call `save()` on a `Model`, like `User`, there are same algorithm that are executed to save the data to the database.

---

### Solution:

To implement __Template Method__, we would have to first have an abstract class which has the template method (incomplete algorithm) defined. In above example, the template method, `parse()` would look like:

```java
void parse() {
    ... // Code for reading the file
    process();  // This is the part that varies depending on concrete parsers
    ... // Code for output
}
```

With this, we will also make the `process()` method to be mandatory to be implemented in subclasses, namely `PdfParser`, `TxtParser`, and `CsvParser`. 

<br><br>

---

### 8.0 - Composite 🗂

__Reference [HERE](https://www.youtube.com/watch?v=EWDmWbJ4wRA)__

The definition:

? The __Composite__ pattern composes object into tree structure to represent part-whole hierarchies. Composite let client treat individual objects and composition of objects uniformly.

The idea is, no matter whether an object is an individual unit, or it is an composition of multiple objects, we are able to treat it uniformly/transparently under the same interface. 

__Composite__ pattern will consist of leaf and intermediate nodes. The intermediate nodes are responsible to keep track of its composed children. Because the __Composite__ pattern forms a tree structure, it is natural to also utilize __Recursion__ in computations. 

### Solution:

The __Composite__ pattern is very commonly used in frameworks that are __Component__ based, like `React.js`. If we create a `Navbar`, `Footer` or `Post` in React, all of them actually inherits from `React.Component`. 

* These concrete components can be either leaf node (Not composed of any other component), or a composition of other smaller components.
* However, leaf node or intermediate node, we are able to treat them uniformly under a common interface. For example, all of the components require a `render()` method to draw the UI on the screen.

Another example is simply the file structure. Say we are developing a program that involves file structure, say we have leaf nodes as `File` like `txt` or `exe`, and intermediate nodes as `Directory` that may contain other files or directories, all of them should have a `listFiles()` method implemented. For simple `File`, `listFiles()` should just return the name of the file, while `listFile()` on `Directory` will combine all the results of `listFile()` of its children by recursion and return it.