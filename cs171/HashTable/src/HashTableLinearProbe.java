public class HashTableLinearProbe<Key, Value> {
    private Key[] keys;
    private Value[] vals;
    private int size;
    private int M;

    public HashTableLinearProbe() {
        this(16);
    }

    @SuppressWarnings("unchecked")
    public HashTableLinearProbe(int capacity) {
        this.M = capacity;
        this.keys = (Key[]) new Object[M];
        this.vals = (Value[]) new Object[M];
    }

    private int hash(Key key) {
        return (key.hashCode() & 0x7fffffff) % M;
    }

    public void put(Key key, Value val) {
        int i;
        for (i = hash(key); this.keys[i] != null; i = (i + 1)%M) {
            if(this.keys[i].equals(key)) {
                 this.vals[i] = val;
                 return;
            }
            
        }
        this.keys[i] = key;
        this.vals[i] = val;
        this.size++;
    }

    public Value get(Key key) {
        if(this.size >= M/2) resize(2*M);
        int i = hash(key);
        for(; keys[i] != null; i = (i + 1)%M) {
            if(keys[i].equals(key)) {
                return vals[i];
            }
        }
        return null;
    }

    public boolean contains(Key key) {
        return get(key) != null;
    }

    public void delete(Key key) {
        if(!contains(key)) return;
        int i = hash(key);
        while (!key.equals(keys[i])) {
            i = (i + 1) % M;
        }
        keys[i] = null;
        vals[i] = null;
        i = (i+1) % M;

        while (keys[i] != null) {
            Key tempKey = keys[i];
            Value tempVal = vals[i];
            keys[i] = null;
            vals[i] = null;
            put(tempKey, tempVal);
            i = (i+1) % M;
        }
        size--;
        if(size > 0 && size <= M/8) resize(M/2);
    }
    @SuppressWarnings("unchecked")
    private void resize(int capacity) {
        HashTableLinearProbe<Key, Value> t = new HashTableLinearProbe(capacity);
        for(int i = 0; i < M; i++) {
            if(keys[i] != null) {
                t.put(keys[i], vals[i]);
            }
        }
        this.keys = t.keys;
        this.vals = t.vals;
        this.M = t.M;
    }
}