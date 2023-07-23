public class BinarySearchTree <T extends Comparable<T>>{
    private int nodeCount = 0;
    private Node root = null;

    private class Node{
        private Node left;
        private Node right;
        private T data;

        public Node(Node left, Node right, T data) {
            this.left = left;
            this.right = right;
            this.data = data;
        }
    }

    public int size(){
        return nodeCount;
    }

    public boolean isEmpty(){
        return size() == 0;
    }

    public void add(T element){
        root = addRecersive(element, root);
        nodeCount++;
    }

    private Node addRecersive(T element, Node node){
        if(node == null){
            node = new Node(null, null, element);
        }
        else {
            if(element.compareTo(node.data) > 0){
                node.right = addRecersive(element, node.right);
            }
            else {
                node.left = addRecersive(element, node.left);
            }
        }
        return node;
    }

    public boolean contains(T element){
        return containsRecursive(element, root);
    }

    private boolean containsRecursive(T element, Node node){
        if(node == null){
            return false;
        }
        else if(node.data == element){
            return true;
        }
        else if(element.compareTo(node.data) > 0){
            return containsRecursive(element, node.right);
        }
        else {
            return containsRecursive(element, node.left);
        }
    }

    private Node findMin(Node node){
        while (node.left != null){
            node = node.left;
        }

        return node;
    }

    public void remove(T element){
        if(contains(element)){
            root = removeRecursive(element, root);
            nodeCount --;
        }
    }

    private Node removeRecursive(T element, Node node){
        if(node == null) return null;

        int cmp = element.compareTo(node.data);
        if(cmp > 0){
            return removeRecursive(element, node.right);
        }
        else if(cmp < 0){
            return removeRecursive(element, node.left);
        }

        else {
            if(node.right == null){
                Node leftNode = node.left;

                node.data = null;
                node = null;

                return leftNode;
            }
            else if(node.left == null){
                Node rightNode = node.right;

                node.data = null;
                node = null;

                return rightNode;
            }
            else {
                Node temp = findMin(node.right);

                node.data = temp.data;

                return removeRecursive(element, temp);
            }
        }
    }

    public void printDiagram(){
        printSubTree(root, "", false); // this function is written by ChatGPT
    }

    private void printSubTree(Node node, String prefix, boolean isLeft) {
        if (node == null) {
            return;
        }

        String nodeStr = "───" + node.data + "───";
        String connectorStr = isLeft ? "┌" : "└";

        System.out.println(prefix + connectorStr + nodeStr);

        String newPrefix = prefix + (isLeft ? "│   " : "    ");

        printSubTree(node.left, newPrefix, true);
        printSubTree(node.right, newPrefix, false);
    }

    public int height() {
        return height(root);
    }

    private int height(Node node) {
        if (node == null)
            return 0;

        return Math.max(height(node.left), height(node.right)) + 1;
    }

    public void printInOrderTraversal(){
        inOrderTraversal(root);
    }

    private void inOrderTraversal(Node node){
        if(node == null){
            return;
        }

        inOrderTraversal(node.left);
        System.out.println(node.data);
        inOrderTraversal(node.right);
    }
}