import MainPage from "./pages/MainPage"
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

function App() {
   
  return (
  <>
    <Router>
      <Routes>
        <Route path="/" element={<MainPage />}>
        </Route>
      </Routes>
    </Router>
  </>
  )
}

export default App
