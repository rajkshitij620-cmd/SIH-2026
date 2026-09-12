import React, { useState, useEffect, useRef } from 'react';
import { Flame, Users, Clock, ShieldCheck, Sparkles, MapPin, Layers, Info, TrendingUp, AlertTriangle, ChevronRight, Navigation } from 'lucide-react';

const CITIES_HEAT_DATA = {
  jaipur: {
    name: 'Jaipur, Rajasthan',
    tagline: 'Pink City Heritage & Bazaars',
    baseCoord: { lat: 26.9124, lng: 75.7873 },
    hotspots: [
      { id: 'j1', name: 'Hawa Mahal', type: 'Heritage', baseIntensity: 0.92, morningRush: 0.4, middayRush: 0.95, eveningRush: 0.88, nightRush: 0.2, x: 55, y: 40, rating: 4.8, tip: 'Visit before 9:00 AM to get clear photos with minimal crowd.' },
      { id: 'j2', name: 'Amer Fort & Maota Lake', type: 'Fort', baseIntensity: 0.89, morningRush: 0.7, middayRush: 0.92, eveningRush: 0.6, nightRush: 0.35, x: 65, y: 20, rating: 4.9, tip: 'Light & Sound show at 7:30 PM has moderate crowd.' },
      { id: 'j3', name: 'City Palace & Jantar Mantar', type: 'Palace', baseIntensity: 0.85, morningRush: 0.5, middayRush: 0.9, eveningRush: 0.75, nightRush: 0.1, x: 52, y: 48, rating: 4.7, tip: 'Book composite tickets online to bypass main gate queues.' },
      { id: 'j4', name: 'Johari & Bapu Bazaars', type: 'Market / Shopping', baseIntensity: 0.95, morningRush: 0.2, middayRush: 0.6, eveningRush: 0.98, nightRush: 0.85, x: 48, y: 62, rating: 4.6, tip: 'Peak shopping rush from 5:30 PM to 8:30 PM.' },
      { id: 'j5', name: 'Nahargarh Fort Sunset Point', type: 'Viewpoint', baseIntensity: 0.88, morningRush: 0.3, middayRush: 0.4, eveningRush: 0.96, nightRush: 0.7, x: 42, y: 25, rating: 4.8, tip: 'Arrive 45 mins before sunset to catch parking & seating.' },
      { id: 'j6', name: 'Albert Hall Museum', type: 'Museum', baseIntensity: 0.72, morningRush: 0.35, middayRush: 0.7, eveningRush: 0.82, nightRush: 0.4, x: 56, y: 75, rating: 4.5, tip: 'Night lighting is spectacular and calmer than afternoon.' }
    ]
  },
  varanasi: {
    name: 'Varanasi, Uttar Pradesh',
    tagline: 'Ancient Ghats & Spiritual Hub',
    baseCoord: { lat: 25.3176, lng: 82.9739 },
    hotspots: [
      { id: 'v1', name: 'Dashashwamedh Ghat (Ganga Aarti)', type: 'Spiritual / Aarti', baseIntensity: 0.98, morningRush: 0.6, middayRush: 0.4, eveningRush: 0.99, nightRush: 0.5, x: 58, y: 55, rating: 4.9, tip: 'Reach the ghat by 5:30 PM or take a boat for unobstructed Aarti view.' },
      { id: 'v2', name: 'Kashi Vishwanath Temple Corridor', type: 'Temple', baseIntensity: 0.96, morningRush: 0.95, middayRush: 0.85, eveningRush: 0.92, nightRush: 0.6, x: 52, y: 45, rating: 4.9, tip: 'Sugam Darshan queue moves fastest between 11:30 AM - 1:00 PM.' },
      { id: 'v3', name: 'Assi Ghat', type: 'Ghat & Morning Yoga', baseIntensity: 0.82, morningRush: 0.94, middayRush: 0.3, eveningRush: 0.85, nightRush: 0.4, x: 45, y: 75, rating: 4.7, tip: 'Subah-e-Banaras morning music & Aarti at 5:30 AM is mesmerizing.' },
      { id: 'v4', name: 'Manikarnika Ghat', type: 'Historic Ghat', baseIntensity: 0.78, morningRush: 0.6, middayRush: 0.7, eveningRush: 0.75, nightRush: 0.6, x: 62, y: 38, rating: 4.6, tip: 'Respect local traditions; photography is strictly prohibited.' },
      { id: 'v5', name: 'Godowlia Chowk Food Walk', type: 'Food / Market', baseIntensity: 0.9, morningRush: 0.4, middayRush: 0.65, eveningRush: 0.95, nightRush: 0.88, x: 42, y: 50, rating: 4.8, tip: 'Best time for Banarasi Chaat & Lassi is 4:00 PM to 8:00 PM.' }
    ]
  },
  kolkata: {
    name: 'Kolkata, West Bengal',
    tagline: 'City of Joy, Culture & Cuisine',
    baseCoord: { lat: 22.5726, lng: 88.3639 },
    hotspots: [
      { id: 'k1', name: 'Victoria Memorial & Maidan', type: 'Monument', baseIntensity: 0.9, morningRush: 0.5, middayRush: 0.75, eveningRush: 0.94, nightRush: 0.3, x: 45, y: 65, rating: 4.8, tip: 'Gardens are very peaceful before 9:30 AM.' },
      { id: 'k2', name: 'Howrah Bridge & Mallick Ghat Flower Market', type: 'Landmark', baseIntensity: 0.95, morningRush: 0.98, middayRush: 0.8, eveningRush: 0.92, nightRush: 0.5, x: 40, y: 30, rating: 4.7, tip: 'Flower market is most vibrant between 6:00 AM - 8:00 AM.' },
      { id: 'k3', name: 'Park Street Dining & Heritage', type: 'Food / Nightlife', baseIntensity: 0.92, morningRush: 0.2, middayRush: 0.7, eveningRush: 0.96, nightRush: 0.95, x: 55, y: 60, rating: 4.9, tip: 'Expect 20-30 min restaurant queue on weekend evenings.' },
      { id: 'k4', name: 'Dakshineswar Kali Temple', type: 'Temple', baseIntensity: 0.93, morningRush: 0.9, middayRush: 0.6, eveningRush: 0.88, nightRush: 0.2, x: 42, y: 15, rating: 4.9, tip: 'Take the scenic AC Ferry from Belur Math to skip road traffic.' },
      { id: 'k5', name: 'College Street & Indian Coffee House', type: 'Books & Culture', baseIntensity: 0.8, morningRush: 0.3, middayRush: 0.85, eveningRush: 0.88, nightRush: 0.3, x: 58, y: 40, rating: 4.6, tip: 'Historical book stalls remain lively throughout afternoon.' }
    ]
  },
  delhi: {
    name: 'Delhi NCR',
    tagline: 'Historic Capital & Modern Hub',
    baseCoord: { lat: 28.6139, lng: 77.2090 },
    hotspots: [
      { id: 'd1', name: 'India Gate & Kartavya Path', type: 'Monument', baseIntensity: 0.92, morningRush: 0.4, middayRush: 0.5, eveningRush: 0.98, nightRush: 0.85, x: 52, y: 55, rating: 4.8, tip: 'Well-lit evening walks with ice-cream stalls till 11 PM.' },
      { id: 'd2', name: 'Chandni Chowk & Red Fort', type: 'Heritage / Street Food', baseIntensity: 0.98, morningRush: 0.5, middayRush: 0.95, eveningRush: 0.96, nightRush: 0.6, x: 58, y: 35, rating: 4.7, tip: 'Pedestrianized zone is best explored by E-rickshaw or walking.' },
      { id: 'd3', name: 'Qutub Minar Complex', type: 'UNESCO Heritage', baseIntensity: 0.86, morningRush: 0.6, middayRush: 0.88, eveningRush: 0.8, nightRush: 0.1, x: 42, y: 80, rating: 4.8, tip: 'Early mornings have the softest sunlight for architecture photography.' },
      { id: 'd4', name: 'Connaught Place (CP Central Hub)', type: 'Shopping & Metro', baseIntensity: 0.94, morningRush: 0.3, middayRush: 0.75, eveningRush: 0.97, nightRush: 0.9, x: 50, y: 45, rating: 4.7, tip: 'Radial blocks are easy to navigate with Rajiv Chowk Metro.' },
      { id: 'd5', name: 'Humayun’s Tomb', type: 'Heritage Garden', baseIntensity: 0.82, morningRush: 0.5, middayRush: 0.78, eveningRush: 0.85, nightRush: 0.1, x: 62, y: 65, rating: 4.8, tip: 'Spacious Mughal gardens never feel uncomfortably packed.' }
    ]
  },
  goa: {
    name: 'Goa',
    tagline: 'Sun, Sand & Coastal Heritage',
    baseCoord: { lat: 15.2993, lng: 74.1240 },
    hotspots: [
      { id: 'g1', name: 'Baga & Calangute Beach', type: 'Beach & Watersports', baseIntensity: 0.96, morningRush: 0.4, middayRush: 0.7, eveningRush: 0.98, nightRush: 0.92, x: 38, y: 35, rating: 4.6, tip: 'Shacks stay lively with music until late night.' },
      { id: 'g2', name: 'Old Goa Churches (Basilica of Bom Jesus)', type: 'Heritage', baseIntensity: 0.85, morningRush: 0.6, middayRush: 0.85, eveningRush: 0.6, nightRush: 0.1, x: 55, y: 48, rating: 4.8, tip: 'Modest dress code required for cathedral entry.' },
      { id: 'g3', name: 'Anjuna & Vagator Sunset Cliff', type: 'Sunset / Cafes', baseIntensity: 0.92, morningRush: 0.2, middayRush: 0.45, eveningRush: 0.99, nightRush: 0.85, x: 32, y: 25, rating: 4.9, tip: 'Chapora Fort sunset gets busy from 5:15 PM.' },
      { id: 'g4', name: 'Palolem Beach (South Goa)', type: 'Scenic Beach', baseIntensity: 0.75, morningRush: 0.5, middayRush: 0.6, eveningRush: 0.82, nightRush: 0.5, x: 65, y: 85, rating: 4.8, tip: 'Calm waters ideal for morning kayaking.' }
    ]
  }
};

