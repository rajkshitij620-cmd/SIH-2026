import React, { useState, useEffect, useRef, useMemo } from 'react';
import { Flame, Users, Clock, ShieldCheck, Sparkles, MapPin, Layers, Info, TrendingUp, AlertTriangle, ChevronRight, Navigation } from 'lucide-react';

export const CITIES_HEAT_DATA = {
  bengaluru: {
    name: 'Bengaluru, Karnataka',
    tagline: 'Silicon Valley, Royal Palaces & Garden City',
    baseCoord: { lat: 12.9716, lng: 77.5946 },
    hotspots: [
      { id: 'b1', name: 'Lalbagh Botanical Garden & Glass House', type: 'Botanical Garden', baseIntensity: 0.90, morningRush: 0.88, middayRush: 0.45, eveningRush: 0.92, nightRush: 0.15, x: 48, y: 68, rating: 4.8, tip: 'Early morning walkers enjoy peaceful flora between 6:00 AM - 8:30 AM before tourist queues.' },
      { id: 'b2', name: 'Bangalore Palace & Royal Grounds', type: 'Royal Palace', baseIntensity: 0.88, morningRush: 0.40, middayRush: 0.92, eveningRush: 0.78, nightRush: 0.10, x: 52, y: 24, rating: 4.7, tip: 'Audio tour included with ticket; morning lighting is best for Tudor-style facade photos.' },
      { id: 'b3', name: 'Cubbon Park & Vidhana Soudha', type: 'Heritage & Park', baseIntensity: 0.94, morningRush: 0.94, middayRush: 0.50, eveningRush: 0.95, nightRush: 0.45, x: 44, y: 44, rating: 4.8, tip: 'Sundays are vehicle-free. Vidhana Soudha illuminates on weekend evenings (7:00 PM - 8:30 PM).' },
      { id: 'b4', name: 'Commercial Street & Brigade Road', type: 'Shopping & Stroll', baseIntensity: 0.96, morningRush: 0.20, middayRush: 0.65, eveningRush: 0.98, nightRush: 0.90, x: 64, y: 48, rating: 4.6, tip: 'Peak shopping rush from 5:00 PM onwards. Use MG Road Metro station to bypass road traffic.' },
      { id: 'b5', name: 'Bannerghatta Biological Park & Safari', type: 'Safari & Wildlife', baseIntensity: 0.86, morningRush: 0.75, middayRush: 0.95, eveningRush: 0.45, nightRush: 0.05, x: 40, y: 88, rating: 4.6, tip: 'Book tiger & lion jungle safari online in advance for the 10:00 AM morning slot.' },
      { id: 'b6', name: 'Indiranagar 100ft Road Dining Corridor', type: 'Food & Cafes', baseIntensity: 0.93, morningRush: 0.15, middayRush: 0.60, eveningRush: 0.90, nightRush: 0.98, x: 78, y: 44, rating: 4.9, tip: 'Bustling artisanal coffee shops and microbreweries stay lively till 11:30 PM.' },
      { id: 'b7', name: 'Tipu Sultan Summer Palace & KR Market', type: 'Heritage / Market', baseIntensity: 0.84, morningRush: 0.90, middayRush: 0.70, eveningRush: 0.75, nightRush: 0.25, x: 36, y: 56, rating: 4.5, tip: 'KR Flower Market is most vibrant between 5:30 AM - 7:30 AM for vivid photography.' }
    ]
  },
  jaipur: {
    name: 'Jaipur, Rajasthan',
    tagline: 'Pink City Heritage, Forts & Bazaars',
    baseCoord: { lat: 26.9124, lng: 75.7873 },
    hotspots: [
      { id: 'j1', name: 'Hawa Mahal', type: 'Heritage', baseIntensity: 0.92, morningRush: 0.40, middayRush: 0.95, eveningRush: 0.88, nightRush: 0.20, x: 55, y: 40, rating: 4.8, tip: 'Visit before 9:00 AM from Wind View Cafe across the street for clear shots.' },
      { id: 'j2', name: 'Amer Fort & Maota Lake', type: 'Fort', baseIntensity: 0.89, morningRush: 0.70, middayRush: 0.92, eveningRush: 0.60, nightRush: 0.35, x: 65, y: 20, rating: 4.9, tip: 'Light & Sound show at 7:30 PM has moderate crowd.' },
      { id: 'j3', name: 'City Palace & Jantar Mantar', type: 'Palace', baseIntensity: 0.85, morningRush: 0.50, middayRush: 0.90, eveningRush: 0.75, nightRush: 0.10, x: 52, y: 48, rating: 4.7, tip: 'Composite tickets help bypass individual counter queues.' },
      { id: 'j4', name: 'Johari & Bapu Bazaars', type: 'Market / Shopping', baseIntensity: 0.95, morningRush: 0.20, middayRush: 0.60, eveningRush: 0.98, nightRush: 0.85, x: 48, y: 62, rating: 4.6, tip: 'Peak shopping rush from 5:30 PM to 8:30 PM for textiles and jewellery.' },
      { id: 'j5', name: 'Nahargarh Fort Sunset Point', type: 'Viewpoint', baseIntensity: 0.88, morningRush: 0.30, middayRush: 0.40, eveningRush: 0.96, nightRush: 0.70, x: 42, y: 25, rating: 4.8, tip: 'Arrive 45 mins before sunset to secure parking and hill edge seats.' },
      { id: 'j6', name: 'Albert Hall Museum', type: 'Museum', baseIntensity: 0.72, morningRush: 0.35, middayRush: 0.70, eveningRush: 0.82, nightRush: 0.40, x: 56, y: 75, rating: 4.5, tip: 'Night yellow lighting is magnificent and calmer than afternoon.' }
    ]
  },
  varanasi: {
    name: 'Varanasi, Uttar Pradesh',
    tagline: 'Ancient Ghats, Temples & Ganga Aarti',
    baseCoord: { lat: 25.3176, lng: 82.9739 },
    hotspots: [
      { id: 'v1', name: 'Dashashwamedh Ghat (Ganga Aarti)', type: 'Spiritual / Aarti', baseIntensity: 0.98, morningRush: 0.60, middayRush: 0.40, eveningRush: 0.99, nightRush: 0.50, x: 58, y: 55, rating: 4.9, tip: 'Reach the ghat steps by 5:30 PM or hire a wooden boat for panoramic view.' },
      { id: 'v2', name: 'Kashi Vishwanath Temple Corridor', type: 'Temple', baseIntensity: 0.96, morningRush: 0.95, middayRush: 0.85, eveningRush: 0.92, nightRush: 0.60, x: 52, y: 45, rating: 4.9, tip: 'Sugam Darshan queue moves fastest between 11:30 AM - 1:00 PM.' },
      { id: 'v3', name: 'Assi Ghat & Subah-e-Banaras', type: 'Ghat & Morning Yoga', baseIntensity: 0.82, morningRush: 0.94, middayRush: 0.30, eveningRush: 0.85, nightRush: 0.40, x: 45, y: 75, rating: 4.7, tip: 'Subah-e-Banaras sunrise music and yoga at 5:30 AM is unforgettable.' },
      { id: 'v4', name: 'Manikarnika & Harishchandra Ghats', type: 'Historic Ghat', baseIntensity: 0.78, morningRush: 0.60, middayRush: 0.70, eveningRush: 0.75, nightRush: 0.60, x: 62, y: 38, rating: 4.6, tip: 'Sacred grounds; maintain silence and avoid photography.' },
      { id: 'v5', name: 'Godowlia Chowk Food Walk', type: 'Food / Market', baseIntensity: 0.90, morningRush: 0.40, middayRush: 0.65, eveningRush: 0.95, nightRush: 0.88, x: 42, y: 50, rating: 4.8, tip: 'Best time for Banarasi Tamatar Chaat & Blue Lassi is 4:30 PM - 8:30 PM.' },
      { id: 'v6', name: 'Sarnath Buddhist Complex & Deer Park', type: 'Heritage / Stupa', baseIntensity: 0.80, morningRush: 0.50, middayRush: 0.80, eveningRush: 0.65, nightRush: 0.10, x: 70, y: 18, rating: 4.8, tip: 'Dhamek Stupa and archaeological museum are peaceful in late morning.' }
    ]
  },
  delhi: {
    name: 'Delhi NCR',
    tagline: 'Historic Capital, Mughal Monuments & Urban Hubs',
    baseCoord: { lat: 28.6139, lng: 77.2090 },
    hotspots: [
      { id: 'd1', name: 'India Gate & Kartavya Path', type: 'Monument', baseIntensity: 0.92, morningRush: 0.40, middayRush: 0.50, eveningRush: 0.98, nightRush: 0.85, x: 52, y: 55, rating: 4.8, tip: 'Well-lit evening walks with ice-cream kiosks operate till 11:30 PM.' },
      { id: 'd2', name: 'Chandni Chowk & Red Fort', type: 'Heritage / Street Food', baseIntensity: 0.98, morningRush: 0.50, middayRush: 0.95, eveningRush: 0.96, nightRush: 0.60, x: 58, y: 35, rating: 4.7, tip: 'Pedestrianized zone is best navigated on foot or electric rickshaw.' },
      { id: 'd3', name: 'Qutub Minar Complex', type: 'UNESCO Heritage', baseIntensity: 0.86, morningRush: 0.60, middayRush: 0.88, eveningRush: 0.80, nightRush: 0.10, x: 42, y: 80, rating: 4.8, tip: 'Early mornings have optimal angle of sunlight on minaret carvings.' },
      { id: 'd4', name: 'Connaught Place (CP Central Ring)', type: 'Shopping & Metro', baseIntensity: 0.94, morningRush: 0.30, middayRush: 0.75, eveningRush: 0.97, nightRush: 0.90, x: 50, y: 45, rating: 4.7, tip: 'Radial blocks are easy to navigate with Rajiv Chowk interchange.' },
      { id: 'd5', name: 'Humayun’s Tomb & Sunder Nursery', type: 'Heritage Garden', baseIntensity: 0.82, morningRush: 0.50, middayRush: 0.78, eveningRush: 0.85, nightRush: 0.10, x: 62, y: 65, rating: 4.8, tip: 'Spacious Mughal gardens and heritage lake are calm throughout the day.' },
      { id: 'd6', name: 'Lotus Temple & Kalkaji', type: 'Spiritual / Peace', baseIntensity: 0.85, morningRush: 0.45, middayRush: 0.88, eveningRush: 0.82, nightRush: 0.05, x: 66, y: 76, rating: 4.7, tip: 'Silent meditation hall is closed on Mondays; plan accordingly.' }
    ]
  },
  goa: {
    name: 'Goa',
    tagline: 'Sun, Beaches, Coastal Forts & Nightlife',
    baseCoord: { lat: 15.2993, lng: 74.1240 },
    hotspots: [
      { id: 'g1', name: 'Baga & Calangute Beach', type: 'Beach & Watersports', baseIntensity: 0.96, morningRush: 0.40, middayRush: 0.70, eveningRush: 0.98, nightRush: 0.92, x: 38, y: 35, rating: 4.6, tip: 'Watersports run till 4:30 PM; shacks host music till late evening.' },
      { id: 'g2', name: 'Old Goa Churches (Basilica of Bom Jesus)', type: 'Heritage', baseIntensity: 0.85, morningRush: 0.60, middayRush: 0.85, eveningRush: 0.60, nightRush: 0.10, x: 55, y: 48, rating: 4.8, tip: 'Cover shoulders and knees for church entry; morning mass is solemn.' },
      { id: 'g3', name: 'Anjuna & Vagator Sunset Cliff', type: 'Sunset / Cafes', baseIntensity: 0.92, morningRush: 0.20, middayRush: 0.45, eveningRush: 0.99, nightRush: 0.85, x: 32, y: 25, rating: 4.9, tip: 'Chapora Fort sunset ridge gets crowded from 5:15 PM onwards.' },
      { id: 'g4', name: 'Palolem Beach (South Goa)', type: 'Scenic Beach', baseIntensity: 0.75, morningRush: 0.50, middayRush: 0.60, eveningRush: 0.82, nightRush: 0.50, x: 65, y: 85, rating: 4.8, tip: 'Calm crescent bay ideal for morning kayaking and dolphin spotting.' },
      { id: 'g5', name: 'Fort Aguada & Sinquerim Lighthouse', type: 'Fort & Coast', baseIntensity: 0.86, morningRush: 0.40, middayRush: 0.82, eveningRush: 0.94, nightRush: 0.15, x: 35, y: 42, rating: 4.7, tip: 'Great Arabian Sea horizon view; visit around 4:00 PM for cool breezes.' }
    ]
  },
  mumbai: {
    name: 'Mumbai, Maharashtra',
    tagline: 'City of Dreams, Marine Drive & Gateway',
    baseCoord: { lat: 18.9220, lng: 72.8347 },
    hotspots: [
      { id: 'm1', name: 'Gateway of India & Colaba Causeway', type: 'Landmark / Shopping', baseIntensity: 0.96, morningRush: 0.50, middayRush: 0.85, eveningRush: 0.98, nightRush: 0.88, x: 46, y: 78, rating: 4.8, tip: 'Take Elephanta ferry from Jetty 1 before 11:00 AM to avoid midday heat.' },
      { id: 'm2', name: 'Marine Drive (Queen’s Necklace)', type: 'Promenade / Sunset', baseIntensity: 0.94, morningRush: 0.70, middayRush: 0.40, eveningRush: 0.99, nightRush: 0.95, x: 38, y: 70, rating: 4.9, tip: 'Evening sea breeze & city lights are spectacular from Nariman Point.' },
      { id: 'm3', name: 'Bandra Bandstand & Carter Road', type: 'Coast / Cafes', baseIntensity: 0.90, morningRush: 0.40, middayRush: 0.55, eveningRush: 0.96, nightRush: 0.92, x: 42, y: 42, rating: 4.8, tip: 'Bandra Fort offers a scenic view of the Bandra-Worli Sea Link.' },
      { id: 'm4', name: 'Chhatrapati Shivaji Maharaj Terminus (CSMT)', type: 'UNESCO Heritage', baseIntensity: 0.95, morningRush: 0.98, middayRush: 0.80, eveningRush: 0.98, nightRush: 0.60, x: 50, y: 68, rating: 4.8, tip: 'Victorian Gothic illumination lights up between 7:00 PM - 10:00 PM.' },
      { id: 'm5', name: 'Juhu Beach & Pav Bhaji Stalls', type: 'Beach & Street Food', baseIntensity: 0.92, morningRush: 0.45, middayRush: 0.50, eveningRush: 0.97, nightRush: 0.90, x: 36, y: 32, rating: 4.6, tip: 'Famous Mumbai street food stalls operate at full swing in evening.' }
    ]
  },
  kolkata: {
    name: 'Kolkata, West Bengal',
    tagline: 'City of Joy, Colonial Heritage & Culture',
    baseCoord: { lat: 22.5726, lng: 88.3639 },
    hotspots: [
      { id: 'k1', name: 'Victoria Memorial & Maidan', type: 'Monument', baseIntensity: 0.90, morningRush: 0.50, middayRush: 0.75, eveningRush: 0.94, nightRush: 0.30, x: 45, y: 65, rating: 4.8, tip: 'Marble galleries and sprawling gardens are very peaceful before 9:30 AM.' },
      { id: 'k2', name: 'Howrah Bridge & Flower Market', type: 'Landmark / Market', baseIntensity: 0.95, morningRush: 0.98, middayRush: 0.80, eveningRush: 0.92, nightRush: 0.50, x: 40, y: 30, rating: 4.7, tip: 'Mallick Ghat flower market is most vibrant between 6:00 AM - 8:00 AM.' },
      { id: 'k3', name: 'Park Street Dining & Heritage', type: 'Food / Nightlife', baseIntensity: 0.92, morningRush: 0.20, middayRush: 0.70, eveningRush: 0.96, nightRush: 0.95, x: 55, y: 60, rating: 4.9, tip: 'Historic bakeries and continental restaurants get 20 min queues on weekends.' },
      { id: 'k4', name: 'Dakshineswar Kali Temple', type: 'Temple', baseIntensity: 0.93, morningRush: 0.90, middayRush: 0.60, eveningRush: 0.88, nightRush: 0.20, x: 42, y: 15, rating: 4.9, tip: 'Take the scenic AC Ferry from Belur Math to skip road traffic.' },
      { id: 'k5', name: 'College Street & Indian Coffee House', type: 'Books & Culture', baseIntensity: 0.80, morningRush: 0.30, middayRush: 0.85, eveningRush: 0.88, nightRush: 0.30, x: 58, y: 40, rating: 4.6, tip: 'Historic book stalls remain lively throughout afternoon and evening.' }
    ]
  },
  agra: {
    name: 'Agra, Uttar Pradesh',
    tagline: 'Mughal Architecture & Taj Mahal Wonder',
    baseCoord: { lat: 27.1767, lng: 78.0081 },
    hotspots: [
      { id: 'a1', name: 'Taj Mahal (East & West Gates)', type: 'World Wonder', baseIntensity: 0.99, morningRush: 0.96, middayRush: 0.90, eveningRush: 0.98, nightRush: 0.10, x: 54, y: 45, rating: 4.9, tip: 'Enter at 5:45 AM sunrise gate opening for surreal views and few crowds.' },
      { id: 'a2', name: 'Agra Fort Mughal Citadel', type: 'UNESCO Fort', baseIntensity: 0.90, morningRush: 0.50, middayRush: 0.92, eveningRush: 0.75, nightRush: 0.10, x: 44, y: 40, rating: 4.8, tip: 'Explore Diwan-i-Khas and view of Taj Mahal across Yamuna river.' },
      { id: 'a3', name: 'Mehtab Bagh (Moonlight Garden)', type: 'Sunset Garden', baseIntensity: 0.85, morningRush: 0.30, middayRush: 0.40, eveningRush: 0.96, nightRush: 0.05, x: 56, y: 32, rating: 4.7, tip: 'Direct reflection of Taj Mahal at sunset without interior entry crowd.' },
      { id: 'a4', name: 'Fatehpur Sikri Royal Complex', type: 'Historic Palace', baseIntensity: 0.82, morningRush: 0.45, middayRush: 0.88, eveningRush: 0.65, nightRush: 0.05, x: 22, y: 70, rating: 4.8, tip: 'Buland Darwaza is 40 km from city; best combined on morning road trip.' },
      { id: 'a5', name: 'Sadar Bazaar Food & Petha Street', type: 'Market / Food', baseIntensity: 0.88, morningRush: 0.20, middayRush: 0.55, eveningRush: 0.94, nightRush: 0.85, x: 48, y: 65, rating: 4.6, tip: 'Authentic Agra Petha & Chaat stalls peak between 6:00 PM - 9:00 PM.' }
    ]
  },
  manali: {
    name: 'Manali, Himachal Pradesh',
    tagline: 'Snow Valleys, Himalayan Peaks & River Adventure',
    baseCoord: { lat: 32.2432, lng: 77.1892 },
    hotspots: [
      { id: 'mn1', name: 'Solang Valley Adventure Arena', type: 'Snow & Adventure', baseIntensity: 0.94, morningRush: 0.70, middayRush: 0.98, eveningRush: 0.60, nightRush: 0.05, x: 45, y: 22, rating: 4.8, tip: 'Start by 8:30 AM to bypass the Solang mountain pass vehicle queue.' },
      { id: 'mn2', name: 'Old Manali Cafes & Wooden Bridges', type: 'Culture / Cafes', baseIntensity: 0.88, morningRush: 0.30, middayRush: 0.60, eveningRush: 0.92, nightRush: 0.95, x: 38, y: 46, rating: 4.8, tip: 'Charming riverside bakeries and live acoustic music in evening.' },
      { id: 'mn3', name: 'Hadimba Devi Ancient Forest Temple', type: 'Spiritual / Heritage', baseIntensity: 0.90, morningRush: 0.85, middayRush: 0.90, eveningRush: 0.70, nightRush: 0.10, x: 42, y: 52, rating: 4.7, tip: 'Surrounded by towering Cedar/Deodar forests; very serene in early morning.' },
      { id: 'mn4', name: 'Mall Road & Tibetan Monasteries', type: 'Shopping & Stroll', baseIntensity: 0.96, morningRush: 0.25, middayRush: 0.70, eveningRush: 0.99, nightRush: 0.90, x: 55, y: 58, rating: 4.6, tip: 'Pedestrian only zone; peak woollen shopping rush 5:00 PM - 8:30 PM.' },
      { id: 'mn5', name: 'Atal Tunnel & Sissu Waterfall', type: 'Scenic Highway', baseIntensity: 0.92, morningRush: 0.75, middayRush: 0.94, eveningRush: 0.50, nightRush: 0.05, x: 62, y: 15, rating: 4.9, tip: 'Engineering marvel into Lahaul valley; check winter road conditions.' },
      { id: 'mn6', name: 'Vashisht Village & Hot Sulphur Springs', type: 'Hot Springs / Temple', baseIntensity: 0.80, morningRush: 0.80, middayRush: 0.65, eveningRush: 0.75, nightRush: 0.20, x: 60, y: 44, rating: 4.5, tip: 'Natural warm springs are refreshing in the crisp morning air.' }
    ]
  }
};

