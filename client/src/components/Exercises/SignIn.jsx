import React, { Component } from "react";
import { Container, Typography, TextField, Button } from "@material-ui/core";
import { Alert } from "@material-ui/lab";

import CssBaseline from "@material-ui/core/CssBaseline";
import Link from "@material-ui/core/Link";
import Grid from "@material-ui/core/Grid";
import Box from "@material-ui/core/Box";
import { withStyles } from "@material-ui/core/styles";

const useStyles = (theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  form: {
    width: "100%", // Fix IE 11 issue.
    marginTop: theme.spacing(3),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
});

const initialState = {
  email: "",
  password: "",
  emailError: "",
  passwordError: ""
};

class SignIn extends Component {
  constructor(props) {
    super(props);

    this.state = {
      email: "",
      password: "",
      emailError: "",
      passwordError: "",
      msg: "",
      status: null,
    };
    
  }

  validate = () => {
    let emailError = ''
    let passwordError = ''

    if (!this.state.email.includes("@")) {
      console.log("Invalid email");
      emailError = "Invalid Email!"
     }
    if (this.state.password.length <= 4) {
      console.log("Password must have 5 or more character");
      passwordError = "Paswword must contains atleast 5 characters."
    }
    if (emailError || passwordError) {
      this.setState({emailError, passwordError})
      return false;
    }

    return true;
  };

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    const isValid = this.validate()

    if (isValid) {
      console.log("valid");
      fetch("/signin", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.state),
      }).then((response) =>
        response.json().then((data) => {
          this.setState({
            emailError: "",
            msg: data["msg"],
            status: data["status"],
          });
          console.log("okk");
          console.log(data);
          sessionStorage.setItem("access_token", data["access_token"]);
          if (this.state.status) {
            console.log(this.state.status);

            this.props.history.push("/");
          }
        })
      );
      this.setState(initialState)
      
    }
    this.setState({
      msg: '',
      status: null
    })
  };

  render() {
    const { classes } = this.props;
    return (
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <div className={classes.paper}>
          <Typography component="h1" variant="h5">
            Sign in
          </Typography>
          <form
            className={classes.form}
            onSubmit={this.handleSubmit}
            noValidate
          >
            <TextField
              variant="outlined"
              margin="normal"
              type="email"
              required
              fullWidth
              id="email"
              label="Email Address"
              name="email"
              autoFocus
              value={this.state.email}
              onChange={this.handleChange}
            />
            {this.state.emailError ? (
              <p
                style={{
                  padding: 0,
                  margin: 0,
                  color: "red",
                  fontSize: "14px",
                  textAlign: "center",
                }}
              >
                {this.state.emailError}
              </p>
            ) : null}
            <TextField
              variant="outlined"
              type="password"
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              value={this.state.password}
              onChange={this.handleChange}
            />
            {this.state.passwordError ? (
              <p
                style={{
                  padding: 0,
                  margin: 0,
                  color: "red",
                  fontSize: "14px",
                  textAlign: "center",
                }}
              >
                {this.state.passwordError}
              </p>
            ) : null}
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
            >
              Sign In
            </Button>
            <Grid container>
              <Grid item>
                <Link href="/signup" variant="body2">
                  {"Don't have an account? Sign Up"}
                </Link>
              </Grid>
            </Grid>
          </form>
          <p>
            {this.state.msg ? (
              <Alert severity={this.state.status? 'success': 'error'}>{this.state.msg}</Alert>
            ) : null}
          </p>
        </div>
        <Box mt={8}></Box>
      </Container>
    );
  }
}

export default withStyles(useStyles)(SignIn);
