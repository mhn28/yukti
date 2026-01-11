export default function DataModule() {
  return (
    <div>
      <h2>Data</h2>
      <table className="data-grid">
        <thead>
          <tr>
            <th>Group</th>
            <th>Value</th>
            <th>Condition</th>
            <th>Replicate</th>
            <th>Notes</th>
          </tr>
        </thead>
        <tbody>
          {Array.from({ length: 30 }).map((_, i) => (
            <tr key={i}>
              <td contentEditable />
              <td contentEditable />
              <td contentEditable />
              <td contentEditable />
              <td contentEditable />
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
