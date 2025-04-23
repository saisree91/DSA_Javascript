function view(){
    let arr=[2,3,4,5,6];
    let num=0;
    let ele=parseInt(document.getElementById('element').value);
    for(let i=0;i<arr.length;i++){ 
        if(arr[i]==ele){ 
        document.write(`element ${ele} found at index ${i}`) ;
        num=1;
    } 

} 
if(num==0){
    document.write("Element not found in array");
}

    }