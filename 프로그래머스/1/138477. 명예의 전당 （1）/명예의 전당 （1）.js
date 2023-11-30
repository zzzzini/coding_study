function solution(k, score) {
    var answer = [];
    var fame = [];
    
    for(var i=0; i<score.length; i++) {
        if(fame.length == k) {
            if(fame[fame.length-1] >= score[i]) {
                answer.push(fame[fame.length-1]);
                continue;
            }
            fame.pop();
        }
        fame.push(score[i]);
        fame.sort((a, b) => b - a);
        answer.push(fame[fame.length-1]);
    }
    return answer;
}