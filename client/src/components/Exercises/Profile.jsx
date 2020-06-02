import React, { Component } from "react";
import jwt_decode from "jwt-decode";
import { getProfiledata } from "../actions/getdata";
import { Link } from "@material-ui/core";

import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";

class Profile extends Component {
  constructor() {
    super();
    this.state = {
      name: "",
      email: "",
      errors: {},
    };
  }

  componentDidMount() {
    const token = sessionStorage.getItem("access_token");
    let token_data = "Bearer " + token;
    console.log(token_data);

    getProfiledata(token_data).then((data) => {
      console.log(data);
      this.setState({
        name: data["UserName"],
        email: data.UserEmail,
      });
    });

    console.log(sessionStorage.getItem("access_token"));
  }

  render() {
    return (
      <div style={{ backgroundColor: "#D6D6D6" }}>
        <h3>Name: {this.state.name}</h3>
        <h3>Email: {this.state.email}</h3>

        <Card
          style={{
            maxWidth: "90%",
            height: "auto",
            marginLeft: "auto",
            marginRight: "auto",
          }}
        >
          <CardActionArea>
            <CardMedia
              style={{
                borderRadius: "50%",
                width: "300px",
                height: "100%",
                margin: "20px 0 0 20px",
              }}
              component="img"
              height="140"
              image="https://image.shutterstock.com/image-photo/mountains-during-sunset-beautiful-natural-600w-407021107.jpg"
              title="Profile"
            />
            <Link
              href="/#"
              variant="body2"
              style={{ margin: "10px 0 0 100px" }}
            >
              Upload Profile Pic
            </Link>
            <CardContent>
              <Typography gutterBottom variant="h5" component="h2">
                {this.state.name}
              </Typography>
              <Typography variant="body2" color="textSecondary" component="p">
                Lizards are a widespread group of squamate reptiles, with over
                6,000 species, ranging across all continents except Antarctica.
              </Typography>
            </CardContent>
          </CardActionArea>
          <CardActions>
            <Button size="small" color="primary">
              Edit Profile
            </Button>
            <Button size="small" color="primary">
              Change Password
            </Button>
          </CardActions>
        </Card>
      </div>
    );
  }
}

export default Profile;
