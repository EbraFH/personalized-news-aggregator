import React from "react";
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect,
} from "react-router-dom";
import Login from "./components/Login";
import Register from "./components/Register";
import Preferences from "./components/Preferences";
import NewsSummaries from "./components/NewsSummaries";
// Import the global styles
import "./styles/GlobalStyles.css";

function App() {
  return (
    <Router>
      <div>
        <Switch>
          {/* Redirect root to login page */}
          <Route exact path="/" render={() => <Redirect to="/login" />} />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/preferences" component={Preferences} />
          <Route path="/news" component={NewsSummaries} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
