import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <div class="Container1">
       <h1 class="title">PropEvalify</h1>
       <p class="motto">Helping you find the right price!</p>

    </div>


    <div class="user-input">
      <input></input>

    </div>
       
    </>
  )
}

export default App
