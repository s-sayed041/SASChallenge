import { motion, AnimatePresence } from "framer-motion";
import { useEffect, useState } from "react";

export default function SlotMachine({ events, spinning }) {
  const [displayEvents, setDisplayEvents] = useState([]);
  const [rolling, setRolling] = useState(false);

  useEffect(() => {
    if (spinning) {
      // Start rolling animation
      setRolling(true);
      setDisplayEvents([]);
    } else if (events.length > 0) {
      // Stop animation and show results after slight delay
      setTimeout(() => {
        setRolling(false);
        setDisplayEvents(events.slice(0, 3));
      }, 1500);
    }
  }, [spinning, events]);

  const placeholder = [
    "🎵", "🎭", "🍹", "🎬", "🎨", "🎤", "⚽", "🕺", "🎧", "🍔", "🚴"
  ];

  const reelVariants = {
    start: { y: 0 },
    roll: { y: ["0%", "-300%", "0%"], transition: { duration: 1.5, ease: "easeInOut", repeat: 0 } },
  };

  return (
    <div className="relative bg-orange-500 p-8 rounded-3xl flex justify-center items-center space-x-6">
      {[0, 1, 2].map((reelIndex) => (
        <div key={reelIndex} className="bg-white w-36 h-52 overflow-hidden rounded-2xl flex items-center justify-center text-black relative">
          <motion.div
            className="flex flex-col items-center justify-center text-5xl"
            animate={rolling ? "roll" : "start"}
            variants={reelVariants}
          >
            {/* During spin: show emojis */}
            {rolling && placeholder.map((icon, i) => (
              <div key={i} className="h-16 flex items-center justify-center">{icon}</div>
            ))}

            {/* After spin: show actual event */}
            {!rolling && displayEvents[reelIndex] && (
              <AnimatePresence>
                <motion.div
                  key={displayEvents[reelIndex].id}
                  initial={{ scale: 0.8, opacity: 0 }}
                  animate={{ scale: 1, opacity: 1 }}
                  exit={{ opacity: 0 }}
                  className="flex flex-col items-center p-2"
                >
                  <img
                    src={displayEvents[reelIndex].logo?.url}
                    alt=""
                    className="h-20 w-20 object-cover rounded-md"
                  />
                  <p className="text-xs font-semibold mt-1 text-center">
                    {displayEvents[reelIndex].name.text.slice(0, 25)}...
                  </p>
                </motion.div>
              </AnimatePresence>
            )}
          </motion.div>
        </div>
      ))}
    </div>
  );
}
