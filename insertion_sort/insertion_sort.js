let arr=[6,4,5,1,3,2];
        let n=arr.length-2;
        let res_arr=[];
        res_arr[0]=arr[0];
        let curr_size=1;
        for(let i=1;i<arr.length;i++){
            for(let j=i-1;j>=0;j--){
                if(arr[i]<res_arr[j]){
                    res_arr[j+1]=res_arr[j];
                    res_arr[j]=arr[i];
                }
            }
        }

        document.write(res_arr);