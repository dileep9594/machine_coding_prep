import java.util.UUID;

public class User{
    public String id;
    public String username;

    public User(String username){
        this.id =  UUID.randomUUID().toString() ;
        this.username = username ;
    }
    public String getId(){
        return this.id ;
    }
    public void setId(String id){
        this.id = id ;
    }
    public String getUsername(){
        return this.username ;
    }
    public void setUsername(String username){
        this.username = username ;
    }
}