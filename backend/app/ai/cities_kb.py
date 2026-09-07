"""Comprehensive Indian Cities Knowledge Base for TourMitra AI Assistant.
Provides deep, authoritative tourism data for Indian state capitals, heritage centers, and tourist hubs.
"""
from typing import Optional, Dict, Any

INDIAN_CITIES_KB: Dict[str, Dict[str, Any]] = {
    "patna": {
        "name": "Patna",
        "state": "Bihar",
        "description": "Ancient historic capital on the banks of Ganga (historic Pataliputra), world-famous for sacred Sikh heritage, Mauryan history, museums, and rich culture.",
        "famous_places": [
            "Golghar (Historic granary with Ganga view)",
            "Takht Sri Patna Sahib (Birthplace of Guru Gobind Singh Ji)",
            "Bihar Museum & Patna Museum (World-class art & Yakshi statue)",
            "Buddha Smriti Park & Karuna Stupa",
            "Mahavir Mandir (One of the holiest Hanuman shrines)",
            "Kumhrar (Ancient Mauryan 80-pillared hall ruins)",
            "Sabhyata Dwar & Marine Drive Ganga Riverfront"
        ],
        "famous_food": [
            "Litti Chokha with Desi Ghee & Baingan Bharta",
            "Silao Khaja & Chandrakala",
            "Gaya Tilkut & Anarsa",
            "Dal Pitha (Traditional steamed rice dumplings)",
            "Sattu Sharbat & Kachori Jalebi",
            "Bihari Mutton Kebab & Champaran Handi Meat",
            "Chana Ghugni with Poha"
        ],
        "temples_spiritual": [
            "Takht Sri Patna Sahib (5 Takhts of Sikhism)",
            "Mahavir Mandir (Patna Junction)",
            "Badi Patan Devi & Chhoti Patan Devi (51 Shaktipeeth)",
            "Sheetla Mata Mandir (Agam Kuan)",
            "Buddha Smriti Relic Stupa"
        ],
        "heritage_sites": [
            "Kumhrar (Mauryan Empire Archaeological Excavations)",
            "Golghar (1786 British architectural marvel)",
            "Padri Ki Haveli (Oldest Catholic church in Bihar)",
            "Qila House / Jalan Museum (Jade & Mughal antiques)"
        ],
        "budget": {
            "budget": "₹1,000 – ₹1,500/day (Dharamshala/Budget stay + Local transport + Litti Chokha/Street food)",
            "mid": "₹2,200 – ₹3,500/day (3-star hotel + AC cabs + Family restaurants)",
            "luxury": "₹5,000+/day (Hotel Maurya / Lemon Tree + Private chauffeur + Fine dining)"
        },
        "best_time": "October to March (Pleasant winter climate; ideal for Chhath Puja, Prakash Parv, and riverfront visits)",
        "specialties": "Madhubani paintings, Tikuli craft, Bhagalpuri silk sarees, and stone pottery."
    },
    "lucknow": {
        "name": "Lucknow",
        "state": "Uttar Pradesh",
        "description": "The City of Nawabs, celebrated globally for refined Tehzeeb, Awadhi Nawabi cuisine, intricate Chikankari embroidery, and grand Mughal-Baroque architecture.",
        "famous_places": [
            "Bara Imambara & Bhool Bhulaiya (Labyrinth)",
            "Chhota Imambara (Palace of Lights)",
            "Rumi Darwaza (Iconic 60-ft gateway)",
            "British Residency (1857 Mutiny historical site)",
            "Ambedkar Memorial Park (Gomti Nagar)",
            "Hazratganj (Heritage promenade & shopping boulevard)",
            "Janeshwar Mishra Park (Asia largest eco-park)",
            "Clock Tower (Ghanta Ghar) & Picture Gallery"
        ],
        "famous_food": [
            "Tunday Kababi Galawati Kebabs with Roomali Roti",
            "Awadhi Mutton Dum Biryani & Kakori Kebabs",
            "Prakash ki Kulfi (Aminabad)",
            "Makhan Malai / Nimish (Winter saffron dessert)",
            "Tokri Chaat (Royal Café, Hazratganj)",
            "Sheermal & Mughlai Kulcha Nihari (Rahim’s, Chowk)",
            "Malai Paan & Raja Thandai"
        ],
        "temples_spiritual": [
            "Bara Imambara & Asfi Mosque",
            "Hanuman Setu Temple (Near Lucknow University)",
            "Chandrika Devi Temple (Ancient Gomti river shrine)",
            "Mankameshwar Mandir",
            "Jama Masjid (Hussainabad)"
        ],
        "heritage_sites": [
            "Bara Imambara & Shahi Baoli (Stepwell)",
            "Rumi Darwaza (Constantinople architecture design)",
            "British Residency & Museum",
            "Kaiserbagh Palace Complex & Chattar Manzil"
        ],
        "budget": {
            "budget": "₹1,200 – ₹1,800/day (Guesthouse + Auto/Metro + Aminabad/Chowk food)",
            "mid": "₹2,800 – ₹4,500/day (Heritage 3/4-star hotel + Hazratganj cafes + Cab tours)",
            "luxury": "₹6,500+/day (Taj Mahal Lucknow / Hyatt Regency + Nawabi banquets)"
        },
        "best_time": "October to March (Chilly, pleasant evenings perfect for heritage walks and culinary trails)",
        "specialties": "Hand-stitched Chikankari kurtas, Zardozi work, Attar (natural perfumes from Kannauj), and bone carving craft."
    },
    "delhi": {
        "name": "Delhi",
        "state": "National Capital Territory",
        "description": "India capital combining millennia of Mughal & Sultanate heritage, colonial Rajpath architecture, and greatest street food culture.",
        "famous_places": [
            "Red Fort (Lal Qila UNESCO World Heritage)",
            "Qutub Minar & Iron Pillar",
            "Humayun Tomb (Precursor to Taj Mahal)",
            "India Gate & Kartavya Path",
            "Lotus Temple (Baháʼí House of Worship)",
            "Akshardham Temple (Grand architectural complex)",
            "Chandni Chowk & Jama Masjid",
            "National War Memorial & Rashtrapati Bhavan",
            "Hauz Khas Village & Lodhi Garden"
        ],
        "famous_food": [
            "Old Delhi Chhole Bhature (Sita Ram Diwan Chand)",
            "Paranthe Wali Gali (Stuffed fried parathas)",
            "Karim & Al Jawahar Mutton Korma and Kebabs",
            "Butter Chicken & Dal Makhani (Moti Mahal origin)",
            "Dahi Bhalla (Natraj, Chandni Chowk)",
            "Kuremal Mohan Lal Kulfi (Stuffed real-fruit kulfi)",
            "Momos & Tibetan Delicacies (Majnu Ka Tilla)"
        ],
        "temples_spiritual": [
            "Swaminarayan Akshardham Temple",
            "Lotus Temple (Bahai House of Worship)",
            "Jama Masjid (One of India largest mosques)",
            "Gurudwara Bangla Sahib (Sacred Sarovar & 24/7 Langar)",
            "Birla Mandir (Laxminarayan Temple)",
            "Nizamuddin Dargah (Famous Thursday Qawwalis)",
            "Kalkaji Mandir & ISKCON Temple"
        ],
        "heritage_sites": [
            "Red Fort (Emperor Shah Jahan citadel)",
            "Qutub Minar Complex (1192 AD Afghan architecture)",
            "Humayun Tomb (Mughal garden tomb)",
            "Jantar Mantar (Astronomical observatory)",
            "Purana Qila & Agrasen Ki Baoli (Historic stepwell)"
        ],
        "budget": {
            "budget": "₹1,200 – ₹1,800/day (Hostels in Paharganj/South Delhi + Metro pass + Street eats)",
            "mid": "₹3,000 – ₹5,000/day (Boutique hotel + Uber/Metro + Connaught Place dining)",
            "luxury": "₹7,500+/day (The Imperial / The Leela Palace + Luxury culinary dining)"
        },
        "best_time": "October to March (Crisp winter weather ideal for monuments and food tours)",
        "specialties": "Khari Baoli spice market, Dilli Haat handicrafts, Janpath silver jewelry, Sarojini Nagar textiles."
    },
    "mumbai": {
        "name": "Mumbai",
        "state": "Maharashtra",
        "description": "The City of Dreams, financial capital of India, home to Bollywood, British Victorian Gothic architecture, and the Arabian Sea coastline.",
        "famous_places": [
            "Gateway of India & The Taj Mahal Palace Hotel",
            "Marine Drive (Queen Necklace) & Chowpatty Beach",
            "Chhatrapati Shivaji Maharaj Terminus (CSMT UNESCO Site)",
            "Elephanta Caves (UNESCO rock-cut Shiva sculptures)",
            "Bandra-Worli Sea Link & Bandra Bandstand (Mannat)",
            "Siddhivinayak Temple & Haji Ali Dargah",
            "Colaba Causeway & Kala Ghoda Art District",
            "Juhu Beach & Sanjay Gandhi National Park"
        ],
        "famous_food": [
            "Vada Pav & Pav Bhaji (Sardar / Cannon)",
            "Misal Pav & Kanda Poha",
            "Bombay Duck (Bombil Fry) & Malvani Coastal Seafood",
            "Bun Maska & Irani Chai (Kyani & Co. / Britannia)",
            "Bhel Puri & Sev Puri (Girgaon Chowpatty)",
            "Frankie & Falooda (Badshah, Crawford Market)",
            "Parsi Dhansak & Berry Pulao"
        ],
        "temples_spiritual": [
            "Shree Siddhivinayak Temple (Prabhadevi)",
            "Haji Ali Dargah (Mosque in the middle of Arabian Sea)",
            "Mahalaxmi Temple & Babulnath Temple",
            "Mount Mary Church (Bandra)",
            "Mumba Devi Temple (City namesake deity)",
            "Global Vipassana Pagoda (Gorai)"
        ],
        "heritage_sites": [
            "CSMT Railway Station (Victorian Gothic Architecture)",
            "Elephanta Island Rock-cut Caves (6th century CE)",
            "Kanheri Caves (Ancient Buddhist rock monasteries)",
            "Kala Ghoda Heritage Precinct & Rajabai Clock Tower"
        ],
        "budget": {
            "budget": "₹1,500 – ₹2,200/day (Hostels in Bandra/Colaba + Local train/BEST bus + Street food)",
            "mid": "₹3,500 – ₹6,000/day (Comfort hotel + Kaali-Peeli/Uber + Coastal restaurants)",
            "luxury": "₹9,000+/day (Taj Lands End / The Oberoi + Rooftop lounges)"
        },
        "best_time": "November to February (Pleasant coastal breezes with low humidity)",
        "specialties": "Colaba street fashion, Bollywood memorabilia, Kolhapuri chappals, Mangalorean spices."
    },
    "kolkata": {
        "name": "Kolkata",
        "state": "West Bengal",
        "description": "The Cultural Capital of India, city of joy, colonial grand architecture, literature, Nobel laureates, and legendary Bengali sweets and street food.",
        "famous_places": [
            "Victoria Memorial & Maidan",
            "Howrah Bridge (Iconic cantilever bridge on Hooghly)",
            "Dakshineswar Kali Temple & Belur Math",
            "Indian Museum (Oldest museum in Asia)",
            "Park Street & Princep Ghat (Riverfront promenade)",
            "St. Paul Cathedral & Marble Palace",
            "Kumartuli (Artisan idol-makers quarter)",
            "Science City & Eco Park (Rajarhat)"
        ],
        "famous_food": [
            "Kolkata Biryani with Aloo & Boiled Egg (Arsalan/Shiraz)",
            "Kathi Roll (Nizam origin at New Market)",
            "Kolkata Phuchka (Tamarind & spicy potato water pani puri)",
            "Rasgulla (Nobin Chandra Das), Sandesh & Mishti Doi",
            "Ilish Macher Jhol, Kosha Mangsho with Luchi",
            "Chelo Kebab & Flurys English Breakfast (Park Street)",
            "Churmur, Singara & Telebhaja"
        ],
        "temples_spiritual": [
            "Dakshineswar Kali Temple (Bhavatarini Kali & Sri Ramakrishna room)",
            "Kalighat Kali Temple (51 Shaktipeeth)",
            "Belur Math (Headquarters of Ramakrishna Math & Mission)",
            "St. Paul Cathedral & St. John Church",
            "Nakhoda Mosque (Chitpur)",
            "Pareshnath Jain Temple"
        ],
        "heritage_sites": [
            "Victoria Memorial Hall (White Makrana marble masterpiece)",
            "Marble Palace (1835 neoclassical mansion & art collection)",
            "National Library & Writers Building",
            "Jorasanko Thakur Bari (Ancestral home of Rabindranath Tagore)"
        ],
        "budget": {
            "budget": "₹1,000 – ₹1,500/day (Sudder street budget stays + Tram/Metro + Phuchka/Rolls)",
            "mid": "₹2,500 – ₹4,000/day (Heritage homestay/Hotel + Yellow taxi/Uber + Park Street dining)",
            "luxury": "₹6,000+/day (The Oberoi Grand / ITC Royal Bengal + Fine dining)"
        },
        "best_time": "October to March (Durga Puja festival in Autumn, winter book fairs & soothing weather)",
        "specialties": "Tant & Jamdani cotton sarees, Terracotta handicrafts, Dokra brass art, Darjeeling tea, Sandesh."
    },
    "varanasi": {
        "name": "Varanasi (Banaras / Kashi)",
        "state": "Uttar Pradesh",
        "description": "One of the world oldest continuously inhabited living cities, spiritual capital of India on the sacred Ganga, home to mystical ghats, evening Aarti, and Banarasi silk.",
        "famous_places": [
            "Kashi Vishwanath Temple & Corridor (Jyotirlinga)",
            "Dashashwamedh Ghat (World-renowned Ganga Aarti)",
            "Assi Ghat (Morning Subah-e-Banaras, Yoga & Sunrise boat ride)",
            "Manikarnika Ghat & Harishchandra Ghat",
            "Sarnath (Where Lord Buddha preached his first sermon - Dhamek Stupa)",
            "BHU Campus & New Vishwanath Temple (VT)",
            "Ramnagar Fort & Museum across Ganga",
            "Tulsi Manas Mandir & Sankat Mochan Hanuman Temple"
        ],
        "famous_food": [
            "Banarasi Paan (Maghai / Meetha Paan)",
            "Kachori Sabzi & Jalebi (Morning Ram Bhandar / Chachi ki Kachori)",
            "Banarasi Tamatar Chaat (Kashi Chaat Bhandar)",
            "Malaiyo / Makhan Malai (Winter saffron froth sweet)",
            "Blue Lassi / Pehalwan Lassi (Kulhad Lassi)",
            "Baati Chokha & Chena Dahi Vada",
            "Laal Peda & Rabri Jalebi"
        ],
        "temples_spiritual": [
            "Kashi Vishwanath Jyotirlinga Temple",
            "Sankat Mochan Hanuman Mandir (Founded by Goswami Tulsidas)",
            "Kaal Bhairav Mandir (Kotwal of Kashi)",
            "Annapurna Devi Mandir & Durga Kund Mandir",
            "Vishalakshi Temple (51 Shaktipeeth)",
            "Sarnath Buddhist Temples & Monasteries"
        ],
        "heritage_sites": [
            "84 Ancient River Ghats (Chet Singh, Munshi, Darbhanga Ghats)",
            "Dhamek Stupa & Ashoka Pillar (Sarnath Archaeological Site)",
            "Ramnagar Fort (18th-century sandstone palace)",
            "Bharat Mata Mandir (Relief map of undivided India carved in marble)"
        ],
        "budget": {
            "budget": "₹900 – ₹1,400/day (Ghatside hostel/ashram + Shared boat/walk + Street delicacies)",
            "mid": "₹2,200 – ₹3,800/day (Heritage haveli stay + Private morning boat + Restaurant thali)",
            "luxury": "₹6,000+/day (BrijRama Palace / Taj Nadesar + Private guided spiritual trails)"
        },
        "best_time": "October to March (Cool river breeze, Dev Deepawali festival in Kartik Purnima is spectacular)",
        "specialties": "Pure Banarasi Zari Silk Sarees, Banarasi Gulabi Meenakari (pink enamel craft), wooden lacquer toys, brass puja utensils."
    },
    "jaipur": {
        "name": "Jaipur",
        "state": "Rajasthan",
        "description": "The Pink City, capital of Rajasthan, UNESCO World Heritage city renowned for majestic Rajput forts, royal palaces, vibrant bazaars, and rich spicy Rajasthani cuisine.",
        "famous_places": [
            "Amber Fort & Sheesh Mahal (Mirror Palace)",
            "Hawa Mahal (Palace of Winds - 953 Jharokhas)",
            "City Palace & Chandra Mahal",
            "Jantar Mantar (UNESCO World Heritage Astronomical Observatory)",
            "Nahargarh Fort & Jaigarh Fort (World largest cannon Jaivana)",
            "Jal Mahal (Water palace on Man Sagar Lake)",
            "Albert Hall Museum (Indo-Saracenic masterpiece)",
            "Patrika Gate & Chokhi Dhani (Ethnic village resort)"
        ],
        "famous_food": [
            "Dal Baati Churma with Ghee & Garlic Chutney",
            "Pyaaz Kachori (Rawat Mishthan Bhandar)",
            "Ghevar (Malai / Mawa Ghevar from LMB Johari Bazaar)",
            "Laal Maas (Royal spicy Rajasthani mutton)",
            "Ker Sangri & Gatte ki Sabzi",
            "Lassi at Lassiwala (MI Road since 1944)",
            "Mawa Kachori & Mirchi Vada"
        ],
        "temples_spiritual": [
            "Govind Dev Ji Temple (Inside City Palace complex)",
            "Birla Mandir (Laxmi Narayan Temple in white marble)",
            "Galtaji Temple (Monkey Temple & Natural Springs)",
            "Moti Dungri Ganesh Mandir",
            "Khole Ke Hanuman Ji"
        ],
        "heritage_sites": [
            "Amber Palace (Majestic hilltop Rajput fort)",
            "Hawa Mahal (1799 pink sandstone facade)",
            "Jantar Mantar (Samrat Yantra sundial)",
            "Nahargarh Fort (Panoramic sunset city views)"
        ],
        "budget": {
            "budget": "₹1,200 – ₹1,800/day (Heritage hostel/guesthouse + E-rickshaw/bus + Street snacks)",
            "mid": "₹2,800 – ₹4,500/day (Haveli hotel + AC cab rental + Chokhi Dhani feast)",
            "luxury": "₹8,000+/day (Rambagh Palace / Jai Mahal Palace + Royal suites)"
        },
        "best_time": "October to March (Warm sunny days and cool desert nights; Jaipur Literature Festival in Jan)",
        "specialties": "Blue Pottery, Jaipuri Razai (quilts), Bandhani & Leheriya tie-dye, Kundan-Meena jewellery, Mojari leather shoes."
    },
    "agra": {
        "name": "Agra",
        "state": "Uttar Pradesh",
        "description": "Home of the Taj Mahal, eternal monument of love, epicenter of Mughal Empire architectural splendor and rich Mughlai gastronomical heritage.",
        "famous_places": [
            "Taj Mahal (UNESCO World Heritage & 7 Wonder of the World)",
            "Agra Fort (Red sandstone citadel of Mughal emperors)",
            "Fatehpur Sikri & Buland Darwaza (40km from Agra)",
            "Mehtab Bagh (Sunset moonlight view of Taj across Yamuna)",
            "Tomb of I timad-ud-Daulah (Baby Taj)",
            "Akbar Tomb at Sikandra",
            "Kinari Bazaar & Sadar Bazaar"
        ],
        "famous_food": [
            "Agra ka Petha (Angoori, Kesar, Paan, Chocolate Petha - Panchhi Petha)",
            "Bedmi Puri with Aloo Sabzi & Jalebi (Deviram Sweets)",
            "Mughlai Biryani, Chicken Tikka & Seekh Kebabs",
            "Dalmoth (Spicy crispy lentil namkeen)",
            "Bhalla Chaat (Sadar Bazaar)",
            "Tandoori Naan with Paneer Butter Masala"
        ],
        "temples_spiritual": [
            "Balkeshwar Temple (Ancient Shiva temple on Yamuna banks)",
            "Mankameshwar Temple (Near Agra Fort)",
            "Gurudwara Guru Ka Taal",
            "Jama Masjid Agra (Built by Jahanara Begum)"
        ],
        "heritage_sites": [
            "Taj Mahal (1632-1653 AD White Makrana Marble monument)",
            "Agra Fort (Jahangiri Mahal, Khas Mahal, Diwan-i-Khas)",
            "Fatehpur Sikri (Buland Darwaza, Salim Chishti Dargah, Panch Mahal)",
            "Itmad-ud-Daulah (Pietra dura inlay work prototype)"
        ],
        "budget": {
            "budget": "₹1,100 – ₹1,600/day (Taj Ganj hostel + Auto + Street food)",
            "mid": "₹2,500 – ₹4,000/day (3-star hotel with Taj view + Cabs + Restaurant meals)",
            "luxury": "₹7,500+/day (The Oberoi Amarvilas with direct Taj view + Mughal royal dining)"
        },
        "best_time": "October to March (Pleasant winter sunshine; Taj Mahotsav festival in February)",
        "specialties": "Marble inlay handicraft (Pietra Dura), Leather shoes and bags, Zari embroidery, Authentic Panchhi Petha."
    },
    "bengaluru": {
        "name": "Bengaluru (Bangalore)",
        "state": "Karnataka",
        "description": "The Silicon Valley of India & Garden City, renowned for pleasant year-round weather, sprawling parks, microbreweries, and legendary South Indian breakfast hubs.",
        "famous_places": [
            "Lalbagh Botanical Garden & Glass House",
            "Cubbon Park & Vidhana Soudha (Neo-Dravidian legislative seat)",
            "Bangalore Palace (Tudor-style royal estate)",
            "Tipu Sultan Summer Palace & Bangalore Fort",
            "Bannerghatta National Park & Biological Reserve",
            "UB City & Brigade Road / MG Road",
            "ISKCON Temple Bangalore (Rajajinagar hillock)",
            "Nandi Hills (Famous sunrise viewpoint 60km away)"
        ],
        "famous_food": [
            "Crispy Benne Masala Dosa (CTR Malleshwaram / Vidyarthi Bhavan)",
            "Rava Idli & Filter Coffee (MTR - Mavalli Tiffin Room)",
            "Bisi Bele Bath & Khara Bath",
            "Mysore Pak (Ghee sweet)",
            "Mangalore Buns & Neer Dosa",
            "Karnataka Donne Biryani (Shivaji Military Hotel)",
            "Craft Beer & Wood-fired Pizzas (Indiranagar & Koramangala)"
        ],
        "temples_spiritual": [
            "Sri Radha Krishna ISKCON Temple (Rajajinagar)",
            "Bull Temple (Nandi Temple, Basavanagudi)",
            "Dodda Ganapathi Temple",
            "St. Mary Basilica (Shivajinagar)",
            "Someshwara Temple (Halasuru - Chola era)"
        ],
        "heritage_sites": [
            "Bangalore Palace (1878 royal palace inspired by Windsor Castle)",
            "Tipu Sultan Summer Palace (Teakwood Indo-Islamic structure)",
            "Vidhana Soudha (Magnificent granite architectural monument)",
            "Devanahalli Fort (Birthplace of Tipu Sultan)"
        ],
        "budget": {
            "budget": "₹1,300 – ₹1,900/day (Hostels in Indiranagar/Koramangala + Metro pass + Darshini breakfast)",
            "mid": "₹3,000 – ₹5,000/day (Business hotel + Uber/Auto + Microbrewery/cafes)",
            "luxury": "₹7,500+/day (The Leela Palace / Taj West End + Fine dining)"
        },
        "best_time": "September to March (Pleasant, moderate climate throughout the year)",
        "specialties": "Mysore Silk sarees, Sandalwood soaps and carvings, Channapatna wooden lacquer toys, Filter coffee powder."
    },
    "hyderabad": {
        "name": "Hyderabad",
        "state": "Telangana",
        "description": "City of Pearls and Nizams, renowned worldwide for world-famous Dum Biryani, historic Charminar, Golconda Fort, and booming Cyberabad IT hub.",
        "famous_places": [
            "Charminar & Makkah Masjid",
            "Golconda Fort & Sound and Light Show",
            "Chowmahalla Palace (Nizam opulent palace)",
            "Qutb Shahi Tombs & Seven Tombs Park",
            "Hussain Sagar Lake & Giant Buddha Statue",
            "Ramoji Film City (World largest film studio complex)",
            "Salar Jung Museum (Veiled Rebecca & Musical Clock)",
            "Birla Mandir & Statue of Equality"
        ],
        "famous_food": [
            "Hyderabadi Mutton Dum Biryani (Paradise / Bawarchi / Shadab)",
            "Haleem (Pista House - during Ramzan season)",
            "Mirchi Ka Salan & Double Ka Meetha",
            "Osmania Biscuits & Irani Chai (Nimrah Cafe beside Charminar)",
            "Boti Kebab, Pathar Ka Gosht & Marag soup",
            "Qubani Ka Meetha with Custard/Ice-cream",
            "Andhra Meals with Gongura Pachadi"
        ],
        "temples_spiritual": [
            "Birla Mandir (White Rajasthani marble atop Naubat Pahad)",
            "Chilkur Balaji Temple (Visa Balaji)",
            "Jagannath Temple (Banjara Hills)",
            "Makkah Masjid (Built with bricks from Mecca soil)",
            "Statue of Equality (1000th birth anniversary of Ramanujacharya)"
        ],
        "heritage_sites": [
            "Charminar (1591 AD landmark with 4 grand arches)",
            "Golconda Fort (Famous acoustic clap system & Koh-i-Noor diamond origin)",
            "Chowmahalla Palace (Coronation hall & vintage car collection)",
            "Salar Jung Museum (One man rare antique collection)"
        ],
        "budget": {
            "budget": "₹1,200 – ₹1,800/day (Guesthouse + Metro/Auto + Biryani & Irani cafe)",
            "mid": "₹2,800 – ₹4,500/day (3-4 star hotel + Cabs + Historic tours & Ramoji)",
            "luxury": "₹8,000+/day (Taj Falaknuma Palace - Live like a Nizam)"
        },
        "best_time": "October to March (Cool, pleasant weather; ideal for walking through old bazaars)",
        "specialties": "Basra Natural Pearls, Lac bangles (Laad Bazaar), Pochampally & Gadwal handloom sarees, Bidri metalware."
    },
    "chennai": {
        "name": "Chennai",
        "state": "Tamil Nadu",
        "description": "Gateway to South India, cultural capital of Carnatic music and Bharatanatyam, home to ancient Dravidian temples and the world 2nd longest natural urban beach.",
        "famous_places": [
            "Marina Beach (World 2nd longest urban beach)",
            "Kapaleeshwarar Temple (Mylapore Dravidian architecture)",
            "San Thome Cathedral Basilica (Apostle St. Thomas tomb)",
            "Fort St. George & Museum (1644 British stronghold)",
            "Government Museum & Bronze Gallery (Egmore)",
            "Guindy National Park & Snake Park",
            "DakshinaChitra Heritage Village (ECR)",
            "Mahabalipuram Shore Temples (1 hr drive UNESCO site)"
        ],
        "famous_food": [
            "Crispy Ghee Podi Dosa & Idli-Vada Sambar (Murugan Idli / Ratna Cafe)",
            "Authentic South Indian Filter Kaapi (Degree Coffee)",
            "Chettinad Chicken Curry & Meen Varuval (Fish Fry)",
            "Pongal with Coconut Chutney & Medu Vada",
            "Jigarthanda & Sundal (Beachside snack)",
            "Kothu Parotta & Parotta Salna",
            "Mysore Pak (Grand Sweets / Sri Krishna Sweets)"
        ],
        "temples_spiritual": [
            "Kapaleeshwarar Temple (Mylapore - Lord Shiva & Goddess Karpagambal)",
            "Parthasarathy Temple (8th-century temple in Triplicane)",
            "San Thome Basilica (Built over tomb of Apostle St. Thomas)",
            "Ashtalakshmi Temple (Besant Nagar Beach)",
            "Vadapalani Murugan Temple"
        ],
        "heritage_sites": [
            "Fort St. George (First English fortress in India)",
            "Ripon Building & Victoria Public Hall (Indo-Saracenic)",
            "Vivekanandar Illam (Vivekananda House Ice House)",
            "Mahabalipuram Pancha Rathas & Shore Temple (Nearby)"
        ],
        "budget": {
            "budget": "₹1,100 – ₹1,700/day (Budget stay + Metro/Local suburban train + Tiffin)",
            "mid": "₹2,600 – ₹4,200/day (3-star hotel + Cabs + Chettinad & seafood restaurants)",
            "luxury": "₹6,500+/day (ITC Grand Chola / Taj Coromandel + Carnatic music experience)"
        },
        "best_time": "November to February (Mild winter pleasant coastal weather; Margazhi Music Season in Dec-Jan)",
        "specialties": "Kanchipuram pure silk sarees, Tanjore gold foil paintings, Bronze Nataraja idols, Filter coffee sets."
    },
    "amritsar": {
        "name": "Amritsar",
        "state": "Punjab",
        "description": "The Golden Heart of Punjab, supreme spiritual seat of Sikhism, land of patriotism, hospitality, and mouth-watering Punjabi gastronomy.",
        "famous_places": [
            "Sri Harmandir Sahib (Golden Temple)",
            "Jallianwala Bagh Memorial & Eternal Flame",
            "Attari-Wagah Border Beating Retreat Ceremony",
            "Partition Museum (Town Hall)",
            "Gobindgarh Fort & Whispering Walls Light Show",
            "Durgiana Temple (Silver Temple)",
            "Ram Tirath Ashram (Valmiki Ashram)",
            "Hall Bazaar & Katra Jaimal Singh Market"
        ],
        "famous_food": [
            "Amritsari Kulcha with Chhole & Imli Chutney (Bhai Kulwant Singh / Monu)",
            "Guru Ka Langar (24/7 world largest community kitchen at Golden Temple)",
            "Amritsari Machhi (Fried Fish at Makhan Fish / Pehalwan)",
            "Ahuja Milk Center Kesar Lassi (Malai topped lassi)",
            "Beera Spiced Tandoori Chicken & Mutton Chaap",
            "Kanha Sweets Poori Chhole with Halwa",
            "Jalebi from Gurdas Ram Jalebiwala (Katrawala)"
        ],
        "temples_spiritual": [
            "Sri Harmandir Sahib (Golden Temple - Akal Takht)",
            "Durgiana Mandir (Dedicated to Goddess Durga & Lakshmi Narayan)",
            "Gurudwara Baba Atal Rai (9-storey octagonal tower)",
            "Gurudwara Chheharta Sahib",
            "Ram Tirath Temple (Birthplace of Luv & Kush)"
        ],
        "heritage_sites": [
            "Jallianwala Bagh (Preserved bullet marks & Martyr Well from 1919)",
            "Gobindgarh Fort (Built by Maharaja Ranjit Singh)",
            "Partition Museum (First museum dedicated to 1947 Partition)",
            "Khalsa College (Grand Victorian-Sikh architectural marvel)"
        ],
        "budget": {
            "budget": "₹900 – ₹1,400/day (Golden Temple Sarai/Budget hotel + Shared e-rickshaws + Langar/Street food)",
            "mid": "₹2,200 – ₹3,800/day (Heritage hotel + AC taxi to Wagah + Dhabas)",
            "luxury": "₹5,500+/day (Taj Swarna / Hyatt Regency + Luxury Wagah VIP tour)"
        },
        "best_time": "October to March (Crisp winter weather; festive atmosphere during Gurpurab and Baisakhi)",
        "specialties": "Phulkari dupattas and suits, Amritsari Papad & Wadian, Punjabi Juttis, Brass Kada."
    },
    "indore": {
        "name": "Indore",
        "state": "Madhya Pradesh",
        "description": "India cleanest city for 7 consecutive years, commercial capital of MP, home to Holkar royal heritage and India greatest night street food market Sarafa Bazaar.",
        "famous_places": [
            "Rajwada Palace (7-storey Holkar dynasty palace)",
            "Sarafa Bazaar (Jewellery market by day, night street food capital by night)",
            "Chappan Dukan (56 Food Stalls street)",
            "Lal Bagh Palace (Opulent palace modelled after Versailles)",
            "Kanch Mandir (Glass Jain Temple)",
            "Annapurna Temple & Khajrana Ganesh Mandir",
            "Patalpani Waterfall & Ralamandal Wildlife Sanctuary",
            "Mahakaleshwar Jyotirlinga Ujjain (55km easy day-trip)"
        ],
        "famous_food": [
            "Indori Poha with Sev & Jeeravan Masala (Prashant / Apna Sweets)",
            "Bhutte Ka Kees (Grated spicy spiced corn sweet & savory dish)",
            "Garadu (Deep fried spiced winter yam)",
            "Joshi Ji Ka Dahi Vada (Famous flying dahi vada at Sarafa)",
            "Khopra Patties (Vijay Chaat House)",
            "Mawa Bati, Rabdi Malpua & Gulab Jamun",
            "Indori Sev, Ratlami Sev & Khatta Meetha Namkeen"
        ],
        "temples_spiritual": [
            "Khajrana Ganesh Mandir (Built by Rani Ahilyabai Holkar)",
            "Kanch Mandir (Entire temple interior intricately inlaid with glass & mirrors)",
            "Annapurna Mandir (Grand elephant gateway)",
            "Gomatgiri Jain Tirth",
            "Bada Ganpati Mandir"
        ],
        "heritage_sites": [
            "Rajwada Palace (Indo-Saracenic & Maratha wooden architecture)",
            "Lal Bagh Palace (European interiors, Italian marble & Belgium glass)",
            "Krishnapura Chhatris (Holkar dynasty cenotaphs on Kahn river)"
        ],
        "budget": {
            "budget": "₹900 – ₹1,400/day (Budget stay + iBus city bus/auto + Chappan & Sarafa street food)",
            "mid": "₹2,200 – ₹3,600/day (Comfort hotel + Cab + Ujjain excursion)",
            "luxury": "₹5,500+/day (Sayaji Hotel / Radisson Blu + Fine dining)"
        },
        "best_time": "October to March (Pleasant, breezy weather ideal for night food explorations)",
        "specialties": "Chanderi & Maheshwari handloom sarees, Indori Sev & Namkeen boxes, Leather toys, Block print fabrics."
    },
    "bhopal": {
        "name": "Bhopal",
        "state": "Madhya Pradesh",
        "description": "The City of Lakes, capital of Madhya Pradesh, blend of grand Begum-era mosques, scenic Upper & Lower lakes, and UNESCO World Heritage prehistoric rock caves.",
        "famous_places": [
            "Upper Lake (Bhojtal) & Boat Club / VIP Road",
            "Taj-ul-Masajid (One of Asia largest and grandest pink stone mosques)",
            "Sanchi Stupa (UNESCO World Heritage Site 45km away)",
            "Bhimbetka Rock Shelters (UNESCO 10,000-year-old prehistoric rock art)",
            "Van Vihar National Park (Open zoo along the lake)",
            "Bharat Bhavan (Multi-arts complex & Tribal Museum)",
            "Shaukat Mahal & Gohar Mahal (Begum architecture)",
            "Bhojeshwar Temple at Bhojpur (Giant monolithic Shiva Lingam)"
        ],
        "famous_food": [
            "Bhopali Gosht Korma & Rizala",
            "Bhopali Poha Jalebi with Sev & Sulaimani Chai",
            "Chatori Gali Street Food (Nalli Nihari & Seekh Kebabs)",
            "Pawa / Biryani & Bhopali Paan",
            "Mawa Bati & Shahi Tukda",
            "Bhopali Keema Pav"
        ],
        "temples_spiritual": [
            "Taj-ul-Masajid (Crown of Mosques)",
            "Bhojpur Shiva Temple (World tallest monolithic Shivling 7.5 ft)",
            "Birla Mandir (Laxmi Narayan Temple with lake view)",
            "Gufa Mandir (Cave Temple)",
            "Moti Masjid"
        ],
        "heritage_sites": [
            "Sanchi Stupa (3rd Century BCE Buddhist monuments built by Emperor Ashoka)",
            "Bhimbetka Caves (Paleolithic and Mesolithic rock art)",
            "Gohar Mahal (Built by Qudsia Begum in 1820)",
            "Tribal Museum (Celebrated anthropological display)"
        ],
        "budget": {
            "budget": "₹1,000 – ₹1,500/day (Guesthouse + City transport + Street food)",
            "mid": "₹2,400 – ₹3,800/day (Lakeview hotel + Cabs to Sanchi/Bhimbetka)",
            "luxury": "₹6,000+/day (Jehan Numa Palace / Courtyard by Marriott)"
        },
        "best_time": "October to March (Cool, green post-monsoon weather and pleasant winters)",
        "specialties": "Bhopali Zardozi work, Batua purses, Chanderi sarees, Bell metal tribal crafts, Gond tribal art paintings."
    },
    "srinagar": {
        "name": "Srinagar",
        "state": "Jammu & Kashmir",
        "description": "Heaven on Earth, nestled in the Kashmir Valley along the Jhelum river and Dal Lake, famous for Houseboats, Shikaras, Mughal gardens, and snow-capped peaks.",
        "famous_places": [
            "Dal Lake & Nigeen Lake (Shikara ride & Floating Vegetable Market)",
            "Mughal Gardens (Shalimar Bagh, Nishat Bagh & Chashme Shahi)",
            "Indira Gandhi Memorial Tulip Garden (Asia largest tulip garden in spring)",
            "Shankaracharya Hilltop Temple",
            "Pari Mahal (Palace of Fairies with Dal Lake panorama)",
            "Hazratbal Shrine (White marble mosque by Dal Lake)",
            "Old City (Downtown Srinagar, Jamia Masjid & Wooden Bridges)",
            "Day trips to Gulmarg (Gondola cable car) & Pahalgam (Betaab Valley)"
        ],
        "famous_food": [
            "Authentic Kashmiri Wazwan (Rogan Josh, Rista, Gushtaba, Tabak Maaz)",
            "Kashmiri Kehwa with Saffron, Almonds & Cardamom",
            "Noon Chai (Pink Salted Tea) with Kashmiri Bakarkhani / Girda bread",
            "Dum Aloo & Kashmiri Haak Saag",
            "Nadru Yakhni (Lotus stem in creamy yogurt gravy)",
            "Modur Pulao (Sweet saffron rice with dry fruits)",
            "Tujji (Kashmiri street-style charcoal barbecue mutton kebabs)"
        ],
        "temples_spiritual": [
            "Shankaracharya Temple (9th-century temple dedicated to Lord Shiva on Gopadari Hill)",
            "Hazratbal Shrine (Houses holy relic Moi-e-Muqqadas)",
            "Jamia Masjid (Historic wooden Indo-Saracenic mosque with 378 Deodar pillars)",
            "Kheer Bhawani Temple (Tulmulla - sacred shrine of Goddess Ragnya)",
            "Khanqah-e-Moula (Historic wooden shrine on Jhelum river)"
        ],
        "heritage_sites": [
            "Hari Parbat Fort (Durrani Fort)",
            "Pari Mahal (Mughal observatory & astrological school built by Dara Shikoh)",
            "Shalimar Bagh (Built by Emperor Jahangir for Empress Nur Jahan in 1619)",
            "Zero Bridge & Historic Wooden Kadals of Srinagar"
        ],
        "budget": {
            "budget": "₹1,500 – ₹2,200/day (Guesthouse/homestay + Shared taxi + Kehwa & street food)",
            "mid": "₹3,500 – ₹5,500/day (Heritage Houseboat on Dal Lake + Shikara tours + Wazwan dinner)",
            "luxury": "₹9,000+/day (The Lalit Grand Palace / Vivanta Dal View + Private helicopter/cabs)"
        },
        "best_time": "March to October for lush greenery, tulips & pleasant weather; December to February for magical snowfall and skiing in Gulmarg",
        "specialties": "Pure Kashmiri Pashmina & Shahtoosh shawls, Kashmiri Saffron (Kesar), Walnuts, Paper-mâché art, Hand-knotted silk carpets, Walnut wood carvings."
    },
    "kochi": {
        "name": "Kochi (Cochin)",
        "state": "Kerala",
        "description": "The Queen of the Arabian Sea, historic port where Portuguese, Dutch, British, and Chinese maritime traditions blend with Kerala backwaters and spice trade.",
        "famous_places": [
            "Fort Kochi & Iconic Chinese Fishing Nets (Cheena Vala)",
            "Mattancherry Palace (Dutch Palace & Ramayana Murals)",
            "Paradesi Jewish Synagogue & Jew Town Antique Street",
            "St. Francis Church (Oldest European church in India)",
            "Marine Drive Kochi & Backwater Ferry Cruise",
            "Kerala Kathakali Centre (Traditional dance & martial arts)",
            "Lulu Mall (One of India largest shopping malls)",
            "Cherai Beach & Vypeen Island"
        ],
        "famous_food": [
            "Kerala Sadya on Banana Leaf (Avial, Sambar, Payasam, Thoran)",
            "Karimeen Pollichathu (Pearl spot fish baked in banana leaf)",
            "Kerala Puttu with Kadala Curry",
            "Appam with Creamy Vegetable or Chicken Stew",
            "Malabar Parotta with Beef/Mutton Roast",
            "Thattu Dosa & Pazham Pori (Crispy ripe banana fritters)",
            "Tender Coconut Ice Cream & Spiced Sulaimani Tea"
        ],
        "temples_spiritual": [
            "Chottanikkara Bhagavathy Temple (Renowned healing temple)",
            "Ernakulathappan Shiva Temple",
            "Paradesi Synagogue (1568 AD Jew Town)",
            "Santa Cruz Cathedral Basilica",
            "St. Francis Church (Where Vasco da Gama was originally buried)"
        ],
        "heritage_sites": [
            "Mattancherry Dutch Palace (Preserved mythological murals)",
            "Fort Emmanuel & Bastion Bungalow",
            "Hill Palace Museum (Tripunithura - Kerala largest archaeological palace)",
            "Bolgatty Palace (1744 Dutch palace on island)"
        ],
        "budget": {
            "budget": "₹1,100 – ₹1,700/day (Fort Kochi guesthouse + Ferry boats + Local cafes)",
            "mid": "₹2,800 – ₹4,500/day (Heritage colonial boutique stay + Kathakali show + Seafood)",
            "luxury": "₹7,000+/day (Brunton Boatyard / Grand Hyatt Kochi Bolgatty)"
        },
        "best_time": "October to March (Pleasant coastal breezes; ideal for backwater cruises and Biennale)",
        "specialties": "Kerala Spices (Cardamom, Black Pepper, Cinnamon, Cloves), Kasavu Gold Zari Sarees, Coir handicrafts, Coconut shell artefacts, Banana chips in coconut oil."
    },
    "goa": {
        "name": "Goa",
        "state": "Goa",
        "description": "India premier coastal paradise, celebrated for golden sandy beaches, Portuguese baroque churches, vibrant nightlife, water sports, and Goan-Portuguese fusion food.",
        "famous_places": [
            "Baga Beach, Calangute Beach & Anjuna Beach (North Goa)",
            "Palolem Beach, Colva Beach & Agonda Beach (South Goa peace)",
            "Basilica of Bom Jesus (UNESCO World Heritage with St. Francis Xavier mortal remains)",
            "Sé Cathedral (Largest church in Asia)",
            "Fort Aguada & Lighthouse (1612 Portuguese fort overlooking Arabian sea)",
            "Chapora Fort (Dil Chahta Hai sunset point)",
            "Dudhsagar Waterfalls (Spectacular 4-tiered 310m cascade)",
            "Fontainhas (Latin Quarter in Panaji with colourful Portuguese villas)"
        ],
        "famous_food": [
            "Goan Fish Curry Thali with Kingfish / Pomfret",
            "Pork / Chicken Vindaloo & Sorpotel",
            "Goan Pao with Ross Omelette",
            "Prawn Balchão & Crab Xec Xec",
            "Bebinca (Traditional 7-layered Goan coconut dessert)",
            "Feni (Traditional Cashew / Palm spirit)",
            "Sannas & Poi (Goan crusty bread)"
        ],
        "temples_spiritual": [
            "Basilica of Bom Jesus (Old Goa)",
            "Sé Cathedral & Church of Our Lady of the Immaculate Conception (Panaji)",
            "Shanta Durga Temple (Kavlem - Konkani Hindu architecture)",
            "Mangueshi Temple (Dedicated to Lord Shiva in Priol)",
            "Brahma Temple (Nagargao)"
        ],
        "heritage_sites": [
            "Fort Aguada & Sinquerim Fort",
            "Chapora Fort & Reis Magos Fort",
            "Fontainhas Latin Quarter (Preserved 18th-century Portuguese streetscapes)",
            "Bragança House & Menezes Bragança Pereira Mansion (Chandor)"
        ],
        "budget": {
            "budget": "₹1,200 – ₹1,900/day (Beach hostel + Scooter rental ₹300-400/day + Beach shacks)",
            "mid": "₹3,000 – ₹5,500/day (Boutique beach resort + Open jeep rental + Water sports)",
            "luxury": "₹8,500+/day (Taj Exotica / W Goa + Private yacht charter & fine dining)"
        },
        "best_time": "November to February (Perfect beach weather, festivals, Christmas & New Year celebrations)",
        "specialties": "Cashew nuts & Feni, Goan Port Wine, Spices from Sahakari Spice Farm, Azulejos ceramic painted tiles, Beach bohemian clothing."
    },
    "puri": {
        "name": "Puri",
        "state": "Odisha",
        "description": "One of the holy Char Dham pilgrimage sites, located on the Bay of Bengal, home to the supreme Lord Jagannath Temple, famous Golden Beach, and world-famous Rath Yatra.",
        "famous_places": [
            "Shree Jagannath Temple (Char Dham Mahaprabhu Temple)",
            "Golden Beach Puri (Blue Flag Certified Pristine Beach)",
            "Konark Sun Temple (UNESCO World Heritage Black Pagoda - 35km)",
            "Chilika Lake & Irrawaddy Dolphin Spotting (Satapada - 50km)",
            "Gundicha Temple (Garden house of Jagannath)",
            "Raghurajpur Heritage Craft Village (Pattachitra painting village)",
            "Swargadwar Beach & Sea Aquarium",
            "Narendra Pokhari (Sacred tank for Chandan Yatra)"
        ],
        "famous_food": [
            "Jagannath Temple Mahaprasad / Abadha (56 Bhog cooked in earthen pots)",
            "Puri Khaja (Crispy layered sweet delicacy from Lord offerings)",
            "Chhena Poda (Caramelized baked cottage cheese sweet)",
            "Rasabali & Chhena Gaja",
            "Dalma with Rice (Traditional lentil and vegetable dish)",
            "Fresh Bay of Bengal Fish Fry, Crab & Prawn Curry (Swargadwar)",
            "Pakhala Bhata (Fermented rice with fried fish and saag)"
        ],
        "temples_spiritual": [
            "Shree Jagannath Temple (12th-century Kalinga architectural miracle)",
            "Gundicha Temple",
            "Lokanatha Temple (Ancient Shiva temple where lingam stays underwater)",
            "Bedi Hanuman Temple & Alarnath Temple (Brahmagiri)",
            "Konark Sun Temple (Grand 13th-century chariot of Sun God)"
        ],
        "heritage_sites": [
            "Konark Sun Temple (UNESCO Architectural marvel with 24 carved stone wheels)",
            "Raghurajpur Crafts Village (Every resident is a Pattachitra master artisan)",
            "Jagannath Temple Meghnad Prachira (Massive outer boundary wall)"
        ],
        "budget": {
            "budget": "₹900 – ₹1,400/day (Dharamshala/Guesthouse near beach + Rickshaw + Temple Mahaprasad)",
            "mid": "₹2,200 – ₹3,800/day (Sea-facing resort on Marine Drive + Cab to Konark & Chilika)",
            "luxury": "₹5,500+/day (Mayfair Waves Puri / Hans Coco Palms)"
        },
        "best_time": "October to March (Pleasant ocean breeze; June-July for the world-famous Rath Yatra chariot festival)",
        "specialties": "Pattachitra cloth paintings, Palm leaf engravings, Sambalpuri and Ikkat handloom sarees, Pipili Applique craft, Puri Khaja boxes."
    },
    "rishikesh": {
        "name": "Rishikesh",
        "state": "Uttarakhand",
        "description": "The Yoga Capital of the World & Gateway to Garhwal Himalayas, nestled along the emerald Ganga with thrilling river rafting, iconic suspension bridges, and evening Ganga Aarti.",
        "famous_places": [
            "Ram Jhula & Laxman Jhula (Iconic suspension bridges across Ganga)",
            "Triveni Ghat (Grand Maha Ganga Aarti at dusk)",
            "Beatles Ashram (Chaurasi Kutia - Maharishi Mahesh Yogi Ashram)",
            "Neelkanth Mahadev Temple (Hilltop Shiva temple surrounded by valleys)",
            "Shivpuri (Famous starting point for White Water River Rafting)",
            "Parmarth Niketan & Geeta Bhawan",
            "Neer Garh & Patna Waterfalls",
            "Kunjapuri Devi Temple (Spectacular Himalayan sunrise viewpoint)"
        ],
        "famous_food": [
            "Ayurvedic Herbal Teas & Organic Vegan Smoothie Bowls",
            "Aloo Poori & Kachori with Jalebi (Chotiwala Restaurant since 1958)",
            "Garhwali Thali (Kafuli, Phaanu, Chainsoo, Jhangora Ki Kheer)",
            "Fresh Wood-fired Thin Crust Pizzas (Little Buddha Cafe / Freedom Cafe)",
            "Falafel Platters & Israeli Shakshuka (Tapovan cafes)",
            "Kulhad Masala Chai with Bun Maska on Ganga Ghats"
        ],
        "temples_spiritual": [
            "Triveni Ghat (Sacred confluence of Ganga, Yamuna & Saraswati)",
            "Neelkanth Mahadev Mandir (Where Lord Shiva consumed Halahala poison)",
            "Bharat Mandir (Oldest temple in Rishikesh established by Adi Shankaracharya)",
            "Parmarth Niketan Ashram & Veda Niketan",
            "Shatrughna & Lakshman Temples"
        ],
        "heritage_sites": [
            "Beatles Ashram / Chaurasi Kutia (Graffiti art & meditation domes from 1968)",
            "Ram Jhula & Janki Setu (Engineering marvels over Ganga)",
            "Old Geeta Press Book Depots & Heritage Ashrams"
        ],
        "budget": {
            "budget": "₹900 – ₹1,500/day (Hostels in Tapovan/Lakshman Jhula + Shared auto + Ashram food)",
            "mid": "₹2,500 – ₹4,200/day (Ganga riverview boutique stay + Rafting & Bungee pass + Cafes)",
            "luxury": "₹7,500+/day (Ananda in the Himalayas / Aloha on the Ganges + Luxury spa retreats)"
        },
        "best_time": "September to November & February to May (Ideal for rafting, trekking, camping, and yoga retreats)",
        "specialties": "Yoga & meditation teacher training certifications, Rudraksha beads, Crystal Sphatik malas, Garhwali handwoven woolen shawls, Organic Himalayan honey and essential oils."
    },
    "ayodhya": {
        "name": "Ayodhya",
        "state": "Uttar Pradesh",
        "description": "The sacred birthplace of Lord Rama (Ram Janmabhoomi), ancient spiritual epicenter on the banks of Saryu river, famous for grand temple architecture and Deepotsav festival.",
        "famous_places": [
            "Shri Ram Janmabhoomi Mandir (Grand Nagara-style Temple)",
            "Hanuman Garhi (Fortress-temple of Lord Hanuman on 76 steps)",
            "Kanak Bhawan (Palace gifted to Sita by Kaikeyi)",
            "Ram Ki Paidi & Saryu Riverfront (Evening Aarti & Laser Show)",
            "Nageshwarnath Temple (Built by Kush, son of Lord Rama)",
            "Gulab Bari & Mani Parbat",
            "Dashrath Mahal & Sita Ki Rasoi",
            "Surya Stambh Dharma Path"
        ],
        "famous_food": [
            "Ayodhya special Bedmi Poori & spicy Hing Aloo Sabzi",
            "Rabri Malpua & Desi Ghee Jalebi",
            "Ramdana Ladoo & Mawa Peda (Prasad)",
            "Samosa Chaat & Dahi Jalebi (Chowk area)",
            "Awadhi Vegetarian Thali & Kadhi Chawal",
            "Kulhad Chai with Makhan Toast"
        ],
        "temples_spiritual": [
            "Shri Ram Janmabhoomi Mandir",
            "Hanuman Garhi Mandir",
            "Kanak Bhawan (Sita-Ram Golden Palace)",
            "Nageshwarnath Mandir",
            "Treta Ke Thakur Mandir",
            "Chhoti Devkali & Badi Devkali Temple"
        ],
        "heritage_sites": [
            "Ram Ki Paidi Ghats along Holy Saryu",
            "Gulab Bari (Mausoleum of Nawab Shuja-ud-Daula with rose gardens)",
            "Mani Parbat (Historic Buddhist and Ramayana era mound)"
        ],
        "budget": {
            "budget": "₹800 – ₹1,300/day (Dharamshala/Ashram stay + E-rickshaw + Satvik food)",
            "mid": "₹2,000 – ₹3,500/day (Comfort hotel + Dedicated darshan cabs + Family dining)",
            "luxury": "₹5,000+/day (Boutique heritage stay / Park Inn by Radisson)"
        },
        "best_time": "October to March (Pleasant weather; Deepotsav during Diwali with millions of diyas is world-record spectacular)",
        "specialties": "Ram Darbar idols, Tulsi malas, Brass puja articles, Saryu Jal containers, Khadau wooden footwear."
    },
    "ahmedabad": {
        "name": "Ahmedabad",
        "state": "Gujarat",
        "description": "India first UNESCO World Heritage City, Manchester of the East, home to Sabarmati Ashram, intricate stepwells, exquisite Gujarati Thali, and vibrant Navratri Garba.",
        "famous_places": [
            "Sabarmati Ashram (Mahatma Gandhi’s Hriday Kunj)",
            "Adalaj Stepwell (5-storey intricate 15th-century stepwell)",
            "Atal Pedestrian Bridge & Sabarmati Riverfront",
            "Sidi Saiyyed Mosque (World-famous Tree of Life stone jali)",
            "Hutheesing Jain Temple (Carved white marble)",
            "Akshardham Temple (Gandhinagar - 25km)",
            "Manek Chowk (Jewellery market turning into bustling midnight street food)",
            "Science City & Auto World Vintage Car Museum"
        ],
        "famous_food": [
            "Unlimited Gujarati Thali (Agashiye / Toran / Sasumaa)",
            "Khamman Dhokla, Khandvi & Fafda Jalebi (Das Khaman / Chandravilas)",
            "Manek Chowk Midnight Snacks (Gwalior Dosa, Chocolate Sandwich, Kulfi)",
            "Sev Khamani, Dabeli & Locho",
            "Undhiyu with Puri & Shrikhand (Winter festival specialty)",
            "Dalvada & Handvo",
            "Ghughra & Mohanthal Sweet"
        ],
        "temples_spiritual": [
            "Hutheesing Jain Temple (Dedicated to 15th Tirthankara Lord Dharmanatha)",
            "Akshardham Gandhinagar (Grand pink sandstone temple complex)",
            "Sidi Saiyyed Mosque & Jama Masjid Ahmedabad",
            "Bhadra Kali Temple (Inside historic Bhadra Fort)",
            "ISCKON Temple (SG Highway)"
        ],
        "heritage_sites": [
            "Adalaj Stepwell (Indo-Islamic architectural stepwell masterpiece)",
            "Sabarmati Ashram (Epicenter of India freedom struggle & Dandi March)",
            "Sidi Saiyyed Mosque (Intricate marble filigree window work)",
            "Pols of Old Ahmedabad (UNESCO preserved wooden architecture neighborhood)"
        ],
        "budget": {
            "budget": "₹1,000 – ₹1,600/day (Budget stay + BRTS / Metro + Fafda-Dhokla breakfast)",
            "mid": "₹2,600 – ₹4,200/day (Heritage haveli stay in Pols + Cabs + Thali feasts)",
            "luxury": "₹6,500+/day (The House of MG / ITC Narmada + Fine Gujarati royal dining)"
        },
        "best_time": "October to March (Warm pleasant days; October for World Longest Dance Festival - Navratri Garba; January for International Kite Festival)",
        "specialties": "Patola silk sarees, Bandhani tie-dye dupattas, Gujarati mirror-work embroidery, Khadi fabrics from Sabarmati Ashram, Namkeens and Farsan."
    },
    "pune": {
        "name": "Pune",
        "state": "Maharashtra",
        "description": "Oxford of the East & Cultural capital of Maharashtra, city of Peshwas, historical Maratha forts, educational institutions, IT parks, and Misal culture.",
        "famous_places": [
            "Shaniwar Wada (18th-century Peshwa fortified palace)",
            "Aga Khan Palace (Historic memorial where Mahatma Gandhi was interned)",
            "Sinhagad Fort (Hilltop fortress of Tanaji Malusare bravery)",
            "Dagdusheth Halwai Ganpati Temple",
            "Osho International Meditation Resort (Koregaon Park)",
            "Raja Dinkar Kelkar Museum (3-storey traditional artifact collection)",
            "Parvati Hill (Hilltop temples and Peshwa museum)",
            "Lonavala & Khandala (Scenic Western Ghats 60km away)"
        ],
        "famous_food": [
            "Puneri Misal Pav (Kata Kirr / Bedekar Tea Stall)",
            "Bakharwadi & Mango Barfi (Chitale Bandhu Mithaiwale)",
            "Puneri Poha & Sabudana Vada",
            "Mastani Drink (Thick flavoured ice-cream milkshake from Sujata Mastani)",
            "Pithla Bhakri & Thecha (At Sinhagad Fort summit)",
            "Bun Maska & Irani Chai (Goodluck Cafe, FC Road)",
            "Kayani Bakery Shrewsbury Biscuits (Camp area)"
        ],
        "temples_spiritual": [
            "Shrimant Dagdusheth Halwai Ganpati Temple",
            "Parvati Temple Complex (Oldest heritage structures in Pune)",
            "Chaturshringi Temple (Senapati Bapat Road hillock)",
            "Trishundha Ganpati Temple (Somwar Peth)",
            "Alandi (Sant Dnyaneshwar Samadhi - 20km)"
        ],
        "heritage_sites": [
            "Shaniwar Wada (Seat of Peshwa rulers of Maratha Empire)",
            "Aga Khan Palace (Italian arches and spacious lawns where Kasturba Gandhi passed away)",
            "Sinhagad Fort (Historical Maratha battle fortress)",
            "Vishrambaug Wada (Peshwa Bajirao II mansion with teak pillars)"
        ],
        "budget": {
            "budget": "₹1,100 – ₹1,600/day (Hostel/Guesthouse + PMPML Bus/Auto + Misal & Street food)",
            "mid": "₹2,500 – ₹4,200/day (3-star hotel + Cab hire + FC Road / KP dining)",
            "luxury": "₹6,000+/day (JW Marriott Pune / Conrad Pune + Luxury Western Ghats tours)"
        },
        "best_time": "July to February (Monsoons make Western Ghats lush green with waterfalls; winters are crisp and cool)",
        "specialties": "Chitale Bakharwadi, Shrewsbury Biscuits, Paithani Silk Sarees, Maharashtrian Kolhapuri Chappals, Brassware from Tambat Ali."
    },
    "darjeeling": {
        "name": "Darjeeling",
        "state": "West Bengal",
        "description": "The Queen of the Hills in the Eastern Himalayas, world-renowned for Champagne of Teas, Toy Train (UNESCO World Heritage), and breathtaking views of Mount Kanchenjunga.",
        "famous_places": [
            "Tiger Hill (Famous sunrise view illuminating Kanchenjunga golden peaks)",
            "Darjeeling Himalayan Railway Toy Train (UNESCO World Heritage joyride to Ghoom)",
            "Batasia Loop & Gorkha War Memorial",
            "Happy Valley Tea Estate (Lush green tea gardens & factory tour)",
            "Padmaja Naidu Himalayan Zoological Park (Red Pandas & Snow Leopards)",
            "Himalayan Mountaineering Institute (HMI & Tenzing Norgay Memorial)",
            "Peace Pagoda & Japanese Buddhist Temple",
            "Mall Road & Chowrasta (Promenade with mountain views)"
        ],
        "famous_food": [
            "Authentic Steamed Momos with fiery red chili Dalle Khursani chutney",
            "Darjeeling First Flush & Second Flush Organic Tea (Nathmulls / Glenary)",
            "Thukpa & Tibetan Gyathuk Noodle Soups",
            "Glenary Bakery Cakes, Apple Pies & Roast Chicken",
            "Shaphalay (Tibetan deep-fried meat or veg pastry)",
            "Traditional Nepali Thali (Gundruk, Churpi chutney, Sel Roti)",
            "Keventers English Breakfast with rooftop Himalayan vista"
        ],
        "temples_spiritual": [
            "Japanese Peace Pagoda (Nipponzan Myohoji)",
            "Ghoom Monastery (Samten Choling & Yiga Choeling)",
            "Mahakal Temple (Observatory Hill sacred to both Hindus & Buddhists)",
            "Bhutia Busty Monastery",
            "Dali Monastery (Drukpa Kagyud Order)"
        ],
        "heritage_sites": [
            "Darjeeling Himalayan Railway (1881 2-ft narrow gauge steam toy train)",
            "Glenary Bakery & Restaurant (Colonial restaurant running over 100 years)",
            "Windamere Hotel (Historic colonial British Raj heritage stay)",
            "St. Andrew Church (1843 historic Anglican church)"
        ],
        "budget": {
            "budget": "₹1,300 – ₹1,800/day (Mall Road homestay + Shared jeeps + Momos & Thukpa)",
            "mid": "₹2,800 – ₹4,800/day (Mountain view hotel + Private sightseeing jeep + Glenary dining)",
            "luxury": "₹7,500+/day (Mayfair Darjeeling / Glenburn Tea Estate + Private tea tasting tours)"
        },
        "best_time": "March to May (Spring blooms with Rhododendrons) and October to December (Crystal-clear views of Kanchenjunga peaks)",
        "specialties": "Darjeeling Tea (First Flush / Muscatel), Tibetan prayer flags, Hand-knitted Himalayan woolens, Hand-carved wooden masks, Dalle Khursani pickles."
    }
}

