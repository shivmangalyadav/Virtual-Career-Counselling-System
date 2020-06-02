import React from "react";
import { AppBar } from "@material-ui/core";
import { Toolbar } from "@material-ui/core";
import { Typography } from "@material-ui/core";
import { Box } from "@material-ui/core";

function Header() {
  return (
    <AppBar position="static" style={{position:'sticky', top: 0, backgroundColor:'orange', color: 'blue', height: '70px'}}>
      <Toolbar>
        <Typography variant="h5">
          <Box fontWeight="fontweightBold" letterSpacing={6} m={1}>
            Virtual Counselling System
          </Box>
        </Typography>
      </Toolbar>
    </AppBar>
  );
}

export default Header;