const TIME_SLOTS = [
  { time: '08:00 AM', label: 'Early Morning', key: 'morningRush', desc: 'Calm & peaceful visit window' },
  { time: '11:30 AM', label: 'Midday Peak', key: 'middayRush', desc: 'High sightseeing footfall' },
  { time: '04:30 PM', label: 'Evening Golden Hour', key: 'eveningRush', desc: 'Sunset & market crowd peak' },
  { time: '08:30 PM', label: 'Night Life & Stroll', key: 'nightRush', desc: 'Dining, lighting & night markets' }
];

// Helper to synthesize dynamic destination hotspots if city is not in predefined list
function generateDynamicCityData(cityName, trip) {
  const cleanName = cityName?.trim() || 'Destination';
  const baseTitle = cleanName.split(',')[0].trim();

  // Try to gather places from trip if available
  const tripPlaces = [];
  if (trip?.destination?.famous_places?.length) {
    tripPlaces.push(...trip.destination.famous_places);
  }
  if (trip?.travel_guide?.famous_places?.length) {
    tripPlaces.push(...trip.travel_guide.famous_places);
  }
  if (trip?.days?.length) {
    trip.days.forEach(d => {
      if (d.famous_places?.length) tripPlaces.push(...d.famous_places);
      if (d.activities?.length) {
        d.activities.forEach(a => {
          if (a.place && !a.place.includes('Traditional') && !a.place.includes('Kitchen') && !a.place.includes('well-reviewed')) {
            tripPlaces.push(a.place);
          }
        });
      }
    });
  }

  // Deduplicate and filter
  const uniquePlaces = Array.from(new Set(tripPlaces)).slice(0, 6);

  const fallbackTemplates = [
    { suffix: 'Historic Fort & Heritage Palace', type: 'Heritage / Monument', rush: [0.45, 0.90, 0.82, 0.15], x: 50, y: 32, tip: 'Visit in the early morning for best photography and minimal queue.' },
    { suffix: 'Central Gardens & Promenade', type: 'Nature & Botanical', rush: [0.85, 0.45, 0.92, 0.30], x: 42, y: 55, tip: 'Peaceful morning walk hours between 6:30 AM and 9:00 AM.' },
    { suffix: 'Old City Bazaar & Food Corridor', type: 'Market / Street Food', rush: [0.20, 0.65, 0.98, 0.92], x: 62, y: 50, tip: 'Peak shopping and local cuisine rush from 5:00 PM to 8:30 PM.' },
    { suffix: 'Sacred Temple & Spiritual Shrine', type: 'Spiritual & Cultural', rush: [0.92, 0.70, 0.85, 0.35], x: 35, y: 68, tip: 'Morning and evening aarti darshan hours are most auspicious.' },
    { suffix: 'Scenic Sunset Viewpoint & Lake', type: 'Viewpoint & Sunset', rush: [0.25, 0.40, 0.96, 0.60], x: 68, y: 28, rating: 4.8, tip: 'Arrive 40 minutes prior to golden hour for unobstructed sunset views.' },
    { suffix: 'Cultural Arts & Crafts Pavilion', type: 'Museum & Arts', rush: [0.30, 0.80, 0.75, 0.10], x: 56, y: 78, tip: 'Composite entry ticket available at entrance; very calm post-lunch.' }
  ];

  const hotspots = [];

  if (uniquePlaces.length >= 3) {
    uniquePlaces.forEach((p, idx) => {
      const template = fallbackTemplates[idx % fallbackTemplates.length];
      hotspots.push({
        id: `dyn_${idx + 1}`,
        name: p,
        type: template.type,
        baseIntensity: 0.85 + (idx % 3) * 0.05,
        morningRush: template.rush[0],
        middayRush: template.rush[1],
        eveningRush: template.rush[2],
        nightRush: template.rush[3],
        x: template.x,
        y: template.y,
        rating: 4.7 + (idx % 3) * 0.1,
        tip: `Top rated landmark in ${baseTitle}. ${template.tip}`
      });
    });
  } else {
    fallbackTemplates.forEach((tpl, idx) => {
      hotspots.push({
        id: `dyn_${idx + 1}`,
        name: `${baseTitle} ${tpl.suffix}`,
        type: tpl.type,
        baseIntensity: 0.88,
        morningRush: tpl.rush[0],
        middayRush: tpl.rush[1],
        eveningRush: tpl.rush[2],
        nightRush: tpl.rush[3],
        x: tpl.x,
        y: tpl.y,
        rating: 4.7,
        tip: `Key famous attraction in ${baseTitle}. ${tpl.tip}`
      });
    });
  }

  return {
    name: cleanName,
    tagline: `Top Tourist Hotspots & Crowd Navigation in ${baseTitle}`,
    baseCoord: { lat: 20.5937, lng: 78.9629 },
    hotspots
  };
}

