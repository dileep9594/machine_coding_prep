package withCDP;

public class TurnOffCommand implements Icommand{

     AirConditioner ac ;

    TurnOffCommand(AirConditioner ac) {
    this.ac = ac;
}
@Override
public void execute(){
    ac.turnOffAC();
}
}
