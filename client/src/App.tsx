import { Provider } from "react-redux"
import { Routes, Route } from "react-router-dom";
import store from "./redux/store/store";
import { Navbar } from "./components";


function App() {

  return (
    <Provider store={store}>
      <Navbar />
      <Routes>

      </Routes>
    </Provider>
  )
}

export default App
