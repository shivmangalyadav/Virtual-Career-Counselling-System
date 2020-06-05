import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import Link from "@material-ui/core/Link";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import { withStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import { Alert } from "@material-ui/lab";

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
  name: "",
  email: "",
  password: "",
  nameError: "",
  emailError: "",
  passwordError: "",
};

class SignUp extends Component {
  constructor(props) {
    super(props);

    this.state = {
      name: "",
      email: "",
      password: "",
      nameError: "",
      emailError: "",
      passwordError: "",
      msg: "",
      status: null,
    };
  }

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  };

  validate = () => {
    let nameError = "";
    let emailError = "";
    let passwordError = "";

    if (!this.state.name) {
      console.log("Name can not be  empty.");
      nameError = "Name can not be  empty.";
    }
    if (!this.state.email.includes("@")) {
      console.log("Email must include '@'");
      emailError = "Invalid Email!";
    }
    if (this.state.password.length <= 4) {
      console.log("Paswword must have minimum 4 character.");
      passwordError = "Paswword must contains atleast 5 characters.";
    }
    if ((nameError || emailError || passwordError) ) {
      this.setState({nameError, emailError, passwordError})
      return false;
    }
    return true
  };

  handleSubmit = (e) => {
    e.preventDefault();
    const isValid = this.validate()
   
    if (isValid) {
    fetch("/user/signup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(this.state),
    }).then((response) =>
      response.json().then((data) => {
        this.setState({
          msg: data["msg"],
          status: data["status"],
        });
        console.log(data);
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
            Sign up
          </Typography>
          <form
            className={classes.form}
            onSubmit={this.handleSubmit}
            noValidate
          >
            <Grid container spacing={2}>
              <Grid item xs={12}>
                <TextField
                  autoComplete="fname"
                  name="name"
                  type="text"
                  variant="outlined"
                  required
                  fullWidth
                  id="name"
                  label="Full Name"
                  autoFocus
                  value={this.state.name}
                  onChange={this.handleChange}
                />
                {this.state.nameError ? (
              <p
                style={{
                  padding: 0,
                  margin: 0,
                  color: "red",
                  fontSize: "14px",
                  textAlign: "center",
                }}
              >
                {this.state.nameError}
              </p>
            ) : null}
              </Grid>
              <Grid item xs={12}>
                <TextField
                  variant="outlined"
                  type="email"
                  required
                  fullWidth
                  id="email"
                  label="Email Address"
                  name="email"
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
              </Grid>
              <Grid item xs={12}>
                <TextField
                  variant="outlined"
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
              </Grid>
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
            >
              Sign Up
            </Button>
            <Grid container justify="flex-end">
              <Grid item>
                <Link href="/signin" variant="body2">
                  Already have an account? Sign in
                </Link>
              </Grid>
            </Grid>
          </form>
          <p>
            {this.state.msg ? (
              <Alert severity={this.state.status ? "success" : "error"}>
                {this.state.msg}
              </Alert>
            ) : null}
          </p>
        </div>
      </Container>
    );
  }
}

export default withStyles(useStyles)(SignUp);
