public class Main {
    public static void main(String[] args) {
        LightingSystem lightingSystem = new LightingSystem();
        SecuritySystem securitySystem = new SecuritySystem();

        HomeAutomationFacade homeAutomationFacade = new HomeAutomationFacade(securitySystem, lightingSystem);
        homeAutomationFacade.getHome();
        homeAutomationFacade.outHome();
    }
}