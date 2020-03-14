* Some key concepts: Elasticsearch is a distributed search software. Elastic search cluster is formed by different type of nodes, such as master node, client node, data node and ingest node. A minimal setup will require a master node which also holds data. To expand the cluster, we can add client node that is master eligible and also holds a copy of data/shard. (In AWS Elasticsearch, the role of nodes is a bit different. There is dedicated master node to manage sharding, and there is data node to hold data which can also handles network I/O).

* Commands

  * Check cluster health: ```curl -X GET "localhost:9200/_cat/health?v&pretty"```

  * Check cluster status: ```curl -X GET "localhost:9200/_cat/nodes?v&pretty"```

  * Create a new index:

    ```
    curl -X PUT "localhost:9200/twitter?pretty" -H 'Content-Type: application/json' -d'
    {
        "settings" : {
            "index" : {
                "number_of_shards" : 3,
                "number_of_replicas" : 2
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

  * Show all documents in one index

    ```
    curl -X GET "localhost:9200/twitter/_search?pretty" -H 'Content-Type: application/json' -d'
    {
        "query": {
            "match_all": {}
        }
    }
    '
    ```

  * Delete an index

    ```
    curl -X DELETE "localhost:9200/twitter?pretty"
    ```

  * Delete all indexes

    ```
    curl -X DELETE "localhost:9200/*"
    ```

  * Delete all documents under index

    ```
  curl -X POST "localhost:9200/twitter/_delete_by_query?pretty" -H 'Content-Type: application/json' -d'
    {
      "query": {
        "match_all": {}
      }
    }
    '
    ```
  
  * Show total number of documents
  
    ```
    curl -X GET "localhost:9200/twitter/_count?q=*"
    ```
  
  * Show total number of document by matching a search criteria (username="John")
  
    ```
    curl -X GET "localhost:9200/twitter/_count?q=username:John"
    ```
  
  * a. Search docuements by criteria(username="John")
  
    ```
    curl -X GET "localhost:9200/twitter/_search?q=username:John"
    ```
  
  * b. Search documents by a list of criteria and filters(username="John" and age > 22) - Also known as 'Compound query'
  
    ```
    curl -X GET "localhost:9200/twitter/_search?
    {
    	"query": {
    		"bool": {
    			"must": {
    				"term": {"username": "John"}
    			},
    			"must_not": {
    				"range" : {
    					"age" : {"gte": 22}
    				}
    			}
    		}
    	}
    }
    ```
  
  * Term query vs match query: 
  
    The `match` query will apply the same standard analyzer to the search term and will therefore match what is stored in the index. The `term` query does not apply any analyzers to the search term, so will only look for that exact term in the inverted index.
  
    ```
    GET /_search
    {
        "query": {
            "term": {
                "user": {
                    "value": "Kimchy",
                    "boost": 1.0
                }
            }
        }
    }
    ```
  
    ```
    GET /_search
    {
        "query": {
            "match" : {
                "message" : {
                    "query" : "this is a test"
                }
            }
        }
    }
    ```
  
  * Cat APIs vs Json APIs:
  
    cat APIs are only intended for human consumption using Kibana console or command line. They are not intended for use by application. For application consumption, JSON API is needed.
  
  * Index can be compared to database, and index name can be similar to database name.
  
  * AWS Elasticsearch service supports regular ES commands, just skip port, e.g.
  
    ```
    curl -X GET https://<ES_cluster_id>.us-west-2.es.amazonaws.com/_cat/health?v
    ```
  
    Also, for anonymous user request,  use an IP-based access policy to allow unsigned requests to Amazon ES domain. (https://aws.amazon.com/premiumsupport/knowledge-center/anonymous-not-authorized-elasticsearch/)