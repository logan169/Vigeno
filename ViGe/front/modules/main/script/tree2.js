/*var treeData = [
  {
    "name": "Annotation",
    "parent": "null",
    "children": [
      {
        "name": "Gene",
        "parent": "Annotation",
        "children": [
          {
            "name": "Exon",
            "parent": "Gene",
            "children": [
            {
              "name": "Sequence 1",
              "parent": "Exon"
            },
            {
              "name": "Sequence 2",
              "parent": "Exon"
            },
            {
              "name": "Sequence 3",
              "parent": "Exon"
            },
            ]
          },
          {
            "name": "Intron",
            "parent": "Gene",
            "children":[
            {
              "name": "Sequence 4",
              "parent": "Exon"
            }
            ]
          },
          {
            "name": "UTR",
            "parent": "Gene",
            "children":[
            {
              "name": "Sequence 7",
              "parent": "Exon"
            }
            ]
          }
        ]
      },

      {
        "name": "Intergene",
        "parent": "Annotation",
        "children":[
                     {
            "name": "Sequence 6",
            "parent": "Intergene"
          }
          ]
      }
    ]
  }
];

*/
var treeData=[{'name': 'peptide', 'parent': 'null', 'children': [{'name': 'AEAEQTLRF', 'parent': 'peptide', 'children': [{'name': 12, 'parent': 'AEAEQTLRF'}]}, {'name': 'AEAGHLEGHCL', 'parent': 'peptide', 'children': [{'name': 14, 'parent': 'AEAGHLEGHCL'}]}, {'name': 'AEAFEAIPRAL', 'parent': 'peptide', 'children': [{'name': 13, 'parent': 'AEAFEAIPRAL'}]}, {'name': 'AEAEKLGGQSY', 'parent': 'peptide', 'children': [{'name': 10, 'parent': 'AEAEKLGGQSY'}]}, {'name': 'AEAELLNLRKI', 'parent': 'peptide', 'children': [{'name': 11, 'parent': 'AEAELLNLRKI'}]}, {'name': 'AEAHARIHL', 'parent': 'peptide', 'children': [{'name': 16, 'parent': 'AEAHARIHL'}]}, {'name': 'AEAHAKVRL', 'parent': 'peptide', 'children': [{'name': 15, 'parent': 'AEAHAKVRL'}]}, {'name': 'AEAEAVREVY', 'parent': 'peptide', 'children': [{'name': 9, 'parent': 'AEAEAVREVY'}]}]}]


//************************************************************functions************************************************
function update(source) {

  // Compute the new tree layout.
  var nodes = tree.nodes(root).reverse(),
	  links = tree.links(nodes);

  // Normalize for fixed-depth.
  nodes.forEach(function(d) { d.y = d.depth * 180; });

  // Update the nodes…
  var node = svg.selectAll("g.node")
	  .data(nodes, function(d) { return d.id || (d.id = ++i); });

  // Enter any new nodes at the parent's previous position.
  var nodeEnter = node.enter().append("g")
	  .attr("class", "node")
	  .attr("transform", function(d) { return "translate(" + source.y0 + "," + source.x0 + ")"; })
	  .on("click", click);

  nodeEnter.append("circle")
	  .attr("r", 1e-6)
	  .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

  nodeEnter.append("text")
	  .attr("x", function(d) { return d.children || d._children ? -13 : 13; })
	  .attr("dy", ".35em")
	  .attr("text-anchor", function(d) { return d.children || d._children ? "end" : "start"; })
	  .text(function(d) { return d.name; })
	  .style("fill-opacity", 1e-6);

  // Transition nodes to their new position.
  var nodeUpdate = node.transition()
	  .duration(duration)
	  .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

  nodeUpdate.select("circle")
	  .attr("r", 10)
	  .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

  nodeUpdate.select("text")
	  .style("fill-opacity", 1);

  // Transition exiting nodes to the parent's new position.
  var nodeExit = node.exit().transition()
	  .duration(duration)
	  .attr("transform", function(d) { return "translate(" + source.y + "," + source.x + ")"; })
	  .remove();

  nodeExit.select("circle")
	  .attr("r", 1e-6);

  nodeExit.select("text")
	  .style("fill-opacity", 1e-6);

  // Update the links…
  var link = svg.selectAll("path.link")
	  .data(links, function(d) { return d.target.id; });

  // Enter any new links at the parent's previous position.
  link.enter().insert("path", "g")
	  .attr("class", "link")
	  .attr("d", function(d) {
		var o = {x: source.x0, y: source.y0};
		return diagonal({source: o, target: o});
	  });

  // Transition links to their new position.
  link.transition()
	  .duration(duration)
	  .attr("d", diagonal);

  // Transition exiting nodes to the parent's new position.
  link.exit().transition()
	  .duration(duration)
	  .attr("d", function(d) {
		var o = {x: source.x, y: source.y};
		return diagonal({source: o, target: o});
	  })
	  .remove();

  // Stash the old positions for transition.
  nodes.forEach(function(d) {
	d.x0 = d.x;
	d.y0 = d.y;
  });
}

// Toggle children on click.
function click(d) {
  if (d.children) {
	d._children = d.children;
	d.children = null;
  } else {
	d.children = d._children;
	d._children = null;
  }
  update(d);
}

// ************** Generate the tree diagram	 *****************
var margin = {top: 20, right: 120, bottom: 20, left: 120},
	width = 960 - margin.right - margin.left,
	height = 500 - margin.top - margin.bottom;

var i = 0,
	duration = 750,
	root;

var tree = d3.layout.tree()
	.size([height, width]);

var diagonal = d3.svg.diagonal()
	.projection(function(d) { return [d.y, d.x]; });

var svg = d3.select("#visRow").append("svg")
	.attr("width", width + margin.right + margin.left)
	.attr("height", height + margin.top + margin.bottom)
  .append("g")
	.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

root = treeData[0];
root.x0 = height / 2;
root.y0 = 0;

update(root);



