let st=[];
   
    let max=5;
    let n;
    size=st.length;
    function push(n){
        n= document.getElementById('insert').value;
            st[size]=n;
            size+=1;
    
        
    }
    function pop(){
        if(size==0){
            alert("stack is empty");
        }
        else{
        st.length-=1;
        size-=1;
        }
    }
    
    function display(){
        document.write(st);
    }
