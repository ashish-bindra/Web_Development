# JavaScript
- Java Script is Full pledged Programming Language. 
- The main purpose of java script is to add functionality (actions) to the HTML.
- Usually we can Java Script in the Front-end and we can use Node JS for Back-end.

## 1. JavaScript Developer's Console
We can use this developer's console to test our java script coding snippets. 
- This is just for testing purpose only and usaully not recommended for main coding.

### How to Launch JavaScript Console: 
- Browser => Right Click => Inspect =>  Console 
- Short-cut: Ctrl+Shift+j

**Note:**
1. To clear console we have to use clear() function. 
2. ; at end of statement is not mandatory in newer versions.

## 2. The 5 Basic JavaScript Primitive Data Types 
Java Script defines the following 5 primitive data types

1. Numbers
2. string
3. boolean
4. null 
5. undefined

1. Numbers:
All these are of "number" type 10 , -10 , 10.5
-  Java Script never cares whether it is integral or float-point or signed and unsigned.
- General Mathematical operators are applicable for numbers
    -  10+20 
    -  10-20 
    -  10/20 
    -  10*20 
    -  10%3 
    -  10**2

Note: We can check the type of variable by using typeof keyword typeof x;

2. string:
Any sequence of characters within either single quotes or double quotes is treated as string.
    
    - 'ashish'
    - "ashish"
- We can apply + operator for Strings also and it acts as concatenation operator.
- Rule: If both arguments are number type then + operator acts as arithmetic addition operator. 
- If atleast one argument is of string type then + operator acts as concatenation operator.
    -   10+20 =>30 
    -  'ashish'+10 => ashish10 
    -  'ashish'+true => ashishtrue
- We can use esacape characters also in the string.
    - 'durga\nsoft' 
    - 'durga\tsoft' 
    - 'This is \' symbol' 
    - 'This is \" symbol' 
    - 'This is \\ symbol'

### Q. How to find the number of characters present in the string? 
We can find by using length variable
- Eg:'durgasoft'.length

### Q. How to access characters of the String? 
- By using index 
- index of first character is zero
 
        'durga'[2] // r 
        'durga'[200] // undefined but no error 
        'durga'[-1] // undefined

> Note: If we are trying to access string elements with out of range index or negative index then we will get undefined value and we won't get any Error.

3. ***boolean:***
The only allowed values are: true and false (case sensitive)

## JavaScript Variables 
Variables are containers to store values.
- Syntax: var variableName=variableValue 
- Eg: 

        var name = "durga" 
        var age = 60 
        var isMarried = false

> Note: JavaScript variables follow CamelCase Convention 

    - studentMobileNumber => Camel case(Java,JavaScript etc) 
    - student_mobile_number => Snake Case(Python ) 
    - student-mobile-number => Kebab Case(Lisp)

Based on provided value automatically type will be considered for variables.

    Eg: var x = 10 
    typeof x => number 
    x = false typeof x => boolean

Hence Java Script is dynamically Typed Programming Language like Python

4. ***null and undefined:***
Variables that are declared but not initialized, are considered as undefined
    - Eg:
     ```js
     var x; 
    - typeof x // undefined
    ```
- null value means nothing. 
- If the value of a variable null means that variable not pointing to any object.
- var currentplayer = 'durga' 
- currentplayer = null //game over
## methods
### 3 most commonly used functions:
1. `alert()`
2. `prompr()`
3. `console.log()`

1. ***alert():**
To display alerts to the end user
    ```js
    alert('Hello there')
    alert(100000) 
    alert(10.5)
    ```
2. console.log(): 
To print messages to the developer's console 
    Eg: console.log('Hello there') 
    console.log(10*20) 

These console message not meant for end user.

3. prompt(): 
- To get input from the end user 
    - `prompt('What is Your Name:')`

- Here we are not saving the value for the future purpose. But we can save as follows 
    - `var name= prompt('What is Your Name:')`

- Based on our requirement we can use this name 
    - `console.log('Hello '+name+' Good Evening') `
    - `alert('Hello '+name+' Good Evening')`

### How to write JavaScript to a seperate File and connect to HTML:
- demo.js: 
 `alert('Hello everyone good evening')`

- html: 
- We can link javascript file to html by using the following <script> tag. 
- <script type="text/javascript" src="demo.js"></script> 
- We can take this script tag either inside head tag or body tag. If we are taking inside head tag then javascript code will be exeucted before processing body. 
- If we are taking inside body tag then javascript code will be executed as the part of body execution.
<!-- <script type="text/javascript" src="domo.js"></script> -->
we can take this on body as well as head part also

