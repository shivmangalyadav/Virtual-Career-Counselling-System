import React, { Component } from "react";

import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Checkbox from "@material-ui/core/Checkbox";
import { Paper, Button } from "@material-ui/core";

class EditProfile extends Component {
  render() {
    return (
      <div style={{ backgroundColor: "#E6F3FF" }}>
        <Paper
          style={{
            width: "600px",
            marginLeft: "auto",
            marginRight: "auto",
            padding: "70px",
          }}
        >
          <Typography component="h1" variant="h4" align="center">
            Edit Profile
          </Typography>
          <Grid container spacing={3}>
            <Grid item xs={12} sm={12}>
              <TextField
                required
                id="firstName"
                name="firstName"
                label="First name"
                fullWidth
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                required
                id="address"
                name="address"
                label="Address  "
                fullWidth
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                required
                id="city"
                name="city"
                label="City"
                fullWidth
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField id="state" name="state" label="State" fullWidth />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                required
                id="zip"
                name="zip"
                label="Zip / Postal code"
                fullWidth
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                required
                id="country"
                name="country"
                label="Country"
                fullWidth
              />
            </Grid>
            <Button style={{display:'flex', margin:'10px 20px 10px auto', justifyContent: 'flex-end'}} variant="contained" color="primary">
              Update
            </Button>
          </Grid>
        </Paper>
      </div>
    );
  }
}

export default EditProfile;
