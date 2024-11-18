public class ConcreteObserver implements Observer {
  private ConcreteSubject subject;

  public ConcreteObserver(ConcreteSubject subject) {
    this.subject = subject;
  }

  @Override
  public void update(String data) {
    // Logic to handle updates from the subject
    System.out.println("ConcreteObserver received update: " + data);
  }
}