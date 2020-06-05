import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";


import Dashboard from "./components/Exercises/Dashboard";
import Profile from "./components/Exercises/Profile";
import Navbar from "./components/Layouts/Navbar";
import SignUp from "./components/Exercises/SignUp";
import SignIn from "./components/Exercises/SignIn";
import Course from "./components/Exercises/Course";


const Routes = () => {
  return (
    <Router>
      <Navbar />

      <Switch>
        <Route path="/" exact={true} component={Dashboard} />
        <Route path="/course" exact={true} component={Course} />
        <Route path="/signin" exact={true} component={SignIn} />
        <Route path="/signup" exact={true} component={SignUp} />
        <Route path="/profile" exact={true} component={Profile} />
      </Switch>
    </Router>
  );
};

export default Routes;
