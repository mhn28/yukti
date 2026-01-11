export default function MainLayout({ dock, content, assistant }) {
  return (
    <div style={{
      display: "grid",
      gridTemplateColumns: "220px 1fr 420px",
      height: "100vh",
      width: "100vw",
      overflow: "hidden"
    }}>
      <div style={{ borderRight: "1px solid #00ff88" }}>
        {dock}
      </div>

      <div style={{ height: "100%", overflow: "hidden" }}>
        {content}
      </div>

      <div style={{ borderLeft: "1px solid #00ff88" }}>
        {assistant}
      </div>
    </div>
  );
}
