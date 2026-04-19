import { useState, useEffect } from 'react'
import './App.css'
import axios from "axios"

function App() {
  const [count, setCount] = useState(0);
  const [array, setArray] = useState([]);


  const fetchAPI = async () => {
    const response = await axios.get("http://127.0.0.1:8080/api/users")
    setArray(response.data.users);
  };

  useEffect(() => {
    fetchAPI()
  }, [])

  return (
    <>
      <h1>Home Page</h1>
    </>
  )
}

export default App
