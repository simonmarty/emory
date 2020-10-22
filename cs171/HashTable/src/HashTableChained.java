public class HashTableChained<Key, Value> {

    private int M;
    private Chain<Key, Value>[] a;

    @SuppressWarnings("unchecked")
    public HashTableChained(int M) {
        this.M = M;
        a = (Chain<Key, Value>[]) new Chain[M];
        for (int i = 0; i < M; i++) {
            a[i] = new Chain<Key, Value>();
        }
    }

    private int hash(Key key) {
        return (key.hashCode() & 0x7fffffff) % M;
    }

    public Value get(Key key) {
        return a[hash(key)].get(key);
    }

    public void put(Key key, Value val) {
        a[hash(key)].put(key, val);
    }
}
