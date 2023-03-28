import { Provider } from "react-redux"
import { Routes, Route } from "react-router-dom";
import store from "./redux/store/store";


function App() {

  return (
    <Provider store={store}>
    <div className="App">
      
    </div>
    </Provider>
  )
}

export default App
