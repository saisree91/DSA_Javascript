let n=prompt("Enter number");
let a;
let result='';
function fib(a){
    if(a<=1){
        return 1;
    }
    else{
         return fib(a-1)+fib(a-2);
    }
}
for(let i=0;i<n;i++){
result+= fib(i)+ '';
    }
    document.write(`the fibnocci series upto ${n} is ${result}`);