- if we take in head part first js will executed after then body will be consider
- if we take in body then first body will execueted after that js will execute

### Demo Application: Age and Death Calculator
demo.js:
```js
var name=prompt('Enter Your Name:');
var age=prompt('Enter Your Age:'); 

agedays = age*365.25 
remainingdays = (60-age)*365.25; 
alert("Hello "+name+"...\nYour Current Age:"+agedays+" days\nYou will be there on the earth only "+remainingdays+" days. No one can change including God also");
```

## Operators:
-------
1. Airthmetic:
+-*/%**

2. comparison:
<,><==, >==, == !=

### Difference between == and ===:
--------
- In the case of == operator internally type coersion will be performed. Hence if arguments are different types first both arguments will be converted to same type and then comparison will be performed. Hence both arguments need not be same type.
    Eg:
    10 == "10" // true 
    10 == 10  //true
- Here only values are important but not types.
- But in the case === operator, type coersion won't be performed. Hence argument types must be same, otherwise we will get false.
    - 10 === 10 // true 
    - 10 === "10" // false
Note: 
- == => Normal equality operator where types are not important but values must be same 
- === => Strict equality operator where both types and values must be same

It is recommended to use === operator because it is more safer and more specific.

== only content will compare but int the case of === equal in addition to content types also be consider thats why === equal is strickt equality

10 == "10" # true
one is number other one is string the answer is true
it never going to check type

10 === "10" # false

null == undefined # true
Nan ==> 0/0


### for any x value including NaN
If the result is undefined then we will get NaN 
Eg: 0/0 // NaN

- For any x value including NaN the following expressions returns false
    - x < NaN
    - x <= NaN
    - x >  NaN
    - x >= NaN
    - x == NaN
For any x value including NaN the following expression returns true x != NaN
always returns false

x !=  NaN

It return true
- X && Y => If both arguments are true then only result is true. i.e if atleast one argument is false then the result is always false
- X || Y => If atleast one argument is true then the result is true. i.e if both arguments are false then only result is false.

## Logical operators:
-----------------

&& ===> AND if both arguments are true
||  ===> OR if ateast one arument is true
! ==> complement


true && false
true || false
!false

## In the logical operator
------------------------
1. 0 value is always treated as false
2. non-zero value is always treated as true
3. '' string  treated as false
4. null, undefined, NaN are treated as false only.

## Condtional statement / Selection
-------------------------

if
if-else

if(b){
    action if b is true
}
else{
    action if b is false
}


1. Write a JS code to check whether the given number is even or not.

### To read number from end user prompt is required
```js
var num = prompt("Enter any number to check: ")
alert(typeof num) // string
if (num % 2 == 0){
    alert("Given Number is Even!!!")
}
else{
    alert("Given Number is not Even")
}
```

```js title="Number type"
var num = Number(prompt("Enter any number to check: "))

alert(typeof num) // Number type

if (num % 2 == 0){
    alert("Given Number is Even!!!")
}
else{
    alert("Given Number is not Even")
}
```

#### Read age from the end user

age < 18
age > 60
```js
var age = Number(prompt("Enter Your Age: "))

if(age > 60){
    alert("Plz wait some more time definetly you will get best match!!! ")
}
else if (age < 18){
    alert('Ypor age is alredy crossed marriage age...No chance of getting marriage!!!')
}
else{
    alert("Thnaks for registration you will get match details by email!!!")
}
```

## Iterative statement / loops:
--------------------------
If want to execute a group of statemnt for multiple types

DRY principle: Font Repeat Yourself

console.log("Hello")
console.log("Hello")
console.log("Hello")
console.log("Hello")
console.log("Hello")
console.log("Hello")
console.log("Hello")


for(59){
    console.log("Hello")
}
It reducre length of code, and readbilty increase

### Loops in js:
1. while
2. for 
3. for-of
4. for-in
5. for-each

### while: 
As loon as some condition is true keep on executing the code

while(condition)
{
    body
}

1. To print Hello 10 times
```js
var count = 1

while(count <= 10){
    console.log("Hello " + count);
    count++ 
}
```
2. To print each charcter present inside a string:
```js
var s = prompt("Enter some word: ")
var i = 0

while(i < s.length){
    console.log(s[i]);
    i++
}
```
#### for loop
1. General for loop
2. forEach() (array)
3. for-of loop (array)
4. for-in loop (object)

1. General for loop

```js
for (var i = 0; i <10; i++){
    alert(i)
}
```

while vs for
-----------
- If we know number of iteration in advance ==> for loop
- If we dont know number of iterations in advance and as long as some condition is true then execute loop body....


