export default function Dock({ active, onSelect }) {
  const items = ["Data", "Tests", "Power", "Plots", "Report", "Assistant"];

  return (
    <div className="dock">
      {items.map(item => (
        <button
          key={item}
          className={active === item ? "dock-btn active" : "dock-btn"}
          onClick={() => onSelect(item)}
        >
          {item}
        </button>
      ))}
    </div>
  );
}
