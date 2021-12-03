function confirmOperation(base, id, text) {
        if(confirm(text) == true) {
            //elem = 1;
            window.location.href = base + id
        }
        else {
             return 0;
        }          
    }