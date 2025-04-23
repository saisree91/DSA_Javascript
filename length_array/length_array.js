function len( num){
    let n=0;
    for(let items of num){
        n+=1;
    }
    document.write(n);

}
let numbers = [12, 13, 14, 25];
len(numbers);