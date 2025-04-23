let arr = [1, 2, 3, 4, 5, 6, 7, 8];
           
            let low = 0;
        let high = arr.length - 1;
        let ele = prompt("enter value to be searched");
            
            function bin_search(low,high,ele){
                let mid = Math.floor((low + high) / 2);
            if (low <= high) {
                if (arr[mid] == ele) {
                    document.write(`element found at index ${mid}`);
                }
                else if (arr[mid] > ele) {
                    bin_search(low,mid-1,ele);
                }
                else {
                    low = mid + 1;
                    bin_search(mid+1,high,ele);
                }
            }
            else {
                document.write("element not found");
            }
        }
    
        bin_search(low,high,ele);