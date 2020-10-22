# Sorting

1. "Priority Queue Sorting"
* Selection sort
* Insertion sort
Both O(n^2)
* Heapsort: Heapify, then all the removes take nO(log n)

The best **comparison-based** sorts achieve time O(n log(n))

* Other sorting algorithms which get O(n log n).
* Showing that you cannot do better than Omega(n log n).
* Algorithms that beat this bound
    - Algorithms that don't (?)

## Divide and conquer
* Break problem into smaller versions and recurse until base case.
* Recombine smaller solutions into solution of original problem.

`T(n) = aT(n/b) + f(n)`

* `T(n)` runtime on instance of size n
* `a`: number of recursive calls
* `b`: size of recursive call
* `f(n)`: time spent on splitting/recombining

For mergesort, `a = b = 2`. Also, mergesort is not in place

## Quicksort
* pick a pivot
* partition
* quicksort(L), quicksort(H)
* return L + p + H

## Quickselect

`QUICKSELECT(array, k):`

* pick a pivot p
* partition the elements
* if k <= |L| return quickselect(L, k)
* else return quickselect(H, k- |L| - 1)
* Average: `O(n)` (`a = 0, b = 2`)

Within quickselect, we can use median-of-medians to pick a pivot.
* Split array into groups of 5.
    - Compute each of their medians
* Compute the median of those medians

Recursive call to quickselect

# Hybrid Sorts

## Introsort

Given a max recursion depth **D**:
* Do quicksort
* If recursion reaches **D**, switch to heapsort.

# Non comparison based sorting

## Bucket sort
* Limited range of keys
* Stable
* Space complexity: O(n + N), where N is the number of categories
* Time complexity: O(cn + N), where c is the time spent indexing
    - Array: c = O(1)
    - BST map: c = O(log N)

## Radix sort
* Repeated use of bucket sort
* **Lexicographic** order for keys (k1, k2, k3, ...): like a dictionary
* Uses *least significant digit order* (right to left)

### Example:

120, 34,201,344,13,320, 1, 132

Bucket for first digit, concatenate
Bucket for second digit, concatenate

## Insertion Sort
* Best for small array
    - Runtime proportional to the number of **inversions**
        * Works well for already sorted data

## Non in-place algorithms
* Use iteration when possible
* Allocate big chunks of memory at once

## Bucket and Radix Sort

* How do we deal with variable-sized buckets?


```
ArrayList<integer> list = new ArrayList<>();
for(int i = 0; i < 1000; i++) {
    list.add(i / 100);
} Collections.shuffle(list);

int[] bucketSizes = new int[10];

for(int i : array) {
    bucketSizes[i]++;
}