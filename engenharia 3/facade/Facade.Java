public class Facade {
    private SubsystemA subsystemA = new SubsystemA();
    private SubsystemB subsystemB = new SubsystemB();
    private SubsystemC subsystemC = new SubsystemC();

    public void operation1() {
        subsystemA.methodA1();
        subsystemA.methodA2();
    }

    public void operation2() {
        subsystemB.methodB1();
        subsystemB.methodB2();
    }
}