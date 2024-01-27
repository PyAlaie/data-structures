public class HashTableLinearProbing<K, V> extends HashTableOpenAddressingBase<K, V>{

    // for the sake of simplicity, we use 1 as our LINEAR_CONSTANT
    private int LINEAR_CONSTANT = 1;

    @Override
    protected int probe(int x) {
        return LINEAR_CONSTANT * x;
    }

    public HashTableLinearProbing(){
        super();
    }
}