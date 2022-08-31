public class Germaine
{
    static object Encode(string h, string c, string n){
    string s = "";

    string[] alpha = h.Split(',');
    string[] code = c.Split(',');

    var encryp = new Dictionary<string,string>();

    for(int i=0; i<code.Length; i++){
        encryp.Add(alpha[i],code[i]);
    }  

    foreach(var i in n){
        if(char.IsWhiteSpace(i))
            {s += i;}
    
    foreach(var k in encryp ){
        if(k.Key.Contains(i))
            {s += k.Value;}
        }
    }
        return s;
}

    static object Decode(string h, string c, string n){
    string o = "";

    string[] alpha = h.Split(',');
    string[] code = c.Split(',');

    var encryp = new Dictionary<string,string>();

    for(int i=0; i<code.Length; i++){
        encryp.Add(alpha[i],code[i]);
    }  

    foreach(var i in n){
        if(char.IsWhiteSpace(i))
            {o += i;}

    foreach(var k in encryp ){
        if(k.Value.Contains(i))
            {o += k.Key;}
        }
    }
        return o;
}

    static void Main(string[] args)
    {
        string p = (@"a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z");
        string m = (@"!,@,#,$,%,^,&,*,(,),_,+,-,?,|,`,/,},{,],[,>,<,~,=,\");
        var Encoded = Encode(p,m,"the boy is good");
        var decoded = Decode(p,m,"]*% @|= ({ &||$");
        Console.WriteLine(Encoded);
        Console.WriteLine(decoded);
    }
}
