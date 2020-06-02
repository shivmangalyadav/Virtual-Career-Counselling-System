import React, { Fragment } from "react";
import Routes from "./Routes";
import Header from "./components/Layouts/Header";
import Footer from "./components/Layouts/Footer";
import EditProfile from "./components/Exercises/EditProfile";

function App() {
  return (
    <div>
      {/* <EditProfile /> */}
      <div>
        <Header />
        <Routes />
      </div>
      <Footer />
    </div>
  );
}

export default App;
