function solution(players, callings) {
    var answer = [];
    var temp;
    var map = new Map();
    
    for (var i=0; i<players.length; i++) {
        map.set(players[i], i);
    }
    
    for (var i=0; i<callings.length; i++) {
        var now = callings[i];
        var prev = players[map.get(now) - 1]
        
        temp = players[map.get(now)-1];
        players[map.get(now)-1] = players[map.get(now)];
        players[map.get(now)] = temp;
        
        map.set(now, map.get(now) - 1);
        map.set(prev, map.get(prev) + 1);
    }
    
    answer = players;
    return answer;
}