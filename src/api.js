
import axios from "axios"

// creating reusable axios instance 
const api = axios.create({
    baseURL: "/api",
})


export default api
