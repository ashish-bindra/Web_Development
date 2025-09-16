# Radis (In-memory db)

- It is faster not big
- TO access API records faster
- Open source in-memory data strucure store which can be used as a database or a cache and message broker
- No SQL key/value storage
- support mulltiple data strucures
- Built in replication(Master-slave server)

**Radis:** Data ia not an ordeing database
we are uing radis as cache, as a message broker as a streming engine and more

Q1. whiat is Radis?
Q2. Why use Radis?
Q How to implemet?
Q4. How improve the performance
Deep driven radis
pic

Q1. What is Radis
Radis is in-memory database which mean it store data in Random Access(RAM).
By doing that its read and write speed is faster

Tradistional DB like MySQL, MongoDB for read and write purpose they are using computer disk

Modren ssp took zoom to read data but when we using Ram it took zons that why radis se RAM as perimary storage thats why we
can able to access data very fast.

- It has disk persistance it an distional feature for durability behind the scan radis  store shape short of data in ssd/hdd so when server restart we wont loss our data

- Thsi adavantage you have seen in preformance we are using cashing system  as radis
so in  see your can access deler by application by doing so user experce is else impoved and primary database load also reduces

## Data types that radis supports

1. String
2. List
3. Set
4. Sorted sets
5. Hashed (key-value)
6. Bitmaps
7. Hyper logs
8. Geospatial indexs

last 3 are compilacated

## Advantages

- Very Flexible
- No schemas and column Name
- Very Fast: Can perform aroung 110000 sets per sec about 110000 set per sec
- Ritch Datatype support
- Caching & Disk per s

## Radis-cli

```
