
I highly suggest reading the book called "Grokking the System Design Interview" or use this [repo's](https://github.com/sharanyaa/grok_sdi_educative) pdf.

## Must Know Topics
* apis design (both rest and graphql)
* sql vs nosql
* caching system (position, policies, write strategies)
* load balancing
* tcp, http, polling, web sockets
* sharding & partitioning
* single point of failure
* indexes
* cdn
* client-server vs p2p 
* cap theorem

## Videos

* Caching: https://youtu.be/U3RkDLtS7uY 
* Tinder: https://youtu.be/tndzLznxq40 
* ELK: https://youtu.be/ZP0NmfyfsoM 
* NoSQL: https://youtu.be/0buKQHokLK8 
* p2p: https://youtu.be/w2u4eN_WWvc 
* redis:  https://youtu.be/OqCK95AS-YE 
* db schema definition tips: https://youtu.be/zBZEz1vZdIQ 
* 7 db paradigm: https://youtu.be/W2Z7fbCLSTw 
* extremely good top tips: https://youtu.be/-m5cMzm9R-s 
* techlead top 7: https://youtu.be/REB_eGHK_P4 

## Books

* "Grokking the System Design Interview"
* "SystemExpert"

## Tips for the interview

### General
1. Make sure all the requirements are clear.
2. Avoid detailing early.
3. Be flexible and fit the use case rather than what you already know.
4. Keep it simple and stupid. Don't make things complicated.
5. Form your thoughts. Avoid speaking without thinking the point through.
6. Be tech aware.

### DB types and examples

* nosql (cassandra, amazon dynamo db, mongo db)
* sql 
* keyvalue stores (redis, memcached, cassandra)
* text search (elasticsearch)
* time series opentsdb from tracking (like prometheus or influxdb) good for appending data and read based on timestamps
* columnar db (cassandra, hbase)

note: this [video](https://youtu.be/W2Z7fbCLSTw) from [@codedio](https://github.com/codediodeio) is extremely helpful about this topic


## Topics

### CDN

They are useful mainly to reduce latency and excessive load on the servers.

They mainly do 2 things:
* cache static assets
* redirect to local servers

There are 2 types of policies you can use to populate the cdn's cache:
* pull: cache after first request
* push: cache before first request, pushing content beforehand

NOTE: You probably want to pair CDNs with a Distributed File System like AWS S3 or GCS to reduce latency.

### SQL vs NoSQL

SQL Pros:
* you can do complex queries on them
* ACID compliant (consistency)
* data is always structured in the way you expect
* transitioning to a NoSQL is easy
* non "SELECT *" are faster than NoSQL
* you can do joins

NoSQL Pros:
* scalability, they are very easy to scale (sharding is supported by default)
* they don't require schemas
* retrieving full elements (rows) is extremely fast compared to SQL
* no joins are required because all informations are stored in the same point

### Load Balancing

Options to implement load balancing:
* nginx (high flexibility)
* cluster of dns (low flexibility)

Most used routing strategies:
* random
* round robin
* load on the most free

### Proxies

Besides being potentially useful to serve cached content, they mainly help with:
* hiding clients' IP addresses (normal proxies)
* hiding servers' IP addresses (reverse proxies)

### APIs

Desining good APIs requires a lot of practice to get right, but the most common stuff to think about are:
* REST vs GraphQL
* pagination
* headers
* query/path params
* body
* outgoing data format

It's always best not to make endpoints "magic", like "/doStuff". You want to have them do as few things as possible and have them be as easy to read as possible.

### Caching

Caching is almost always a good idea because it improves performance by a huge amount and it often doesn't cost much both development and cost wise.

#### Position

You can choose to either put the cache in memory, perhaps with the clients or servers themselves, or have it be an independent entity.

You probably always want at least 1 distributed cache because in that way it can serve the most amount of requests and it can scale independetly.

Local cache can sometimes be a good idea when it's not expected to grow too much in size or/and we need extreme performance.

#### Eviction Policies

One of the most critical decisions to make about caching systems is when to make space for new data.

The two most common policies are:
* LRU: least recently used (easiest to implement)
* LFU: least frequently used

#### Consistency

How do you want to update the data?

There two most common choices are:
* write-through: write first in the cache, then in the db (bad if cache has more replicas)
* write-back: write first the db, then the cache (good for consistency and more replicas)

You probably want to use both in most systems. Just be sure to evaluate the pros and cons for each use case.

### Indexes

Indexes make queries fast but they're not free, they occupy a lot of space and they make writes extremely slow.

The way you want to choose the indexes of your dbs is by looking at your most commonly used  WHERE statements in the queries you want to use.

The difference between clustered and non clustered indexes is that clustered indexes are linked to the real data, non-clustered only reference the real data so they can be sorted, and filtered, in a different way than the real data.


### DBs Reads Scaling

To scale reads efficiency in dbs you want to use a master-slave system where you have N slaves with full copies of the data that are used for reads only and one master to also write on.

After the write, the slaves will receive updates asap.

If the master db goes down, one of the slaves takes its place and creates a new slave.

NOTE: The more slaves you have the less consistent your system will be.

### DBs Storage Scaling (sharding)

To scale the capacity/storage of dbs you either want to parition the tables in sub tables each having a subset of the original columns, which is a vertical type of scaling, or each having a subset of rows, which would be an horizontal type of scaling.

The way you would partition horizontally a table is by taking a column which stores some sort of ID, like user ids or locations ids, hash it, then divide the load through doing a mod of the result of the hash.

NOTE: Using a single hash function will make you have issues once you need to add more capacity to the db. The way you could solve that is by using a partion to store inside other N partitions, like recursive calls, or by using [Consisten Hashing](https://youtu.be/zaRkONvyGr8).


### DBs Writes Scaling

The way you scale DB writes is by creating chunks of updates and, after sorting them, you store them in the database as they are instead of merging them straight away.

With following inserts you can decide whether or not is worth merging some of the previously stored chunks.

Reference: https://youtu.be/_5vrfuwhvlQ

### DBs Schema Definition

To define schemas of dbs you can list all the requirements in sentences and use the "nouns" to define the tables and the "verbs" to define their relationships/status-change.

Reference: https://youtu.be/zBZEz1vZdIQ

### Scaling Parallel Computations

You can divide the task to be done in general sub tasks and assign each to a worker. Also creating a queue of tasks might be required. 

### Web Sockets vs HTTP requests

Normal HTTP requests are a one-way type of connection, where the server can't independetly decide to push messages/requests to the client.

In situations like messaging apps, or where frequent exchanges between client and server are needed, you might want to consider using Web Sockets which use the TCP protocol therefore allowing the server to independetly communicate with the client.