Secreat Agent Application:
--------------------------
Rules:
1. The first character of the name should be 'd'
2. The last character of FAvourite Actor should be 'r'
3. the lucky number should be 7
4. the length of dish should be >= 6


```js
var name = prompt("Enter Your Name: ")
var actor = prompt("Enter Your Favourite Actor:")
var lucky = prompt("Enter Your Lucky Number:")
var dish = prompt("Enter Your Favorite Dish:")

var nameCondition = false
var actorCondition = false
var luckyCondition = false
var dishCondtion = false

if (name[0] =='d'){
    nameCondition = true;
}

if(actor[actor.length-1] == 'r'){
    actorCondition = true;
}

if(lucky == 7){
    luckyCondition = true;
}

if(dish.length >= 6){
    dishCondtion = true;
}

alert("Hello: " + name + "\n Thanks for providing information")

if(nameCondition && actorCondition && luckyCondition && dishCondtion){
    console.log("Helllo Secreate Agent .. Next Operation is");
    console.log("We have to kill atleast 10 sleeping students in the class room b'z these are burden to the country!");
}
```

## Function
If code is repetedly required neer recommended to write such type of code we have to write inside a fuction

to delar a fuction
---------------------
        function functionName(arguments){
            body ...
            retuen value;
        }

- types of parater is optional becouse js is dynamic type
 
```js
function greeting(){
    console.log("Hello Good Evining!!!");
}

greeting()
```

functions with arguments
-----------------------
```js
function greeting(name){
    console.log('Hello ' + name + " Good Evning");
}

var name = prompt("Enter Your Name ")
greeting(name)
```

if we dont pass name if will show undefined

to solve this proble we use default argument
```js
function greeting(name="Guest"){
    console.log('Hello ' + name + " Good Evning");
}

var name = prompt("Enter Your Name ")
greeting()
greeting(name)
```

Function with return values
-------------------------
it will only return one value 

### Write js finction to take number as argument and return its square value
```js
function squareIt(number){
    return number * number;
}

var result = squareIt(4)

console.log("The square of 4 is " + result);
console.log("The square of 5 is " + squareIt(5));
```

### String as argument and return Capitilized String
sunny
Sunny

```js
function captalize(str){
    return str[0].toUpperCase() + str.slice(1);
}

console.log(captalize("ashish"));
```

### To find factorial of given number
### To convert from SnakeCase to KebabCase

Snake case: total_number => words seprate with `_` symbols
Kebab case: total-numer => words seprate with `-` symbols

```js

function snakeToKebob(str){
    var newStr = str.replace("_", "-");
    return newStr;
}

console.log(snakeToKebob("total_number"))
```

* Only first ocurence will be replace

```js
function snakeToKebob(str){
    var newStr = str.replaceAll("_", "-");
    return newStr;
}

console.log(snakeToKebob("total_number_asd"))
```

## Java Script Scopes:
1. Global Scope : The variables which desclar outside of function
2. Local Scope

```js
var x = 10 //global

function f1(){
    console.log(x);
    var y =20; // local variable
    console.log(y)
}
f1()
```
```js

var x = 10 //global

function f1(){
    var x =20; // local variable
    console.log(x) //20
}
f1()
```

## Higer Order Function (decorator in python)
A Function can return another function also

setInterval(functionName, 3000) // this function will be executed for every 3000 milisec, it will continpous infintly

- setInterval() return some value to stop this we pass that value to that function
- claarInterval(1)

```js
function singASong(){
    console.log("Rangamman...Mangamma...")
    console.log("Jil..Jil ...Jigel...Rani...")
}
setInterval(singASong,3000)
```

## Anonymous Function:
We can delacrea function without a name, such type of nameless function is called anonymous
- Just for one time use
- just for instance use

```js
setInterval(function() {console.log("Anonymous Functions")}, 2000)
```

## Array (same as list in python)      
An indexed collection of elemnts

var n1 = 10;
var n2 = 20;
var n3 = 30;

var numbers = [10,20,30,40]

### How to access array elements
index => acces by using index
numbers[1]

### How to update array elemnts:
numbers[2] = 22;

### Is it possible to add new elements
No, 

### Adding new elemnt to the array
numbers[4] = 50

Is it valid or Is it Invalid ?
100% this one is

retrieve
update
add

```js
var friends = ["ashish", "sunny", "bunny", "chinny"];

console.log(friends)

friends[4] = "katrina"
friends[20] = "kreena" 

console.log(friends) // (21) ['ashish', 'sunny', 'bunny', 'chinny', 'katrina', empty × 15, 'kreena']
```

### create empty array

1. var nums = []
2. var numbers = new Array();

