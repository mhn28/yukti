import { useState } from "react";
import { invoke } from "@tauri-apps/api/core";

export default function Assistant() {
  const [out, setOut] = useState("Idle");

  const send = async () => {
    console.log("BUTTON CLICKED");

    try {
      const result = await invoke("run_assistant", {
        payload: JSON.stringify({
          action: "power_analysis",
          params: { alpha: 0.05, power: 0.8 }
        })
      });
      setOut(result);
    } catch (e) {
      console.error("Invoke error:", e);
      setOut(String(e));
    }
  };

  return (
    <div style={{ width: "420px", background: "#0b0f14", color: "#00ffcc", padding: "16px" }}>
      <h3>Yukti Assistant</h3>
      <button onClick={send}>Run Power Analysis</button>
      <pre>{out}</pre>
    </div>
  );
}
