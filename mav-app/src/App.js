import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
import { Route, Routes } from "react-router-dom"

function App() {
  return (
    <>
      <Header />
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/members" element={<Members />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/recruiment" element={<Recruiment />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
