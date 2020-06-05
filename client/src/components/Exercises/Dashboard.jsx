import React, { Component } from "react";
import Tree from "react-d3-tree";

// const svgSquare = {
//   shape: 'rect',
//   shapeProps: {
//     width: "80px",
//     height: "40px",
//     x: -10,
//     y: -10,
//   }
// } 
// const myTreeData = [
//   {
//     name: "Top Level",
//     children: [
//       {
//         name: "Level 2",
//         children: [
//           {name: "Level 3"}
//         ]
//       },
//       {
//         name: "Level 2",
//         children: [{
//           name: 'Level 3'
//       },
//       {
//         name: "Level 3"
//       }]
//       },
//     ],
//   },
// ];

class Dashboard extends Component {
  render() {
    // const name = names.map((n) => <h1>{n}</h1>);
    return (
      <div>
        <h1>Dashboard</h1>
        {this.props.auth}
        {/* <div id="treeWrapper" style={{ width: "90em", height: "70em" }}>
          <Tree data={myTreeData} nodeSvgShape={svgSquare}/>
        </div> */}
      </div>
    );
  }
}

export default Dashboard;
