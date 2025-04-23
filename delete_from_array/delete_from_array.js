function view(){
    let arr=[2,3,4,5,6];
    let ind=parseInt(document.getElementById('index').value);
    for(let i=ind;i<arr.length;i++){
        if(i==arr.length-1){
            arr.length=arr.length-1;
   
        }
        else{
            arr[i]=arr[i+1];
        }
       
    }
    if(ind>=arr.length){
        document.write("out of range. The array remains same ");
    }
    
   
    document.write(arr);
    
    
}