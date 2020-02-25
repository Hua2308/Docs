* Some key concepts: Elasticsearch is a distributed search software. Elastic search cluster is formed by different type of nodes, such as master node, client node, data node and ingest node. A minimal setup will require a master node which also holds data. To expand the cluster, we can add client node that is master eligible and also holds a copy of data/shard. (In AWS Elasticsearch, the role of nodes is a bit different. There is dedicated master node to manage sharding, and there is data node to hold data which can also handles network I/O).

* Commands

  * Check cluster health: ```curl -X GET "localhost:9200/_cat/health?v&pretty"```

  * Check cluster status: ```curl -X GET "localhost:9200/_cat/nodes?v&pretty"```

  * Create a new index entry:

    ```
    curl -X PUT "localhost:9200/twitter?pretty" -H 'Content-Type: application/json' -d'
            }
        }
    }
    '
    ```

  * Get an index

    ```
    curl -X GET "localhost:9200/twitter?pretty"
    ```

  * Show all indices

    ```
    curl -X GET "localhost:9200/_cat/indices?v"
    ```

    ``````
    curl -X GET "localhost:9200/_aliases"
    ``````

  * Delete an index

    ```
    curl -X DELETE "localhost:9200/twitter?pretty"
    ```

  * Delete all indexes

    ```
    curl -X DELETE "localhost:9200/*"
    ```

  * 