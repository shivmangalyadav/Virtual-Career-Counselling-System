import React, { Fragment, Component } from "react";
import { AppBar, Tabs } from "@material-ui/core";
import { Tab } from "@material-ui/core";
import { Link } from "react-router-dom";

class Navbar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      login_token: ''
    }
  }

  componentWillMount() {
    this.setState({
      
      login_token:sessionStorage.getItem('access_token')
    })
  }
  
  render() {
    const {login_token} = this.state

    return (
      <Fragment>
        <AppBar style={{ position: "sticky", top: "60px" }}>
          <Tabs
            style={{
              borderStyle: "circle",
              borderRadius: "2px",
              overflow: "hidden",
              background: "#48494D",
              color: "white",
            }}
          >
            <Tab
              style={{
                width: "20px",
                border: "2px solid red",
                background: "rgb(255, 42, 5)",
              }}
              label="Home"
              component={Link}
              to="/"
            />
            {!login_token ?<>
            <Tab label="Sign In" component={Link} to="/signin" />
            <Tab label="Sign up" component={Link} to="/signup" /> </>: <>
            <Tab label="Profile" component={Link} to="/profile" />
            <Tab
              style={{ float: "right" }}
              label="Logout"
              component={Link}
              to="/logout"
              onChange={this.handleLogout}
            /> </>}
          </Tabs>
          
        </AppBar>
        
      </Fragment>
    );
  }
}

export default Navbar;
