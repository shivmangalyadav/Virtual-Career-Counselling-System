import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";


import Dashboard from "./components/Exercises/Dashboard";
import Logout from "./components/Exercises/Logout";
import Profile from "./components/Exercises/Profile";
import Navbar from "./components/Layouts/Navbar";
import SignUp from "./components/Exercises/SignUp";
import SignIn from "./components/Exercises/SignIn";


const Routes = () => {
  return (
    <Router>
      <Navbar />

      <Switch>
        <Route path="/" exact={true} component={Dashboard} />
        <Route path="/signin" exact={true} component={SignIn} />
        <Route path="/signup" exact={true} component={SignUp} />
        <Route path="/logout" exact={true} component={Logout} />
        <Route path="/profile" exact={true} component={Profile} />
      </Switch>
    </Router>
  );
};

export default Routes;
