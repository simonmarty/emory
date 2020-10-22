# Transport Layer

## Transport services and protocols

* Provide *logical communication* between app processes running on different hosts
* Transport protocols run in end systems
    * send side: breaks app messages into segments, passes to network layer
    
## Transport vs network layer

* Network layer: logical communication between hosts
* Transport: between processes

## DNS Protocol, Messages

Message header:
* identification: 16 bit# for query, reply to query uses the same #
* flags:
  * Query or replay
  * recursion desired
  * recursion available
  * reply is authoritative