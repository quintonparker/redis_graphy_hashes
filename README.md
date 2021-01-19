# graphy hashes demo

This demo combines [Redis](https://redis.io) hash data structures and [Redisearch](https://oss.redislabs.com/redisearch/)
to generate "people" hashes and create a search index to represent a sort of flattened social network graph.

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
2. Download [RedisInsight](https://redislabs.com/redis-enterprise/redis-insight/) GUI client to connect to the Redis database (127.0.0.1:6379)
3. Create the search index by copy/paste the `FT.CREATE` command found in `commands.redis` file using RedisInsight's CLI feature. See https://github.com/quintonparker/redis_graphy_hashes/blob/main/screenshot-create-schema.png
4. Redisearch is now creating the search index in the background. Run `FT.INFO idx:nodes` to inspect the schema metadata. `num_docs` will indicate indexing progress.
5. Run some search queries! See https://github.com/quintonparker/redis_graphy_hashes/blob/main/screenshot-run-queries.png



