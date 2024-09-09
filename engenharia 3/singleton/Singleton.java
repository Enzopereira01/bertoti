public class Singleton {
    private static Singleton instance;
    private Singleton(){}
    public static Sinlgeton getInstance(){
        if(instance == null){
            instance = new Singleton();
        }
        return instance;
    }
}