import './App.css';

import Number from "./components/Numbers.js";

const axios = require('axios').default;
const url = process.env.REACT_APP_BACKEND || "http://localhost:5000/";
axios.defaults.baseURL = url;
axios.defaults.headers.post['Content-Type'] = 'application/json';
axios.defaults.headers.patch['Content-Type'] = 'application/json';
axios.defaults.headers.put['Content-Type'] = 'application/json';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Number/>
      </header>
    </div>
  );
}

export default App;
