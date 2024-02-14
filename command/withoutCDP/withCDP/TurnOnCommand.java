package withCDP;

public class TurnOnCommand implements Icommand{
    AirConditioner ac ;

    TurnOnCommand(AirConditioner ac) {
    this.ac = ac;
}
@Override
public void execute(){
    ac.turnOnAC();
}
    
}
