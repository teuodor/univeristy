import java.io.Serializable;

public class Response implements Serializable {
    private ResponseType type;
    private Object data;

    public Response(){}

    public ResponseType type() {return type;}

    public Object data() {return data;}

    private void type(ResponseType type){this.type = type;}

    private void data(Object data){this.data = data;}

    @Override
    public String toString() {
        if(data() != null)
            return type.toString() + "|" + data.toString();
        else
            return type.toString() + "|null";
    }

    public static class Builder{
        private Response request = new Response();
        public Builder type(ResponseType type){
            request.type(type);
            return this;
        }

        public Builder data(Object data){
            request.data(data);
            return this;
        }

        public Response build(){return request;}

    }
}
