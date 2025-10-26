import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import FiltersPage from "./pages/FiltersPage";
import SlotMachinePage from "./pages/SlotMachinePage";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<FiltersPage />} />
        <Route path="/slot" element={<SlotMachinePage />} />
      </Routes>
    </Router>
  );
}