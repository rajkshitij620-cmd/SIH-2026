"""Comprehensive Indian Cities Knowledge Base for TourMitra AI Assistant.
Provides authoritative, dedicated data for Indian destinations across all aspects:
Food, Places, Temples & Heritage, Budgets, and Best Time to Visit.
"""
from typing import Optional, Dict, Any

INDIAN_CITIES_KB: Dict[str, Dict[str, Any]] = {
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
            "Science City & Eco Park (Rajarhat)",
            "Alipore Zoo & National Library"
        ],
        "famous_food": [
            "Kolkata Biryani with Aloo & Boiled Egg (Arsalan / Shiraz / Royal Indian Hotel)",
            "Kolkata Kathi Rolls (Nizam origin at New Market / Kusum Rolls)",
            "Kolkata Phuchka (Spicy potato & tangy tamarind water at Vivekananda Park)",
            "Iconic Bengali Sweets: Spongy Rasgulla (K.C. Das), Sandesh (Balaram Mullick), and Mishti Doi",
            "Traditional Bengali Cuisine: Kosha Mangsho with hot Luchi, Ilish Macher Jhol, Chingri Malai Curry",
            "Park Street Heritage: Peter Cat Chelo Kebab & Flurys English Breakfast / Pastries",
            "Popular Street Snacks: Jhalmuri, Churmur, Telebhaja, and Singara"
        ],
        "temples_spiritual": [
            "Dakshineswar Kali Temple (Bhavatarini Kali & Sri Ramakrishna room)",
            "Kalighat Kali Temple (One of the 51 Shaktipeeths)",
            "Belur Math (World headquarters of Ramakrishna Math & Mission)",
            "St. Paul Cathedral & St. John Church",
            "Nakhoda Mosque (Chitpur)",
            "Pareshnath Jain Temple (Shitalnath Mandir)"
        ],
        "heritage_sites": [
            "Victoria Memorial Hall (White Makrana marble masterpiece)",
            "Marble Palace (1835 neoclassical mansion & Victorian art)",
            "Jorasanko Thakur Bari (Ancestral mansion of Rabindranath Tagore)",
            "Writers Building, Raj Bhavan & General Post Office (GPO)"
        ],
        "budget": {
            "budget": "₹1,000 – ₹1,500/day (Sudder street budget stays + Tram/Metro + Phuchka/Rolls)",
            "mid": "₹2,500 – ₹4,000/day (Heritage homestay/Hotel + Yellow taxi/Uber + Park Street dining)",
            "luxury": "₹6,000+/day (The Oberoi Grand / ITC Royal Bengal + Fine dining)"
        },
        "best_time": "October to March (Durga Puja festival in Autumn, winter book fairs & soothing pleasant weather)",
        "specialties": "Tant & Jamdani cotton sarees, Terracotta handicrafts, Dokra brass art, Darjeeling tea, Nolen Gur Sandesh."
    },
    "patna": {
        "name": "Patna",
        "state": "Bihar",
        "description": "Ancient historic capital on the banks of Ganga (historic Pataliputra), world-famous for sacred Sikh heritage, Mauryan history, museums, and rich culture.",
        "famous_places": [
            "Golghar (Historic granary with panoramic Ganga view)",
            "Takht Sri Patna Sahib (Birthplace of Guru Gobind Singh Ji)",
            "Bihar Museum & Patna Museum (World-class art & Didarganj Yakshi statue)",
            "Buddha Smriti Park & Karuna Stupa",
            "Mahavir Mandir (One of the holiest Hanuman shrines)",
            "Kumhrar (Ancient Mauryan 80-pillared hall archaeological excavations)",
            "Sabhyata Dwar & Marine Drive Ganga Riverfront promenade"
        ],
        "famous_food": [
            "Litti Chokha roasted with Desi Ghee & Baingan Bharta (Maurya Lok / Station road)",
            "Silao Khaja & Chandrakala (Crispy multi-layered sweet)",
            "Gaya Tilkut, Anarsa & Balushahi",
            "Dal Pitha (Traditional steamed rice dumplings filled with spiced lentils)",
            "Sattu Sharbat (Refreshing roasted gram flour drink) & Kachori Jalebi",
            "Champaran Handi Mutton & Bihari Kebab",
            "Chana Ghugni with Poha / Murhi"
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
            "Tunday Kababi Galawati Kebabs with Roomali Roti (Aminabad & Chowk)",
            "Awadhi Mutton Dum Biryani, Kakori Kebabs & Boti Kebab",
            "Prakash ki Kulfi (Aminabad falooda kulfi)",
            "Makhan Malai / Nimish (Winter morning saffron froth dessert)",
            "Royal Cafe Basket Chaat (Tokri Chaat, Hazratganj)",
            "Sheermal & Mughlai Kulcha Nihari (Rahim in Chowk)",
            "Malai Paan, Raja Thandai & Kashmiri Chai"
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
            "Old Delhi Chhole Bhature (Sita Ram Diwan Chand / Chache Di Hatti)",
            "Paranthe Wali Gali (Stuffed crispy parathas in Chandni Chowk)",
            "Karim & Al Jawahar Mutton Korma, Nihari and Seekh Kebabs (Jama Masjid)",
            "Butter Chicken & Dal Makhani (Moti Mahal origin in Daryaganj)",
            "Dahi Bhalla & Aloo Tikki (Natraj & Bittoo Tikki Wala)",
            "Kuremal Mohan Lal Kulfi (Stuffed real-fruit kulfi in Chawri Bazaar)",
            "Momos, Thukpa & Laphing (Majnu Ka Tilla Tibetan Colony)"
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
            "Vada Pav & Pav Bhaji (Ashok Vada Pav, Sardar Pav Bhaji, Cannon)",
            "Misal Pav & Kanda Poha (Aaswad / Prakash Shakahari)",
            "Bombay Duck (Bombil Fry) & Malvani Coastal Seafood (Gajalee / Mahesh Lunch Home)",
            "Bun Maska & Irani Chai (Kyani & Co. / Britannia & Co. / Cafe Mondegar)",
            "Bhel Puri & Sev Puri (Girgaon Chowpatty & Juhu Beach)",
            "Frankie & Falooda (Badshah at Crawford Market)",
            "Parsi Berry Pulao & Dhansak"
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
            "Banarasi Paan (Maghai & Meetha Paan at Keshav Tambool)",
            "Kachori Sabzi & Jalebi (Morning at Ram Bhandar / Chachi ki Kachori)",
            "Banarasi Tamatar Chaat & Palak Chaat (Kashi Chaat Bhandar)",
            "Malaiyo / Makhan Malai (Winter saffron froth sweet served in kulhads)",
            "Blue Lassi / Pehalwan Lassi (Thick lassi with fresh fruit toppings)",
            "Baati Chokha & Chena Dahi Vada",
            "Laal Peda, Rabri Jalebi & Thandai with Kesar"
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
            "Dal Baati Churma with Pure Desi Ghee & Garlic Chutney (LMB / 1135 AD)",
            "Pyaaz Kachori & Mawa Kachori (Rawat Mishthan Bhandar)",
            "Ghevar (Malai / Mawa Ghevar from LMB Johari Bazaar)",
            "Laal Maas (Royal spicy Rajasthani mutton curry with mathania chillies)",
            "Ker Sangri & Gatte ki Sabzi",
            "Lassi at Lassiwala (MI Road since 1944 in earthen kulhad)",
            "Mirchi Vada & Gulab Sakri"
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
            "Agra ka Petha: Angoori, Kesar, Paan, Chocolate & Gulab Petha (Panchhi Petha)",
            "Bedmi Puri with spicy Aloo Sabzi & crispy Jalebi (Deviram Sweets)",
            "Mughlai Biryani, Chicken Tikka & Seekh Kebabs (Pinch of Spice)",
            "Dalmoth (Spicy crispy lentil and cashew namkeen)",
            "Bhalla Chaat (Agra special potato patty chaat at Sadar Bazaar)",
            "Tandoori Mughlai Kulcha & Shawarma"
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
            "Goan Fish Curry Thali with Kingfish / Pomfret (Fisherman Wharf / Ritz Classic)",
            "Pork / Chicken Vindaloo & Sorpotel with Sannas",
            "Goan Pao with Ross Omelette (Street carts in Panaji / Margao)",
            "Prawn Balchão, Crab Xec Xec & Butter Garlic Calamari",
            "Bebinca (Traditional 7-layered Goan coconut milk dessert)",
            "Feni (Traditional Cashew & Palm spirit) & Port Wine",
            "Goan Poi bread with Chorizo sausage"
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
    "manali": {
        "name": "Manali",
        "state": "Himachal Pradesh",
        "description": "High-altitude Himalayan valley with pine forests, snowy passes, waterfalls, and adventure sports.",
        "famous_places": [
            "Solang Valley (Skiing, Zorbing, Paragliding)",
            "Rohtang Pass & Atal Tunnel (Snow points)",
            "Hadimba Devi Temple (Ancient cedar forest temple)",
            "Jogini Waterfall & Vashisht Hot Springs",
            "Old Manali Village & Manu Temple",
            "Mall Road & Van Vihar"
        ],
        "famous_food": [
            "Himachali Dham (Traditional festive meal: Madra, Chana Khatta, Babru)",
            "Fresh Himalayan Rainbow Trout Fish (Pan-fried with lemon butter)",
            "Siddu with Desi Ghee (Himachali steamed wheat bread with walnut stuffing)",
            "Wood-fired Thin Crust Pizzas & Pasta (Cafe 1947 / Lazy Dog in Old Manali)",
            "Tibetan Thukpa, Momos & Thenthuk",
            "Apple Cider, Fresh Apple Pies & Rhododendron Juice"
        ],
        "temples_spiritual": [
            "Hadimba Devi Temple (1553 AD pagoda-style wooden temple)",
            "Vashisht Temple & Natural Sulphur Hot Springs",
            "Manu Temple (Old Manali - only temple dedicated to Sage Manu in India)",
            "Gadhan Thekchhokling Gompa (Tibetan Buddhist Monastery)"
        ],
        "heritage_sites": [
            "Naggar Castle (Wood & stone medieval palace of Kullu Rajas - 20km)",
            "Museum of Himachal Culture and Folk Art",
            "Roerich Art Gallery (Naggar)"
        ],
        "budget": {
            "budget": "₹1,200 – ₹1,800/day (Old Manali hostel/homestay + Local bus + Siddu & Thukpa)",
            "mid": "₹2,800 – ₹4,800/day (Mountain view resort + Private cab to Rohtang/Solang + Cafes)",
            "luxury": "₹7,000+/day (The Himalayan Resort / Span Resort + Luxury mountain spa)"
        },
        "best_time": "October to June (March-June for pleasant summer; Dec-Feb for snowfall & winter sports)",
        "specialties": "Kullu Woolen Shawls & Caps, Himachali Apple & Pear jams, Apricot oil, Hand-knitted socks, Pine nuts (Chilgoza)."
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
            "Rasabali, Chhena Gaja & Khira Gaja",
            "Dalma with Rice (Traditional Odia lentil and vegetable dish)",
            "Fresh Bay of Bengal Fish Fry, Crab & Prawn Curry (Swargadwar stalls)",
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
    "gangtok": {
        "name": "Gangtok",
        "state": "Sikkim",
        "description": "Clean mountain city with sweeping Kanchenjunga views, Buddhist monasteries, and alpine lakes.",
        "famous_places": [
            "MG Marg (Clean pedestrian promenade with cafes)",
            "Tsomgo Lake (Changu Lake at 12,310 ft) & Baba Mandir",
            "Nathula Pass (Indo-China Border on Old Silk Route)",
            "Rumtek Monastery (Dharma Chakra Centre)",
            "Banjhakri Falls & Energy Park",
            "Tashi Viewpoint & Ganesh Tok (Kanchenjunga panoramas)",
            "Namgyal Institute of Tibetology & Do Drul Chorten"
        ],
        "famous_food": [
            "Authentic Steamed Sikkimese Momos with spicy Dalle Khursani chili sauce",
            "Thukpa & Gyathuk (Tibetan warm noodle broth soups)",
            "Phagshapa (Pork belly stew with radishes and dried chillies)",
            "Sha Phaley (Crispy deep-fried bread stuffed with seasoned meat or cabbage)",
            "Chhurpi Soup & Chhurpi Ningro Curry (Wild fern with yak cheese)",
            "Sel Roti with Aloo Dum (Traditional festival ring-shaped bread)",
            "Tongba (Traditional warm fermented millet drink served in bamboo cup)"
        ],
        "temples_spiritual": [
            "Rumtek Monastery (Largest monastery in Sikkim)",
            "Enchey Monastery (200-year-old Nyingma order shrine)",
            "Do Drul Chorten Stupa (108 prayer wheels)",
            "Lingdum Monastery (Ranka)",
            "Hanuman Tok (Hilltop temple managed by Indian Army)"
        ],
        "heritage_sites": [
            "Namgyal Institute of Tibetology (Rare Mahayana Buddhist relics & manuscripts)",
            "Old Silk Route passes",
            "Ganesh Tok & Tashi Viewpoint historical viewpoints"
        ],
        "budget": {
            "budget": "₹1,300 – ₹1,900/day (MG Marg homestay + Shared sumo jeeps + Momos & Thukpa)",
            "mid": "₹3,000 – ₹5,000/day (Mountain view hotel + Reserved cab to Tsomgo/Nathula)",
            "luxury": "₹7,500+/day (Mayfair Spa Resort / Elgin Nor-Khill)"
        },
        "best_time": "March to June (Blooming Rhododendrons & pleasant weather) and September to December (Crystal-clear views of Himalayan snow peaks)",
        "specialties": "Sikkim Temi Tea, Tibetan Hand-knotted Carpets, Choktse carved wooden tables, Dalle Khursani pickles, Prayer wheels."
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
    },
    "bishnupur": {
        "name": "Bishnupur",
        "state": "West Bengal",
        "description": "Terracotta temples, Baluchari weaving, Malla royal history, and quiet Bengal cultural heritage.",
        "famous_places": [
            "Rasmancha (Oldest terracotta brick structure in Bengal - 1600 AD)",
            "Jor Bangla Temple (Twin hut terracotta temple)",
            "Shyamrai Temple (Pancharatna temple with Krishna murals)",
            "Madan Mohan Temple & Dalmadal Kaman Cannon",
            "Baluchari Silk Weaving Studios",
            "Acharya Jogesh Chandra Purakriti Bhawan (Archaeological Museum)"
        ],
        "famous_food": [
            "Bishnupur Posto Bora (Fried poppy seed patties)",
            "Authentic Bengal Thali with Shorshe Ilish, Katla Kalia & Chholar Dal",
            "Mecha Sandesh & Motichoor Ladoo (Heritage sweets of Bishnupur)",
            "Langcha, Pantua & Rosogolla",
            "Khichuri Bhog at Madan Mohan Temple"
        ],
        "temples_spiritual": [
            "Rasmancha (Unique pyramidal terracotta stage)",
            "Shyamrai Temple (Exquisite Raslila terracotta carvings)",
            "Jor Bangla Temple (Keshta Raya)",
            "Madan Mohan Temple (Active living temple)",
            "Radha Shyam Temple"
        ],
        "heritage_sites": [
            "Malla Dynasty Fort ruins & Stone Gates (Garh Darwaza)",
            "Dalmadal Cannon (Historic royal royal iron cannon)",
            "Gumgarh & Lalbandh lakes"
        ],
        "budget": {
            "budget": "₹900 – ₹1,300/day (Heritage lodge/homestay + Cycle-rickshaw + Bengali thali)",
            "mid": "₹2,000 – ₹3,200/day (Tourist lodge + Private auto tour + Baluchari shopping)",
            "luxury": "₹4,500+/day (Bishnupur Heritage Resort + Guided artisan tours)"
        },
        "best_time": "October to February (Pleasant winter months; Bishnupur Mela festival in December)",
        "specialties": "Baluchari & Swarnachari pure silk sarees (depicting Mahabharata motifs), Terracotta horse figurines (Bankura Horse), Dokra metal art, Dashavatar playing cards (Ganjifa)."
    },
    "shantiniketan": {
        "name": "Shantiniketan (Bolpur)",
        "state": "West Bengal",
        "description": "A calm cultural town shaped by Nobel laureate Rabindranath Tagore, red soil, Baul music, open-air learning, and artisanal crafts.",
        "famous_places": [
            "Visva-Bharati University Campus & Prayer Hall (Upasana Griha made of Belgian glass)",
            "Rabindra Bhavana (Tagore Museum & Uttarayan Complex)",
            "Khoai Sonajhuri Forest & Saturday Haat (Handicraft Fair)",
            "Amar Kutir (Craft Society & Leather Work)",
            "Kala Bhavana (Murals by Nandalal Bose & Ramkinkar Baij)",
            "Kankalitala Temple (51 Shaktipeeth on Kopai river)",
            "Prakriti Bhavan (Nature Art Museum)"
        ],
        "famous_food": [
            "Shantiniketan Traditional Bengali Thali: Bhaat, Shukto, Posto, Macher Jhol, Payesh",
            "Seasonal Kancha Aam / Tomato Chutney with Papad",
            "Poush Mela Special Pithe-Puli, Patishapta & Gokul Pithe (Winter date palm jaggery sweets)",
            "Baul Tea Stalls: Kulhad Chai with Ginger and biscuits in Sonajhuri forest",
            "Chanar Jilipi & Pantua from Bolpur sweet shops"
        ],
        "temples_spiritual": [
            "Upasana Griha (Glass Mandir for silent meditation)",
            "Kankalitala Temple (One of 51 Shaktipeeths on Kopai River)",
            "Chhatimtala (Meditation spot of Maharshi Debendranath Tagore)"
        ],
        "heritage_sites": [
            "Uttarayan Complex: Udayan, Konarka, Shyamali, Punascha, and Udichi (Tagore residences)",
            "Kala Bhavana & Sangeet Bhavana heritage art pavilions",
            "Santiniketan Griha (Oldest building 1863)"
        ],
        "budget": {
            "budget": "₹1,000 – ₹1,500/day (Homestay/Guest house near Khoai + E-rickshaw + Local canteen)",
            "mid": "₹2,400 – ₹3,800/day (Boutique eco-resort + Cab + Heritage dining)",
            "luxury": "₹5,500+/day (Mark & Meadows / Mohor Kutir Resort)"
        },
        "best_time": "November to March (Poush Mela in late December, Basanta Utsav during Holi, and pleasant winter days)",
        "specialties": "Kantha stitch sarees and kurtas, Shantiniketan embossed leather bags & wallets, Batik print textiles, Ektara musical instruments, Dokra jewellery."
    },
    "sundarbans": {
        "name": "Sundarbans",
        "state": "West Bengal",
        "description": "The world largest mangrove forest and delta, UNESCO World Heritage Site, home to the Royal Bengal Tiger, estuarine crocodiles, and peaceful village waterways.",
        "famous_places": [
            "Sajnekhali Watch Tower & Mangrove Interpretation Centre",
            "Dobanki Watch Tower & Canopy Walk (Half-km elevated walkway)",
            "Sudhanyakhali Watch Tower (Sweet water pond for tiger/deer spotting)",
            "Pakhiralay & Godkhali Boat Ghats",
            "Netidhopani Watch Tower (400-year-old temple ruins)",
            "Jharkhali Tiger Rescue Centre & Butterfly Garden",
            "Burir Dabri Watch Tower & Mudwalk"
        ],
        "famous_food": [
            "Fresh Village Mangrove Fish: Parshe, Bhetki, Pabda & Chingri (Prawn) Curry",
            "Sundarbans Pure Raw Wild Mangrove Honey (Moule Honey)",
            "Desi Kankra (Fresh Mud Crab Roast / Curry)",
            "Steamed Rice with Shorshe Ilish & Moong Dal",
            "Traditional Bengali sweets & Nolen Gur Sandesh served on boat tours"
        ],
        "temples_spiritual": [
            "Bonbibi Temples & Shrines (Guardian deity of Sundarbans forests worshipped by all communities)",
            "Netidhopani Temple Ruins (Mythological Behula-Lakhinder site)",
            "Kapilmuni Ashram (Gangasagar - 70km)"
        ],
        "heritage_sites": [
            "UNESCO World Heritage Sundarbans Biosphere Reserve",
            "Sajnekhali Bird Sanctuary & Crocodile Breeding Centre",
            "Traditional Mangrove Wooden Houseboats"
        ],
        "budget": {
            "budget": "₹1,800 – ₹2,500/day (Pakhiralay eco-homestay + Shared boat tour + Village meals)",
            "mid": "₹3,500 – ₹5,500/day (All-inclusive 2D/1N package with private motorboat, meals, forest permits & guide)",
            "luxury": "₹8,000+/day (Sundarban Tiger Camp / Waxpol Wildlife Resort)"
        },
        "best_time": "November to February (Mild, misty winter weather with optimal wildlife and bird spotting)",
        "specialties": "Pure Wild Sundarbans Mangrove Honey, Wooden tiger handicrafts, Bonbibi terracotta masks, Mangrove plant herbal extracts."
    },
    "digha": {
        "name": "Digha",
        "state": "West Bengal",
        "description": "Popular seaside getaway on the Bay of Bengal with gentle beaches, casuarina groves, and fresh seafood.",
        "famous_places": [
            "New Digha Beach (Paved promenade with sea views)",
            "Old Digha Beach & Sea Wall",
            "Udaipur Beach & Talsari Beach (Quiet casuarina stretches)",
            "Marine Aquarium and Regional Centre (MARC)",
            "Digha Science Centre & Planetarium",
            "Amravati Park & Toy Train / Boating Lake",
            "Chandaneswar Shiva Temple (Border of Odisha - 8km)"
        ],
        "famous_food": [
            "Fresh Bay of Bengal Fried Fish: Pomfret, Hilsa, Bhetki, Tiger Prawns, Crab (Beach shacks)",
            "Fish Thali with Rice, Dal, Jhuri Aloo Bhaja, and Macher Kalia",
            "Digha Kaju Barfi (Cashew sweets from local cashew processing units)",
            "Fresh Tender Green Coconut on the beach",
            "Chhena Gaja & Khaja sweets"
        ],
        "temples_spiritual": [
            "Chandaneswar Shiva Temple (Famous pilgrimage shrine across Odisha border)",
            "Bhusandeswar Temple (One of Asia largest Shiva Lingams - 15km)",
            "Jagannath Temple at Digha"
        ],
        "heritage_sites": [
            "Old Digha colonial sea wall constructed by Warren Hastings era memories",
            "Marine Aquarium scientific center"
        ],
        "budget": {
            "budget": "₹900 – ₹1,400/day (Budget hotel near Old/New Digha + Shared auto + Beach fish fry)",
            "mid": "₹2,200 – ₹3,500/day (Sea-facing resort + AC cab + Seafood restaurants)",
            "luxury": "₹5,000+/day (Hotel Sea Hawk / Digha Tourist Lodge)"
        },
        "best_time": "October to March (Pleasant coastal breezes with low humidity and clear blue skies)",
        "specialties": "Seashell ornaments & home decors, Cashew nuts (Kaju), Handwoven mats (Madur), Conch shell bangles (Shakha)."
    },
    "motihari": {
        "name": "Motihari",
        "state": "Bihar",
        "description": "Historic headquarters of East Champaran, land of Mahatma Gandhi 1917 Champaran Satyagraha, and birthplace of George Orwell.",
        "famous_places": [
            "Gandhi Smarak Sangrahalaya (Gandhi Memorial Pillar & Museum)",
            "Kesaria Buddhist Stupa (World tallest ancient Buddhist stupa - 104 ft, 45km away)",
            "George Orwell Birthplace Memorial & Museum",
            "Moti Jheel (Scenic lake dividing the town with sunset embankment)",
            "Someshwar Nath Temple at Areraj (Ancient Shiva temple - 28km)"
        ],
        "famous_food": [
            "Champaran Ahuna Handi Mutton (Slow cooked in sealed earthen pot with garlic pods)",
            "Bihari Litti Chokha with Desi Ghee",
            "Dal Pitha & Sattu Paratha",
            "Tilkut, Anarsa & Khaja",
            "Chana Ghugni with Kachori"
        ],
        "temples_spiritual": [
            "Someshwar Nath Mandir at Areraj (Swayambhu Shivling)",
            "Kesaria Buddhist Stupa & Monastic remains",
            "Bada Ram Mandir (Main town)"
        ],
        "heritage_sites": [
            "Gandhi Memorial (Where Gandhiji launched Champaran Satyagraha)",
            "George Orwell Birthplace Cottage",
            "Kesaria Archaeological excavation site (ASI Protected)"
        ],
        "budget": {
            "budget": "₹800 – ₹1,200/day (Town hotel + E-rickshaw + Handi meat/Litti)",
            "mid": "₹1,800 – ₹3,000/day (Comfort hotel + Cab to Kesaria & Areraj)",
            "luxury": "₹4,500+/day (Hotel Ramson / Boutique stay)"
        },
        "best_time": "October to March (Pleasant winter weather ideal for exploring historical monuments)",
        "specialties": "Champaran Handi clay pots, Sikki grass handicraft baskets, Madhubani art pieces, Organic jaggery."
    }
}

def get_city_knowledge(query: str) -> Optional[Dict[str, Any]]:
    """Finds matching city entry from query string."""
    q = query.lower()
    for key, data in INDIAN_CITIES_KB.items():
        if key in q or data["name"].lower() in q:
            return data
        # Aliases
        if key == "kolkata" and ("calcutta" in q or "kolkata" in q):
            return data
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
        if key == "shantiniketan" and "bolpur" in q:
            return data
    return None

def format_city_guide(city_data: Dict[str, Any], hindi: bool = False, specific_type: Optional[str] = None) -> str:
    """Formats city information strictly based on user intent."""
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

    # 1. FOOD ONLY
    if specific_type == "food":
        if hindi:
            return (
                f"🍛 **{name} ({state}) ke Prasiddh Vyanjan & Food Guide**\n\n"
                f"{name} ka swaad aur khana behad anokha aur prasiddh hai. Yahan ke famous dishes aur street food:\n\n"
                f"{food_str}\n\n"
                f"🛍️ **Prasiddh Mithai & Souvenirs**: {specialties}\n\n"
                f"Agar aapko {name} ke specific restaurants ya iconic food stalls ki location chahiye toh batayein!"
            )
        else:
            return (
                f"🍛 **{name} ({state}) Famous Food & Culinary Delights**\n\n"
                f"{name} is renowned for its iconic traditional cuisines, signature dishes, and vibrant street food culture:\n\n"
                f"{food_str}\n\n"
                f"🛍️ **Local Food Specialties & Gifts**: {specialties}\n\n"
                f"Let me know if you would like recommendations for specific iconic eateries or food streets in {name}!"
            )

    # 2. PLACES & SIGHTSEEING ONLY
    if specific_type == "places":
        if hindi:
            return (
                f"🏛️ **{name} ({state}) ke Pramukh Paryatan Sthal (Sightseeing Attractions)**\n\n"
                f"{desc}\n\n"
                f"**Top Must-Visit Attractions:**\n{places_str}\n\n"
                f"🏰 **Aitihasik Dharohar (Heritage Landmarks):**\n{heritage_str}\n\n"
                f"🗓️ **Ghoomne Ka Best Samay**: {best_time}\n\n"
                f"Kya aapko {name} ke sightseeing ke liye customized day-wise plan chahiye?"
            )
        else:
            return (
                f"🏛️ **Top Attractions & Sightseeing in {name} ({state})**\n\n"
                f"{desc}\n\n"
                f"**Must-Visit Attractions:**\n{places_str}\n\n"
                f"🏰 **Heritage & Historical Landmarks:**\n{heritage_str}\n\n"
                f"🗓️ **Best Time to Visit**: {best_time}\n\n"
                f"Would you like a day-by-day customized sightseeing itinerary for {name}?"
            )

    # 3. TEMPLES & SPIRITUAL ONLY
    if specific_type == "temples":
        if hindi:
            return (
                f"🛕 **{name} ({state}) ke Prasiddh Mandir & Dharmik Sthal**\n\n"
                f"{name} ke sabse prasiddh mandir, aashram aur spiritual sthal:\n\n"
                f"{temples_str}\n\n"
                f"Aapko kisi specific mandir ke darshan timing ya aarti ke baare me jaanna hai?"
            )
        else:
            return (
                f"🛕 **Temples & Spiritual Sanctuaries in {name} ({state})**\n\n"
                f"Here are the prominent historical temples, shrines, and sacred sites in {name}:\n\n"
                f"{temples_str}\n\n"
                f"Would you like details on Darshan timings or Aarti rituals for any specific temple?"
            )

    # 4. BUDGET ONLY
    if specific_type == "budget":
        if hindi:
            return (
                f"💰 **{name} ({state}) Trip Budget Breakdown (Per Day Per Person)**\n\n"
                f"• **Budget Traveller**: {b_low}\n"
                f"• **Mid-Range Traveller**: {b_mid}\n"
                f"• **Luxury Traveller**: {b_lux}\n\n"
                f"💡 *Budget Tip*: Dharamshala ya budget homestays aur public transport / e-rickshaw use karke kharcha kafi kam ho jata hai."
            )
        else:
            return (
                f"💰 **Estimated Per-Day Budget Breakdown for {name} ({state})**\n\n"
                f"• **Budget Traveller**: {b_low}\n"
                f"• **Mid-Range Traveller**: {b_mid}\n"
                f"• **Luxury Traveller**: {b_lux}\n\n"
                f"💡 *Savings Tip*: Booking trains/buses in advance and enjoying local street delicacies keeps costs affordable!"
            )

    # 5. BEST TIME ONLY
    if specific_type == "best_time":
        if hindi:
            return (
                f"🗓️ **{name} ({state}) Ghoomne Ka Sahi Samay (Best Time to Visit)**\n\n"
                f"• **Ideal Season / Months**: {best_time}\n\n"
                f"Iss samay mausam suhana rehta hai aur sightseeing me koi pareshani nahi hoti."
            )
        else:
            return (
                f"🗓️ **Best Time to Visit {name} ({state})**\n\n"
                f"• **Optimal Months & Season**: {best_time}\n\n"
                f"During these months, weather conditions are most pleasant and ideal for sightseeing and outdoor exploring."
            )

    # 6. COMPLETE 360 GUIDE
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
