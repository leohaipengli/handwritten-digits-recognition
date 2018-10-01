var canvas = $('#drawing-board');
var context = document.getElementById('drawing-board').getContext("2d");
var width = canvas[0].width;
var height = canvas[0].height;
var clickX = [];
var clickY = [];
var clickDrag = [];
var paint;
var dataURL = document.getElementById('drawing-board').toDataURL('image/png');
var lineWidth = 12;
document.getElementById('dataURL').value = dataURL;
context.fillStyle = '#000';
context.fillRect(0, 0, width, height);


function addClick(x, y, dragging)
{
    clickX.push(x);
    clickY.push(y);
    clickDrag.push(dragging);
}

function redraw(){
    context.clearRect(0, 0, context.canvas.width, context.canvas.height); // Clears the canvas
    context.fillStyle = '#000';
    context.fillRect(0, 0, width, height);

    context.strokeStyle = "#FFF";
    context.lineJoin = "round";
    context.shadowBlur = 20;
    context.shadowColor = '#FFF';
    context.lineWidth = lineWidth;

    for(var i=0; i < clickX.length; i++) {
        context.beginPath();
        if(clickDrag[i] && i){
            context.moveTo(clickX[i-1], clickY[i-1]);
            // x0 = clickX[i-1];
            // y0 = clickY[i-1];
            // gradMode = 'linear';
        }else{
            context.moveTo(clickX[i]-1, clickY[i]);
            // x0 = clickX[i] - 1;
            // y0 = clickY[i];
            // gradMode = 'radial';
        }
        // x1 = clickX[i];
        // y1 = clickY[i];
        // if(gradMode === 'linear') {
        //     a = (x0+x1) / 2 - (y1-y0) * Math.sqrt(lineWidth / 2 * ((x1-x0)**2 + (y1-y0)**2));
        //     b = (y0+y1) / 2 + (x1-x0) * Math.sqrt(lineWidth / 2 * ((x1-x0)**2 + (y1-y0)**2))
        //     grd=context.createLinearGradient((x0+x1)/2,(y0+y1)/2, a, b);
        //     // grd=context.createLinearGradient(140, 140, 280, 280);
        // } else if(gradMode === 'radial') {
        //     grd=context.createRadialGradient(x1, y1, lineWidth/10+1, x1, y1, lineWidth);
        // }
        // grd.addColorStop(0,"white");
        // grd.addColorStop(1,"gray");
        // context.strokeStyle = grd;
        context.lineTo(clickX[i], clickY[i]);
        context.closePath();
        context.stroke();
    }
}
function reset_board(e) {
    context.clearRect(0, 0, context.canvas.width, context.canvas.height); // Clears the canvas
    clickX = [];
    clickY = [];
    clickDrag = [];
    context.fillStyle = '#000';
    context.fillRect(0, 0, width, height);
}

function stop_drawing() {
    paint = false;
    dataURL = document.getElementById('drawing-board').toDataURL('image/png');
    document.getElementById('dataURL').value = dataURL;
}

canvas.mousedown(function(e){
    var rect = canvas[0].getBoundingClientRect();
    paint = true;
    addClick(e.clientX- rect.left, e.clientY - rect.top);
    redraw();
});

canvas.mousemove(function(e){
    var rect = canvas[0].getBoundingClientRect();
    if(paint){
        addClick(e.clientX- rect.left, e.clientY - rect.top, true);
        redraw();
    }
});

canvas.mouseup(function(e){
    stop_drawing();
});

canvas.mouseleave(function(e){
    stop_drawing();
});

$('#clear').click(function () {
    reset_board();
});

