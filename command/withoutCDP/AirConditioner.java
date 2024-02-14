public class AirConditioner {
    boolean isOn ;
    int temperature ;
    public void turnOnAC(){
        this.isOn = true;
        System.out.println("AC is on");
    }

    public void turnOffAC(){
        this.isOn = false;
        System.out.println("AC is off");
    }

    public void setTemperature(int temperature) {
        this.temperature = temperature;
        System.out.println("temperature changed to " + temperature);
    }
}