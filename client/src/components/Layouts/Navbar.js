import React, { Fragment, Component } from "react";
import { AppBar, Tabs } from "@material-ui/core";
import { Tab } from "@material-ui/core";
import { Link, withRouter  } from "react-router-dom";

class Navbar extends Component {

  logOut(e) {
    e.preventDefault()
    sessionStorage.removeItem('access_token')
    this.props.history.push("/signin")
  }
  
  render() {

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
            <Tab label="Course" component={Link} to="/course" />

            {!sessionStorage.getItem("access_token") ?<>
            <Tab label="Sign In" component={Link} to="/signin" />
            <Tab label="Sign up" component={Link} to="/signup" /> </>: <>
            <Tab label="Profile" component={Link} to="/profile" />
            <Tab
              style={{ float: "right" }}
              label="Logout"
              onClick={this.logOut.bind(this)}
            /> </>}
          </Tabs>
          
        </AppBar>
        
      </Fragment>
    );
  }
}

export default withRouter(Navbar);