### How to find length of an array
legth varable

> nums.length
> friends.length

### is allow to hetrogenous element
yes, 

    var random_collection = ["as", 12, true, null];

### Important methods related to JavaScript arrays:

1. push()
2. pop()
3. unshift()
4. shift()
5. indexOf()
6. slice()
7. splice()

#### 1. push()
To add an element at last postion

```js
var numbers = [10,20,30,40]

console.log(numbers) // (4) [10, 20, 30, 40]

numbers.push(50)
console.log(numbers) //(5) [10, 20, 30, 40, 50]
```

#### 2. pop()
To remove and return last element
```js
console.log(numbers) // (4) [10, 20, 30, 40]
console.log(numbers.pop()) // 40
```

#### 3. unshift()
Is like pus() except that it will add in first place
```js
numbers.unshift(777)
console.log(numbers) // (4) [777, 10, 20, 30]
```

#### 4. shift()
is like pop()

```js
numbers.shift()
console.log(numbers)  // (3) [10, 20, 30]
```

#### 5. indexOf()
return first orccurence, if specifed elemnt not avaliable then return -1
`console.log(numbers.indexOf(10))`

#### 6. slice()
returns from begin index to end-1  index
`console.log(numbers.slice(2,5))`

for clone purpose 
`numbers.slice()`

#### 7. splice()
Removes elements from an array and, if necessary, inserts new elements in their place, returning the deleted elements.
```js
arr = [1,2,3,4,5]
arr.splice(0,2) // [3, 4, 5]
```
### Nested Array 
array of array concept (zagged array)

```js
var nums = [
    [10,20,30], 
    [40,50,60],
    [70,80,90]
]

console.log(nums[0][0])
console.log(nums[0][1])
console.log(nums[1][0])
```

```py title="program to add list of books collection"
var books = []
var input = prompt("WHich operation you want to perform [add | view | exit]:")

while(input != "exit"){
    if(input == "add"){
        var newBook = prompt("Enter Name of the Book to add:");
        books.push(newBook);
    }
    else if (input == "view"){
        console.log("List of Avaliable Book")
        console.log(books)
    }
    else{
        console.log("Choose valid Operation");
        
    }
    input = prompt("Which operation You want to perform [add | view | exit]:")
}
console.log("Thanks for using our application")
```

```js title="while"
var numbers = [10, 20, 30, 40, 50]
var i = 0

while(i < numbers.length){
    console.log(numbers[i]);
    i++;
}
```

```js title="for"
var numbers = [10, 20, 30, 40, 50]

for(var i = 0; i < numbers.length; i++){
    alert(numbers[i])
} 
```
#### for of
```js title="for of"
var numbers = [10, 20, 30, 40, 50]

for (x of numbers){
    alert(x);
}
```
#### forEach() method:
arratobject.forEach(function)

for each element present in array apply specified function
```js
var numbers = [10, 20, 30, 40, 50]

numbers.forEach(function (x) {alert(x);})
```

```js
var heroines = ["sunny", "malika", "veena", "kartrina", "karena"]
heroines.forEach(alert);
```

### How to delete array elements based on index:
- pop(), shift(), slice()

`heroines.slice(3,6)`

- array is mutable
- string is immutable
- Once we create string object we cannot perform any changes to that object.
- If we are trying to perform any chages then with those changes a new object will ber created.

- array mutable eg
```js
var heroines = ["sunny", "malika", "veena", "kartrina", "karena"]

heroines[0] = "money"
console.log(heroines) // // var heroines = ["sunny", "malika", "veena", "kartrina", "karena"]

```
- string immutable eg
```js
var name = "Sunny"

name[0] = 'B'
console.log(name) // Sunny
```

### Q1. Write a JS function to take an array as argument and print its elements in reverse order
```js
nums = [1,2,3,4,5]

function rev(arr){
    return arr.reverse();
}
console.log(rev(nums))
```
### Q2. Write a JS function to take an array as argument and check wheather all elements are identical or not (same or not)
```js
nums = [1,1,1,1,1]

function iden(arr){
    var i = arr[0];
    for(v of arr){
        if(i!=v){
            console.log("Not identical");
            return false
        }
    }
    return true
}
console.log(iden(nums))
```

### Q3. Maximum value of given array?
```js
nums = [1,2,3,4,5]
function max(arr){
    max = arr[0];
    for(v of arr){
        if(max<v){
            max = v;
        }
    }
    return max
}
console.log(max(nums))
```
### Q4. Sum of elements present in the given array?
```js
nums = [1,2,3,4,5]

function sumarr(arr){
    var n = 0
    for(v of arr){
        n+=v;
    }
    console.log(n)
}
sumarr(nums)
```

