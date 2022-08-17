const p = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV');
const m = ('!@#$%^&*()_+-?|\/}{][><_~=`1234567890');

p.split('')
m.split('')

r = '';
const k = ('word in cell');
k.split('')
let dict ={};
for(i=0; i<p.length; i++){
    dict[p[i]] = m[i]
}

for(w of k) {
    if(w in dict){
        r += dict[w]
    }else{ r += w}
}
console.log(r)
