// import * as d3 from d3;

const render = (bus, branch) => {
    console.log(bus, branch);
    const size = {
        viewBox: {minX: 0, minY: 0, width: 1000, height: 1000},
        margin: {left: 20, right: 40, top: 20, bottom: 40},
        padding: {left: 20, right: 40, top: 20, bottom: 40}
    };
    
    console.log("bus property", bus.x, bus.y)
    const x = Object.keys(bus.x).map(d => {
        return bus.x[d];
    });
    const y = Object.keys(bus.x).map(d => {
        return bus.y[d];
    });
    const xY = Object.keys(bus.x).map(d => {
        return {id: bus["bus id"][d], x: bus.x[d], y: bus.y[d]};
    })
    console.log("new x y", xY);

    const xMin = 0;
    const yMin = 0;
    const xMax = d3.max(x);
    const yMax = d3.max(y);
    const xAdditional = xMax * 0.1;
    const yAdditional = yMax * 0.1;
    console.log("xMax, yMax", xMax, yMax);
    
    const xDomain = [xMin, xMax];
    const yDomain = [yMin, yMax];

    const xRange = [size.margin.left + size.padding.left , size.margin.left + size.padding.left + size.viewBox.width - size.margin.right - size.padding.right];
    const yRange = [size.margin.top + size.padding.top, size.margin.top + size.padding.top + size.viewBox.height - size.margin.bottom - size.padding.bottom];
    console.log("xDomain xRange", xDomain, xRange);
    console.log("yDomain yRange", yDomain, yRange);

    const xScale = d3.scaleLinear(xDomain, xRange);
    const yScale = d3.scaleLinear(yDomain, yRange);

    const mouseover = (event, d) => {
        // 콘솔 대신 툴바 띄우기
        console.log("mouseover event", event, d);
        nodes.filter((m, i) => {
            return m === d;
        })
            .attr("fill", "blue")
            .attr("fill-opacity", 0.8);

        edges.filter((m, i) => {
            return (m.from == d.id || m.to == d.id);
        })
            .attr("stroke-width", "2px")
            .attr("stroke-opacity", 1);
        // 간선과 인접한 정점도 강조할 것
    };

    const mouseout = (event, d) => {
        // console.log("mouseout event", event, d);
        nodes.attr("fill", "black")
            .attr("fill-opacity", 0.4);
        
        edges.attr("stroke-width", "1px")
            .attr("stroke-opacity", 0.2);
    }

    const svg = d3.select("#main")
        .attr("viewBox", `${size.viewBox.minX}, ${size.viewBox.minY}, ${size.viewBox.width}, ${size.viewBox.height}`);
    
    const border = svg.append("g")
        .append("rect")
        .attr("fill", "none")
        .attr("stroke", "black")
        .attr("width", size.margin.left + size.viewBox.width - size.margin.left)
        .attr("height", size.margin.top + size.viewBox.height - size.margin.top);

    const edges = svg.append("g")
        .selectAll("path")
        .data(branch)
        .join("path")
        .attr("d", d => `M${xScale(x[d.from-1])}, ${yScale(y[d.from-1])} L${xScale(x[d.to-1])}, ${yScale(y[d.to-1])}`)
        .attr("stroke", "black")
        .attr("fill", "none")
        .attr("stroke-opacity", 0.2);
    
    const nodes = svg.append("g")
        .selectAll("circle")
        .data(xY)
        .join("circle")
        .attr("cx", d => (xScale(d.x)))
        .attr("cy", d => (yScale(d.y)))
        .attr("r", 5)
        .attr("fill", "black")
        .attr("fill-opacity", 0.4)
        .on("mouseover", mouseover)
        .on("mouseout", mouseout);
}

d3.json("../../random bus generator/result/bus-1062 random position.json")
    .then(bus => {
        d3.csv("../../random bus generator/data/branch-1062.csv")
            .then(branch => {
                render(bus, branch);
            })
    })

