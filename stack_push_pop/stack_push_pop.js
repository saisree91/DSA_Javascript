let st=[];
    let n;
    let max=5;
    size=st.length;
    function push(n){
        if(size==max){
            document.write("stack is full you cannot insert" + "" + n);
        }
        else{
            st[size]=n;
            size+=1;
        }
        
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
    push(1);
    push(2);
    push(3);
    pop();
    push(4);
    push(5);
    pop()
    push(6);
    push(7);
    push(8)