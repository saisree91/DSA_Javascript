let arr=[1,2,3,4,5];
let a,b,i,j,temp;
let n=Math.floor(arr.length/2);
function swap(a,b){
    if(a<=b){
    temp=arr[a];
    arr[a]=arr[b];
    arr[b]=temp;
    swap(a+1,b-1);
    }
}
    swap(0,arr.length-1);
document.write(arr);