// Find matching city key or generate dynamic
function resolveCityData(targetCity, trip) {
  if (!targetCity) {
    return CITIES_HEAT_DATA.bengaluru;
  }
  const clean = targetCity.toLowerCase().trim();

  // Direct and alias matches
  if (clean.includes('bengaluru') || clean.includes('bangalore')) return CITIES_HEAT_DATA.bengaluru;
  if (clean.includes('jaipur')) return CITIES_HEAT_DATA.jaipur;
  if (clean.includes('varanasi') || clean.includes('kashi') || clean.includes('banaras')) return CITIES_HEAT_DATA.varanasi;
  if (clean.includes('delhi') || clean.includes('ncr') || clean.includes('new delhi')) return CITIES_HEAT_DATA.delhi;
  if (clean.includes('goa')) return CITIES_HEAT_DATA.goa;
  if (clean.includes('mumbai') || clean.includes('bombay')) return CITIES_HEAT_DATA.mumbai;
  if (clean.includes('kolkata') || clean.includes('calcutta')) return CITIES_HEAT_DATA.kolkata;
  if (clean.includes('agra')) return CITIES_HEAT_DATA.agra;
  if (clean.includes('manali') || clean.includes('solang') || clean.includes('kullu')) return CITIES_HEAT_DATA.manali;

  // Check any other key in CITIES_HEAT_DATA
  for (const [key, data] of Object.entries(CITIES_HEAT_DATA)) {
    if (clean.includes(key) || data.name.toLowerCase().includes(clean)) {
      return data;
    }
  }

  // Dynamic fallback for any other destination in India
  return generateDynamicCityData(targetCity, trip);
}

