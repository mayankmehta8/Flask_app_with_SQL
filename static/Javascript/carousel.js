let n=0

function next(){
    if(n==-400)
    {
        n=100
    }
    let count=0
    let interval = setInterval(function(){
        count+=1;
        n -= 1;
        if(count === 100){
            clearInterval(interval);
        }
    
        document.getElementById('Frame').style.marginLeft=n+"vw"
    
    }, 5);

    document.getElementById('Frame').style.marginLeft=n+"vw"
}


function prev(){
    if(n==0)
    {
        n=-500
    }
    let count=0
    let interval = setInterval(function(){
        count+=1;

        n += 1;
        if(count === 100){
            clearInterval(interval);
        }
    
        document.getElementById('Frame').style.marginLeft=n+"vw"
    
    }, 5);


}
