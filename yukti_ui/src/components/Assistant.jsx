import { invoke } from "@tauri-apps/api/core";
import { useState } from "react";

export default function Assistant() {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");

  const send = async () => {
    const response = await invoke("run_assistant", { query: input });
    setOutput(response);
  };

  return (
    <div style={{ padding: "16px", color: "#00ff88" }}>
      <h3>Assistant</h3>
      <textarea
        style={{ width: "100%", height: "80px" }}
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button onClick={send}>Send</button>
      <pre>{output}</pre>
    </div>
  );
}
