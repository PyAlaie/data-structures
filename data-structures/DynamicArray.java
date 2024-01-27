
@SuppressWarnings("unchecked")
public class DynamicArray <T> implements Iterable <T>{
    private int capacity;
    private int length = 0;
    private T[] array;

    public DynamicArray(){
        this(16);
    }

    public DynamicArray(int capacity){
        this.capacity = capacity;
        array = (T[]) new Object[capacity];
    }

    public void append(T object){
        if(length < capacity){
            array[length] = object;
        }
        else{
            capacity *= 2;
            T[] newArray = (T[]) new Object[capacity];
            for(int i = 0; i < length; i++){
                newArray[i] = array[i];
            }
            array = newArray;
        }
        length++;
    }

    public int size(){
        return length;
    }    

    public T get(int index){
        return array[index];
    }

    public boolean isEmpty(){
        return length == 0;
    }

    public void clear(){
        array = (T[]) new Object[this.capacity];
        length = 0;
    }

    public int indexOf(T obj){
        for(int i = 0; i < length; i++){
            if(array[i] == obj){
                return i;
            }
        }
        return -1;
    }

    public void removeAt(int index){
        T objToRemove = array[index];
        T[] newArray = (T[]) new Object[this.capacity];

        for(int i = 0, j = 0; i < length; i ++){
            if(array[i] != objToRemove){
                newArray[j] = array[i];
                j++;
            }
        }
        length --;
        array = newArray;
    }

    public void remove(T obj){
        removeAt(indexOf(obj));
    }

    public void set(int index, T obj) {
        array[index] = obj;
    }

    @Override
    public String toString() {
        if (length == 0) return "[]";
        else {
            StringBuilder sb = new StringBuilder(length).append("[");

            for (int i = 0; i < length - 1; i++) 
                sb.append(array[i] + ", ");

            return sb.append(array[length - 1] + "]").toString();
        }
    }

    @Override
    public java.util.Iterator<T> iterator() {
        return new java.util.Iterator<T>() {
        int index = 0;
        
        @Override
        public boolean hasNext() {
            return index < length;
        }

        @Override
        public T next() {
            return array[index++];
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }
        };
    }
}