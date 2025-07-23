import React from "react";

export default function SignalCard({ symbol, signal }) {
  return (
    <div className={`signal-card ${signal.toLowerCase()}`}>
      <h3>{symbol}</h3>
      <p>{signal}</p>
    </div>
  );
}
