let str="good";
        let Obj_str={};
        for(let i=0;i<str.length;i++){
            let key=str[i];
            if(!Obj_str[key]){
                Obj_str[key]=1;
            }
            else{
                Obj_str[key] += 1;
            }
        }
        let max=0;
        let max_occ = "";
       
        document.write(keys);
        for (let key of keys) {
            if (Obj_str[key] > max) {
               max = Obj_str[key];
               max_occ = key;
    }
}
        document.write(`Maximum Occuring letter is ${max_occ}`);