const TIME_SLOTS = [
  { time: '08:00 AM', label: 'Early Morning', key: 'morningRush', desc: 'Calm & peaceful visit window' },
  { time: '11:30 AM', label: 'Midday Peak', key: 'middayRush', desc: 'High sightseeing footfall' },
  { time: '04:30 PM', label: 'Evening Golden Hour', key: 'eveningRush', desc: 'Sunset & market crowd peak' },
  { time: '08:30 PM', label: 'Night Life & Stroll', key: 'nightRush', desc: 'Dining, lighting & night markets' }
];

export default function TouristHeatmap({ initialCity = 'jaipur', embedded = false }) {
  const [selectedCityKey, setSelectedCityKey] = useState(() => {
    const clean = initialCity?.toLowerCase().trim() || 'jaipur';
    return Object.keys(CITIES_HEAT_DATA).find(k => clean.includes(k)) || 'jaipur';
  });

  const [activeLayer, setActiveLayer] = useState('crowd'); // 'crowd' | 'popularity' | 'safety'
  const [timeIndex, setTimeIndex] = useState(2); // default: 04:30 PM Evening
  const [selectedHotspot, setSelectedHotspot] = useState(null);
  const canvasRef = useRef(null);

  const cityData = CITIES_HEAT_DATA[selectedCityKey] || CITIES_HEAT_DATA.jaipur;
  const currentSlot = TIME_SLOTS[timeIndex];

  // Draw Heatmap on HTML5 Canvas
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    ctx.clearRect(0, 0, width, height);

    // Subtle grid & roads texture
    ctx.strokeStyle = '#33415518';
    ctx.lineWidth = 1;
    for (let x = 0; x < width; x += 35) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, height);
      ctx.stroke();
    }
    for (let y = 0; y < height; y += 35) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
      ctx.stroke();
    }

    // Connective arterial routes
    ctx.strokeStyle = '#0d948825';
    ctx.lineWidth = 2.5;
    ctx.setLineDash([4, 6]);
    ctx.beginPath();
    cityData.hotspots.forEach((spot, idx) => {
      const px = (spot.x / 100) * width;
      const py = (spot.y / 100) * height;
      if (idx === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    });
    ctx.stroke();
    ctx.setLineDash([]);

    // Draw Heat Blobs (Radial Gradients)
    cityData.hotspots.forEach((spot) => {
      const px = (spot.x / 100) * width;
      const py = (spot.y / 100) * height;
      
      let intensity = spot[currentSlot.key] || 0.6;
      let radius = 65 + intensity * 55;

      if (activeLayer === 'popularity') {
        intensity = spot.baseIntensity;
        radius = 70 + intensity * 50;
      } else if (activeLayer === 'safety') {
        intensity = spot.nightRush > 0.4 ? 0.9 : 0.6;
        radius = 80;
      }

      const grad = ctx.createRadialGradient(px, py, 4, px, py, radius);
      
      if (activeLayer === 'crowd') {
        if (intensity >= 0.85) {
          grad.addColorStop(0, 'rgba(239, 68, 68, 0.75)'); // Red Hot
          grad.addColorStop(0.35, 'rgba(249, 115, 22, 0.5)'); // Orange
          grad.addColorStop(0.7, 'rgba(234, 179, 8, 0.25)'); // Yellow
          grad.addColorStop(1, 'rgba(234, 179, 8, 0)');
        } else if (intensity >= 0.55) {
          grad.addColorStop(0, 'rgba(245, 158, 11, 0.7)'); // Amber
          grad.addColorStop(0.4, 'rgba(234, 179, 8, 0.4)');
          grad.addColorStop(0.8, 'rgba(59, 130, 246, 0.15)');
          grad.addColorStop(1, 'rgba(59, 130, 246, 0)');
        } else {
          grad.addColorStop(0, 'rgba(16, 185, 129, 0.7)'); // Calm Emerald
          grad.addColorStop(0.4, 'rgba(20, 184, 166, 0.35)');
          grad.addColorStop(1, 'rgba(20, 184, 166, 0)');
        }
      } else if (activeLayer === 'popularity') {
        grad.addColorStop(0, 'rgba(168, 85, 247, 0.8)'); // Purple / Royal
        grad.addColorStop(0.4, 'rgba(236, 72, 153, 0.4)');
        grad.addColorStop(1, 'rgba(236, 72, 153, 0)');
      } else {
        // Safety Layer
        grad.addColorStop(0, 'rgba(16, 185, 129, 0.85)'); // Green Shield
        grad.addColorStop(0.45, 'rgba(14, 165, 233, 0.4)');
        grad.addColorStop(1, 'rgba(14, 165, 233, 0)');
      }

      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(px, py, radius, 0, Math.PI * 2);
      ctx.fill();
    });

    // Draw Hotspot Hub Pins & Labels
    cityData.hotspots.forEach((spot) => {
      const px = (spot.x / 100) * width;
      const py = (spot.y / 100) * height;
      const isSelected = selectedHotspot?.id === spot.id;
      const intensity = spot[currentSlot.key] || 0.6;

      // Pulse ring for top rush
      if (intensity >= 0.85 && activeLayer === 'crowd') {
        ctx.strokeStyle = 'rgba(239, 68, 68, 0.6)';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(px, py, 18, 0, Math.PI * 2);
        ctx.stroke();
      }

      // Pin center
      ctx.fillStyle = isSelected ? '#0f766e' : '#0f172a';
      ctx.beginPath();
      ctx.arc(px, py, isSelected ? 8 : 6, 0, Math.PI * 2);
      ctx.fill();

      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Label background & text
      const text = spot.name;
      ctx.font = 'bold 11px system-ui, sans-serif';
      const textWidth = ctx.measureText(text).width;

      ctx.fillStyle = isSelected ? 'rgba(15, 23, 42, 0.95)' : 'rgba(255, 255, 255, 0.92)';
      ctx.beginPath();
      ctx.roundRect(px - textWidth / 2 - 6, py + 10, textWidth + 12, 18, 5);
      ctx.fill();
      ctx.strokeStyle = isSelected ? '#0d9488' : 'rgba(203, 213, 225, 0.8)';
      ctx.lineWidth = 1;
      ctx.stroke();

      ctx.fillStyle = isSelected ? '#38bdf8' : '#0f172a';
      ctx.textAlign = 'center';
      ctx.fillText(text, px, py + 23);
    });

  }, [cityData, activeLayer, timeIndex, selectedHotspot]);

  const avgRush = Math.round(
    (cityData.hotspots.reduce((acc, curr) => acc + (curr[currentSlot.key] || 0.5), 0) / cityData.hotspots.length) * 100
  );

  return (
    <section className={`card ${embedded ? 'mt-6' : 'py-8 max-w-6xl mx-auto'}`}>
      {/* Header & City Selector */}
      <div className="flex flex-wrap items-center justify-between gap-4 border-b border-slate-100 dark:border-slate-800 pb-5">
        <div>
          <div className="flex items-center gap-2">
            <span className="inline-flex items-center gap-1 rounded-full bg-rose-500/10 text-rose-600 dark:text-rose-400 px-2.5 py-0.5 text-xs font-extrabold uppercase tracking-wide">
              <Flame size={13} className="animate-pulse" /> Live Heatmap
            </span>
            <span className="text-xs text-slate-400">· Real-Time Footfall AI</span>
          </div>
          <h2 className="mt-1 text-2xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
            Tourist Crowd & Popularity Heatmap
          </h2>
          <p className="mt-1 text-xs sm:text-sm text-slate-600 dark:text-slate-400">
            Track peak crowd density, discover peaceful time slots, and explore safe tourist corridors in <b>{cityData.name}</b>.
          </p>
        </div>

        {/* City Filter Pills */}
        <div className="flex flex-wrap items-center gap-1.5">
          {Object.entries(CITIES_HEAT_DATA).map(([key, data]) => (
            <button
              key={key}
              onClick={() => {
                setSelectedCityKey(key);
                setSelectedHotspot(null);
              }}
              className={`rounded-xl px-3 py-1.5 text-xs font-semibold transition ${
                selectedCityKey === key
                  ? 'bg-teal-800 text-white shadow-md'
                  : 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
              }`}
            >
              {data.name.split(',')[0]}
            </button>
          ))}
        </div>
      </div>

      {/* Layer Switcher & Time Controls Bar */}
      <div className="mt-5 grid gap-4 md:grid-cols-3">
        {/* Layer Mode Switch */}
        <div className="md:col-span-2 flex flex-wrap items-center gap-2 bg-slate-100/80 dark:bg-slate-800/80 p-1.5 rounded-2xl">
          <button
            onClick={() => setActiveLayer('crowd')}
            className={`flex-1 flex items-center justify-center gap-1.5 rounded-xl py-2 px-3 text-xs font-bold transition ${
              activeLayer === 'crowd'
                ? 'bg-white dark:bg-slate-900 text-rose-600 dark:text-rose-400 shadow-sm'
                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
            }`}
          >
            <Flame size={14} />
            <span>Crowd Density (भीड़-भाड़)</span>
          </button>

          <button
            onClick={() => setActiveLayer('popularity')}
            className={`flex-1 flex items-center justify-center gap-1.5 rounded-xl py-2 px-3 text-xs font-bold transition ${
              activeLayer === 'popularity'
                ? 'bg-white dark:bg-slate-900 text-purple-600 dark:text-purple-400 shadow-sm'
                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
            }`}
          >
            <Sparkles size={14} />
            <span>Top Popularity Hubs</span>
          </button>

          <button
            onClick={() => setActiveLayer('safety')}
            className={`flex-1 flex items-center justify-center gap-1.5 rounded-xl py-2 px-3 text-xs font-bold transition ${
              activeLayer === 'safety'
                ? 'bg-white dark:bg-slate-900 text-emerald-600 dark:text-emerald-400 shadow-sm'
                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
            }`}
          >
            <ShieldCheck size={14} />
            <span>Safe Tourist Corridors</span>
          </button>
        </div>

        {/* Live Capacity Gauge */}
        <div className="flex items-center justify-between rounded-2xl bg-teal-50/70 dark:bg-teal-950/40 border border-teal-100 dark:border-teal-900/60 px-4 py-2">
          <div>
            <p className="text-[10px] font-bold uppercase tracking-wider text-teal-800 dark:text-teal-300">City Crowd Index</p>
            <p className="text-base font-extrabold text-teal-950 dark:text-teal-100">{avgRush}% Footfall Capacity</p>
          </div>
          <span className={`rounded-full px-2.5 py-1 text-xs font-bold ${
            avgRush >= 80 ? 'bg-rose-100 text-rose-700 dark:bg-rose-950 dark:text-rose-300' :
            avgRush >= 50 ? 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300' :
            'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300'
          }`}>
            {avgRush >= 80 ? 'High Rush' : avgRush >= 50 ? 'Moderate' : 'Smooth / Calm'}
          </span>
        </div>
      </div>

      {/* Time-of-Day Slider */}
      <div className="mt-4 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-900/50 p-4">
        <div className="flex items-center justify-between mb-2.5">
          <div className="flex items-center gap-2 text-xs font-bold text-slate-800 dark:text-slate-200">
            <Clock size={14} className="text-teal-600 dark:text-teal-400" />
            <span>Simulate Time of Day: <b className="text-teal-700 dark:text-teal-300">{currentSlot.time}</b> ({currentSlot.label})</span>
          </div>
          <span className="text-[11px] text-slate-500">{currentSlot.desc}</span>
        </div>

        <div className="grid grid-cols-4 gap-2">
          {TIME_SLOTS.map((slot, idx) => (
            <button
              key={idx}
              onClick={() => setTimeIndex(idx)}
              className={`rounded-xl py-2 px-2 text-center text-xs font-bold transition border ${
                timeIndex === idx
                  ? 'border-teal-600 bg-teal-800 text-white shadow-sm'
                  : 'border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:border-teal-300'
              }`}
            >
              <div>{slot.time}</div>
              <div className="text-[10px] font-normal opacity-85 truncate mt-0.5">{slot.label}</div>
            </button>
          ))}
        </div>
      </div>

      {/* Main Heatmap Visualizer Canvas & Detail Sidebar */}
      <div className="mt-5 grid gap-5 lg:grid-cols-3">
        {/* Visual Map Canvas */}
        <div className="lg:col-span-2 relative rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-950 overflow-hidden shadow-inner min-h-[360px] flex items-center justify-center">
          <canvas
            ref={canvasRef}
            width={620}
            height={400}
            className="w-full h-auto max-h-[440px] block cursor-crosshair"
            onClick={(e) => {
              const rect = e.currentTarget.getBoundingClientRect();
              const clickX = ((e.clientX - rect.left) / rect.width) * 100;
              const clickY = ((e.clientY - rect.top) / rect.height) * 100;
              const closest = cityData.hotspots.reduce((prev, curr) => {
                const distPrev = Math.hypot(prev.x - clickX, prev.y - clickY);
                const distCurr = Math.hypot(curr.x - clickX, curr.y - clickY);
                return distCurr < distPrev ? curr : prev;
              });
              if (closest && Math.hypot(closest.x - clickX, closest.y - clickY) < 18) {
                setSelectedHotspot(closest);
              }
            }}
          />

          {/* Map Overlay Badges */}
          <div className="absolute top-3 left-3 bg-slate-900/85 backdrop-blur-md px-3 py-1.5 rounded-xl border border-slate-700 text-white text-[11px] font-medium shadow">
            <b>{cityData.name}</b> · {activeLayer === 'crowd' ? 'Live Heatmap' : activeLayer === 'popularity' ? 'Popularity Map' : 'Safety Map'}
          </div>

          {/* Color Gradient Legend */}
          <div className="absolute bottom-3 right-3 bg-slate-900/90 backdrop-blur-md px-3 py-2 rounded-xl border border-slate-700 text-[11px] text-white space-y-1">
            <div className="font-bold text-[10px] uppercase text-slate-400">Heatmap Legend</div>
            {activeLayer === 'crowd' ? (
              <div className="flex items-center gap-2 text-xs">
                <span className="inline-block w-3 h-3 rounded-full bg-emerald-500" /> Low (0-45%)
                <span className="inline-block w-3 h-3 rounded-full bg-amber-400" /> Med (45-75%)
                <span className="inline-block w-3 h-3 rounded-full bg-rose-500" /> Rush (75-100%)
              </div>
            ) : activeLayer === 'popularity' ? (
              <div className="flex items-center gap-2 text-xs">
                <span className="inline-block w-3 h-3 rounded-full bg-pink-500" /> Top Ranked
                <span className="inline-block w-3 h-3 rounded-full bg-purple-500" /> Heritage Hub
              </div>
            ) : (
              <div className="flex items-center gap-2 text-xs">
                <span className="inline-block w-3 h-3 rounded-full bg-emerald-400" /> Safe & Well-Lit
                <span className="inline-block w-3 h-3 rounded-full bg-sky-400" /> Police Kiosk
              </div>
            )}
          </div>
        </div>

        {/* Hotspots List & Clicked Item Advice */}
        <div className="space-y-3 flex flex-col justify-between">
          <div className="space-y-2.5 max-h-[340px] overflow-y-auto pr-1">
            <p className="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">
              Hotspots & Crowd Status ({cityData.hotspots.length}):
            </p>

            {cityData.hotspots.map((spot) => {
              const intensity = Math.round((spot[currentSlot.key] || 0.6) * 100);
              const isSelected = selectedHotspot?.id === spot.id;

              return (
                <article
                  key={spot.id}
                  onClick={() => setSelectedHotspot(spot)}
                  className={`cursor-pointer rounded-xl p-3 border transition ${
                    isSelected
                      ? 'border-teal-600 bg-teal-50/70 dark:bg-teal-950/60 shadow-sm'
                      : 'border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 hover:border-teal-300'
                  }`}
                >
                  <div className="flex items-center justify-between gap-2">
                    <b className="text-xs sm:text-sm text-slate-900 dark:text-white line-clamp-1">{spot.name}</b>
                    <span className={`shrink-0 rounded-full px-2 py-0.5 text-[10px] font-extrabold ${
                      intensity >= 85 ? 'bg-rose-100 text-rose-700 dark:bg-rose-950 dark:text-rose-300' :
                      intensity >= 55 ? 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300' :
                      'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300'
                    }`}>
                      {intensity}% Rush
                    </span>
                  </div>

                  <div className="mt-1 flex items-center justify-between text-[11px] text-slate-500">
                    <span>{spot.type} · ★ {spot.rating}</span>
                    <span className="text-teal-700 dark:text-teal-400 font-medium">View Advice →</span>
                  </div>
                </article>
              );
            })}
          </div>

          {/* Selected Spot Smart Advice Card */}
          {selectedHotspot ? (
            <div className="rounded-2xl border border-teal-200 dark:border-teal-800 bg-teal-50 dark:bg-teal-950/70 p-4 space-y-2">
              <div className="flex items-center justify-between">
                <span className="text-xs font-bold text-teal-950 dark:text-teal-200">{selectedHotspot.name}</span>
                <span className="text-[11px] text-teal-800 dark:text-teal-300 font-bold">★ {selectedHotspot.rating}</span>
              </div>
              <p className="text-xs text-slate-700 dark:text-slate-300 font-medium">
                <b>AI Visitor Tip:</b> {selectedHotspot.tip}
              </p>
              <a
                href={`https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(selectedHotspot.name + ' ' + cityData.name)}`}
                target="_blank"
                rel="noreferrer"
                className="inline-flex items-center gap-1 text-xs font-bold text-teal-800 dark:text-teal-300 underline mt-1"
              >
                <span>Navigate on Live Map</span>
                <ChevronRight size={13} />
              </a>
            </div>
          ) : (
            <div className="rounded-2xl border border-dashed border-slate-300 dark:border-slate-700 p-4 text-center text-xs text-slate-500">
              Select any hotspot on the map or list to view live crowd mitigation tips & best visit hours.
            </div>
          )}
        </div>
      </div>
    </section>
  );
}
