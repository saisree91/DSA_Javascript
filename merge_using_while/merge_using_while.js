function view(){
    let arr1=[4,1,3,2,7,4];
    let arr2=[8,5,7];
    let arr3;
    let length1=arr1.length;
    let length2=arr2.length;
    let i=length1;
    while(i<=(length1+length2-1)){
        arr1[i]=arr2[i-length1];
        i++;
    }
    document.write(arr1);
}