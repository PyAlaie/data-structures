public class HashTableQuadraticProbing<K, V> extends HashTableOpenAddressingBase<K, V>{

    @Override
    protected int probe(int x) {
        return (x * x + x) >> 1;
    }

    public HashTableQuadraticProbing(){
        super();
    }
}