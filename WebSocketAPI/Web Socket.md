###1. Definition: 
Web socket supports bidirectional web-client communication, that transaction can be initiated by either the client or server.
###2. Advantage: 
a. HTTP request carries a bunch of headers and cookie data, which increases latency. Web socket keeps a persistent connection and does not need the overhead.
b. bidirection/duplex communciation
c. stateful (Connecting, Open, Closing, Closed)
###3. How does it work:
Step 1: Websocket handshake. Client sends a regular HTTP request with **Upgrade** header to inform the server client wishes to establish a WebSocket connection. E.g.

```
GET ws://websocket.example.com/ HTTP/1.1
Origin: http://example.com
Connection: Upgrade
Host: websocket.example.com
Upgrade: websocket
```

Step 2. Server response. If the server supports the WebSocket protocol, it agrees to the upgrade and returns a response with Upgrade header:

```
HTTP/1.1 101 WebSocket Protocol Handshake
Date: Wed, 16 Oct 2013 10:07:34 GMT
Connection: Upgrade
Upgrade: WebSocket
```

Now the WebSocket connection is up that users the same underlying TCP/IP connection.

Step 3. Data is transferred as _message_, each of which consists of one or more frames.