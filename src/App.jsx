
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

// Components/pages 
import Home from "./components/pages/Home"
import Reports from "./components/pages/Reports"
import SendSMS from "./components/pages/SendSMS"


//Styling 
import './App.css'


function App() {

  return (

    <>
    <Router>

      {/*Navigation*/}
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/reports">Reports</Link></li>
          <li><Link to="/sendsms">SendSMS</Link></li>
        </ul>
      </nav>

      {/*Page Routes*/}

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/reports" element={<Reports />} />
        <Route path="/sendsms" element={<SendSMS />} />
      </Routes>
    </Router>
    </>
  )
}

export default App
