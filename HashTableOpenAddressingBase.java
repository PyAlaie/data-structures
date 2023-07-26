import java.util.Arrays;

public abstract class HashTableOpenAddressingBase <K,V>{
    protected double loadFactor = 0.5;
    protected int capacity = 4, size = 0, threshold;

    protected K[] keys;
    protected V[] values;

    protected K TOMBStONE = (K) new Object();

    protected HashTableOpenAddressingBase() {
        threshold = (int) (this.capacity * loadFactor);
    
        keys = (K[]) new Object[this.capacity];
        values = (V[]) new Object[this.capacity];
    }

    public void clear(){
        for(int i = 0; i < capacity; i++){
            keys[i] = null;
            values[i] = null;
        }

        size = 0;
    }

    public int size(){
        return size;
    }

    public int getCapacity(){
        return capacity;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    public void put(K key, V value){
        if(size >= threshold){
            resizeTable();
        }

        int bucketIndex = normalizeIndex(key);
        insertIntoBucket(key, value, bucketIndex);
    }

    public void resizeTable(){
        capacity *= 2;
        threshold = (int) (capacity * loadFactor);

        K[] newKeys = (K[]) new Object[capacity];
        V[] newValues = (V[]) new Object[capacity];

        K[] keysTmp = Arrays.copyOfRange(keys, 0, capacity/2);
        V[] valuesTmp = Arrays.copyOfRange(values, 0, capacity/2);

        keys = newKeys;
        values = newValues;
        size = 0;
        
        for(int i = 0; i < capacity/2; i++){
            if(keysTmp[i] != TOMBStONE && keysTmp[i] != null){
                put(keysTmp[i], valuesTmp[i]);
            }
            keysTmp[i] = null;
            valuesTmp[i] = null;
        }
    }

    public void insertIntoBucket(K key, V value, int bucketIndex){
        int probeAmount = 0;

        while(keys[bucketIndex] != null && keys[bucketIndex] != key && keys[bucketIndex] != TOMBStONE){
            probeAmount++;
            bucketIndex += probe(probeAmount);
            bucketIndex %= capacity;
        }

        // we have the index to insert/update... 
        if(keys[bucketIndex] == TOMBStONE){
            keys[bucketIndex] = key;
            values[bucketIndex] = value;
        }
        else{
            keys[bucketIndex] = key;
            values[bucketIndex] = value;
        }
        size++;
    }

    public int normalizeIndex(K key){
        int hash = (key.hashCode() & 0x7FFFFFFF) % capacity;
        return hash;
    }

    protected abstract int probe(int x);

    public boolean containsKey(K key){
        return get(key) != null;
    }

    public K[] getKeys(){
        return keys;
    }

    public V[] getValues(){
        return values;
    }

    public V get(K key){
        int bucketIndex = normalizeIndex(key);
        int probeAmount = 0;

        while(keys[bucketIndex] != key && keys[bucketIndex] != null){
            probeAmount++;
            bucketIndex += probe(probeAmount);
            bucketIndex %= capacity;
        }

        return values[bucketIndex];
    }

    public void remove(K key){
        int bucketIndex = normalizeIndex(key);
        int probeAmount = 0;

        while(keys[bucketIndex] != key && keys[bucketIndex] != null){
            probeAmount++;
            bucketIndex += probe(probeAmount);
            bucketIndex %= capacity;
        }

        if(keys[bucketIndex] != null){
            keys[bucketIndex] = TOMBStONE;
            values[bucketIndex] = null;
        }
    }
}