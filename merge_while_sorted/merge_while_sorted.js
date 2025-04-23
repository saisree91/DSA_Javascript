function view(){
    let arr1=[3,7,12,36,79,80];
    let arr2=[4,9,45,63];
    let arr3=[];
    let a1=0;
    let a2=0;
    let a3=0;
    let length1=arr1.length;
    let length2=arr2.length;
   while(a1<length1 && a2<length2){
        if(arr1[a1]<arr2[a2]){
            arr3[a3]=arr1[a1];
            a1++;
        }
        else{
            arr3[a3]=arr2[a2];
            a2++;
        }
        a3++;
    }
    for(let e1=a1;e1<length1;e1++){
        arr3[a3]=arr1[e1];
        a3++;
    }
    for(let e2=a2;e2<length2;e2++){
        arr3[a3]=arr2[e2];
        a3++;
    }

document.write(arr3);
}