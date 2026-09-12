import React, { useState, useEffect, useRef } from 'react';
import { MapPin, Search, ChevronRight } from 'lucide-react';

export const ALL_INDIAN_DESTINATIONS = [
  // A
  { name: 'Agra', state: 'Uttar Pradesh', tag: 'Taj Mahal & Mughal Fort', category: 'Heritage' },
  { name: 'Ahmedabad', state: 'Gujarat', tag: 'Sabarmati & Heritage City', category: 'Heritage' },
  { name: 'Amritsar', state: 'Punjab', tag: 'Golden Temple & Wagah', category: 'Spiritual' },
  { name: 'Ayodhya', state: 'Uttar Pradesh', tag: 'Ram Mandir & Saryu Ghat', category: 'Spiritual' },
  { name: 'Ajmer', state: 'Rajasthan', tag: 'Dargah Sharif & Ana Sagar', category: 'Spiritual' },
  { name: 'Alwar', state: 'Rajasthan', tag: 'Bhangarh Fort & Sariska', category: 'Heritage' },
  { name: 'Alleppey (Alappuzha)', state: 'Kerala', tag: 'Houseboats & Backwaters', category: 'Coastal' },
  { name: 'Almora', state: 'Uttarakhand', tag: 'Kumaon Hills & Binsar', category: 'Mountains' },
  { name: 'Anjuna', state: 'Goa', tag: 'Flea Market & Sunset Point', category: 'Coastal' },
  { name: 'Auli', state: 'Uttarakhand', tag: 'Skiing Capital & Himalayan View', category: 'Mountains' },
  { name: 'Aurangabad (Chhatrapati Sambhajinagar)', state: 'Maharashtra', tag: 'Ajanta & Ellora Caves', category: 'Heritage' },
  { name: 'Agartala', state: 'Tripura', tag: 'Ujjayanta Palace', category: 'Heritage' },
  { name: 'Aizawl', state: 'Mizoram', tag: 'Lushai Hills & Culture', category: 'Mountains' },
  { name: 'Asansol', state: 'West Bengal', tag: 'Industrial & Cultural Hub', category: 'City' },

  // B
  { name: 'Bengaluru (Bangalore)', state: 'Karnataka', tag: 'Silicon Valley & Cubbon Park', category: 'Metro' },
  { name: 'Bhopal', state: 'Madhya Pradesh', tag: 'City of Lakes & Upper Lake', category: 'Heritage' },
  { name: 'Bhubaneswar', state: 'Odisha', tag: 'Temple City & Lingaraj', category: 'Spiritual' },
  { name: 'Bodh Gaya', state: 'Bihar', tag: 'Mahabodhi Temple & Enlightenment', category: 'Spiritual' },
  { name: 'Bikaner', state: 'Rajasthan', tag: 'Junagarh Fort & Camel Desert', category: 'Heritage' },
  { name: 'Badrinath', state: 'Uttarakhand', tag: 'Char Dham Himalayan Shrine', category: 'Spiritual' },
  { name: 'Bharatpur', state: 'Rajasthan', tag: 'Keoladeo Bird National Park', category: 'Nature' },
  { name: 'Bhuj', state: 'Gujarat', tag: 'Gateway to Great Rann of Kutch', category: 'Heritage' },
  { name: 'Belgaum (Belagavi)', state: 'Karnataka', tag: 'Belgaum Fort & Waterfalls', category: 'Heritage' },
  { name: 'Bellary (Ballari)', state: 'Karnataka', tag: 'Ballari Fort & Hampi Gateway', category: 'Heritage' },
  { name: 'Bareilly', state: 'Uttar Pradesh', tag: 'Zari Zardozi & Jhumka City', category: 'City' },
  { name: 'Bhagalpur', state: 'Bihar', tag: 'Silk City & Vikramshila Ruins', category: 'Heritage' },
  { name: 'Begusarai', state: 'Bihar', tag: 'Kanwar Lake Bird Sanctuary', category: 'Nature' },
  { name: 'Bilaspur', state: 'Chhattisgarh', tag: 'Kanan Pendari & Ratanpur', category: 'Heritage' },
  { name: 'Bokaro', state: 'Jharkhand', tag: 'Steel City & Garga Dam', category: 'City' },
  { name: 'Burdwan (Bardhaman)', state: 'West Bengal', tag: 'Curzon Gate & 108 Shiva Temples', category: 'Heritage' },
  { name: 'Baddi', state: 'Himachal Pradesh', tag: 'Foothills Industrial & Scenic', category: 'Mountains' },

  // C
  { name: 'Chandigarh', state: 'Punjab / Haryana', tag: 'Rock Garden & Sukhna Lake', category: 'City' },
  { name: 'Chennai', state: 'Tamil Nadu', tag: 'Marina Beach & Kapaleeshwarar', category: 'Coastal' },
  { name: 'Coimbatore', state: 'Tamil Nadu', tag: 'Adiyogi Shiva & Marudamalai', category: 'Spiritual' },
  { name: 'Coorg (Madikeri)', state: 'Karnataka', tag: 'Coffee Plantations & Abbey Falls', category: 'Mountains' },
  { name: 'Chikmagalur', state: 'Karnataka', tag: 'Mullayanagiri Peak & Coffee', category: 'Mountains' },
  { name: 'Chittorgarh', state: 'Rajasthan', tag: 'Chittorgarh Fort & Padmini Palace', category: 'Heritage' },
  { name: 'Cuttack', state: 'Odisha', tag: 'Silver City & Barabati Fort', category: 'Heritage' },
  { name: 'Cherrapunji (Sohra)', state: 'Meghalaya', tag: 'Living Root Bridges & Waterfalls', category: 'Nature' },
  { name: 'Chamba', state: 'Himachal Pradesh', tag: 'Chaugan & Himalayan Valleys', category: 'Mountains' },
  { name: 'Calicut (Kozhikode)', state: 'Kerala', tag: 'Kappad Beach & Malabar Food', category: 'Coastal' },

  // D
  { name: 'Delhi NCR', state: 'Delhi', tag: 'India Gate, Red Fort & Qutub Minar', category: 'Metro' },
  { name: 'Darjeeling', state: 'West Bengal', tag: 'Tiger Hill Sunrise & Tea Gardens', category: 'Mountains' },
  { name: 'Dehradun', state: 'Uttarakhand', tag: 'Robber’s Cave & Forest Research', category: 'Mountains' },
  { name: 'Dalhousie', state: 'Himachal Pradesh', tag: 'Khajjiar Mini Switzerland & Hills', category: 'Mountains' },
  { name: 'Dharamshala & Mcleodganj', state: 'Himachal Pradesh', tag: 'Dalai Lama Temple & Triund Trek', category: 'Mountains' },
  { name: 'Dwarka', state: 'Gujarat', tag: 'Dwarkadhish Temple & Beyt Dwarka', category: 'Spiritual' },
  { name: 'Diu', state: 'Dadra & Nagar Haveli', tag: 'Nagoa Beach & Portuguese Fort', category: 'Coastal' },
  { name: 'Daman', state: 'Dadra & Nagar Haveli', tag: 'Jampore Beach & Moti Daman', category: 'Coastal' },
  { name: 'Digha', state: 'West Bengal', tag: 'Marine Beach & Sea Promenade', category: 'Coastal' },
  { name: 'Dhanbad', state: 'Jharkhand', tag: 'Maithon Dam & Coal Capital', category: 'City' },
  { name: 'Dibrugarh', state: 'Assam', tag: 'Tea City of India & Brahmaputra', category: 'Nature' },

  // G
  { name: 'Goa', state: 'Goa', tag: 'Calangute, Baga Beach & Old Goa Churches', category: 'Coastal' },
  { name: 'Gangtok', state: 'Sikkim', tag: 'Tsomgo Lake & Rumtek Monastery', category: 'Mountains' },
  { name: 'Gokarna', state: 'Karnataka', tag: 'Om Beach & Mahabaleshwar Temple', category: 'Coastal' },
  { name: 'Gulmarg', state: 'Jammu & Kashmir', tag: 'Gondola Cable Car & Snow Slopes', category: 'Mountains' },
  { name: 'Gwalior', state: 'Madhya Pradesh', tag: 'Gwalior Fort & Scindia Palace', category: 'Heritage' },
  { name: 'Gaya', state: 'Bihar', tag: 'Vishnupad Temple & Falgu River', category: 'Spiritual' },
  { name: 'Gandhinagar', state: 'Gujarat', tag: 'Akshardham Temple & Capital', category: 'Spiritual' },
  { name: 'Gorakhpur', state: 'Uttar Pradesh', tag: 'Gorakhnath Temple & Gita Press', category: 'Spiritual' },
  { name: 'Guwahati', state: 'Assam', tag: 'Kamakhya Temple & Brahmaputra Cruise', category: 'Spiritual' },
  { name: 'Gir National Park', state: 'Gujarat', tag: 'Asiatic Lion Safari', category: 'Nature' },

  // H
  { name: 'Hampi', state: 'Karnataka', tag: 'UNESCO Vijayanagara Ruins & Stone Chariot', category: 'Heritage' },
  { name: 'Haridwar', state: 'Uttarakhand', tag: 'Har Ki Pauri & Ganga Aarti', category: 'Spiritual' },
  { name: 'Hyderabad', state: 'Telangana', tag: 'Charminar, Golconda Fort & Biryani', category: 'Metro' },
  { name: 'Hoshiarpur', state: 'Punjab', tag: 'Citrus Groves & Wooden Inlay', category: 'City' },
  { name: 'Hubli (Hubballi)', state: 'Karnataka', tag: 'Unkal Lake & Glass House', category: 'City' },
  { name: 'Howrah', state: 'West Bengal', tag: 'Howrah Railway Station & Botanic Garden', category: 'Heritage' },
  { name: 'Haldwani', state: 'Uttarakhand', tag: 'Gateway to Kumaon Hills', category: 'Mountains' },
  { name: 'Hajipur', state: 'Bihar', tag: 'Ramchaura Mandir & Banana Capital', category: 'City' },
  { name: 'Hazaribagh', state: 'Jharkhand', tag: 'National Park & Canary Hill', category: 'Nature' },

  // J
  { name: 'Jaipur', state: 'Rajasthan', tag: 'Hawa Mahal, Amer Fort & Johari Bazaar', category: 'Heritage' },
  { name: 'Jaisalmer', state: 'Rajasthan', tag: 'Golden Fort & Sam Sand Dunes', category: 'Heritage' },
  { name: 'Jodhpur', state: 'Rajasthan', tag: 'Mehrangarh Fort & Blue City', category: 'Heritage' },
  { name: 'Jammu', state: 'Jammu & Kashmir', tag: 'Raghunath Temple & Bahu Fort', category: 'Spiritual' },
  { name: 'Jalandhar', state: 'Punjab', tag: 'Devi Talab Mandir & Sports City', category: 'City' },
  { name: 'Jabalpur', state: 'Madhya Pradesh', tag: 'Bhedaghat Marble Rocks & Dhuandhar', category: 'Nature' },
  { name: 'Jamshedpur', state: 'Jharkhand', tag: 'Jubilee Park & Dalma Hills', category: 'City' },
  { name: 'Junagadh', state: 'Gujarat', tag: 'Girnar Hills & Uparkot Fort', category: 'Heritage' },
  { name: 'Jhansi', state: 'Uttar Pradesh', tag: 'Jhansi Fort & Rani Mahal', category: 'Heritage' },
  { name: 'Joshimath', state: 'Uttarakhand', tag: 'Shankaracharya Math & Valley of Flowers Base', category: 'Mountains' },

  // K
  { name: 'Kolkata', state: 'West Bengal', tag: 'Victoria Memorial, Howrah Bridge & Sweets', category: 'Metro' },
  { name: 'Kochi (Cochin)', state: 'Kerala', tag: 'Fort Kochi, Chinese Nets & Mattancherry', category: 'Coastal' },
  { name: 'Kodaikanal', state: 'Tamil Nadu', tag: 'Princess of Hill Stations & Kodai Lake', category: 'Mountains' },
  { name: 'Kasol & Parvati Valley', state: 'Himachal Pradesh', tag: 'Tosh, Kheerganga & River Cafes', category: 'Mountains' },
  { name: 'Kedarnath', state: 'Uttarakhand', tag: 'Sacred Jyotirlinga Himalayan Peak', category: 'Spiritual' },
  { name: 'Khajuraho', state: 'Madhya Pradesh', tag: 'UNESCO Temples & Chandela Sculptures', category: 'Heritage' },
  { name: 'Kanyakumari', state: 'Tamil Nadu', tag: 'Vivekananda Rock & Southernmost Tip', category: 'Coastal' },
  { name: 'Kanpur', state: 'Uttar Pradesh', tag: 'Bithoor & Ganga Barrage', category: 'City' },
  { name: 'Katra', state: 'Jammu & Kashmir', tag: 'Vaishno Devi Base Camp', category: 'Spiritual' },
  { name: 'Kullu', state: 'Himachal Pradesh', tag: 'Great Himalayan National Park & Rafting', category: 'Mountains' },
  { name: 'Kohima', state: 'Nagaland', tag: 'Hornbill Festival & Dzukou Valley', category: 'Mountains' },
  { name: 'Kota', state: 'Rajasthan', tag: 'Seven Wonders Park & Chambal Riverfront', category: 'Heritage' },

  // L
  { name: 'Ladakh (Leh)', state: 'Ladakh', tag: 'Pangong Lake, Khardung La & Nubra Valley', category: 'Mountains' },
  { name: 'Lucknow', state: 'Uttar Pradesh', tag: 'Bara Imambara, Rumi Darwaza & Awadhi Food', category: 'Heritage' },
  { name: 'Lonavala & Khandala', state: 'Maharashtra', tag: 'Tiger’s Leap, Bhushi Dam & Chikki', category: 'Mountains' },
  { name: 'Lakshadweep', state: 'Lakshadweep', tag: 'Agatti & Bangaram Coral Atolls', category: 'Coastal' },
  { name: 'Ludhiana', state: 'Punjab', tag: 'Lodhi Fort & Maharaja Ranjit Singh War Museum', category: 'City' },
  { name: 'Lansdowne', state: 'Uttarakhand', tag: 'Tip-in-Top & Pine Forest Hill Station', category: 'Mountains' },
  { name: 'Lavasa', state: 'Maharashtra', tag: 'Planned Italian Town Waterfront', category: 'Nature' },

  // M
  { name: 'Mumbai', state: 'Maharashtra', tag: 'Gateway of India, Marine Drive & Bollywood', category: 'Metro' },
  { name: 'Manali', state: 'Himachal Pradesh', tag: 'Solang Valley, Rohtang Pass & Old Manali', category: 'Mountains' },
  { name: 'Madurai', state: 'Tamil Nadu', tag: 'Meenakshi Amman Temple', category: 'Spiritual' },
  { name: 'Mahabalipuram (Mamallapuram)', state: 'Tamil Nadu', tag: 'Shore Temple & Pancha Rathas', category: 'Heritage' },
  { name: 'Mysuru (Mysore)', state: 'Karnataka', tag: 'Mysore Palace & Chamundi Hills', category: 'Heritage' },
  { name: 'Mathura & Vrindavan', state: 'Uttar Pradesh', tag: 'Krishna Janmabhoomi & Banke Bihari', category: 'Spiritual' },
  { name: 'Mount Abu', state: 'Rajasthan', tag: 'Dilwara Temples & Nakki Lake', category: 'Mountains' },
  { name: 'Munnar', state: 'Kerala', tag: 'Tea Plantations & Eravikulam National Park', category: 'Mountains' },
  { name: 'Mussoorie', state: 'Uttarakhand', tag: 'Kempty Falls, Gun Hill & Mall Road', category: 'Mountains' },
  { name: 'Mangalore (Mangaluru)', state: 'Karnataka', tag: 'Panambur Beach & Seafood', category: 'Coastal' },
  { name: 'Meerut', state: 'Uttar Pradesh', tag: 'Augarnath Temple & 1857 Memorial', category: 'City' },
  { name: 'Muzaffarpur', state: 'Bihar', tag: 'Shahi Litchi & Garib Sthan Mandir', category: 'City' },
  { name: 'Motihari', state: 'Bihar', tag: 'Gandhi Smarak & George Orwell Birthplace', category: 'Heritage' },
  { name: 'Mahabaleshwar', state: 'Maharashtra', tag: 'Venna Lake & Strawberry Farms', category: 'Mountains' },
  { name: 'Mandu', state: 'Madhya Pradesh', tag: 'Jahaz Mahal & Rani Roopmati Pavilion', category: 'Heritage' },

  // N
  { name: 'Nainital', state: 'Uttarakhand', tag: 'Naini Lake, Naina Devi & Snow View', category: 'Mountains' },
  { name: 'Nagpur', state: 'Maharashtra', tag: 'Orange City & Deekshabhoomi', category: 'City' },
  { name: 'Nashik', state: 'Maharashtra', tag: 'Trimbakeshwar Temple & Sula Vineyards', category: 'Spiritual' },
  { name: 'Neemrana', state: 'Rajasthan', tag: 'Neemrana Fort Palace & Ziplining', category: 'Heritage' },
  { name: 'Nandi Hills', state: 'Karnataka', tag: 'Sunrise Viewpoint & Tipu’s Drop', category: 'Mountains' },
  { name: 'Nalanda & Rajgir', state: 'Bihar', tag: 'Ancient University Ruins & Ropeway', category: 'Heritage' },
  { name: 'Noida', state: 'Uttar Pradesh', tag: 'Buddh Circuit & DLF Mall', category: 'City' },

  // P
  { name: 'Patna', state: 'Bihar', tag: 'Golghar, Takht Sri Patna Sahib & Ganga Ghats', category: 'Heritage' },
  { name: 'Puri', state: 'Odisha', tag: 'Jagannath Temple & Golden Beach', category: 'Spiritual' },
  { name: 'Pushkar', state: 'Rajasthan', tag: 'Brahma Temple & Sacred Lake', category: 'Spiritual' },
  { name: 'Pune', state: 'Maharashtra', tag: 'Shaniwar Wada & Sinhagad Fort', category: 'Heritage' },
  { name: 'Pondicherry (Puducherry)', state: 'Puducherry', tag: 'French Colony, Promenade & Auroville', category: 'Coastal' },
  { name: 'Pahalgam', state: 'Jammu & Kashmir', tag: 'Betaab Valley & Aru Valley', category: 'Mountains' },
  { name: 'Panaji', state: 'Goa', tag: 'Fontainhas Latin Quarter & Mandovi River', category: 'Coastal' },
  { name: 'Prayagraj (Allahabad)', state: 'Uttar Pradesh', tag: 'Triveni Sangam & Kumbh Mela', category: 'Spiritual' },
  { name: 'Pachmarhi', state: 'Madhya Pradesh', tag: 'Satpura Queen & Bee Falls', category: 'Mountains' },
  { name: 'Port Blair', state: 'Andaman & Nicobar', tag: 'Cellular Jail & Radhanagar Beach', category: 'Coastal' },
  { name: 'Porbandar', state: 'Gujarat', tag: 'Kirti Mandir & Gandhi Birthplace', category: 'Heritage' },
  { name: 'Palampur', state: 'Himachal Pradesh', tag: 'Tea Capital & Dhauladhar Views', category: 'Mountains' },

  // R
  { name: 'Rishikesh', state: 'Uttarakhand', tag: 'Lakshman Jhula, Yoga & River Rafting', category: 'Spiritual' },
  { name: 'Ranthambore', state: 'Rajasthan', tag: 'Tiger Safari & Ranthambore Fort', category: 'Nature' },
  { name: 'Rameshwaram', state: 'Tamil Nadu', tag: 'Ramanathaswamy Temple & Pamban Bridge', category: 'Spiritual' },
  { name: 'Ranchi', state: 'Jharkhand', tag: 'Hundru Falls & Tagore Hill', category: 'Nature' },
  { name: 'Raipur', state: 'Chhattisgarh', tag: 'Swami Vivekananda Sarovar', category: 'City' },
  { name: 'Rajkot', state: 'Gujarat', tag: 'Watson Museum & Gandhi Smriti', category: 'Heritage' },
  { name: 'Rohtang Pass', state: 'Himachal Pradesh', tag: 'High Altitude Snow Pass', category: 'Mountains' },
  { name: 'Rourkela', state: 'Odisha', tag: 'Vedvyas & Hanuman Vatika', category: 'City' },
  { name: 'Ratnagiri', state: 'Maharashtra', tag: 'Alphonso Mangoes & Ganpatipule', category: 'Coastal' },

  // S
  { name: 'Shimla', state: 'Himachal Pradesh', tag: 'Mall Road, Ridge & Jakhoo Temple', category: 'Mountains' },
  { name: 'Srinagar', state: 'Jammu & Kashmir', tag: 'Dal Lake Shikara, Houseboats & Mughal Gardens', category: 'Mountains' },
  { name: 'Spiti Valley (Kaza)', state: 'Himachal Pradesh', tag: 'Key Monastery & Chandratal Lake', category: 'Mountains' },
  { name: 'Shillong', state: 'Meghalaya', tag: 'Scotland of the East & Elephant Falls', category: 'Mountains' },
  { name: 'Surat', state: 'Gujarat', tag: 'Diamond City, Textile Hub & Dumas Beach', category: 'City' },
  { name: 'Shirdi', state: 'Maharashtra', tag: 'Sai Baba Samadhi Temple', category: 'Spiritual' },
  { name: 'Somnath', state: 'Gujarat', tag: 'First Jyotirlinga Temple on Arabian Sea', category: 'Spiritual' },
  { name: 'Siliguri', state: 'West Bengal', tag: 'Gateway to North East & Darjeeling', category: 'City' },
  { name: 'Sonmarg', state: 'Jammu & Kashmir', tag: 'Meadow of Gold & Thajiwas Glacier', category: 'Mountains' },
  { name: 'Sanchi', state: 'Madhya Pradesh', tag: 'Great Buddhist Stupa & UNESCO Site', category: 'Heritage' },
  { name: 'Sarnath', state: 'Uttar Pradesh', tag: 'Dhamek Stupa & Ashoka Pillar', category: 'Heritage' },
  { name: 'Sundarbans', state: 'West Bengal', tag: 'Royal Bengal Tiger Mangrove Delta', category: 'Nature' },

  // T
  { name: 'Tirupati', state: 'Andhra Pradesh', tag: 'Sri Venkateswara Tirumala Temple', category: 'Spiritual' },
  { name: 'Thiruvananthapuram (Trivandrum)', state: 'Kerala', tag: 'Padmanabhaswamy Temple & Kovalam', category: 'Coastal' },
  { name: 'Thrissur', state: 'Kerala', tag: 'Vadakkunnathan Temple & Pooram Festival', category: 'Spiritual' },
  { name: 'Thanjavur (Tanjore)', state: 'Tamil Nadu', tag: 'Brihadeeswarar Big Temple & Paintings', category: 'Heritage' },
  { name: 'Thekkady (Periyar)', state: 'Kerala', tag: 'Elephant & Wildlife Boat Safari', category: 'Nature' },
  { name: 'Tawang', state: 'Arunachal Pradesh', tag: 'Tawang Monastery & Sela Pass', category: 'Mountains' },
  { name: 'Tezpur', state: 'Assam', tag: 'Agnigarh & Cultural City', category: 'Heritage' },

  // U
  { name: 'Udaipur', state: 'Rajasthan', tag: 'City of Lakes, City Palace & Lake Pichola', category: 'Heritage' },
  { name: 'Ujjain', state: 'Madhya Pradesh', tag: 'Mahakaleshwar Jyotirlinga & Mahakal Lok', category: 'Spiritual' },
  { name: 'Uttarkashi', state: 'Uttarakhand', tag: 'Vishwanath Temple & Trekking Hub', category: 'Mountains' },
  { name: 'Udupi', state: 'Karnataka', tag: 'Krishna Mutt & Malpe St. Mary’s Island', category: 'Coastal' },

  // V
  { name: 'Varanasi (Kashi / Banaras)', state: 'Uttar Pradesh', tag: 'Kashi Vishwanath, Ganga Ghats & Aarti', category: 'Spiritual' },
  { name: 'Visakhapatnam (Vizag)', state: 'Andhra Pradesh', tag: 'Rishikonda Beach, Araku Valley & Submarine', category: 'Coastal' },
  { name: 'Vadodara (Baroda)', state: 'Gujarat', tag: 'Laxmi Vilas Palace & Sayaji Baug', category: 'Heritage' },
  { name: 'Varkala', state: 'Kerala', tag: 'Varkala Cliff Beach & Papanasam', category: 'Coastal' },
  { name: 'Vijayawada', state: 'Andhra Pradesh', tag: 'Kanaka Durga Temple & Prakasam Barrage', category: 'Spiritual' },
  { name: 'Vellore', state: 'Tamil Nadu', tag: 'Vellore Fort & Sripuram Golden Temple', category: 'Heritage' },
  { name: 'Vapi', state: 'Gujarat', tag: 'Industrial Hub & Daman Gateway', category: 'City' },

  // W
  { name: 'Wayanad', state: 'Kerala', tag: 'Edakkal Caves, Chembra Peak & Waterfalls', category: 'Nature' },
  { name: 'Warangal', state: 'Telangana', tag: 'Thousand Pillar Temple & Warangal Fort', category: 'Heritage' }
];

