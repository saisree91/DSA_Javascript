let arr=[6,5,4,3,2,1];
        let n=arr.length-1;
        while(n)
    {
        for(i=0;i<arr.length-1;i++){
            if(arr[i+1]<arr[i]){
                let temp=arr[i];
                arr[i]=arr[i+1];
                arr[i+1]=temp;
            }
        }
        n--;
    }

    document.write(arr);