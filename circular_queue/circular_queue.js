let cirque=[];
        let cap=5;
        let front=0; 
        let rear=-1;
        let curr_size=0;
        function push(ele){
            if(curr_size==cap){
                document.write("queue is full");
            }
            else{
                rear=(rear+1)%cap;
                cirque[rear]=ele;
                curr_size+=1;
            }
            }

        function pop(){
            front=(front+1)%cap;
            curr_size-=1;
        }

        push(1);
        push(2);
        push(3);
        pop();
        push(4);
        push(5);
        
        
        push(6);
        pop();
        
        
        let empty_spaces=front-rear-1;
        let i=front;
        while(curr_size)
        {
            document.write(cirque[i]);
            i=(i+1)%cap;
            curr_size-=1;
        }
        
        document.write(empty_spaces);