import java.io.Serializable;

public class Request implements Serializable {
    private RequestType type;
    private Object data;

    public Request(){}

    public RequestType type() {return type;}

    public Object data() {return data;}

    private void type(RequestType type){this.type = type;}

    private void data(Object data){this.data = data;}

    @Override
    public String toString() {
        return type.toString() + "|" + data.toString();
    }

    public static class Builder{
        private Request request = new Request();
        public Builder type(RequestType type){
            request.type(type);
            return this;
        }

        public Builder data(Object data){
            request.data(data);
            return this;
        }

        public Request build(){return request;}

    }


}
