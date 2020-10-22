# Chapter 6

## Frequent Pattern Analysis

* Inferring substructures that occurs frequently in a dataset
* frequent itemsets, association rule mining
* Motivation: Finding inherent regularities in data
  * What products were purchased together etc
* Applications
  * Basket data analysis
  * Cross-marketing
  * Catalog design
  * Sale campaign analysis
  * Web log analysis
  * etc

### Example

* itemset: A set of one or more items
* k-itemset X = {x<sub>1</sub>, ..., x<sub>k</sub>}
* Support *s* is the probability that a transaction contains X&cup;Y
* Confidence *c* is the conditional probability that a transaction having X also contains Y

### Closed patterns and max patterns
* An itemset X is closed if X is frequent and there exists no super-pattern Y&sup;X with the same support as X
* An itemset X is a **max-pattern** if X is frequent and there exists no frequent super-pattern Y&sup;X

## Scalable Frequent Itemset Mining Methods

### Apriori

* **Downward-closure**: Any subset of a frequent itemset *must* be frequent 
* if `{beer,diaper,nuts}` is frequent, so is `{beer, diaper}`

* **Apriori pruning principle**: If there is any itemset which is infrequent, its superset should not be generated/tested
  
Method
* Scan DB once to get frequent 1-itemset
* *Generate* length (k+1) *candidate* itemsets from length k *frequent* itemsets
* *Test* the candidates against DB

# Pattern Growth Approach

## Construct FP-tree from a Transaction Database
