package withCDP;

public class Main {
    public static void main(String[] args){
        AirConditioner aircondition  = new AirConditioner();

        MyRemoteControl remoteObj = new MyRemoteControl();

        remoteObj.setCommand(new TurnOnCommand(aircondition));
        remoteObj.pressButton();
    }
}
