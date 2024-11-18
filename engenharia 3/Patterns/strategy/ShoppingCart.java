// ShoppingCart.java
public class ShoppingCart {
    private double totalPrice;
    private DiscountStrategy discountStrategy;

    public ShoppingCart(double totalPrice) {
        this.totalPrice = totalPrice;
    }

    public void setDiscountStrategy(DiscountStrategy discountStrategy) {
        this.discountStrategy = discountStrategy;
    }

    public double getFinalPrice() {
        if (discountStrategy == null) {
            return totalPrice;
        }
        return discountStrategy.applyDiscount(totalPrice);
    }
}
