// // cypher code
string p = @"a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z";
string m = (@"!,@,#,$,%,^,&,*,(,),_,+,-,?,|,`,/,},{,],[,>,<,~,=,\");


// string[] alpha = p.Split(',');
// string[] code = m.Split(',');

// var encryp = new Dictionary<string,string>();

// for(int i=0; i<code.Length; i++){
//     encryp.Add(alpha[i],code[i]);
// }

// string n = "germaine is a good programmer";
// string s = "";

// string n1 = "&%}-!(?% ({ ! @!$ `}|&}!--%}";
// string o = "";

// foreach(var i in n){
//     if(char.IsWhiteSpace(i))
//     {
//         s += i;
//     }

//     foreach(var k in encryp )
//     {
//     if(k.Key.Contains(i))
//     {
//         s += k.Value;
//     }
//     }
// }


// foreach(var c in n1){
//     if(char.IsWhiteSpace(c))
//     {
//         o += c;
//     }

//     foreach(var k in encryp )
//     {
//     if(k.Value.Contains(c))
//     {
//         o += k.Key;
//     }
//     }
// }

// Console.WriteLine(s);
// Console.WriteLine(o);

//ANOTHER METHOD OF WRITING THE CYPHER CODE

string[] alpha = p.Split(',');
string[] code = m.Split(',');

var encryp = new Dictionary<string,string>();

for(int i=0; i<code.Length; i++){
    encryp.Add(alpha[i],code[i]);
}

string n = "the quick brown fox";
string s = "";

string n1 = "&%}-!(?% ({ ! &||$ `}|&}!--%}";
string o = "";

int r =0;

for(int i=0;i<n.Length;i++){
        if(char.IsWhiteSpace(n[i]))
        {
            s += n[i];
            r++;
        }
        if(encryp.ContainsKey(n[i].ToString()))
        {
            foreach(var k in encryp)
            {
            if(k.Key.Contains(n[i])){
            s += k.Value;
                }
            }
        }
}


for(int i=0;i<n1.Length;i++){
        if(char.IsWhiteSpace(n1[i]))
        {
            o += n1[i];
            r++;
        }
        if(encryp.ContainsValue(n1[i].ToString()))
        {
            foreach(var k in encryp)
            {
            if(k.Value.Contains(n1[i])){
            o += k.Key;
                }
            }
        }
}

Console.WriteLine(s);
Console.WriteLine(o);