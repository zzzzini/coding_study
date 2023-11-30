function solution(food) {
    var answer = '';
    var rev = '';
    
    for (var i=1; i<food.length; i++) {
        if (food[i] % 2) food[i] -= 1;
        
        for (var j=0; j<food[i]/2; j++) {
            answer += i;
        }
    }
    
    for (var i=answer.length-1; i>=0; i--) {
        rev += answer[i];
    }
    
    answer += 0;
    answer += rev;
    return answer;
}