import java.math.BigDecimal;
import java.util.Date;

public class WalletService {
    private WalletDao dao;
    
    public WalletService(){

        this.dao = new WalletDao();

    }

    public void createWallet(String name, BigDecimal amount){
         Account account =  new Account(name , amount);
         dao.getAccountMap().put(account.getAccountNumber(), account);
         System.out.println("Account created for the User"+ name +"with account number" + account.getAccountNumber());
    }

    public void transfer(int fromAccNumber, int toAccNumber,BigDecimal transferAmount){
        if (!validate(fromAccNumber,toAccNumber,transferAmount)){
            return;
        }
        Transaction transaction = new Transaction(fromAccNumber, toAccNumber, transferAmount, new Date());
        Account fromAccount = dao.getAccountMap().get(fromAccNumber);
        Account toAccount = dao.getAccountMap().get(toAccNumber);
        if(fromAccount.getBalance().compareTo(transferAmount)<0){
            System.out.println("Insufficient funds");
            return;
        }
        fromAccount.setBalance(fromAccount.getBalance().subtract(transferAmount));
        toAccount.setBalance(toAccount.getBalance().add(transferAmount));
        fromAccount.getTranactions().add(transaction);
        toAccount.getTranactions().add(transaction);
        System.out.println("transaction is successfull");


    }

    private boolean validate(int fromAccNumber, int toAccNumber, BigDecimal transferAmount) {

        if(fromAccNumber == toAccNumber) {
            System.out.println("Sender and Receiver cannot be same.");
            return false;
        }
        if (transferAmount.compareTo(new BigDecimal(0.0001)) < 0) {
            System.out.println("Amount too low");
            return false;
        }
        if (!dao.getAccountMap().containsKey(fromAccNumber)) {
            System.out.println("Invalid Sender account number");
            return false;
        }
        if (!dao.getAccountMap().containsKey(toAccNumber)) {
            System.out.println("Invalid Receiver account number");
            return false;
        }
        return true;
    }

    public void statement(int accountNum) {
        Account account = dao.getAccountMap().get(accountNum);
        if(account == null) {
            System.out.println("Invalid Account Number");
            return;
        }
        System.out.println("Summary for account number: " + accountNum);
        System.out.println("Current Balance: " + account.getBalance());
        System.out.println("Your Transaction History");
        System.out.println(account.getTranactions());
    }
    public void overview() {
        for (int accNum : dao.getAccountMap().keySet()) {
            System.out.print("Balance for account number " + accNum + ": ");
            System.out.println(dao.getAccountMap().get(accNum).getBalance());
        }
    }

}
