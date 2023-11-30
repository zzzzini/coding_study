function solution(name, yearning, photo) {
    var answer = [];
    var map = new Map();
    var score;
    
    for (var i=0; i<name.length; i++) {
        map.set(name[i], i);
    }
    
    for (var i=0; i<photo.length; i++) {
        score = 0;
        
        photo[i].forEach(function(item) {
            if (name.includes(item)) {
                score += yearning[map.get(item)];   
            }
        })
        
        answer[i] = score;
    }
    return answer;
}