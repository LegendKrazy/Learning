
var checkPointRadius = 400;
var laps = parseInt(readline()); // number of laps
var checkPointCount = parseInt(readline()); // number of checkpoints for one lap
var checkPointX = [];
var checkPointY = [];
for (var i = 0; i < checkPointCount; i++) {
    var inputs = readline().split(' ');
    checkPointX[i] = parseInt(inputs[0]);
    checkPointY[i] = parseInt(inputs[1]);
}

function coord(x, y) {
    this.x = x;
    this.y = y;
}

function vector(x, y) {
    this.x = x;
    this.y = y;
}

    
function nextEdge(x, y, nextCheckPointId){
    
    var curPoint = new coord(x,y);
    printErr('curPoint: ' + curPoint.x + ', ' + curPoint.y);
    
    var nextPoint = new coord(checkPointX[nextCheckPointId], checkPointY[nextCheckPointId]);
    printErr('nextPoint: ' + nextPoint.x + ', ' + nextPoint.y);
    
    var afterPoint = new coord(0,0);
    if (nextCheckPointId < checkPointCount - 1){    
        afterPoint.x = checkPointX[nextCheckPointId + 1];
        afterPoint.y = checkPointY[nextCheckPointId + 1];
    }
    else {
        afterPoint.x = checkPointX[0];
        afterPoint.y = checkPointY[0];     
    }
    printErr('afterPoint: ' + afterPoint.x + ', ' + afterPoint.y);  
    
    var m1 = new coord(((afterPoint.x + curPoint.x) / 2),(afterPoint.y + curPoint.y) / 2);
    printErr('m1: ' + m1.x + ', ' + m1.y);
    
    var opp = nextPoint.y - m1.y;
    printErr('opp: ' + opp);
    
    var adj = m1.x - nextPoint.x;
    printErr('adj: ' + adj);
    
    theta = Math.atan(opp/adj);
    printErr('theta: ' + theta);
    
    var vectorSign = new vector(1,1);
    if (nextPoint.x - m1.x > 0){
        vectorSign.x = -1;
    }
    if (nextPoint.y - m1.y < 0){
        vectorSign.y = -1;
    }
    if (nextPoint.y - m1.y > 0 && nextPoint.x - m1.x < 0){
        vectorSign.y = -1;
    }
    if (nextPoint.y -m1.y < 0 && nextPoint.x - m1.x > 0){
        vectorSign.x = 1;
        vectorSign.y = 1;
    }

    
    var edgeVector = new vector(vectorSign.x * checkPointRadius * Math.cos(theta), vectorSign.y * checkPointRadius * Math.sin(theta));
    printErr('edgeVector: ' + edgeVector.x + ', ' + edgeVector.y);
    
    var edgePoint = new coord(Math.round(nextPoint.x + edgeVector.x), Math.round(nextPoint.y + edgeVector.y));
    return edgePoint;
    
}

function boostControl(){
    if (Math.abs(vx[0]) < boostThreshold && Math.abs(vy[0]) < boostThreshold){
        thrustLevel = 'BOOST';
    }
}


// game loop
while (true) {
    var x = [];
    var y = [];
    var vx = [];
    var vy = [];
    var nextCheckPointId = [];
    var thrustLevel = 100;
    for (var i = 0; i < playerCount; i++) {
        var inputs = readline().split(' ');
        x[i] = parseInt(inputs[0]);
        y[i] = parseInt(inputs[1]);
        vx[i] = parseInt(inputs[2]);
        vy[i] = parseInt(inputs[3]);
        nextCheckPointId[i] = parseInt(inputs[4]);
    }


    //print('8000 4500 100'); // Coordinates of target point X Y, followed by the thrust to feed to the engines (0 to 100 or BOOST).
    printErr('Speed Vector: ' + vx[0] + ', ' + vy[0]);
    if (nextCheckPointId[0] === 0){
        var target = nextEdge(checkPointX[checkPointCount - 1], checkPointY[checkPointCount - 1], nextCheckPointId[0]);
    }
    else{
        var target = nextEdge(checkPointX[nextCheckPointId[0] - 1], checkPointY[nextCheckPointId[0] - 1], nextCheckPointId[0]);
    }
    printErr('nextEdge: ' + target.x + ', ' + target.y);
    
    boostControl();
    print(target.x + ' ' + target.y + ' ' + thrustLevel);
}
