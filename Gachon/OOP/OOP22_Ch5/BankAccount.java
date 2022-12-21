package OOP22_Ch5;

public class BankAccount {
    public double amount;
    public double rate;

    public void showNewBalance(){
        double newAmount = amount + (rate / 100.0) * amount;
        System.out.println("With interest added, the new amount is $" + newAmount);
    }

    public static void main(String[] args){
        BankAccount myAccount = new BankAccount();
        myAccount.amount = 100.00;
        myAccount.rate = 5;

        double newAmount = 800.00;
        myAccount.showNewBalance();
        System.out.println("I wish my new amount were $" + newAmount);
    }
}
