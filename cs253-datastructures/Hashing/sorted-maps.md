# Sorted maps

* `min()`
* `max()`
* `ceil()`
* `floor()`
* `predecessor(k)`, `successor(k)`
* `submap(k1,k2)`

## Dynamic Order Statistics

```
if k < abs(L)
```

``` 
rank = left(x).size + 1
tempRoot = x
while tempRoot != root:
    if tempRoot is a right child:
        rank += left(parent(tempRoot)).size + 1
    tempRoot = parent(tempRoot)
return rank
```

## Skip Lists

A **probabilistic** sorted map data structure.
**Hierarchical**, like BSTs

