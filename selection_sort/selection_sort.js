let arr=[14,11,18,16,9,2];
        // let min,temp;
        // for(i=0;i<arr.length;i++){
        //     min=i;
        //     for(j=i+1;j<arr.length;j++){
        //         if(arr[j]<arr[i] && arr[j]<arr[min]){
        //             min=j;
        //         }
        //     }
        //     temp=arr[i];
        //     arr[i]=arr[min];
        //     arr[min]=temp;
        // }

        let max,temp;
        for(i=0;i<arr.length;i++){
            max=i;
            for(j=i+1;j<arr.length;j++){
                if(arr[j]>arr[i] && arr[j]>arr[max]){
                    max=j;
                }
            }
            temp=arr[i];
            arr[i]=arr[max];
            arr[max]=temp;
        }

        document.write(arr);