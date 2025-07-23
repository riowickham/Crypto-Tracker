import React, { useEffect, useState } from "react";
import Navbar from "./components/Navbar";
import SignalCard from "./components/SignalCard";
import "./App.css";

function App() {
  const [signals, setSignals] = useState([]);

  useEffect(() => {
    const fetchSignals = async () => {
      const res = await fetch("http://127.0.0.1:8000/signals"); // change to Railway URL after deploy
      const data = await res.json();
      setSignals(data);
    };
    fetchSignals();
    const interval = setInterval(fetchSignals, 60000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="app">
      <Navbar />
      <h1>📈 Real-Time Crypto & Stock Signals</h1>
      <div className="signals-container">
        {signals.map((s, i) => (
          <SignalCard key={i} symbol={s.symbol} signal={s.signal} />
        ))}
      </div>
    </div>
  );
}

export default App;
