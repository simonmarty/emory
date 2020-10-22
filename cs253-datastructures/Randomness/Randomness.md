# Shuffling an array

* For an array of n **distinct** elements, there are **n!** many permutations
* How do we generate a uniform random permutation?
* Swapping two elements repeatedly is slow

## Fisher-Yates shuffle

* Create a new array
* While the original array is nonempty:
    - Remove a random element from original array and append to new array.

```
public static void shuffle(int[] array) {
    ThreadLocalRandom t = new TLR;
    for(int i = 0; i < array.length; i++) {
        int j = t.current().nextInt(array.length - i) + i;
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}
```

In code, we only have pseudorandom number generators (PRNGs)
* Output determined by seeds
* Multiple instancees eliminate, e.g. correlation