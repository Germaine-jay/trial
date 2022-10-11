public class Germaine
{
    static object Encode(string h, string c, string n){
    string s = "";

    char[] alpha = h.ToCharArray();
    char [] code = c.ToCharArray();

    var encryp = new Dictionary<char,char>();

    for(int i=0; i<code.Length; i++){
        encryp.Add(alpha[i],code[i]);
    }  

    foreach(var i in n){
        if(char.IsWhiteSpace(i))
            {s += i;}
    
    foreach(var k in encryp ){
        if((k.Key).ToString().Contains(i))
            {s += k.Value;}
        }
    }
        return s;
}

    static object Decode(string h, string c, string n){
    string o = "";

    char[] alpha = h.ToCharArray();
    char [] code = c.ToCharArray();

    var encryp = new Dictionary<char,char>();

    for(int i=0; i<code.Length; i++){
        encryp.Add(alpha[i],code[i]);
    }  

    foreach(var i in n){
        if(char.IsWhiteSpace(i))
            {o += i;}

    foreach(var k in encryp ){
        if((k.Value).ToString().Contains(i))
            {o += k.Key;}
        }
    }
        return o;
}

    static void Main(string[] args)
    {
        string p = (@"abcdefghijklmnopqrstuvwxyz");
        string m = (@"!@#$%^&*()_+-?|`/}{][><~=\");
        var Encoded = Encode(p,m,"the boy is good");
        var decoded = Decode(p,m,"]*% @|= ({ &||$");
        Console.WriteLine(Encoded);
        Console.WriteLine(decoded);
    }
}
