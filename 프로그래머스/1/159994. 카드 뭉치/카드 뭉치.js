function solution(cards1, cards2, goal) {
    var answer = '';
    var solve = true;
    var idx;
    
    goal.forEach(function(item) {
        if (cards1.includes(item) && cards1.indexOf(item) == 0) {
            idx = cards1.indexOf(item);
            cards1.splice(idx, 1);
        }
        else if (cards2.includes(item) && cards2.indexOf(item) == 0) {
            idx = cards2.indexOf(item);
            cards2.splice(idx, 1);
        }
        else {
            solve = false;
        }
    })
    
    if (solve) {
        answer += "Yes";
    }
    
    else {
        answer += "No";
    }
    
    return answer;
}