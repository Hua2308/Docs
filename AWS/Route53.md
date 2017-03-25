* __DNS record type__:
  * CNAME/Alias: domain name => another domain name
  * A record: domain name => IP address

* __Blue-green stacks DNS setup__:
  * Cname: site domain name => internal domain name (DNS Registry or company DNS server)
      * Note: one entry. simple routing.
  * Cname: internal domain name => 
      * blue stack name 
      * green stack name 
      * Note: two entries. weight-based routing. If blue is active, its weight is 100.
  * Cname: blue stack name => 
      * blue west elb name (if request originates us_west_2)
      * blue east elb name (if request originates us_east_1)
      * default name (if request not originates from us_west_2 or us_east_1) => 
          * blue west elb name (if blue west elb has lower latency)
          * blue east elb name (if blue east elb has lower latency)
          * Note: two entries. latency-based routing.
      * Note: Three entries. geolocation-based routing. 

* __Blue-green deployment__:
  * Deploy to inactive stack and test.
  * Toggle internal domain name to point to inactive stack (weight based routing)
  * Tear down previous active stack. (but keep elb)
