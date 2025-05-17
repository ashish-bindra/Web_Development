## jQuery

Plain javascript (Vanilla JS), we required to write everything on our own jQuery is js libray

Vanililla JS Code:
----------------

var myh1 = document.querySelectorAll('h1');

for(h1 of myh1){
    h1.style.color = 'red';
}

jQuery:
------
$('h1').css('color','red')

- Jquery is a JS libray
- It contain serval functions and objects to select/grab html element and to mainipulate styles very easily.

- AJAX, Animations
- Browser compatibility

Advantages:
----------
- Rich Library ... less code and do more
- readability
- clear and shorter code
- Ease of use
- AJAX support
- Cross Browser support

Limitation *
-----------
*** Youmightnotneedjquery.com***

1. Whatever jquery is doing....js can do
2. Performance effect
3. just to use $() 10K line code need to load


### How to connect with JQuery:
1. By locally
2. By CDN
- minified : for production
    - no comment no spaces   
- uncompressed: for developer

Element Selector
id selector
class selector
* selector
descendent selector
adjucent selector
attribute selector
nth-of-type

h1:nth-of-type(odd){}


Manipulate HTML Elements:
--------------------------
$() ===> To select/Grab html element
css() ==> To manipulate elements


```js
$('li')
$('li:nth-of-type(2)').css('background', 'pink')
$('li:nth-of-type(odd)').css('background', 'red')

$('li:first')
$('li:first-od-type')
$('li':nth-of-type(1))
$('li').first()


$('li').last()
```

Q1. Write Vanilla Js and jQuery code to change all h1 tags text color as awhite and backgraound as red?
```js

var allh1 = document.querySelectorAll('h1`)

for(h1 of allh1s){
    h1.style.color = "white"
}

$('h1').css({color: "white', background: 'red'}); 
```
Q2. Write VJS and jQuery cod to set all li tags font size as 20px

```js

var all = document.querySelectorAll('li')

for(li of all){
    li.style.fontSize = '20px';
}

$('li').css('fontSize', '20px')

```

1. Select all paragraph tags and set background as green
```js
 $('p').css('background', 'green')
```
2. Select all paragraph tags with class 'remaining' and make them 200px width
```js
$('.remaining').css('width', '200px')
```

3. Select all paragrap
5. Select only 3rd p tag and change fontsize as 30px
```js
$('p:nth-of-type(3)').css('fontSize', '30px')
```