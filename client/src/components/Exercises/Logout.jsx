import React, { Component } from "react";

export class Logout extends Component {
  constructor(props) {
    super(props);
    this.state = {
      msg: ''
    }
  }
  
  componentDidMount() {
    const token = sessionStorage.getItem("access_token");
    console.log(token);
    sessionStorage.removeItem('access_token')
    this.props.history.push("/signin")
  }
  render() {
    return (
      <div>
        <h1>{this.token}</h1>
      </div>
    );
  }
}

export default Logout;
