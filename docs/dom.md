## DOM (Document Object Model)
By using DOM javascript can communicates with HTML and CSS

- document => Html
- Object => javaScript

it is a mediater/broker (interface)

<draw an image here>

dom always b/w html and js and act as intermediate
S

just type `document` on console you will get total html page
- document
- console.dir(document)

Document object conatins total hrml of a page

### Important DOM attribute
----------------------
- document.URL
- document.head
- document.body
- document.links

### Important DOM Methods
-----------------------------

To grap html elemnts into java secipt, we have to use the following methods on DOM

1. document.getElemntById('special')
2. document.getElementByClassName('first') //array
3. document.getElementByTagName('li')  //array

css selector

4. document.querySelector('#specila")
5. document.quertSelectorAll('.first');

examples
-------
```js
console.log(document.getElementsByTagName('h1'));
console.log(document.getElementsByTagName('p'))

console.log(document.getElementById('first'))
console.log(document.getElementsByClassName('special'))
console.log(document.getElementsByClassName('special')[0])

console.log(document.querySelector('#first')) 
console.log(document.querySelector('.special'))

console.log(document.querySelectorAll('.special'))
console.log(document.querySelectorAll('.special')[0])

console.log(document.querySelector('h1+p'))  
// p#first.special
```

### example to change the css

```js
var p1 = document.querySelector('#first')
var p4 = document.querySelector('#last')

p1.style.color = 'red';
p4.style.color = 'green';

```

```js
var h1 = document.querySelector('h1')
var p = document.querySelector('p')
var h2 = document.querySelector('h2')
var ul = document.querySelector('ul')

// console.log(document.querySelector('h1'))
h1.style.color = "red"
h2.style.color = "cyan"
p.style.color = "orange"
ul.style.color = "green"
```

To get random value
---------------------
```js
Math.floor(Math.random() * 15)
```

### Program to genrate the random color
```js
function getRandomColor(){
    var letters = "0123456789ABCSEDF";
    var color = "#"

    for (var i = 0; i<6; i++){

        var ch = Math.floor(Math.random() * 16)
        color = color + letters[ch]
    }
    console.log(color)
}
getRandomColor()
```

### JS program to genrate random color on html using js
```js
function getRandomColor(){
    var letters = "0123456789ABCSEDF";
    var color = "#"

    for (var i = 0; i<6; i++){

        var ch = Math.floor(Math.random() * 16)
        color = color + letters[ch]
    }
    return color
}

var h1 = document.querySelector('h1')
var p = document.querySelector('p')
var h2 = document.querySelector('h2')
var ul = document.querySelector('ul')

h1.style.color = getRandomColor()
h2.style.color = getRandomColor()
p.style.color  = getRandomColor()
ul.style.color = getRandomColor()
```

Demo program to change the color every seconds
```js
function getRandomColor(){
    var letters = "0123456789ABCSEDF";
    var color = "#"

    for (var i = 0; i<6; i++){

        var ch = Math.floor(Math.random() * 16)
        color = color + letters[ch]
    }
    return color
}

var h1 = document.querySelector('h1')
var p = document.querySelector('p')
var h2 = document.querySelector('h2')
var ul = document.querySelector('ul')


function changeColor(){

    h1.style.color = getRandomColor()
    h2.style.color = getRandomColor()
    p.style.color  = getRandomColor()
    ul.style.color = getRandomColor()
}

setInterval(changeColor, 1000)
```

### we can setup click on even t two types
1. addEventListener
2. onclick()
- document.getElementById("start").addEventListener("click", changeColor);
 

### TO grab html elements
```js
var myh1 = document.querySelector('h1');

console.log(myh1.textContent)
```

From javaScript by using dom we can change content of html also
#### TO change the content
```js
var myh1 = document.querySelector('h1');

myh1.textContent = "Ashish Bindra"
```

we can change innerHTML also
#### To change the content of innerHTML
```js
var myh1 = document.querySelector('h1');

myh1.innerHTML = '<a href = "https://abc.com"> abc.com</a>'

```

> Assingment: innerText vs textContet

#### To get the link and chage the link
```js
var abc = document.querySelector('a')
console.log(abc.getAttribute('href')) //https://abc.com

abc.setAttribute('href', "http://test.com")
console.log(abc.getAttribute('href')) // http://test.com

```

For javascript by using dom:
1. We can change content of html also textContent and inner html
2. We can get attribute values and we can chnage attribute values also

#### Assingment to change the linke color and backgraound color of google.com using console

```js
var links = document.querySelectorAll('a')

for(link of links){
    link.style.color = 'white'
    link.style.background = 'Green'
}
```

### Event Handling by using DOM
- event
- listener

#### To change background color by clicking the button using addEventListener

```js
function getRandomColor(){
    var letters = "0123456789ABCSEDF";
    var color = "#"

    for (var i = 0; i<6; i++){

        var ch = Math.floor(Math.random() * 16)
        color = color + letters[ch]
    }
    return color
}

// var btn = document.querySelector('#background')
var btn = document.querySelector('button')
console.log(btn)

btn.addEventListener('click',chageBgColor);

function chageBgColor(){
    var body = document.querySelector('body')
    body.style.background = getRandomColor();
}
```

```js title="anonymus function used"
var btn = document.querySelector('button')
console.log(btn)

btn.addEventListener('click',function (){
    var body = document.querySelector('body')
    body.style.background = getRandomColor();
}
);
```

listenter alway replonsible to listen events
- whenever event occures listener is going to certain action atomatically


### How To implemnt Event Handling

element.addEventListener(event, function)

function => activty 
#### Types of event
- click
- dblclick
- mouseover
- mouseout
- ...

#### To change color of h1 tage on single click operation:
```js title="anonymus function used"
var btn = document.querySelector('button')

btn.addEventListener('click',function (){
    btn.style.color = getRandomColor();
}
);
```
#### dbclick
```js title="anonymus function used"
var btn = document.querySelector('button')

btn.addEventListener('dblclick',function (){
    btn.style.color = getRandomColor();
}
);
```

#### Exersize like paperjs.org

#### mouseover
```js title="anonymus function used"
var btn = document.querySelector('button')

btn.addEventListener('mouseover',function (){
    btn.style.color = getRandomColor();
}
);
```

#### Assingment to create 3 button and perform following opration on them
1. on first bution click 
    -   Color of lackdround chage
2. scond buttion click
    - Coloe of bution change
3. houver of muse name of bution should chage into random city name 
- color of buttion should change 
- when you hover out it should back to normal

```js
function getRandomColor(){
    var letters = "0123456789ABCSEDF";
    var color = "#"

    for (var i = 0; i<6; i++){

        var ch = Math.floor(Math.random() * 16)
        color = color + letters[ch]
    }
    return color
}

function  getRandomName(){
    var names = ["HYD", "BANGALOR", "CHENNAI", "MUMBAI", "PATIALA", "LUCKHNOW", "PUNE", "MOHALI"]
    
    var i = Math.floor(Math.random() *(names.length))
    console.log(names[i])
    return names[i]
}

// var btn = document.querySelector('#background')
var btn1 = document.querySelector('#b1')
var btn2 = document.querySelector('#b2')
var btn3 = document.querySelector('#b3')

btn1.addEventListener('click',function (){
    var body = document.querySelector('body')
    body.style.background = getRandomColor();
}
);

btn2.addEventListener('click',function (){
    btn2.style.background = getRandomColor();
}
);
btn3.addEventListener('mouseover',function (){
    btn3.style.color = 'white';
    btn3.textContent = getRandomName();
    btn3.style.background = getRandomColor();
}
);
btn3.addEventListener('mouseout',function (){
    btn3.style.background = 'red';
    btn3.style.color = 'white';

    btn3.textContent = "Hover mee"
}
);
```

### Program to TTT Implementation(Tic-tac toe):
Assingment can done two way
- clicking one `x` xlixk again `O` then click again empty
- click to `x` duble click to `O` write click to earase
```js
restart = document.querySelector('#restart')
td = document.querySelectorAll('td')

console.log(restart)
console.log(restart.innerHTML)

restart.addEventListener("click",function(){
 for(cell of td){
    cell.textContent = ''
 }
});

function contentChange(){
    if(this.textContent ===''){
        this.textContent = 'X'
    }
    else if (this.textContent == 'X'){
        this.textContent = 'O'
    }
    else{
        this.textContent = ''
    }
}

for(cell of td){
    cell.addEventListener('click',contentChange)
}```