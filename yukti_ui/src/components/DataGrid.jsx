export default function DataGrid() {
  const rows = Array.from({ length: 200 }, (_, i) => i + 1);
  const cols = ["Group", "Value", "Condition", "Replicate", "Notes"];

  return (
    <div style={{
      height: "100%",
      overflow: "auto",
      background: "#000",
      padding: "10px"
    }}>
      <table
        style={{
          borderCollapse: "collapse",
          width: "100%",
          color: "#00ff88",
          fontFamily: "monospace"
        }}
      >
        <thead>
          <tr>
            {cols.map(c => (
              <th
                key={c}
                style={{
                  border: "1px solid #00ff88",
                  padding: "6px",
                  background: "#111",
                  position: "sticky",
                  top: 0
                }}
              >
                {c}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map(r => (
            <tr key={r}>
              {cols.map(c => (
                <td
                  key={c}
                  contentEditable
                  suppressContentEditableWarning
                  style={{
                    border: "1px solid #00ff88",
                    padding: "6px",
                    minWidth: "120px"
                  }}
                />
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
