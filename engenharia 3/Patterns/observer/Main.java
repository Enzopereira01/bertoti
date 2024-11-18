public class Main {
  public static void main(String[] args) {
    ConcreteSubject concreteSubject = new ConcreteSubject();
    ConcreteObserver concreteObserver = new ConcreteObserver(concreteSubject);

    concreteSubject.registerObserver(concreteObserver);

    concreteSubject.setState("New State");
  }
}