### Book Management Application:
-------------------------------
add, list, exit, delete

```js
var books = []
var input = prompt("Which operation you want to perform [add | view | delete | exit]:")

while(input != "exit"){
    if(input == "add"){
        addBook();
    }
    else if(input == "view"){
        viewBook();
    }
    else if(input == "delete"){
        deleteBook();
    }
    else{
        console.log("Please choose valid option");
    }
    input = prompt("Which operation you want to perform [add | view | delete | exit]:")
}
console.log("Thanks for using our application!!")

function addBook(){
    var newBook = prompt("Enter Book name to add:")
    books.push(newBook)
}

function viewBook(){
    console.log("List of avaliable Boos:")
    for(book of books){
        console.log(book);
    }
}

function deleteBook(){
    var name = prompt("Enter Name oof the book to delete:")
    var index = books.indexOf(name)
    
    if (index ==-1){
        console.log("Specified book not Avaliable") 
    }else{
        books.splice(index,1)
        console.log("specified Book Deleted");
    }
}
```

### object // (map,dict)
------
want to repres jey-value pairs 

var variablename = {key1: value1......}
```js
var movie = {
    name: "Bahubali",
    year: 2016,
    hero: "Prabhas"
}
```
### How to access values from the object
-----------------------------------------
Order is not applivcable and hence index not applicable.

```js
var movie = {
    name: "Bahubali",
    year: 2016,
    hero: "Prabhas"
}

console.log(movie.name);
console.log(movie["hero"]);
```

### How to create an insilize empty object

var nums = {}

var nums = new Object()


nums["fno] = 100

nums.sno = 200

## Iterating Objects:
------------------------
Recommended to use for-in loop
; => in newer version it is optional
 
```js
var nums = {fno: 100, sno: 200, tno: 300}

for(key in nums){   
    // console.log(key)
    // console.log(nums[key])
    console.log(key + ": "+ nums[key]) // recomended
    // console.log(key + ": "+ nums.key) Not working
}
```

## Arrays vs Objects
array:
1. individual object
2. order will be maintained
3. By using index we can access and update data

Objects:
1. ket-value pairs
2. order wont maintained
3. By using key 

### Nesting of Arrays and Objects

arrays of ojects:
----------------------
var moviews = [ { name:"b", yeay:1111,hero:"pra},
                { name:"b", yeay:1111,hero:"pra},
                { name:"b", yeay:1111,hero:"pra}]
```js
var movies = [
    {name: "Sanju", year: 2016, hero: "Prabhas"},
    {name: "Bahubali", year: 2018, hero: "Ranbir"},
    {name: "spider", year: 2017, hero: "Mahes"},
]
console.log(movies)
console.log(movies[1])
console.log(movies[0]["hero"])
```

ojects of arrays
----------------

var numbergroups = {
    fg: [10, 20,30],
    sg: [1,2,3],
    tg: [22,33,44],
}

Object Methods:
----------------
method as a member
javaScript objects can conatin methods also

```js
var myobj = {
    a: "apple",
    b: "banana",
    m1: function(){console.log("Object Method");}
}

myobj.m1()
```
### this keyword

`this` => current object

```js
var movie = {
    name: "Bahubali",
    year: 2016,
    hero: "Prabhas",

    getInfo: function(){
        console.log("Moview Name: " + this.name);
        console.log("Released Year: " + this.year);
        console.log("Hero Name: " + this.hero);
    }
}

movie.getInfo()
```

### It is possible to refer already existing function as object method.

```js
function demo(){
    console.log("Name of fun is " + this.name)
}

var movie = {
    name: "Bahubali",
    year: 2016,
    hero: "Prabhas",

    getInfo: demo
}
movie.getInfo()
```

### mini - pro 
- I watched Bahubali and Moview is Hit!!!
- I have not seen Sanju but Movie is Hit!!!
- I watched Spider and Moview is Flop!!!

name
iswatched
isHit

```js
var movies = [
    {name: "Bahubali", isWatched: "true", isHit: "true"},
    {name: "Sanju", isWatched: "flase", isHit: "true"},
    {name: "Spider", isWatched: "true", isHit: "false"},
]

movies.forEach(function(movie){
    var result = ""

    if(movie.isWatched == 'true'){
        result = result + "I watched ";
    }
    else{
        result = result + "I have not seen ";
    }
    
    result = result + movie.name

    if(movie.isHit == 'true'){
        result = result + " and Movie is Hit!!!"
    }else{
        result = result + " and Movie is Flop!!!"
    }
    console.log(result);
});
```