export default function CityAutocomplete({ 
  value, 
  onChange, 
  placeholder = "e.g. Varanasi, Goa, Jaipur, Bengaluru, Agra…", 
  id = "destination", 
  name = "destination",
  required = true, 
  className = "",
  inputClassName = "",
  showIcon = true,
  iconSize = 18,
  autoFocus = false
}) {
  const [query, setQuery] = useState(value || '');
  const [isOpen, setIsOpen] = useState(false);
  const [highlightedIndex, setHighlightedIndex] = useState(-1);
  const wrapperRef = useRef(null);

  useEffect(() => {
    setQuery(value || '');
  }, [value]);

  // Filter cities based on user input
  const cleanQ = query.trim().toLowerCase();
  
  const suggestions = cleanQ.length === 0
    ? []
    : ALL_INDIAN_DESTINATIONS.filter(item => {
        const nameLower = item.name.toLowerCase();
        const stateLower = item.state.toLowerCase();
        const tagLower = item.tag.toLowerCase();
        return nameLower.startsWith(cleanQ) || 
               nameLower.includes(cleanQ) || 
               stateLower.startsWith(cleanQ) || 
               tagLower.includes(cleanQ);
      }).sort((a, b) => {
        // Boost cities whose name STARTS WITH query
        const aStarts = a.name.toLowerCase().startsWith(cleanQ);
        const bStarts = b.name.toLowerCase().startsWith(cleanQ);
        if (aStarts && !bStarts) return -1;
        if (!aStarts && bStarts) return 1;
        return 0;
      }).slice(0, 8);

  const handleSelect = (dest) => {
    const selectedName = dest.name.includes('(') ? dest.name.split('(')[0].trim() : dest.name;
    setQuery(selectedName);
    onChange(selectedName);
    setIsOpen(false);
    setHighlightedIndex(-1);
  };

  const handleKeyDown = (e) => {
    if (!isOpen || suggestions.length === 0) {
      if (e.key === 'ArrowDown' && suggestions.length > 0) {
        setIsOpen(true);
      }
      return;
    }

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setHighlightedIndex(prev => (prev < suggestions.length - 1 ? prev + 1 : 0));
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setHighlightedIndex(prev => (prev > 0 ? prev - 1 : suggestions.length - 1));
    } else if (e.key === 'Enter') {
      if (highlightedIndex >= 0 && highlightedIndex < suggestions.length) {
        e.preventDefault();
        handleSelect(suggestions[highlightedIndex]);
      }
    } else if (e.key === 'Escape') {
      setIsOpen(false);
      setHighlightedIndex(-1);
    }
  };

  // Click outside listener
  useEffect(() => {
    const handleClickOutside = (e) => {
      if (wrapperRef.current && !wrapperRef.current.contains(e.target)) {
        setIsOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    document.addEventListener('touchstart', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
      document.removeEventListener('touchstart', handleClickOutside);
    };
  }, []);

  return (
    <div className={`relative ${className}`} ref={wrapperRef}>
      <div className="relative flex items-center w-full">
        {showIcon && (
          <MapPin size={iconSize} className="absolute left-3.5 top-1/2 -translate-y-1/2 text-teal-600 dark:text-teal-400 pointer-events-none z-10" />
        )}
        <input
          id={id}
          name={name}
          type="text"
          value={query}
          onChange={(e) => {
            const val = e.target.value;
            setQuery(val);
            onChange?.(val);
            setIsOpen(val.trim().length > 0);
            setHighlightedIndex(0);
          }}
          onFocus={() => {
            if (query.trim().length > 0) setIsOpen(true);
          }}
          onKeyDown={handleKeyDown}
          placeholder={placeholder}
          autoComplete="off"
          autoFocus={autoFocus}
          required={required}
          className={inputClassName ? inputClassName : `input ${showIcon ? '!pl-10' : ''} text-base w-full`}
        />
      </div>

      {/* Autocomplete Suggestion Dropdown */}
      {isOpen && suggestions.length > 0 && (
        <div className="absolute left-0 right-0 top-full mt-1.5 max-h-72 overflow-y-auto rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-xl z-50 animate-in fade-in duration-100">
          <div className="p-1.5 space-y-1">
            <div className="px-3 py-1.5 text-[10px] font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 border-b border-slate-100 dark:border-slate-800 flex justify-between items-center">
              <span>Suggested Indian Destinations</span>
              <span className="text-[9px] font-normal lowercase">Press ↑↓ to navigate</span>
            </div>

            {suggestions.map((dest, index) => {
              const isHighlighted = highlightedIndex === index;
              return (
                <div
                  key={dest.name + index}
                  onClick={() => handleSelect(dest)}
                  onMouseEnter={() => setHighlightedIndex(index)}
                  className={`cursor-pointer rounded-xl px-3 py-2.5 flex items-center justify-between gap-3 transition-colors ${
                    isHighlighted
                      ? 'bg-teal-50 dark:bg-teal-950/70 text-teal-900 dark:text-teal-200'
                      : 'hover:bg-slate-50 dark:hover:bg-slate-800/60 text-slate-800 dark:text-slate-200'
                  }`}
                >
                  <div className="flex items-center gap-2.5 min-w-0 flex-1">
                    <div className={`grid h-8 w-8 shrink-0 place-items-center rounded-lg ${
                      isHighlighted 
                        ? 'bg-teal-700 text-white shadow-xs' 
                        : 'bg-slate-100 dark:bg-slate-800 text-slate-500 dark:text-slate-400'
                    }`}>
                      <MapPin size={15} />
                    </div>

                    <div className="min-w-0 flex-1">
                      <div className="flex items-center gap-1.5">
                        <span className="font-bold text-sm text-slate-900 dark:text-white truncate">
                          {dest.name}
                        </span>
                        <span className="text-xs text-slate-400 font-medium">
                          · {dest.state}
                        </span>
                      </div>
                      <p className="text-xs text-slate-500 dark:text-slate-400 truncate mt-0.5">
                        {dest.tag}
                      </p>
                    </div>
                  </div>

                  <div className="shrink-0 flex items-center gap-1.5">
                    <span className="hidden sm:inline-block rounded-md bg-slate-100 dark:bg-slate-800 px-2 py-0.5 text-[10px] font-semibold text-slate-600 dark:text-slate-300">
                      {dest.category}
                    </span>
                    <ChevronRight size={14} className="text-slate-400" />
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}
