# graphy hashes demo

This demo combines [Redis](https://redis.io) hash data structures and [Redisearch](https://oss.redislabs.com/redisearch/)
to generate "people" hashes and create a search index to represent a sort of flattened social network graph.

## Architecture
![Architecture](/architecture.png)

## Requirements
Docker

## Running the Demo
To run the demo:
```
$ git clone https://github.com/quintonparker/redis_graphy_hashes
$ cd redis_graphy_hashes
$ docker-compose up
```

1. You'll notice node_generator.py will be generating up to 1M hash keys
2. At any point in time you may apply the search schema syntax found in commands.redis
3. Optional. Download [RedisInsight](https://redislabs.com/redis-enterprise/redis-insight/) to browse the database and perform search queries
