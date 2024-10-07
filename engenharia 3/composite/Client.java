public class Client {
    public static void main(String[] args) {
        Composite root = new Composite();
        Composite composite1 = new Composite();
        Composite composite2 = new Composite();

        root.add(composite1);
        root.add(composite2);

        composite1.add(new Leaf());
        composite1.add(new Leaf());

        composite2.add(new Leaf());

        root.operation();
    }
}