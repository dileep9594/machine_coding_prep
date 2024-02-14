public class Main {
    public static void main(String[] args){
        AirConditioner ac = new AirConditioner();
        ac.turnOnAC();
        ac.setTemperature(24);
        ac.turnOffAC();
    }
}

//  problem with the implementation
// 1. Lack of abstraction :
//    a. today of process of turning on AC is simple, but if there are more steps, client has to aware all of that, which is not good.
// 2.  Undo/Redo functionality :
//  what if i want to implement the undo/redo functionality. how it will be handeled.
// 3. Difficulty in Coode maintenance :
// what if in future , we have to support more commands for more devices example Bulb.