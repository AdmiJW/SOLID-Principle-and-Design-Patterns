# 🤹 Behavioral Design Patterns 🤹

---
## 1.0 - __Strategy__ 🗺

---

> __Reference [__HERE__](https://www.youtube.com/watch?v=v9ejT8FO-7I)__

__Strategy__ design pattern, by formal definition, goes as follows:

> Strategy design pattern defines a family of algorithm, encapsulates them and make them interchangable.

Makes no sense right? Let's see an example use case:

---

### Problem:

We have learnt about inheritances. Let's say we have a `Duck` abstract class, which will have 2 methods: `quack()` and `fly()`.

Now, we will have 2 child classes inheriting from this `Duck` class: `CityDuck` and `WildDuck`.

Let's imagine some problem here:

* What if both ducks share the same `quack()` behavior? We shouldn't implement the function into the base class `Duck` because maybe there are more type of `Duck` that doesn't share the same `quack()` behavior.

* Let's say that `CityDuck` doesn't know how to fly. We are still having to implement the `fly()` method regardless due to inheriting from the `Duck` class.

The inheritance way of solving this problem, especially case 1, is to __use more inheritance__. For the `Ducks` that will have certain `quack()` behavior, we may make a `NormalQuackingDuck` class, that will be in turn inherited by the `CityDuck` and `WildDuck`.

However, as the program grows and more ducks are introduced, the inheritance tree quickly expands, and complexity goes out of hand (Inheritance forms a tree, and common behaviors cannot be shared __Horizontally__ - Like how `CityDuck` and `WildDuck` cannot share the same `quack`)

---

### Solution:

You may describe __Strategy__ pattern as *"using composition instead of inheritance"*. What if each of these methods (Eg: `quack`), can be an object and assigned to a `Duck` instance? That quickly solves the sharing problem faced earlier!

Instead of making deep, inheritance tree like introducing `NormalQuackingDuck` and whatsoever, let's instead extract those behaviors out and make them objects! (For __Java__, use abstract classes):

* `QuackBehavior` - must define `quack()` for those inheriting it
* `FlyBehavior` - must define `fly()` for those inheriting it

Now, since both ducks is able to quack and fly, the class definition would look something like:

```java
class Duck {
    QuackBehavior quackingBehavior;
    FlyBehavior flyingBehavior;
    ...

    void quack() {
        this.quackingBehavior.quack();
    }
    ...
}
```

Since both `CityDuck` and `WildDuck` share the same quacking behavior, we would define a __concrete__ `QuackBehavior` instance that can be used by both classes:

```java
class NormalQuackBehavior extends QuackBehavior {
    public void quack() {...}
}
```

---

Now, we can get rid of the inheritance tree in its entirety! All the behaviors of `Duck`s are __extracted__ away and implemented in the form of composition rather than inheritance!

It become a lot easier to extend the functionality, whether we want to add a `RubberDuck`, or add a `swim()` method

<br><br>



---
## 2.0 - __Observer__ 👀

---

__References [HERE](https://www.youtube.com/watch?v=_BpmfnqjgzQ)__

__Observer__ pattern, official defined as:

> A one to many dependency, where when the core dependency changes its state, all the other dependencies are notified

### Problem:

Think of this as a Weather System, where when the Station changes the weather state, all the subscribed clients (your phone, other weather websites) needs to be notified in real time.

This design pattern essentially helps to change from __poll__ process to __push__ process. In __polling__, the observers has to keep checking on the observable at fixed intervals. However, this process may be taxing on the observable (server), and still possibly causes delay in information (Say weather updates in 1s but observer polling interval is 10s). Instead in __push__, the server notifies all the observers about the update.

---

### Solution:

Conceptually, __Observer__ design pattern is implemented by first having two __interfaces__:

* `Observer` - Need to implement `addObserver`, `removeObserver` and `notify` method on inherited classes
* `Observable` - Need to implement `onUpdate` method on inherited classes

The concrete `Observable` classes, like `WeatherStation`, should keep track of a list of `Observable`s and notify them whenever there is an update.

Also, it is suggested that concrete `Observer`s should keep a reference to the `Observable` they are subscribed to, to get the state whenever they want, say through `weatherStation.getWeather()`


<br><br>



---
## 3.0 - __Command__ 🗯

__Reference [HERE](https://www.youtube.com/watch?v=9qA5kw8dcSU)__

The definition:

> __Command__ pattern encapsulates a request as object, thereby letting us parameterize other object with different request queue or by require and support undoable requests.

In essence, __Command__ design pattern is similar to __Strategy__ pattern, where the methods of `Invoker` is an object rather than merely functions.

The __Command__ pattern consists of `Invoker` (the one sending the commands), `Receiver` (the one receiving the commands), and `Command` themselves. An abstract `Command` would commonly have an `execute()` and `unexecute()` method, and used to create concrete `Command`s like `TurnOnCommand` and `ChangeSpeedCommand`

---

### Problem:

Think of this: You are programming for a programmable/configurable remote control, where each button can be configured to perform different actions. How would you program such system?

Maybe you suggest to have a internal state keeping track of what each button does, encoded as string or integers. Like:

```json
{
    button1Action: 'turnon',
    button2Action: 'changeSpeed'
}
```

Then in the actual event handler, we could:

```java
public void onButton1Pressed(args) {
    if (state.button1Action == 'turnon') ...
    else...
}
```

---

### Solution:

However, if you learnt __Strategy__ pattern, where methods themselves are already objects, suddenly we can just have our code like so:

```java
class RemoteControl {
    Command button1Command = new TurnOnCommand(receiver);
    Command button2Command = new ChangeSpeedCommand(receiver);

    public void onButton1Pressed(args) {
        button1Command.execute(args);
    }
}
```

The actual implementation of the command is now encapsulated inside the concrete `Command` itself. For example in the `TurnOnCommand`, `exeucte()` will contain `receiver.turnOn()`.

Now, since the `Command` itself had became class attribute, the `Command` suddenly become very easily swappable in the `Invoker`!

---

### Furthermore...

That's not all the benefits of __Command__ pattern! Think: functions themselves cannot possibly be saved in data structure (Unless you are using a language where functions are first class citizens), but `Command` object can! This opens up the possibility of __History__ and __Undo__ functionality!

Previously in our `Command` interface, we have `execute()` and `unexecute()`. If those `Command` are saved in the `Invoker` as a __Stack__ data structure, we could now very easily perform __undo__! Just pop the top `Command` and call its `unexecute()`!

<br><br>

---


## 4.0 - Iterator ⛓

__Reference [HERE](https://www.youtube.com/watch?v=uNTNEfwYXhI)__

The definition of __Iterator__ pattern is:

> The __Iterator__ pattern provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

The __Iterator__ pattern iterates over the items in a collection, enumerating all the items in the collection.

We shall be quite familiar with iterators, especially those coming from `Python`. `range()`, `for ... in ...` all utilizes range (And __Generators__). 

The __Iterator__ pattern has certain advantages:

* Abstract away underlying data structure (Set, List, Tree..., all are iterable!)
* Do not expose the whole data structure at once - You'll only get the next element when you call `next()`.
* Lazy evaluation, especially effective on infinite collection like Fibonacci number generator.
* Avoiding mutation of the underlying data
* Ability to pause iteration and resume it whenever possible.

With iterator, we are able to abstract away on how to iterate over a data structure. No matter we have arrays (which iterate by index), linked list (iterate by pointer), tree (preorder, postorder, inorder, level order), or set etc, we will always use the common interface of __Iterator__.

---

### Solution:

The common way of implementing an __Iterator__ is by first defining two interfaces, `Iterable` and `Iterator` (Sounds familiar in `Java`?)

* The `Iterable` will only require to have the method `getIterator()`. In Python, this is done by `__iter__()`.
* The `Iterator` will have several methods, like `hasNext()`, `next()`, and `current()` (maybe?)

With these two classes, __Iterator__ pattern is very easily implemented. 

<br><br>

---

## 5.0 - State 🎞️

__Reference [HERE](https://www.youtube.com/watch?v=N12L5D78MAA)__

The __State__ pattern states that:

> The __State__ pattern allows object to alter its behavior when its internal state changes. The object will appear to change its class.

The __State__ pattern, essentially is the way of implementing a __State Machine__, which involves states, connected by transitions, and outputs. With the __State__ pattern, we are able to make different decision based on the state that we are currently in.

The __State__ pattern consist of, first, the `Context` interface, which we can think as the entire of the __State Machine__. For example, a `Game` that will have different states, is considered a `Context`. The `Game`'s `render()`, `update()`, and `input()` method etc will have different behavior depending on the `State` that it is currently in. Then of course, the `Context` will contain a single concrete `State` that implements the unified interface.

The __State__ pattern is very commonly used in games or anything that can be represented in different states. It is much more easier to use compared to, say using `if-else` statements to check for individual boolean values to determine the next action.

---

### Example:

The Gate/Validators that we see in Metro stations which require scanning of tickets or Identification Card(IC), can be a good example where we will use the __State__ pattern.

The Metro Gate may have different states such as `GateOpenState`, `GateCloseState`, and `GateProcessingState`. Each one of these states should implement the common interface `GateState`, which includes the output methods `getSensorLight()` and `getMessage()` as well as their own transition function `transition()` depending on the input. For example, within the `GateProcessingState`, if `transactionSuccess()` is invoked, then the state should be transitioned to `GateOpenState`.

<br><br>

---

## 6.0 - Null Object ⁉️

__Reference [HERE](https://www.youtube.com/watch?v=adGhT_-JbZI)__

The __Null Object__ design pattern is defined as 

> A __null object__ is an object with no referenced value or with defined neutral ("null") behavior. The null object design pattern describes the uses of such objects and their behavior (or lack thereof)

Does it ever occurred to you when writing code, that your method takes in a argument, and you realize that you need to __null check__ the argument before proceeding with your normal logic? Isn't it somehow better if we are able to treat `null` as if it is an expected object without __null checking__?

This is exactly what __Null Object__ pattern proposes. Instead of having to check for `null` value which introduces more branching and complicate our code, we will introduce a __Null Object__, which implements the same interface as the object we'll expect, yet the behavior is same as that of what we'll do in case of `null` value. Using this pattern eliminates the following code:

```java
if (obj == null)
    // Code that executes when obj is null
else
    // Code that executes if non-null
```

The __Null Object__ can be considered as an extension of the __Strategy__ pattern, where concrete classes don't exactly have to own a particular method (Strategy), by defining a `NoMethod` class that will be used instead.

---

### Situations:

* We are developing a forum website. In `PostList` we have a `addPost(post)` method. We realize that the `post` argument passed in may be null. In this case, instead of say:

    ```java
    if (post == null)
        return "<li></li>";
    else
        return "<li>" + post.getEscapedText() + "</li>";
    ```
    What we can do to eliminate the above snippet is to define a `EmptyPost` object, that when `getEscapedText()`, `getAuthor()` or `getDate()` is called, returns empty string.

* We are developing a game. Our character, `Avatar` has 4 methods `moveLeft()`, `moveRight()`, `moveUp()`, and `moveDown()`. We have decided to use __Strategy__ pattern so that each methods are actual object themselves, like `AvatarStrategy moveLeftStrategy = new MoveLeftStrategy(this)`. 

    Then, we decided that in some levels, the `Avatar` shouldn't be able to move up or down. In this case, we can define a `NullMoveStrategy` and assign it to the strategy responsible for moving up and down

* We are designing a GUI application. We have `OKButton` and `CancelButton` in our message box. We've decided to implement __Command__ strategy so that each button is tied to a single `Command`. Now, in some circumstances we may want to disable the `OKButton` normal behavior. Then using __Null Object__ pattern, we tie the `OKButton` with the `NothingCommand` that does nothing upon `execute()`.

* When `getIterator()` is called on a collection that is empty, an instance of `EmptyIterator` may be returned, which `hasNext()` is always set to false. (Or in __Python__, always raise `StopIteration`)

<br><br>

---

## 7.0 - Visitor 🏃🏼

The __Visitor__ design pattern, definition:

> The __Visitor__ design pattern is a way of separating an algorithm from an object structure on which it operates. A practical result of this separation is the ability to add new operations to existing object structures without modifying the structures

This design pattern is exactly what the name is implying. We have a object, that will be "visited" by a __Visitor__, which will modify the behavior of the object without modifying the underlying code structure of the visited object. 

---

### Example:

We have opened up a shop that consist of multiple `Goods`. Each one of the concrete `Goods` have a `getOriginalPrice()` method to return the price of the item. 

Suddenly, the government imposes some tax to be applied on different goods. That means the price returned by the `getOriginalPrice()` is no longer the price that should be charged to the buyer. There may be __Wine Tax__, __Service Tax__ or __Sugar Tax__.

Without having to modify the code on the concrete `Goods` itself, we can directly inject a new method `getPriceAfterTax(Visitor)` method into the `Goods`, which will accept a `Visitor` in the parameter, returning the modified price after tax is imposed on it.

Now whenever we need to calculate the price on various goods, we use the `getPriceAfterTax()` method, passing in the correct `Visitor` that corresponds to the type of good we are selling.


<br><br>

---

## 8.0 - Chain of Responsibility 🏃🏼

The definition for __Chain of Responsibility__ is:

> The __Chain of Responsibility__ involves sending data to an object for processing, and if that object can't use it, it sends the request to other objects that may be able to use it. This decouples the request and its processing.

Usually, we want to process some input data. The data can either be __(1)__ processed under several operations, or there are __(2)__ several possible operations possible, but one and only one is able to process the data given.

Without __Chain of Responsibility__, you might implement it as so:

__(1)__
```java
if (data.satisfyCondition1)
    // process 1
if (data.satisfyCondition2)
    // process 2
if (data.satisfyCondition3)
    // process 3
```

__(2)__
```java
if (data.satisfyCondition1)
    // process 1
else if (data.satisfyCondition2)
    // process 2
else (data.satisfyCondition3)
    // process 3
```

This `if else` branching may bloat up as the condition grows. What __Chain of Responsibility__ suggests is to separate each condition into individual `Handlers`, and the data is passed through the chain of `Handlers`, just like a water flowing through a pipe, with processing capability.

This pattern is seen commonly in __Middlewares__, where data is processed before reaching the terminal. For example, in `Node.js`'s `express.js` framework, middlewares are essentially implementing this pattern! __Middlewares__ like `express.json()` and `express.static()` will receive the HTML request passed to it, and after processing, pass to the next middleware via `next()` method.

---

### Problem Statement:

We want to implement a calculator. Instead of doing it as so:

```java
if (operation == '+') // do addition
else if (operation == '-') // do substraction
...
```

We can use __Chain of Responsibility__ and decouple each operation into independent units instead. This proves to be particularly useful when our calculator starts to develop!