import { useState } from "react";
import Dock from "./components/Dock";
import DataModule from "./modules/DataModule";
import TestsModule from "./modules/TestsModule";
import PowerModule from "./modules/PowerModule";
import PlotsModule from "./modules/PlotsModule";
import ReportModule from "./modules/ReportModule";
import Assistant from "./components/Assistant";
import TopMenu from "./components/TopMenu";

export default function App() {
  const [active, setActive] = useState("Data");

  const renderModule = () => {
    switch (active) {
      case "Data": return <DataModule />;
      case "Tests": return <TestsModule />;
      case "Power": return <PowerModule />;
      case "Plots": return <PlotsModule />;
      case "Report": return <ReportModule />;
      default: return <div>Select a module</div>;
    }
  };

  return (
    <div className="app-root">
      <TopMenu />
      <div className="main-layout">
        <Dock active={active} onSelect={setActive} />
        <div className="workspace">
          {renderModule()}
        </div>
        <Assistant />
      </div>
    </div>
  );
}
