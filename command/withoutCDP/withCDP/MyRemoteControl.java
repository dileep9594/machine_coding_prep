package withCDP;

public class MyRemoteControl {
    Icommand command ;
    MyRemoteControl(){

    }
    public void setCommand(Icommand command ) {
        this.command = command;
    }

    public void pressButton(){
        command.execute();
    }
}
