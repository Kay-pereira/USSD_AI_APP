
import { useState,useEffect } from "react"
import api from "../../api"
import { Link } from "react-router-dom";
import "./css/Home.css"

function Home(){
    //const [message, Setmessage] = useState("")

//callind django api when the page loads 
   /* useEffect(() => {
        api.get("/test/")
        .then((res) => Setmessage(res.data.message))
        .catch((err) => console.log("Api Error:", err))
    }, []); */


    return(
         <div className="container">
      <h1 className="title">Welcome to Kwesi's AI USSD System</h1>
      <p className="description">
        Use this system to send SMS, ask AI questions, and check delivery reports.
      </p>
      <div className="buttons">
        <Link to="/sendsms" className="btn">Send SMS</Link>
        <Link to="/reports" className="btn">Delivery Reports</Link>
      </div>
    </div>
    )
}

export default Home 
