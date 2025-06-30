# Realtime communications

- chatapp
- Real time dashboard **
- Treading - stocks, teams, sport event

## 1. Long Polling

client sent request again and angin some interval of time
peos:

- Rest Implementation
- Works erverywhere

corns:

- High Latency
- Wastage

## Server sent Events

- lightweight
- work with proxies

can auto reconnect

-> less control on client side

## web sockets

if cannel open communicate both side

- Bi-direction
- scalable with brokers(kafka, radis)

corn:

- proxies

## public private key criptograpy

2 key genrate

1. public : Can share with anyone,
    - but data encript with public key will deript with private key only

    - public key should be distrubuted

2. private key: Not share with any one, should be scure

## stateless and statefull

stateless: we are not storing state anywhere in bd or file eg. jwt
statefull: we store information in db

## What is Jwt

Token need to be there for login

jwt =>  Json web Token

it an encripted token
token: collection of random character

three componet we have means three .

 there are alot of alog for encript
 eg sha256 ...

### jwr structure

1. which alogo we use
2. what info we have have
3. signature

Hearder = {
    alg:sh256
    typr:"jwt
}

payload = {
    "id/sub": "123213",
    "name": "ashish",
    "iat": 12312321321}

iat = isue at / experies at

token should exipre it very import
verify signature = your 256 bit secreate

## authtication

user give unique signature to serve

- to verfy the user

## authoize

- to authrize user which user need to acces which information

## How do you securley store a JWT on client side

store on local store , or we can store on session, cokkies.

- it should expire so need not to very

## use case of jwt

- authtication
-authorization
- information excenge

## how to invalidate jwt

- we nee dto fix the time of expire time

## refress token

whenever client send request it should send token also
some time token expire then server send 401 status code and server has refess taoken also use has 2 token access token and refres token it send the request and get new refess token

we stor erefress toekn in db

## JWT vs Session

3- tier macanism like client, server and db

whenver we request db we consume a resoure and it dalay in network
beacuse machine is process and we also proform read write i/o operration also

application logic is complex but they mainly perform crud operations

## session

state mens we goin statefull

to unique field in db
whenver we need to access a recource we need to call db everytime to validate

- we sould avoid  i/o operation less

<https://freeapi.app>
