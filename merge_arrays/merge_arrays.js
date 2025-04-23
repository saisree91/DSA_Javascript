function view(){
    let arr1=[4,1,3,2,7,4];
    let arr2=[8,5,7];
    let length1=arr1.length;
    let length2=arr2.length;
    for(let i=length1;i<=(length1+length2-1);i++){
        arr1[i]=arr2[i-length1];
    }
    document.write(arr1);
}