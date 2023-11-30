function solution(t, p) {
    var answer = 0;
    var l = t.length - p.length + 1;
    var counter = 0;
    
    for(var i=0; i<l; i++) {
        var str = t.slice(i,i+p.length);
        
        if (parseInt(p) >= parseInt(str)) {
            counter += 1;
        }
    }
    
    answer = counter;
    return answer;
}