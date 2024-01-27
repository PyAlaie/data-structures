import java.security.Key;

public class HashTableDoubleHashing<K, V> extends HashTableOpenAddressingBase<K, V>{

    @Override
    protected int probe(int x) {
        return x * secondHash(x);
    }

    private int secondHash(Integer x){
        // this function should generate a new hash of key
        // but for now we're just gonna return the good old friendly hashCode function resualt :)
        return x.hashCode();
    }

    public HashTableDoubleHashing(){
        super();
    }
}