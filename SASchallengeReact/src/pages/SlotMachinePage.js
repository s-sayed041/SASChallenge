import { useLocation } from "react-router-dom";
import { useState } from "react";
import SlotMachine from "../components/SlotMachine";

export default function SlotMachinePage() {
  const location = useLocation();
  const filters = location.state?.filters || {};
  const [events, setEvents] = useState([]);
  const [spinning, setSpinning] = useState(false);

  const handleSpin = async () => {
    setSpinning(true);
    const params = new URLSearchParams(filters);
    const res = await fetch(`/api/events/?${params.toString()}`);
    const data = await res.json();
    setEvents(data.events || []);
    setSpinning(false);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-[#0b1330] text-white">
      <SlotMachine events={events} spinning={spinning} />
      <button
        onClick={handleSpin}
        className="mt-8 px-6 py-3 bg-orange-500 rounded-xl text-white text-lg font-semibold hover:bg-orange-600 transition"
      >
        {spinning ? "Spinning..." : "Spin 🎰"}
      </button>
    </div>
  );
}
