public class Main {
    public static void main(String[] args) {
        // Cria um carrinho de compras com preço total de 100.0
        ShoppingCart cart1 = new ShoppingCart(100.0);
        
        // Aplica desconto percentual de 10%
        cart1.setDiscountStrategy(new PercentageDiscount(10));
        System.out.println("Preço final com desconto percentual: " + cart1.getFinalPrice());
        
        // Cria outro carrinho de compras com preço total de 100.0
        ShoppingCart cart2 = new ShoppingCart(100.0);
        
        // Aplica desconto fixo de 20
        cart2.setDiscountStrategy(new FixedAmountDiscount(20));
        System.out.println("Preço final com desconto fixo: " + cart2.getFinalPrice());
    }
}
