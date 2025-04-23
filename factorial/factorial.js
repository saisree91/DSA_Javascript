let n=prompt("Enter number");
let result;
function fact(n){
    if(n==1){
       return 1;
    
    }
    else{
        return n*fact(n-1);
    }

}

document.write(`Factorial of ${n} is ${fact(n)}`);