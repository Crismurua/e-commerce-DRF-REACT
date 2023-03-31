import { Provider } from "react-redux"
import { Routes, Route } from "react-router-dom";
import store from "./redux/store/store";
import { Navbar, Footer } from "./components";
import { Home, Login } from "./pages";
import './App.css';


function App() {

  return (
    <Provider store={store}>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
      </Routes>
      <Footer />
    </Provider>
  )
}

export default App
