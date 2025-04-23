function view(){
    let arr=[2,3,4,5,6];
    let ele=parseInt(document.getElementById('element').value);
    let ind=parseInt(document.getElementById('index').value);
    for(let i=arr.length-1;i>=ind;i--){
        if(i==ind){
        arr[i+1]=arr[i];
        arr[i]=ele;
    }
    else{
        arr[i+1]=arr[i];
    }
    }

   
    document.write(arr);
    
    
}