export default function TouristHeatmap({ initialCity = 'bengaluru', trip = null, embedded = false }) {
  const [activeLayer, setActiveLayer] = useState('crowd'); // 'crowd' | 'popularity' | 'safety'
  const [timeIndex, setTimeIndex] = useState(2); // default: 04:30 PM Evening
  const [selectedHotspot, setSelectedHotspot] = useState(null);
  const canvasRef = useRef(null);

  // Compute active city data dynamically whenever initialCity or trip changes
  const cityData = useMemo(() => {
    return resolveCityData(initialCity, trip);
  }, [initialCity, trip]);

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
          grad.addColorStop(0, 'rgba(239, 68, 68, 0.78)'); // Red Hot
          grad.addColorStop(0.35, 'rgba(249, 115, 22, 0.52)'); // Orange
          grad.addColorStop(0.7, 'rgba(234, 179, 8, 0.25)'); // Yellow
          grad.addColorStop(1, 'rgba(234, 179, 8, 0)');
        } else if (intensity >= 0.55) {
          grad.addColorStop(0, 'rgba(245, 158, 11, 0.72)'); // Amber
          grad.addColorStop(0.4, 'rgba(234, 179, 8, 0.4)');
          grad.addColorStop(0.8, 'rgba(59, 130, 246, 0.15)');
          grad.addColorStop(1, 'rgba(59, 130, 246, 0)');
        } else {
          grad.addColorStop(0, 'rgba(16, 185, 129, 0.72)'); // Calm Emerald
          grad.addColorStop(0.4, 'rgba(20, 184, 166, 0.35)');
          grad.addColorStop(1, 'rgba(20, 184, 166, 0)');
        }
      } else if (activeLayer === 'popularity') {
        grad.addColorStop(0, 'rgba(168, 85, 247, 0.82)'); // Purple / Royal
        grad.addColorStop(0.4, 'rgba(236, 72, 153, 0.42)');
        grad.addColorStop(1, 'rgba(236, 72, 153, 0)');
      } else {
        // Safety Layer
        grad.addColorStop(0, 'rgba(16, 185, 129, 0.88)'); // Green Shield
        grad.addColorStop(0.45, 'rgba(14, 165, 233, 0.42)');
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
        ctx.strokeStyle = 'rgba(239, 68, 68, 0.65)';
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
      const text = spot.name.length > 28 ? spot.name.slice(0, 26) + '…' : spot.name;
      ctx.font = 'bold 11px system-ui, sans-serif';
      const textWidth = ctx.measureText(text).width;

      ctx.fillStyle = isSelected ? 'rgba(15, 23, 42, 0.95)' : 'rgba(255, 255, 255, 0.94)';
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
    (cityData.hotspots.reduce((acc, curr) => acc + (curr[currentSlot.key] || 0.5), 0) / (cityData.hotspots.length || 1)) * 100
  );

  return (
    <section className={`card ${embedded ? 'mt-6' : 'py-8 max-w-6xl mx-auto'}`}>
      {/* Header */}
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
            Track peak crowd density, discover peaceful time slots, and explore safe tourist corridors in <b className="text-teal-800 dark:text-teal-300">{cityData.name}</b>.
          </p>
        </div>

        {/* Current Active Destination Status Badge */}
        <div className="flex items-center gap-2">
          <div className="flex items-center gap-2 rounded-xl bg-teal-50 dark:bg-teal-950/80 border border-teal-200 dark:border-teal-800/80 px-3.5 py-1.5 text-xs font-bold text-teal-900 dark:text-teal-200 shadow-xs">
            <MapPin size={14} className="text-teal-600 dark:text-teal-400" />
            <span>Destination: {cityData.name.split(',')[0]}</span>
          </div>
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
              if (!cityData.hotspots || cityData.hotspots.length === 0) return;
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
