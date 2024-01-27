public class LinkedList<T> implements Iterable<T>{
    private int size = 0;
    private Node <T> head = null;
    private Node <T> tail = null;

    private class Node <T> {
        private T data;
        private Node<T> next, perv;

        public Node(T data, Node<T> next, Node<T> perv) {
            this.data = data;
            this.next = next;
            this.perv = perv;
        }

        @java.lang.Override
        public java.lang.String toString() {
            return data.toString();
        }
    }

    public void clear(){
        Node<T> t = head;
        while(t.next != null){
            Node<T> next = t.next;
            t.next = null;
            t.perv = null;
            t.data = null;
            t = null;
            t = next;
        }
        head = null;
        size = 0;
    }

    public int size(){
        return this.size;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    public void append(T element){
        Node<T> newNode = new Node<>(element, null, tail);
        if(!isEmpty()){
            tail.next = newNode;
            tail = newNode;
        }
        else {
            head = newNode;
            tail = newNode;
        }
        size++;
    }

    public void insert(T element, int index){
        // Inserting to first
        if (index <= 0){
            Node<T> newNode = new Node<>(element, head, null);
            head.perv = newNode;
            head = newNode;
        }
        // Inserting to last
        else if(index >= size){
            Node<T> newNode = new Node<>(element, null, tail);
            tail.next = newNode;
            tail = newNode;
        }
        // Inserting to middle
        else {
            int trevIndex = 0;
            Node<T> pervNode;
            Node<T> nextNode = head;
            while(trevIndex < index){
                nextNode = nextNode.next;
                trevIndex++;
            }
            pervNode = nextNode.perv;
            Node<T> newNode = new Node<>(element, nextNode, pervNode);
            nextNode.perv = newNode;
            pervNode.next = newNode;
        }
        size++;
    }

    public T pop(){
        T returningData = tail.data;

        tail = tail.perv;
        size --;

        if(isEmpty()){
            head = null;
            tail = null;
        }
        else {
            tail.next = null;
        }

        return returningData;
    }

    public void remove(T element){
        Node<T> trav = head;

        while (trav != null){
            if (trav.data == element){
                if(trav.perv == null){ // removing head
                    head = trav.next;
                    trav.data = null;
                    trav.next = null;
                    trav.perv = null;
                    head.perv = null;
                }
                else if(trav.next == null) { // removing tail
                    tail = trav.perv;
                    trav.data = null;
                    trav.next = null;
                    trav.perv = null;
                    tail.next = null;
                }
                else { // removing from middle
                    trav.next.perv = trav.perv;
                    trav.perv.next = trav.next;
                    trav.data = null;
                    trav.next = null;
                    trav.perv = null;
                }
            }
            else {
                trav = trav.next;
            }
        }
    }

    public T get(int index){
        Node<T> trav = head;

        int travIndex = 0;
        while (trav != null){
            if(travIndex == index){
                return trav.data;
            }
            travIndex ++;
            trav = trav.next;
        }

        return null;
    }

    public int indexOf(T element){
        Node<T> trav = head;
        int index = 0;

        while (trav != null){
            if (trav.data == element){
                return index;
            }
            index++;
            trav = trav.next;
        }
        return -1;
    }

    public boolean contains(T element){
        Node<T> trav = head;

        while (trav != null){
            if (trav.data == element){
                return trav;
            }
            trav = trav.next;
        }
        return false;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[ ");
        Node<T> trav = head;
        while (trav != null) {
            sb.append(trav.data + ", ");
            trav = trav.next;
        }
        sb.append(" ]");
        return sb.toString();
    }

    @Override
    public java.util.Iterator<T> iterator() {
        return new java.util.Iterator<T>() {
            private Node<T> trav = head;

            @Override
            public boolean hasNext() {
                return trav != null;
            }

            @Override
            public T next() {
                T data = trav.data;
                trav = trav.next;
                return data;
            }

            @Override
            public void remove() {
                throw new UnsupportedOperationException();
            }
        };
    }
}