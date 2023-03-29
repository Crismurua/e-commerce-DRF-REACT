import { Provider } from "react-redux"
import { Routes, Route } from "react-router-dom";
import store from "./redux/store/store";
import { Navbar } from "./components";
import { Home } from "./pages";
import './App.css';


function App() {

  return (
    <Provider store={store}>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </Provider>
  )
}

export default App
