import java.util.ArrayList;
import java.util.List;

public class Subject {
  private List<Observer> observers = new ArrayList<>();

  public void registerObserver(Observer observer) {
    observers.add(observer);
  }

  public void removeObserver(Observer observer) {
    observers.remove(observer);
  }

  public void notifyObservers() {
    for (Observer observer : observers) {
      observer.update(getState());
    }
  }

  // Placeholder for concrete state management
  public String getState() {
    return null;
  }

  // Placeholder for concrete state management
  public void setState(String state) {}
}