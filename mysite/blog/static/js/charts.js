var xDataString = document.getElementById('x-data').value;
var yDataString = document.getElementById('y-data').value;

var xData = JSON.parse(xDataString);
var yData = JSON.parse(yDataString);
var data = [];

for(let i = 0; i < xData.length; i++) {
    data.push({x: xData[i], y: yData[i]});
}

var margin = { top: 20, right: 20, bottom: 30, left: 40 },
width = 600 - margin.left - margin.right,
height = 400 - margin.top - margin.bottom;

var svg = d3.select("#scatterPlot")
.append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var x = d3.scaleLinear().range([0, width]);
var y = d3.scaleLinear().range([height, 0]);

x.domain(d3.extent(data, function (d) { return parseFloat(d.x); })).nice();
y.domain(d3.extent(data, function (d) { return parseFloat(d.y); })).nice();

svg.selectAll(".dot")
    .data(data)
    .enter().append("circle")
    .attr("class", "dot")
    .attr("r", 3.5)
    .attr("cx", function (d) { return x(parseFloat(d.x)); })
    .attr("cy", function (d) { return y(parseFloat(d.y)); });

svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

svg.append("g")
    .call(d3.axisLeft(y));
