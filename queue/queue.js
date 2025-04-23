let q=[];
let size=q.length;
let ele;
function enqueue(ele){
    ele=document.getElementById('insert').value;
    q[size]=ele;
    size=q.length;
    
}

function dequeue(){
    for(i=0;i<q.length-1;i++)
{
    q[i]=q[i+1];
}
q.length-=1;
    size=q.length;
}

function display(){
    document.write(q);
    document.write(q.length);
}

function front(){
    document.write(q[0]);
}

function rear(){
    document.write(q[q.length-1]);
}

function isempty(){
    if(q.length==0){
        document.write("queue is empty");
    }
    else{
        document.write("queue is not empty");
    }
}