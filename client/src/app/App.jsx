import { useState, useEffect } from 'react'
import axios from "axios"
import { Routes, Route } from "react-router-dom"

import Encounter from "../features/encounter/components/Encounter"
import Encounters from "../features/encounters/components/Encounters"

function App() {

  return (
    <Routes>
      <Route path = "/" element = {<Encounters/>}></Route>
      <Route path = "/encounters" element = {<Encounters/>}></Route>
      <Route path = "/encounters/:id" element = {<Encounter/>}></Route>
    </Routes>
  )
}

export default App
