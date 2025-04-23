let str='good morning';
let result="";
let st=[];
let size=0;

function push(char){
    st[size]=char;
    size+=1;
}

function pop(){
    rem=st[st.length-1];
    st.length-=1;
    size-=1; 
    return rem;
}

for(let i=0;i<str.length;i++){
    push(str[i]);
}

for(let i=0;i<str.length;i++){
    res_char=pop();
    result+=res_char;
}

    document.write(result);