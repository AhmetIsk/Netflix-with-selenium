import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import SigninPage from "./pages/SigninPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<SigninPage/>}/>
      </Routes>
    </Router>
  );
}

export default App;
