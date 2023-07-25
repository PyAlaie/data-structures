import java.util.*;

class Entry <K, V>{
    private K key;
    private V value;

    public Entry(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public boolean equals(Object object) {
        if (this == object) return true;
        if (object == null || getClass() != object.getClass()) return false;
        if (!super.equals(object)) return false;
        Entry<?, ?> entry = (Entry<?, ?>) object;
        return java.util.Objects.equals(key, entry.key) && java.util.Objects.equals(value, entry.value);
    }

    public K getKey() {
        return key;
    }

    public void setKey(K key) {
        this.key = key;
    }

    public V getValue() {
        return value;
    }

    public void setValue(V value) {
        this.value = value;
    }

    @java.lang.Override
    public java.lang.String toString() {
        return "Entry{" +
                "key=" + key +
                ", value=" + value +
                '}';
    }
}

public class HashTableSeparateChaining <K,V> {
    private double maxLoadFactor = 0.8;
    private int capacity = 4, threshold, size = 0;

    private ArrayList<Entry<K,V>>[] table;

    public HashTableSeparateChaining() {
        threshold = (int) (capacity * maxLoadFactor);
        table = new ArrayList[capacity];
    }

    public int size(){
        return size;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    private int normalizeIndex(int hash){
        // removing the negetive sign and moding it into capacity
        return (hash & 0x7FFFFFFF) % capacity;
    }

    public void clear(){
        Arrays.fill(table, null);
        size = 0;
    }

    public boolean containsKey(K key){
        int index = normalizeIndex(key.hashCode());
        return searchKeyInBucket(key, index) != null;
    }

    public void put(K key, V value){
        int index = normalizeIndex(key.hashCode());
        addEntryToBucket(key, value, index);
    }

    public Entry<K,V> searchKeyInBucket(K key, int bucketIndex){
        ArrayList<Entry<K, V>> bucket = table[bucketIndex];

        if(bucket == null) return null;

        for(Entry<K,V> entry : bucket){
            if(entry.getKey().equals(key)){
                return entry;
            }
        }
        return null;
    }

    public void addEntryToBucket(K key, V value, int bucketIndex){
        ArrayList<Entry<K,V>> bucket = table[bucketIndex];
        Entry<K,V> entry = new Entry<>(key, value);

        if (bucket == null){
            bucket = new ArrayList<Entry<K,V>>();
            table[bucketIndex] = bucket;
        }

        // ckecking if key already exists
        Entry<K, V> existentEntry = searchKeyInBucket(key, bucketIndex);
        if(existentEntry == null){
            // inserting new entry
            bucket.add(entry);
            size++;

            if(size > threshold){
                resizeTable();
            }
        }
        else {
            // updateing new entry
            existentEntry.setValue(value);
        }
    }

    public void resizeTable(){
        capacity *= 2;
        threshold = (int) (capacity * maxLoadFactor);

        ArrayList<Entry<K,V>>[] newTable = new ArrayList[capacity];

        for(int i = 0; i < table.length; i++){
            if(table[i] != null){
                for(Entry<K,V> entry : table[i]){
                    int index = normalizeIndex(entry.getKey().hashCode());
                    ArrayList<Entry<K, V>> bucket = newTable[index];
                    if (bucket == null) {
                        newTable[index] = new ArrayList<>();
                    }
                    newTable[index].add(entry);
                }
                table[i].clear();
                table[i] = null;
            }
        }

        table = newTable;
    }

    public V get(K key){
        int index = normalizeIndex(key.hashCode());

        Entry<K,V> entry = searchKeyInBucket(key, index);
        if (entry != null){
            return entry.getValue();
        }

        return null;
    }

    public void remove(K key){
        int index = normalizeIndex(key.hashCode());
        removeFromBucket(key, index);
    }

    public void removeFromBucket(K key, int index){
        ArrayList<Entry<K,V>> bucket = table[index];
        if(bucket != null){
            Entry<K,V> entry = searchKeyInBucket(key, index);
            bucket.remove(entry);
            size--;
        }
    }
}