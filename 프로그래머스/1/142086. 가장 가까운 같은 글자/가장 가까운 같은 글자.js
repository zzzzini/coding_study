function solution(s) {
    var answer = [];
    var counter;
    var len;
    for (var i=0; i<s.length; i++) {
        counter = 0;
        len = 0;
        
        for (var j=0; j<i; j++) {
            if (s[i] == s[j]) {
                counter += 1;
                len = i-j;
            }
        }
        if (counter > 0) {
            answer[i] = len;
        }
        else {
            answer[i] = -1;
        }
        
    }
    
    return answer;
}