import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function FiltersPage() {
  const [categories, setCategories] = useState([]);
  const [filters, setFilters] = useState({
    price: "",
    type: "",
    alcohol: "false",
    distance: "5km"
  });
  const navigate = useNavigate();

  // Fetch categories from Django backend
  useEffect(() => {
    fetch("/api/categories/")
      .then(res => res.json())
      .then(data => setCategories(data.categories))
      .catch(console.error);
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFilters((prev) => ({ ...prev, [name]: value }));
  };

  const handleNext = () => {
    navigate("/slot", { state: { filters } }); // pass filters to slot machine page
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-[#0b1330] text-white">
      <div className="w-40 h-40 bg-gray-300 rounded-full flex items-center justify-center text-black text-xl font-bold">
        Logo
      </div>
      <h1 className="mt-6 text-2xl font-semibold">snouting tonight?</h1>

      <div className="flex gap-3 mt-8">
        <select name="price" onChange={handleChange} className="bg-gray-200 text-black p-2 rounded-md">
          <option value="">price</option>
          <option value="free">Free</option>
          <option value="paid">Paid</option>
        </select>

        <select name="type" onChange={handleChange} className="bg-gray-200 text-black p-2 rounded-md">
          <option value="">event type</option>
          {categories.map(cat => (
            <option key={cat.id} value={cat.id}>{cat.name}</option>
          ))}
        </select>

        <select name="alcohol" onChange={handleChange} className="bg-gray-200 text-black p-2 rounded-md">
          <option value="false">alcohol?</option>
          <option value="true">Yes</option>
          <option value="false">No</option>
        </select>

        <select name="distance" onChange={handleChange} className="bg-gray-200 text-black p-2 rounded-md">
          <option value="5km">distance</option>
          <option value="1km">1 km</option>
          <option value="5km">5 km</option>
          <option value="10km">10 km</option>
        </select>
      </div>

      <button
        onClick={handleNext}
        className="mt-8 px-6 py-3 bg-orange-500 rounded-xl text-white text-lg font-semibold hover:bg-orange-600 transition"
      >
        Next →
      </button>
    </div>
  );
}