def get_city_knowledge(query: str) -> Optional[Dict[str, Any]]:
    """Finds matching city entry from query string."""
    q = query.lower()
    for key, data in INDIAN_CITIES_KB.items():
        if key in q or data["name"].lower() in q:
            return data
        # Handle aliases
        if key == "bengaluru" and "bangalore" in q:
            return data
        if key == "varanasi" and any(alias in q for alias in ["banaras", "benares", "kashi"]):
            return data
        if key == "patna" and "pataliputra" in q:
            return data
        if key == "kochi" and "cochin" in q:
            return data
        if key == "ayodhya" and "saket" in q:
            return data
        if key == "amritsar" and "golden temple" in q:
            return data
    return None

def format_city_guide(city_data: Dict[str, Any], hindi: bool = False, specific_type: Optional[str] = None) -> str:
    """Formats a city into an authentic, highly detailed response matching user preference."""
    name = city_data["name"]
    state = city_data["state"]
    desc = city_data["description"]
    nl = chr(10)
    places_str = nl.join(["   • " + str(p) for p in city_data["famous_places"]])
    food_str = nl.join(["   • " + str(f) for f in city_data["famous_food"]])
    temples_str = nl.join(["   • " + str(t) for t in city_data["temples_spiritual"]])
    heritage_str = nl.join(["   • " + str(h) for h in city_data["heritage_sites"]])
    budget_dict = city_data["budget"]
    b_low = budget_dict.get("budget", "₹1,000 – ₹1,500/day")
    b_mid = budget_dict.get("mid", "₹2,500 – ₹4,000/day")
    b_lux = budget_dict.get("luxury", "₹6,000+/day")
    best_time = city_data["best_time"]
    specialties = city_data["specialties"]

    if specific_type == "food":
        if hindi:
            return (
                f"🍛 **{name} ({state}) ke Prasiddh Vyanjan & Food Guide**\n\n"
                f"{name} ka swaad aur khana behad anokha aur prasiddh hai:\n\n"
                f"{food_str}\n\n"
                f"🛍️ **Khareedari & Souvenirs**: {specialties}\n\n"
                f"Kya aapko {name} ke specific restaurants ya food streets ke baare me jaanna hai?"
            )
        else:
            return (
                f"🍛 **{name} ({state}) Famous Food & Culinary Delights**\n\n"
                f"{name} is renowned for its iconic traditional cuisines and vibrant street food culture:\n\n"
                f"{food_str}\n\n"
                f"🛍️ **Local Specialties & Gifts**: {specialties}\n\n"
                f"Would you like recommendations for the best iconic eateries or food streets in {name}?"
            )

    if specific_type == "places":
        if hindi:
            return (
                f"🏛️ **{name} ({state}) ke Pramukh Paryatan Sthal**\n\n"
                f"{desc}\n\n"
                f"**Top Attractions & Famous Places:**\n{places_str}\n\n"
                f"🏰 **Dharohar & Historical Sites:**\n{heritage_str}\n\n"
                f"🗓️ **Ghoomne Ka Sabse Accha Samay**: {best_time}\n\n"
                f"Kya aapko {name} ka day-wise complete travel plan chahiye?"
            )
        else:
            return (
                f"🏛️ **Top Attractions & Sightseeing in {name} ({state})**\n\n"
                f"{desc}\n\n"
                f"**Must-Visit Attractions:**\n{places_str}\n\n"
                f"🏰 **Heritage & Historic Landmarks:**\n{heritage_str}\n\n"
                f"🗓️ **Best Time to Visit**: {best_time}\n\n"
                f"Would you like a day-by-day customized itinerary for {name}?"
            )

    # Complete Travel & Famous Things Guide
    if hindi:
        return (
            f"🌟 **{name} ({state}) – Sampoorna Travel & Heritage Guide**\n\n"
            f"{desc}\n\n"
            f"1. 🏛️ **Prasiddh Sthal & Attractions (Famous Places)**:\n{places_str}\n\n"
            f"2. 🍛 **Prasiddh Khana & Swaad (Famous Food)**:\n{food_str}\n\n"
            f"3. 🛕 **Mandir, Gurudwara & Dharmik Sthal (Spiritual Sites)**:\n{temples_str}\n\n"
            f"4. 🏰 **Aitihasik Dharohar (Heritage & History)**:\n{heritage_str}\n\n"
            f"5. 💰 **Per-Day Anumanit Budget (Per Person)**:\n"
            f"   • **Budget**: {b_low}\n"
            f"   • **Mid-Range**: {b_mid}\n"
            f"   • **Luxury**: {b_lux}\n\n"
            f"6. 🗓️ **Ghoomne Ka Sabse Accha Samay (Best Time to Visit)**: {best_time}\n"
            f"7. 🛍️ **Prasiddh Handicrafts & Shopping**: {specialties}\n\n"
            f"Aapko {name} ke hotels, cab booking ya day-wise itinerary me madad chahiye toh batayein!"
        )
    else:
        return (
            f"🌟 **{name} ({state}) – Complete Travel & Heritage Guide**\n\n"
            f"{desc}\n\n"
            f"1. 🏛️ **Famous Places & Must-Visit Attractions**:\n{places_str}\n\n"
            f"2. 🍛 **Famous Food & Iconic Cuisines**:\n{food_str}\n\n"
            f"3. 🛕 **Temples & Spiritual Sanctuaries**:\n{temples_str}\n\n"
            f"4. 🏰 **Historic & Heritage Landmarks**:\n{heritage_str}\n\n"
            f"5. 💰 **Estimated Per-Day Budget Breakdown**:\n"
            f"   • **Budget Traveller**: {b_low}\n"
            f"   • **Mid-Range Traveller**: {b_mid}\n"
            f"   • **Luxury Traveller**: {b_lux}\n\n"
            f"6. 🗓️ **Best Season / Time to Visit**: {best_time}\n"
            f"7. 🛍️ **Local Specialties & Handlooms**: {specialties}\n\n"
            f"Let me know if you would like a tailored day-wise itinerary, hotel suggestions, or route guidance for {name}!"
        )
