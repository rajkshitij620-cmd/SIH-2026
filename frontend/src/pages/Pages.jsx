import {useEffect,useRef,useState} from 'react';
import {Link,useLocation,useNavigate,useParams} from 'react-router-dom';
import {Camera,ChevronDown,Eye,EyeOff,ImageUp,Save,Send,Trash2,MapPin,Sun,CloudRain,Sparkles,Copy,Check,RotateCcw,Languages,Globe,Compass,ShieldCheck,ArrowRight,TrendingUp,Calendar,Users,User,Sparkle,Search,IndianRupee,RefreshCw} from 'lucide-react';
import {api} from '../services/api'; import {useAuth} from '../context/AuthContext'; import DestinationCard from '../components/DestinationCard';
export function LatestGroupTravelPlan(){const nav=useNavigate(),[err,setErr]=useState('');useEffect(()=>{api.get('/travel-groups').then(groups=>{if(!groups.length)throw new Error('No connected travel group yet. Connect with a TravelMate first.');nav(`/travel-plan/${groups[0].id}`,{replace:true})}).catch(x=>setErr(x.message))},[nav]);return <div className="shell py-12">{err?<section className="card max-w-xl"><p className="text-slate-700">{err}</p><Link className="btn mt-5" to="/plan">Plan a group trip</Link></section>:<p>Opening your group travel plan…</p>}</div>}
export function GroupTravelPlan(){const {id}=useParams(),nav=useNavigate(),[data,setData]=useState(),[err,setErr]=useState('');useEffect(()=>{api.get('/travel-groups').then(groups=>{const group=groups.find(item=>item.id===id);if(!group)throw new Error('Travel group not found');return api.get('/trips/'+group.trip_id).then(trip=>setData({group,trip}))}).catch(x=>setErr(x.message))},[id]);if(err)return <div className="shell py-12 text-red-600">{err}</div>;if(!data)return <div className="shell py-12">Loading your shared travel plan…</div>;const {group,trip}=data,guide=trip.travel_guide;const save=async(tripId)=>{try{const saved=await api.post(`/trips/${tripId}/save`);setData(d=>({...d,trip:saved}));nav('/saved-tours')}catch(x){setErr(x.message)}};return <div className="shell py-10"><div className="flex flex-wrap items-center justify-between gap-3"><p className="eyebrow">Your group travel plan</p><div className="flex items-center gap-2"><button onClick={()=>save(trip.id)} className="btn !py-1.5 !px-3 text-xs"><Save size={14}/> {trip.saved?'Saved':'Save Tour'}</button><Link className="btn-ghost !py-1.5 !px-3 text-xs" to="/groups">Open group chat</Link></div></div><section className="card mt-4 border-teal-200 bg-teal-50"><h1 className="text-3xl font-bold">{trip.destination.name} · {trip.input.days} days</h1><p className="mt-2 text-slate-600">{group.member_ids.length} connected travellers · {formatDate(group.start_date)} – {formatDate(group.end_date)}</p><p className="mt-2 text-sm text-teal-900">This shared plan is designed to stay within the total group budget of ₹{trip.input.budget.toLocaleString()}.</p></section><DayWisePlacesChart trip={trip}/>{guide&&<GuideHighlights guide={guide}/>}<section className="mt-6"><aside className="card max-w-md"><p className="eyebrow">Group budget</p><p className="mt-2 text-xl font-semibold">₹{trip.input.budget.toLocaleString()} total</p>{trip.budget_breakdown&&Object.entries(trip.budget_breakdown).map(([name,value])=><p className="mt-3 flex justify-between" key={name}><span className="capitalize">{name}</span><b>₹{Math.round(value)}</b></p>)}</aside></section><div className="mt-6 flex gap-3"><button onClick={()=>save(trip.id)} className="btn"><Save size={16}/> {trip.saved?'Saved':'Save Tour'}</button><Link className="btn-ghost" to="/groups">Open group chat</Link></div></div>}
const Field=({n,label,type='text',d='',autoComplete})=><div className="mt-4"><label className="label" htmlFor={n}>{label}</label><input className="input" id={n} name={n} type={type} defaultValue={d} autoComplete={autoComplete} required/></div>;
const allIndiaDestinations = [
 {id:'dest-agra',name:'Taj Mahal & Agra Fort',place:'Agra, Uttar Pradesh',city:'Agra',category:'Heritage',rating:'4.9',cost:'2,200',image:'https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=900&q=85',badge:'Mughal Wonder'},
 {id:'dest-varanasi',name:'Kashi Vishwanath & Ganga Ghats',place:'Varanasi, Uttar Pradesh',city:'Varanasi',category:'Spiritual',rating:'4.8',cost:'1,800',image:'https://images.unsplash.com/photo-1571536802807-30451e3955d8?auto=format&fit=crop&w=900&q=85',badge:'Sacred Ghats'},
 {id:'dest-jaipur',name:'Hawa Mahal & Amer Fort',place:'Jaipur, Rajasthan',city:'Jaipur',category:'Heritage',rating:'4.9',cost:'2,500',image:'https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=900&q=85',badge:'Royal City'},
 {id:'dest-kerala',name:'Alleppey Backwaters & Houseboats',place:'Alleppey, Kerala',city:'Alleppey',category:'Coastal',rating:'4.9',cost:'3,200',image:'https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=900&q=85',badge:'Scenic Waters'},
 {id:'dest-ladakh',name:'Pangong Lake & Khardung La',place:'Ladakh',city:'Ladakh',category:'Mountains',rating:'4.9',cost:'4,500',image:'https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=900&q=85',badge:'High Altitude'},
 {id:'dest-goa',name:'Palolem & Fort Aguada',place:'Goa',city:'Goa',category:'Coastal',rating:'4.8',cost:'2,800',image:'https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=900&q=85',badge:'Sun & Sand'},
 {id:'dest-amritsar',name:'Golden Temple & Wagah Border',place:'Amritsar, Punjab',city:'Amritsar',category:'Spiritual',rating:'4.9',cost:'1,900',image:'https://images.unsplash.com/photo-1588096344356-9e6b26525f21?auto=format&fit=crop&w=900&q=85',badge:'Sacred Shrine'},
 {id:'dest-udaipur',name:'City Palace & Lake Pichola',place:'Udaipur, Rajasthan',city:'Udaipur',category:'Heritage',rating:'4.9',cost:'3,000',image:'https://images.unsplash.com/photo-1615836245337-f5b9b2303f10?auto=format&fit=crop&w=900&q=85',badge:'City of Lakes'},
 {id:'dest-manali',name:'Solang Valley & Rohtang Pass',place:'Manali, Himachal Pradesh',city:'Manali',category:'Mountains',rating:'4.8',cost:'2,800',image:'https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=900&q=85',badge:'Snow Peaks'},
 {id:'dest-kolkata',name:'Victoria Memorial & Howrah Bridge',place:'Kolkata, West Bengal',city:'Kolkata',category:'Heritage',rating:'4.7',cost:'1,800',image:'https://images.unsplash.com/photo-1558431382-27e303142255?auto=format&fit=crop&w=900&q=85',badge:'City of Joy'},
 {id:'dest-rishikesh',name:'Lakshman Jhula & Ganga Aarti',place:'Rishikesh, Uttarakhand',city:'Rishikesh',category:'Spiritual',rating:'4.8',cost:'2,000',image:'https://images.unsplash.com/photo-1609137144822-1efcb3be3028?auto=format&fit=crop&w=900&q=85',badge:'Yoga Capital'},
 {id:'dest-puri',name:'Jagannath Temple & Golden Beach',place:'Puri, Odisha',city:'Puri',category:'Coastal',rating:'4.7',cost:'1,600',image:'https://images.unsplash.com/photo-1590447158019-883d8d5f8bc7?auto=format&fit=crop&w=900&q=85',badge:'Holy Coast'},
 {id:'dest-hampi',name:'Vijayanagara Ruins & Stone Chariot',place:'Hampi, Karnataka',city:'Hampi',category:'Heritage',rating:'4.9',cost:'2,100',image:'https://images.unsplash.com/photo-1600100397608-f010f443b74a?auto=format&fit=crop&w=900&q=85',badge:'UNESCO Gem'},
 {id:'dest-gangtok',name:'Tsomgo Lake & Rumtek Monastery',place:'Gangtok, Sikkim',city:'Gangtok',category:'Mountains',rating:'4.8',cost:'2,600',image:'https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=900&q=85',badge:'Eastern Himalayas'},
 {id:'dest-mumbai',name:'Gateway of India & Marine Drive',place:'Mumbai, Maharashtra',city:'Mumbai',category:'Coastal',rating:'4.7',cost:'3,400',image:'https://images.unsplash.com/photo-1570168007204-dfb528c6958f?auto=format&fit=crop&w=900&q=85',badge:'Dream City'},
 {id:'dest-jaisalmer',name:'Golden Fort & Thar Sand Dunes',place:'Jaisalmer, Rajasthan',city:'Jaisalmer',category:'Heritage',rating:'4.8',cost:'2,700',image:'https://images.unsplash.com/photo-1577717903315-1691ae25ab3f?auto=format&fit=crop&w=900&q=85',badge:'Desert Safari'},
 {id:'dest-ooty',name:'Nilgiri Mountains & Tea Estates',place:'Ooty, Tamil Nadu',city:'Ooty',category:'Mountains',rating:'4.7',cost:'2,400',image:'https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?auto=format&fit=crop&w=900&q=85',badge:'Queen of Hills'},
 {id:'dest-meghalaya',name:'Living Root Bridges & Waterfalls',place:'Cherrapunji, Meghalaya',city:'Cherrapunji',category:'Nature',rating:'4.9',cost:'3,100',image:'https://images.unsplash.com/photo-1627894483216-2138af692e32?auto=format&fit=crop&w=900&q=85',badge:'Rainforest Trail'},
 {id:'dest-madurai',name:'Meenakshi Amman Dravidian Temple',place:'Madurai, Tamil Nadu',city:'Madurai',category:'Spiritual',rating:'4.9',cost:'1,700',image:'https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=900&q=85',badge:'Dravidian Marvel'},
 {id:'dest-darjeeling',name:'Tiger Hill Sunrise & Tea Gardens',place:'Darjeeling, West Bengal',city:'Darjeeling',category:'Mountains',rating:'4.8',cost:'2,500',image:'https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=900&q=85',badge:'Himalayan Views'},
 {id:'dest-sundarbans',name:'Royal Bengal Mangrove Safari',place:'Sundarbans, West Bengal',city:'Sundarbans',category:'Nature',rating:'4.7',cost:'2,300',image:'https://images.unsplash.com/photo-1511497584788-876760111969?auto=format&fit=crop&w=900&q=85',badge:'Mangrove Delta'},
 {id:'dest-bishnupur',name:'Terracotta Temples & Baluchari',place:'Bishnupur, West Bengal',city:'Bishnupur',category:'Heritage',rating:'4.7',cost:'1,200',image:'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?auto=format&fit=crop&w=900&q=85',badge:'Terracotta Art'},
 {id:'dest-shantiniketan',name:'Tagore Visva-Bharati & Sonajhuri',place:'Shantiniketan, West Bengal',city:'Shantiniketan',category:'Nature',rating:'4.6',cost:'1,300',image:'https://images.unsplash.com/photo-1598091383021-15ddea10925d?auto=format&fit=crop&w=900&q=85',badge:'Cultural Oasis'}
];

const popularCities=['Agra','Varanasi','Jaipur','Goa','Kerala','Ladakh','Kolkata','Udaipur','Manali','Amritsar'];

export function Home(){
 const {user}=useAuth(),nav=useNavigate(),[hasPreviousTrip,setHasPreviousTrip]=useState(false),[searchCity,setSearchCity]=useState(''),[activeCategory,setActiveCategory]=useState('All'),[displayedPlaces,setDisplayedPlaces]=useState([]),[isShuffling,setIsShuffling]=useState(false);

 const shuffleAndSet=(cat='All')=>{
  setIsShuffling(true);
  const pool=cat==='All'?allIndiaDestinations:allIndiaDestinations.filter(d=>d.category===cat);
  const shuffled=[...pool].sort(()=>0.5-Math.random());
  setDisplayedPlaces(shuffled.slice(0,6));
  setTimeout(()=>setIsShuffling(false),300);
 };

 useEffect(()=>{
  if(!user)return;
  api.get('/trips/history').then(trips=>setHasPreviousTrip(trips.length>0)).catch(()=>setHasPreviousTrip(false));
 },[user]);

 // Every time user lands on Home page, dynamically pick a fresh randomized set of famous Indian destinations
 useEffect(()=>{
  shuffleAndSet('All');
 },[]);

 const handleCategorySelect=(cat)=>{
  setActiveCategory(cat);
  shuffleAndSet(cat);
 };

 const handleQuickSearch=(e)=>{
  e.preventDefault();
  if(searchCity.trim()){
   nav(`/plan?destination=${encodeURIComponent(searchCity.trim())}`);
  }else{
   nav('/plan');
  }
 };

 return (
  <div className="space-y-16">
   {/* Full-Screen Panoramic Travel Scenic Background Section (starts directly from the very top under transparent navbar) */}
   <div className="relative -mx-5 sm:-mx-8 -mt-16 sm:-mt-20 overflow-hidden bg-slate-950/20 pt-24 sm:pt-28 pb-12 sm:pb-16 lg:pb-20 px-4 sm:px-8 border-b border-slate-200/60 dark:border-slate-800/80">
    {/* Full-Screen Panoramic Travel Scenic Background Image with Full 100% Opacity */}
    <div 
     className="absolute inset-0 bg-cover bg-center bg-no-repeat opacity-100 scale-105 transition-transform duration-1000"
     style={{
      backgroundImage: `url('/hero-bg.jpg')`
     }}
    />
    {/* Subtle Edge Gradients */}
    <div className="absolute inset-0 bg-gradient-to-b from-stone-50/15 via-transparent to-stone-50/30 dark:from-[#0b0f19]/25 dark:via-transparent dark:to-[#0b0f19]/40 pointer-events-none" />

    {/* Ambient Soft Glows */}
    <div className="absolute top-0 right-0 -mt-20 -mr-20 h-96 w-96 rounded-full bg-teal-300/30 dark:bg-teal-500/15 blur-3xl pointer-events-none"/>
    <div className="absolute bottom-0 left-0 -mb-20 -ml-20 h-96 w-96 rounded-full bg-emerald-300/20 dark:bg-emerald-500/10 blur-3xl pointer-events-none"/>

    {/* Centered Hero Card (Original Clean Card Component) */}
    <div className="relative z-10 max-w-4xl mx-auto rounded-3xl bg-gradient-to-br from-teal-50/90 via-white/95 to-emerald-50/80 dark:from-slate-800/95 dark:via-slate-800/90 dark:to-teal-950/75 p-6 sm:p-12 lg:p-14 border border-teal-100/90 dark:border-teal-700/40 shadow-2xl shadow-slate-300/60 dark:shadow-slate-950/60 backdrop-blur-md">
     <div className="max-w-3xl">
      <h1 className="font-serif text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight text-slate-900 dark:text-white">
       Explore India with AI Precision
      </h1>
      <p className="mt-2 text-sm sm:text-base text-slate-600 dark:text-slate-200">
       Smart itineraries, live weather updates & verified TravelMate connections.
      </p>

      {/* Search & Quick Planner Bar */}
      <form onSubmit={handleQuickSearch} className="mt-8 flex flex-col sm:flex-row items-stretch sm:items-center gap-2 rounded-2xl sm:rounded-full bg-white dark:bg-slate-700/90 p-2 border border-slate-200 dark:border-slate-600 shadow-lg shadow-slate-200/60 dark:shadow-slate-950/40">
       <div className="flex flex-1 items-center gap-3 px-4 py-2">
        <MapPin size={20} className="text-teal-600 dark:text-teal-300 shrink-0"/>
        <input 
         type="text" 
         value={searchCity}
         onChange={(e)=>setSearchCity(e.target.value)}
         placeholder="Where in India are you travelling? (e.g. Varanasi, Goa, Jaipur, Manali)" 
         className="w-full bg-transparent text-sm sm:text-base text-slate-900 dark:text-white placeholder:text-slate-400 dark:placeholder:text-slate-300 outline-none font-medium"
        />
       </div>
       <button type="submit" className="btn !bg-gradient-to-r !from-teal-800 !to-teal-900 dark:!from-teal-400 dark:!to-emerald-400 !text-white dark:!text-slate-950 font-bold !rounded-xl sm:!rounded-full px-6 py-3 flex items-center justify-center gap-2 shadow-md shadow-teal-900/10 dark:shadow-teal-400/20 hover:scale-[1.02] active:scale-95 transition-all">
        <span>{hasPreviousTrip?'Plan New Trip':'Plan My Trip'}</span>
        <ArrowRight size={16}/>
       </button>
      </form>

      {/* Popular Chips */}
      <div className="mt-4 flex flex-wrap items-center gap-2 text-xs text-slate-600 dark:text-slate-300">
       <span className="font-semibold text-slate-700 dark:text-slate-200">Popular:</span>
       {popularCities.map((city)=>(
        <button 
         key={city} 
         type="button" 
         onClick={()=>nav(`/plan?destination=${encodeURIComponent(city)}`)}
         className="rounded-full bg-slate-100 hover:bg-teal-50 dark:bg-slate-700/90 dark:hover:bg-teal-900/60 border border-slate-200 dark:border-slate-600 hover:border-teal-300 dark:hover:border-teal-400 px-3 py-1 text-xs text-slate-700 hover:text-teal-800 dark:text-slate-100 dark:hover:text-teal-200 transition shadow-sm"
        >
         {city}
        </button>
       ))}
      </div>
     </div>
    </div>
   </div>

   {/* Rest of the Page in Shell Container */}
   <div className="shell space-y-16">

    {/* 1. Curated India Highlights Gallery with Dynamic Rotating Showcase (Directly after Hero Card) */}
    <div>
     <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 border-b border-slate-100 dark:border-slate-800 pb-5">
      <div>
       <h2 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
        Explore India
       </h2>
      </div>
      
      {/* Category Filter Pills & Quick Shuffle Button */}
      <div className="flex flex-wrap items-center gap-2">
       <div className="flex flex-wrap gap-1.5">
        {['All','Heritage','Spiritual','Coastal','Mountains','Nature'].map(cat=>(
         <button 
          key={cat}
          type="button"
          onClick={()=>handleCategorySelect(cat)}
          className={`rounded-xl px-3 py-1.5 text-xs font-semibold transition ${
           activeCategory===cat
            ? 'bg-teal-700 text-white shadow-sm'
            : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
          }`}
         >
          {cat}
         </button>
        ))}
       </div>

       <button
        type="button"
        onClick={()=>shuffleAndSet(activeCategory)}
        className="inline-flex items-center gap-1.5 rounded-xl border border-teal-200 dark:border-teal-800 bg-teal-50/80 dark:bg-teal-950/70 hover:bg-teal-100 dark:hover:bg-teal-900 px-3 py-1.5 text-xs font-semibold text-teal-800 dark:text-teal-200 transition-all active:scale-95 shadow-sm"
        title="Discover more places"
       >
        <RefreshCw size={13} className={isShuffling?'animate-spin':''}/>
        <span>Shuffle Places</span>
       </button>
      </div>
     </div>

     <div className={`mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3 transition-opacity duration-300 ${isShuffling?'opacity-40':'opacity-100'}`}>
      {displayedPlaces.map(place=>(
       <article key={place.id} className="group relative flex flex-col overflow-hidden rounded-2xl border border-slate-200/80 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm hover:shadow-xl hover:border-teal-400/50 transition-all duration-300 hover:-translate-y-1">
        <div className="relative h-56 w-full overflow-hidden bg-slate-950">
         <img 
          className="h-full w-full object-cover transition-transform duration-500 ease-out group-hover:scale-105" 
          src={place.image} 
          alt={place.name}
          loading="lazy"
         />
         <div className="absolute inset-0 bg-gradient-to-t from-slate-950/85 via-slate-950/30 to-transparent"/>
         
         <div className="absolute top-3 left-3 right-3 flex justify-between items-center">
          <span className="rounded-full bg-teal-900/80 backdrop-blur-md px-2.5 py-1 text-xs font-semibold text-teal-200 border border-teal-500/30 shadow">
           {place.badge}
          </span>
          <span className="rounded-full bg-slate-900/80 backdrop-blur-md px-2.5 py-1 text-xs font-bold text-amber-300 shadow">
           ★ {place.rating}
          </span>
         </div>

         <div className="absolute bottom-3 left-4 right-4">
          <h3 className="text-lg font-bold text-white drop-shadow-sm line-clamp-1">{place.name}</h3>
          <p className="flex items-center gap-1 text-xs font-medium text-slate-300 mt-1">
           <MapPin size={13} className="text-teal-400"/>
           {place.place}
          </p>
         </div>
        </div>

        <div className="flex flex-1 items-center justify-between p-4">
         <div>
          <span className="text-[10px] uppercase font-semibold tracking-wider text-slate-400">Est. Daily Budget</span>
          <p className="text-sm font-bold text-slate-800 dark:text-slate-100">₹{place.cost} <span className="text-xs font-normal text-slate-500">/ day</span></p>
         </div>
         <button 
          type="button" 
          onClick={()=>nav(`/plan?destination=${encodeURIComponent(place.city||place.place.split(',')[0])}`)}
          className="inline-flex items-center gap-1.5 rounded-xl bg-teal-50 hover:bg-teal-700 dark:bg-teal-950/50 dark:hover:bg-teal-600 px-3.5 py-2 text-xs font-semibold text-teal-700 hover:text-white dark:text-teal-300 dark:hover:text-white transition-all duration-200 group-hover:bg-teal-700 group-hover:text-white"
         >
          <span>Plan Trip</span>
          <ArrowRight size={13}/>
         </button>
        </div>
       </article>
      ))}
     </div>
    </div>

    {/* 2. 3-Step Journey Banner */}
    <div className="rounded-3xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-900/50 p-8 sm:p-12">
     <div className="grid gap-8 md:grid-cols-3 relative">
      <div className="flex flex-col items-center text-center p-4">
       <div className="grid h-14 w-14 place-items-center rounded-2xl bg-teal-800 text-white font-bold text-xl shadow-lg shadow-teal-700/20 mb-4">
        1
       </div>
       <h3 className="text-base font-bold text-slate-900 dark:text-white">Input Dates & Budget</h3>
       <p className="mt-2 text-xs text-slate-600 dark:text-slate-400">
        Select single or group travel and set your total budget and travel dates.
       </p>
      </div>

      <div className="flex flex-col items-center text-center p-4">
       <div className="grid h-14 w-14 place-items-center rounded-2xl bg-teal-800 text-white font-bold text-xl shadow-lg shadow-teal-700/20 mb-4">
        2
       </div>
       <h3 className="text-base font-bold text-slate-900 dark:text-white">AI Generates Day-Wise Chart</h3>
       <p className="mt-2 text-xs text-slate-600 dark:text-slate-400">
        Get morning, afternoon and evening landmarks aligned with live weather forecasts and stays.
       </p>
      </div>

      <div className="flex flex-col items-center text-center p-4">
       <div className="grid h-14 w-14 place-items-center rounded-2xl bg-teal-800 text-white font-bold text-xl shadow-lg shadow-teal-700/20 mb-4">
        3
       </div>
       <h3 className="text-base font-bold text-slate-900 dark:text-white">Save Tour or Connect Groups</h3>
       <p className="mt-2 text-xs text-slate-600 dark:text-slate-400">
        Save your complete guide for offline access or find verified TravelMates to share expenses.
       </p>
      </div>
     </div>

     <div className="mt-8 text-center">
      <Link to="/plan" className="btn !py-3 !px-8 text-sm">
       {hasPreviousTrip?'Start Planning Trip':'Start Your Journey with Tourmitra'}
      </Link>
     </div>
    </div>

    {/* 3. Stats / Key Metrics Bar (Near Footer) */}
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
     {[
      {label:'Curated Indian Destinations',value:'500+',icon:Compass,color:'text-teal-600 dark:text-teal-400'},
      {label:'Official Indian Languages',value:'22',icon:Languages,color:'text-purple-600 dark:text-purple-400'},
      {label:'Weather-Adaptive Accuracy',value:'100%',icon:Sun,color:'text-amber-500 dark:text-amber-400'},
      {label:'Crowd Mitigation Score',value:'Low',icon:ShieldCheck,color:'text-emerald-600 dark:text-emerald-400'}
     ].map((stat,i)=>(
      <div key={i} className="card flex items-center gap-4 !p-5 hover:border-teal-300 transition-all">
       <div className={`grid h-12 w-12 shrink-0 place-items-center rounded-2xl bg-slate-100 dark:bg-slate-800 ${stat.color}`}>
        <stat.icon size={24}/>
       </div>
       <div>
        <p className="text-2xl font-extrabold text-slate-900 dark:text-white">{stat.value}</p>
        <p className="text-xs font-medium text-slate-500 dark:text-slate-400 leading-tight">{stat.label}</p>
       </div>
      </div>
     ))}
    </div>

    {/* 4. 3 Core Technology Pillars (Right before Footer) */}
    <div className="grid gap-6 md:grid-cols-3">
     <div className="card hover:shadow-xl transition-all duration-300 border-t-4 border-t-teal-500">
      <div className="grid h-12 w-12 place-items-center rounded-2xl bg-teal-50 text-teal-700 dark:bg-teal-950/60 dark:text-teal-300 mb-4">
       <Sparkles size={24}/>
      </div>
      <h3 className="text-lg font-bold text-slate-900 dark:text-white">Demand-Aware AI Scheduling</h3>
      <p className="mt-2 text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
       Intelligently redistributes visitor footfall by suggesting pristine alternate sights and optimized time slots to eliminate overcrowded queues.
      </p>
     </div>

     <div className="card hover:shadow-xl transition-all duration-300 border-t-4 border-t-amber-500">
      <div className="grid h-12 w-12 place-items-center rounded-2xl bg-amber-50 text-amber-700 dark:bg-amber-950/60 dark:text-amber-300 mb-4">
       <Sun size={24}/>
      </div>
      <h3 className="text-lg font-bold text-slate-900 dark:text-white">Live Weather Adaptability</h3>
      <p className="mt-2 text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
       Integrated with live meteorological data to automatically substitute indoor cultural experiences during sudden rain or extreme heat waves.
      </p>
     </div>

     <div className="card hover:shadow-xl transition-all duration-300 border-t-4 border-t-purple-500">
      <div className="grid h-12 w-12 place-items-center rounded-2xl bg-purple-50 text-purple-700 dark:bg-purple-950/60 dark:text-purple-300 mb-4">
       <Users size={24}/>
      </div>
      <h3 className="text-lg font-bold text-slate-900 dark:text-white">Smart TravelMates Grouping</h3>
      <p className="mt-2 text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
       Find verified co-travelers heading to the same destination on similar dates with matching budgets, complete with shared itineraries and group chats.
      </p>
     </div>
    </div>
   </div>
  </div>
 );
}

export function Auth({register=false}){const {auth}=useAuth(),nav=useNavigate(),location=useLocation(),[mode,setMode]=useState(register?'register':'login'),[err,setErr]=useState(''),[msg,setMsg]=useState(location.state?.message||''),[showPassword,setShowPassword]=useState(false);useEffect(()=>{setMode(register?'register':'login');setErr('');setMsg(location.state?.message||'');setShowPassword(false)},[register,location.state]);const go=async e=>{e.preventDefault();setErr('');setMsg('');const body=Object.fromEntries(new FormData(e.target));try{if(mode==='register'){await auth('/auth/register',body);nav('/',{replace:true})}else if(mode==='reset'){await auth('/auth/reset-password',{email:body.email,new_password:body.password});nav('/',{replace:true})}else{await auth('/auth/login',body);nav('/',{replace:true})}}catch(x){if(mode==='register'&&x.message==='Email is already registered'){setErr('An account already exists with this email. Please sign in or reset your password below.');setMode('login');return}setErr(x.message)}};return <div className="shell grid min-h-[70vh] place-items-center"><form onSubmit={go} className="card w-full max-w-md"><p className="eyebrow">Welcome to Tourmitra</p><h1 className="mt-2 text-2xl font-bold">{mode==='register'?'Create your account':mode==='reset'?'Reset your password':'Sign in to plan better'}</h1>{msg&&<p className="mt-3 text-sm text-teal-700" role="status">{msg}</p>}{mode==='register'&&<Field n="name" label="Name" autoComplete="name"/>}<Field n="email" label="Email" type="email" d={location.state?.email||''} autoComplete="email"/><div className="relative"><Field n="password" label={mode==='reset'?'New Password':'Password'} type={showPassword?'text':'password'} autoComplete={mode==='login'?'current-password':'new-password'}/><button className="absolute bottom-3 right-3 text-slate-500 hover:text-teal-800" type="button" onClick={()=>setShowPassword(value=>!value)} aria-label={showPassword?'Hide password':'Show password'}>{showPassword?<EyeOff size={18}/>:<Eye size={18}/>}</button></div>{err&&<p className="mt-3 text-sm text-red-600" role="alert">{err}</p>}<button className="btn mt-6 w-full">{mode==='register'?'Create account':mode==='reset'?'Update password & sign in':'Sign in'}</button><div className="mt-4 flex flex-wrap items-center justify-between text-sm">{mode==='login'?<><button type="button" onClick={()=>{setMode('reset');setErr('')}} className="text-teal-800">Forgot / Reset password?</button><Link to="/register" className="text-teal-800">Create account</Link></>:mode==='reset'?<><button type="button" onClick={()=>{setMode('login');setErr('')}} className="text-teal-800">Back to Sign in</button><Link to="/register" className="text-teal-800">Create account</Link></>:<><Link to="/login" className="text-teal-800">Already registered? Sign in</Link><button type="button" onClick={()=>{setMode('reset');setErr('')}} className="text-teal-800">Reset password</button></>}</div></form></div>}
const Avatar=({user,size='h-12 w-12'})=>user?.avatar_url?<img className={`${size} rounded-full object-cover`} src={user.avatar_url} alt="Profile"/>:<div className={`${size} grid place-items-center rounded-full bg-teal-800 font-semibold text-white`}>{(user?.name||'T').split(' ').map(x=>x[0]).join('').slice(0,2)}</div>;
const PhotoSource=({photo,onGallery,onCamera,onRemove})=><section className="trip-photo-panel mt-5 overflow-hidden rounded-xl border border-slate-200 bg-white sm:col-span-2"><div className="border-b border-slate-100 px-4 py-3"><p className="font-semibold text-slate-800">Trip photo <span className="text-red-600">*</span></p><p className="mt-1 text-sm text-slate-500">Required · JPEG, JPG or PNG · maximum 4 MB</p></div><details className="group border-b border-slate-100"><summary className="flex cursor-pointer list-none items-center justify-between gap-3 px-4 py-4 font-medium text-slate-700"><span className="flex items-center gap-2"><ImageUp size={18} className="text-teal-700"/>Upload from gallery</span><ChevronDown size={18} className="transition group-open:rotate-180"/></summary><div className="px-4 pb-4"><button type="button" className="btn-ghost" onClick={onGallery}>Choose a photo</button></div></details><details className="group"><summary className="flex cursor-pointer list-none items-center justify-between gap-3 px-4 py-4 font-medium text-slate-700"><span className="flex items-center gap-2"><Camera size={18} className="text-teal-700"/>Take a live photo</span><ChevronDown size={18} className="transition group-open:rotate-180"/></summary><div className="px-4 pb-4"><button type="button" className="btn-ghost" onClick={onCamera}>Open camera</button></div></details>{photo&&<div className="flex items-center gap-3 border-t border-slate-100 px-4 py-3"><img className="h-16 w-16 rounded-lg object-cover" src={photo} alt="Selected trip"/><span className="text-sm text-teal-800">Photo selected</span><button type="button" className="ml-auto text-sm font-medium text-red-600" onClick={onRemove}>Remove</button></div>}</section>;
const LiveCamera=({onCapture,onClose})=>{const videoRef=useRef(),[error,setError]=useState('');useEffect(()=>{let stream;const start=async()=>{try{if(!navigator.mediaDevices?.getUserMedia)throw new Error('Camera is not supported by this browser.');stream=await navigator.mediaDevices.getUserMedia({video:{facingMode:{ideal:'user'}},audio:false});if(videoRef.current){videoRef.current.srcObject=stream;await videoRef.current.play()}}catch(x){setError(x.message||'Camera access was not available.')}};start();return()=>stream?.getTracks().forEach(track=>track.stop())},[]);const capture=()=>{const video=videoRef.current;if(!video?.videoWidth)return;const canvas=document.createElement('canvas');canvas.width=video.videoWidth;canvas.height=video.videoHeight;canvas.getContext('2d').drawImage(video,0,0);onCapture(canvas.toDataURL('image/jpeg',0.9))};return <div className="fixed inset-0 z-50 grid place-items-center bg-slate-950/75 p-4" role="dialog" aria-modal="true" aria-label="Take live photo"><section className="card w-full max-w-lg"><h2 className="text-xl font-semibold">Take live photo</h2>{error?<><p className="mt-3 text-red-600">{error}</p><button className="btn-ghost mt-5" type="button" onClick={onClose}>Close</button></>:<><video className="mt-4 aspect-video w-full rounded-lg bg-slate-900 object-cover" ref={videoRef} muted playsInline/><div className="mt-4 flex justify-end gap-2"><button className="btn-ghost" type="button" onClick={onClose}>Cancel</button><button className="btn" type="button" onClick={capture}>Capture photo</button></div></>}</section></div>};
const formatDate=(value)=>value?new Intl.DateTimeFormat('en-IN',{day:'numeric',month:'short',year:'numeric'}).format(new Date(`${value}T00:00:00`)):'';
const GuideHighlights=({guide})=>{const stay=guide.best_stay,restaurants=guide.restaurants||[];return <section className="card mt-6"><p className="eyebrow">Complete destination guide</p><h2 className="mt-2 text-xl font-semibold">Destination guide & recommendations</h2><div className="mt-4 space-y-2 text-sm text-slate-600">{guide.famous_places?.length>0&&<p><b>Top attractions:</b> {guide.famous_places.join(' · ')}</p>}{guide.best_time?.length>0&&<p><b>Best time to visit:</b> {guide.best_time.join(' · ')}</p>}{guide.weather_advice&&<p><b>Weather advice:</b> {guide.weather_advice}</p>}{guide.local_transportation&&<p><b>Local transport:</b> {guide.local_transportation}</p>}</div><div className="mt-6 grid gap-4 md:grid-cols-2"><article className="rounded-lg border border-teal-100 bg-teal-50 p-4"><p className="text-sm font-medium text-teal-800">Recommended hotel (within budget)</p>{stay?<><h3 className="mt-2 font-semibold">{stay.name}</h3><p className="mt-1 text-sm text-slate-600">₹{stay.price} / night · ★ {stay.rating}</p><p className="mt-2 text-sm text-slate-600">{stay.description}</p></>:<p className="mt-2 text-sm text-slate-600">No verified hostel or stay fits this budget yet.</p>}<p className="mt-3 text-xs text-slate-500">Stay allowance: up to ₹{guide.stay_budget_per_night?.toLocaleString()||0} per night</p></article><article className="rounded-lg border border-amber-100 bg-amber-50 p-4"><p className="text-sm font-medium text-amber-800">Recommended food option (within budget)</p>{restaurants[0]?<><h3 className="mt-2 font-semibold">{restaurants[0].name}</h3><p className="mt-1 text-sm text-slate-600">₹{restaurants[0].price} / person · ★ {restaurants[0].rating}</p><p className="mt-2 text-sm text-slate-600">{restaurants[0].description}</p></>:<p className="mt-2 text-sm text-slate-600">No verified restaurant fits this budget yet.</p>}</article></div></section>};
const cleanPlace=(name,dest='City')=>{if(!name||typeof name!=='string'||name.includes('Museum, gallery')||name.includes('craft studio')||name.includes('Local landmark')||name.includes('well-reviewed'))return `${dest} Famous Landmark`;return name};
const DayWisePlacesChart=({trip})=>{if(!trip?.days?.length)return null;const destName=trip.destination?.name||trip.input?.destination||'Destination',famousPlaces=trip.destination?.famous_places||trip.travel_guide?.famous_places||[];return <section className="card mt-6"><div className="flex flex-wrap items-center justify-between gap-3 border-b border-slate-100 pb-4"><div><p className="eyebrow">Day-Wise Tour Guide & Chart</p><h2 className="mt-1 text-2xl font-bold">Famous Places Organised Day-Wise</h2><p className="mt-1 text-sm text-slate-600">All top attractions and landmarks structured into a daily schedule chart with real-time weather alignment.</p></div><span className="rounded-full bg-teal-100 px-3.5 py-1 text-xs font-semibold text-teal-900">{trip.days.length} Day Schedule Chart</span></div>{famousPlaces.length>0&&<div className="mt-5 rounded-xl border border-teal-100 bg-teal-50/70 p-4"><p className="text-xs font-semibold uppercase tracking-wider text-teal-900">Top Famous Attractions Covered in this Destination:</p><div className="mt-2.5 flex flex-wrap gap-2">{famousPlaces.map((place,i)=><span key={i} className="inline-flex items-center gap-1.5 rounded-lg border border-teal-200 bg-white px-3 py-1 text-xs font-semibold text-teal-900 shadow-sm"><MapPin size={13} className="text-teal-600"/>{place}</span>)}</div></div>}<div className="mt-6 overflow-x-auto rounded-xl border border-slate-200"><table className="w-full text-left text-sm"><thead className="border-b border-slate-200 bg-slate-100/80 text-xs font-semibold uppercase tracking-wider text-slate-700"><tr><th className="px-4 py-3">Day & Date</th><th className="px-4 py-3">Weather & Suitability</th><th className="px-4 py-3">Key Famous Places</th><th className="px-4 py-3">Morning Landmark (9:30 AM)</th><th className="px-4 py-3">Afternoon Food (1:00 PM)</th><th className="px-4 py-3">Evening Sightseeing (4:30 PM)</th></tr></thead><tbody className="divide-y divide-slate-100 bg-white">{trip.days.map((day)=>{const indoor=day.weather?.outdoor_suitability==='low';const morning=day.activities?.find(a=>a.time?.includes('AM')||a.time==='09:30 AM'||a.time==='10:00 AM'||a.category?.includes('Sightseeing')||a.category?.includes('Heritage'));const lunch=day.activities?.find(a=>a.category==='Food'||a.time==='01:00 PM'||a.time==='01:30 PM');const evening=day.activities?.find(a=>a.time?.includes('PM')&&a!==lunch);const dayPlaces=(day.famous_places?.length>0?day.famous_places:[cleanPlace(morning?.place,destName),cleanPlace(evening?.place,destName)]).filter(p=>Boolean(p)&&!p.includes('Museum, gallery')&&!p.includes('craft studio'));return <tr key={day.day} className="hover:bg-slate-50 transition-colors"><td className="px-4 py-3.5 font-medium whitespace-nowrap"><span className="inline-block rounded bg-teal-900 px-2 py-0.5 text-xs font-bold text-white">Day {day.day}</span><p className="mt-1 text-xs text-slate-500">{formatDate(day.date)}</p></td><td className="px-4 py-3.5"><span className={`inline-flex items-center gap-1.5 rounded-full px-2.5 py-0.5 text-xs font-medium ${indoor?'bg-sky-100 text-sky-800':'bg-emerald-100 text-emerald-800'}`}>{indoor?<CloudRain size={12}/>:<Sun size={12}/>}{day.weather?.condition||(indoor?'Indoor Plan':'Good Outdoor')}</span></td><td className="px-4 py-3.5"><div className="flex flex-wrap gap-1.5">{(dayPlaces.length?dayPlaces:[`${destName} Highlights`]).map((p,idx)=><span key={idx} className="rounded bg-teal-50 px-2 py-0.5 text-xs font-medium text-teal-800 border border-teal-200">★ {cleanPlace(p,destName)}</span>)}</div></td><td className="px-4 py-3.5 text-slate-700"><span className="font-semibold text-teal-950">{cleanPlace(morning?.place,destName)}</span></td><td className="px-4 py-3.5 text-slate-700"><span>{lunch?.place&&!lunch.place.includes('well-reviewed')?lunch.place:`${destName} Traditional Kitchen`}</span></td><td className="px-4 py-3.5 text-slate-700"><span className="font-semibold text-slate-900">{cleanPlace(evening?.place,destName)}</span></td></tr>})}</tbody></table></div><div className="mt-6 grid gap-4 md:grid-cols-2">{trip.days.map((day)=>{const indoor=day.weather?.outdoor_suitability==='low';const cleanedDayPlaces=(day.famous_places?.length>0?day.famous_places:[cleanPlace(day.activities?.[0]?.place,destName),cleanPlace(day.activities?.[2]?.place,destName)]).filter(p=>Boolean(p)&&!p.includes('Museum, gallery')&&!p.includes('craft studio'));return <article key={day.day} className={`rounded-xl border p-5 ${indoor?'border-sky-200 bg-sky-50/40':'border-slate-200 bg-white'} shadow-sm`}><div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3"><div><div className="flex items-center gap-2"><span className="rounded bg-teal-800 px-2.5 py-0.5 text-xs font-bold text-white">Day {day.day}</span><h3 className="font-bold text-slate-900">{day.theme?.includes('Indoor discovery')?'Cultural & Heritage discovery':day.theme}</h3></div><p className="mt-1 text-xs text-slate-500">{formatDate(day.date)}</p></div><span className={`inline-flex items-center gap-1 rounded-full px-2.5 py-1 text-xs font-semibold ${indoor?'bg-sky-100 text-sky-800':'bg-emerald-100 text-emerald-800'}`}>{indoor?<CloudRain size={13}/>:<Sun size={13}/>}{day.weather?.condition||'Clear Weather'}</span></div>{cleanedDayPlaces.length>0&&<div className="mt-3 flex flex-wrap items-center gap-1.5"><span className="text-xs font-semibold text-slate-500">Day Landmarks:</span>{cleanedDayPlaces.map((p,idx)=><span key={idx} className="rounded bg-teal-50 px-2 py-0.5 text-xs font-semibold text-teal-800 border border-teal-200">★ {cleanPlace(p,destName)}</span>)}</div>}<div className="mt-4 space-y-3">{day.activities?.map((activity,index)=>{const isGeneric=activity.place?.includes('Museum, gallery')||activity.place?.includes('craft studio')||activity.place?.includes('well-reviewed');const placeTitle=cleanPlace(activity.place,destName);const cost=activity.estimated_cost>0?activity.estimated_cost:activity.category==='Food'?300:0;const travelTime=activity.travel_time&&!activity.travel_time.includes('Confirm')?activity.travel_time:'15-20 mins';const whyText=isGeneric?`Recommended ${activity.category?.toLowerCase()} for Day ${day.day} in ${destName}.`:activity.why_recommended;return <div key={index} className="flex items-start gap-3 rounded-lg border border-slate-100 bg-slate-50/80 p-3"><div className="mt-0.5 grid h-7 w-7 shrink-0 place-items-center rounded-md bg-teal-100 text-teal-800 font-bold text-xs">{activity.time?.slice(0,2)||'09'}</div><div className="min-w-0 flex-1"><div className="flex flex-wrap items-center justify-between gap-1"><b className="text-sm text-slate-900">{placeTitle}</b><span className="text-xs font-medium text-slate-500">{activity.time}</span></div><p className="mt-0.5 text-xs text-teal-800 font-medium">{activity.category} {cost>0&&`· ₹${cost}`} {`· ⏱️ ${travelTime}`}</p><p className="mt-1 text-xs text-slate-600">{whyText}</p></div></div>})}</div></article>})}</div></section>};

export function Planner(){
 const {user}=useAuth(),nav=useNavigate(),locationRoute=useLocation(),searchParams=new URLSearchParams(locationRoute.search),prefilledDest=searchParams.get('destination')||'';
 const [travelType,setTravelType]=useState('single'),[destinationInput,setDestinationInput]=useState(prefilledDest),[budgetInput,setBudgetInput]=useState('15000'),[location,setLocation]=useState(''),[coords,setCoords]=useState({}),[photo,setPhoto]=useState(''),[age,setAge]=useState(''),[cameraTarget,setCameraTarget]=useState(null),[draft,setDraft]=useState(null),[makingGroup,setMakingGroup]=useState(false),[load,setLoad]=useState(false),[err,setErr]=useState(''),[hasPreviousTrip,setHasPreviousTrip]=useState(false),galleryRef=useRef(),cameraRef=useRef();

 useEffect(()=>{api.get('/trips/history').then(trips=>setHasPreviousTrip(trips.length>0)).catch(()=>setHasPreviousTrip(false))},[]);
 useEffect(()=>{if(prefilledDest)setDestinationInput(prefilledDest)},[prefilledDest]);

 const getUserCurrentLocation=()=>{setErr('');if(!navigator.geolocation){setErr('Location is unavailable on this device. Enter your city manually.');return}navigator.geolocation.getCurrentPosition(p=>{setCoords({current_location_latitude:p.coords.latitude,current_location_longitude:p.coords.longitude});setLocation('Near your current location')},()=>setErr('Location permission is required for Single Travel. Enter your city manually.'))};
 const readImage=(file,onLoad)=>{setErr('');if(!file)return;if(!['image/jpeg','image/png'].includes(file.type)){setErr('Upload a JPEG, JPG, or PNG photo only.');return}if(file.size>4*1024*1024){setErr('Each photo must be 4 MB or smaller.');return}const reader=new FileReader();reader.onload=()=>onLoad(reader.result);reader.readAsDataURL(file)};
 const selectPhoto=file=>readImage(file,setPhoto);
 const createTrip=async(data)=>{setLoad(true);setErr('');try{const t=await api.post('/trips/plan',data);sessionStorage.setItem('trip',JSON.stringify(t));sessionStorage.setItem('latest_trip_id',t.id);nav(data.connection_option==='connect_people'?`/find-travelers?trip=${t.id}`:`/tour-guide?trip=${t.id}`)}catch(x){setErr(x.message)}finally{setLoad(false)}};
 const submit=e=>{e.preventDefault();const f=Object.fromEntries(new FormData(e.target));const data={...f,destination:destinationInput.trim(),budget:Number(budgetInput)||15000,travellers:travelType==='group'?Math.max(2,Number(f.travellers)||2):1,days:1,interests:['culture','food'],preferences:['balanced'],travel_type:travelType};if(travelType==='group')delete data.gender;setErr('');if(travelType==='single')setDraft(data);else createTrip(data)};
 const submitGroup=e=>{e.preventDefault();if(!photo){setErr('A trip photo is required. Upload a JPEG, JPG, or PNG photo.');return}if(!location){setErr('Location is required to make a group. Use your current location or enter your city manually.');return}if(age&&(Number(age)<18||Number(age)>120)){setErr('Please enter a valid age (18 to 120).');return}createTrip({...draft,connection_option:'connect_people',trip_photo:photo,current_location_city:location,age:Number(age)||undefined,...coords})};

 if(draft&&!makingGroup)return (
  <div className="shell max-w-xl py-12 sm:py-16">
   <section className="card text-center p-6 sm:p-8">
    <div className="mx-auto grid h-14 w-14 place-items-center rounded-2xl bg-teal-50 dark:bg-teal-950 text-teal-700 dark:text-teal-300">
     <Compass size={28}/>
    </div>
    <p className="eyebrow mt-4">Single Travel Selection</p>
    <h1 className="text-2xl sm:text-3xl font-bold mt-1">How would you like to explore {draft.destination}?</h1>
    <p className="mt-3 text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
     Get a tailored day-wise Solo Tour Guide, or match with verified TravelMates travelling to the same destination on similar dates.
    </p>
    
    <div className="mt-8 grid gap-4 sm:grid-cols-2">
     <button 
      type="button"
      className="btn !bg-gradient-to-r !from-teal-800 !to-teal-900 !py-4 flex flex-col items-center justify-center gap-1.5 hover:scale-[1.02] transition shadow-md" 
      onClick={()=>createTrip({...draft,connection_option:'single_travelling'})} 
      disabled={load}
     >
      <User size={20}/>
      <span className="font-bold text-sm">{load?'Building guide…':'Solo Tour Guide'}</span>
      <span className="text-[11px] font-normal text-teal-200">Personalized day schedule</span>
     </button>

     <button 
      type="button"
      className="btn !bg-gradient-to-r !from-purple-800 !to-indigo-900 !py-4 flex flex-col items-center justify-center gap-1.5 hover:scale-[1.02] transition shadow-md" 
      onClick={()=>{setErr('');setMakingGroup(true)}} 
      disabled={load}
     >
      <Users size={20}/>
      <span className="font-bold text-sm">Make Group</span>
      <span className="text-[11px] font-normal text-purple-200">Match with TravelMates</span>
     </button>
    </div>

    <button type="button" className="btn-ghost mt-5 text-xs text-slate-500" onClick={()=>setDraft(null)} disabled={load}>
     ← Edit trip details
    </button>
    {err&&<p className="mt-4 text-sm text-red-600 dark:text-red-400" role="alert">{err}</p>}
   </section>
  </div>
 );

 if(draft&&makingGroup)return (
  <div className="shell max-w-xl py-12 sm:py-16">
   <form onSubmit={submitGroup} className="card p-6 sm:p-8">
    <p className="eyebrow">TravelMates Matchmaking</p>
    <h1 className="mt-1 text-2xl sm:text-3xl font-bold">Add Group Finder Profile</h1>
    <p className="mt-2 text-sm text-slate-600 dark:text-slate-400">
     A trip photo, your age and current location help AI calculate compatibility scores with fellow travellers heading to {draft.destination}.
    </p>

    <input ref={galleryRef} className="hidden" type="file" accept="image/jpeg,image/png,.jpg,.jpeg,.png" onChange={e=>selectPhoto(e.target.files?.[0])}/>
    <input ref={cameraRef} className="hidden" type="file" accept="image/jpeg,image/png" capture="environment" onChange={e=>selectPhoto(e.target.files?.[0])}/>
    
    <PhotoSource photo={photo} onGallery={()=>galleryRef.current?.click()} onCamera={()=>setCameraTarget('trip')} onRemove={()=>setPhoto('')}/>
    
    <div className="mt-5 rounded-xl border border-teal-100 dark:border-teal-900 bg-teal-50/70 dark:bg-teal-950/40 p-4">
     <b className="text-xs font-semibold uppercase tracking-wider text-teal-900 dark:text-teal-200">Age & Location</b>
     <div className="mt-3 grid gap-3 sm:grid-cols-2">
      <div>
       <label className="label" htmlFor="group-age">Age (years)</label>
       <input id="group-age" type="number" min="18" max="120" className="input bg-white dark:bg-slate-900" value={age} onChange={e=>setAge(e.target.value)} placeholder="e.g. 24" aria-label="Age"/>
      </div>
      <div>
       <label className="label">Current Location City</label>
       <input className="input bg-white dark:bg-slate-900" value={location} onChange={e=>setLocation(e.target.value)} placeholder="e.g. Delhi, Mumbai, Patna" aria-label="Current city" required/>
      </div>
     </div>
     <button type="button" className="btn-ghost mt-3 text-xs flex items-center gap-1.5" onClick={getUserCurrentLocation}>
      <MapPin size={13}/> Use My Current GPS City
     </button>
    </div>

    {err&&<p className="mt-4 text-sm text-red-600 dark:text-red-400" role="alert">{err}</p>}

    <div className="mt-6 flex gap-3">
     <button className="btn flex-1" disabled={load}>{load?'Finding TravelMates…':'Find TravelMates'}</button>
     <button type="button" className="btn-ghost" onClick={()=>{setErr('');setMakingGroup(false)}} disabled={load}>Back</button>
    </div>
   </form>
{cameraTarget!==null&&<LiveCamera onClose={()=>setCameraTarget(null)} onCapture={image=>{setPhoto(image);setCameraTarget(null)}}/>}
  </div>
 );

 return (
  <div className="shell max-w-3xl py-10 sm:py-14">
   <div className="text-center max-w-xl mx-auto">
    <h1 className="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white">
     {hasPreviousTrip?'Plan Another Journey with AI':'Craft Your Personalized Journey'}
    </h1>
   </div>

   <form onSubmit={submit} className="card mt-8 p-6 sm:p-8 space-y-6">
    {/* Travel Mode Toggle Cards */}
    <div>
     <label className="label">Select Travel Mode</label>
     <div className="mt-2 grid grid-cols-1 sm:grid-cols-2 gap-3">
      <div 
       onClick={()=>setTravelType('single')}
       className={`cursor-pointer rounded-2xl border-2 p-4 transition-all duration-200 ${
        travelType==='single'
         ? 'border-teal-600 bg-teal-50/60 dark:bg-teal-950/40 shadow-sm'
         : 'border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 hover:border-slate-300'
       }`}
      >
       <div className="flex items-center justify-between">
        <div className="flex items-center gap-2 font-bold text-slate-900 dark:text-white">
         <User size={18} className={travelType==='single'?'text-teal-600':'text-slate-400'}/>
         <span>Solo Traveler</span>
        </div>
        <span className="rounded-full bg-teal-100 dark:bg-teal-900 px-2.5 py-0.5 text-[10px] font-bold text-teal-800 dark:text-teal-200">Solo & Matchmaking</span>
       </div>
       <p className="mt-2 text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
        Generate a personalized solo tour guide or connect with verified TravelMates heading to this destination.
       </p>
      </div>

      <div 
       onClick={()=>setTravelType('group')}
       className={`cursor-pointer rounded-2xl border-2 p-4 transition-all duration-200 ${
        travelType==='group'
         ? 'border-teal-600 bg-teal-50/60 dark:bg-teal-950/40 shadow-sm'
         : 'border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 hover:border-slate-300'
       }`}
      >
       <div className="flex items-center justify-between">
        <div className="flex items-center gap-2 font-bold text-slate-900 dark:text-white">
         <Users size={18} className={travelType==='group'?'text-teal-600':'text-slate-400'}/>
         <span>Group & Family</span>
        </div>
        <span className="rounded-full bg-emerald-100 dark:bg-emerald-900 px-2.5 py-0.5 text-[10px] font-bold text-emerald-800 dark:text-emerald-200">Full Guide & Split</span>
       </div>
       <p className="mt-2 text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
        Complete multi-person itinerary with automated per-head shared budget splitting for friends and family.
       </p>
      </div>
     </div>
    </div>

    {/* Destination Input */}
    <div>
     <label className="label" htmlFor="destination">Destination City or Heritage Site</label>
     <div className="relative mt-1">
      <MapPin size={18} className="absolute left-3.5 top-1/2 -translate-y-1/2 text-teal-600"/>
      <input 
       className="input !pl-10 text-base" 
       id="destination" 
       name="destination" 
       value={destinationInput}
       onChange={e=>setDestinationInput(e.target.value)}
       placeholder="e.g. Varanasi, Goa, Jaipur, Agra, Manali, Kerala Backwaters…" 
       autoComplete="address-level2" 
       required
      />
     </div>
    </div>

    {/* Dates Row */}
    <div className="grid gap-4 sm:grid-cols-2">
     <div>
      <label className="label" htmlFor="start_date">Trip Start Date</label>
      <input className="input" id="start_date" name="start_date" type="date" required/>
     </div>
     <div>
      <label className="label" htmlFor="end_date">Trip End Date</label>
      <input className="input" id="end_date" name="end_date" type="date" required/>
     </div>
    </div>

    {/* Budget & Presets */}
    <div>
     <div className="flex items-center justify-between">
      <label className="label" htmlFor="budget">Total Estimated Budget (₹ INR)</label>
      <span className="text-xs text-slate-500 font-medium">Smartly allocated across stays, food & transit</span>
     </div>
     <div className="relative mt-1">
      <IndianRupee size={16} className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400"/>
      <input 
       className="input !pl-9" 
       id="budget" 
       name="budget" 
       type="number" 
       min="1000" 
       step="500" 
       value={budgetInput}
       onChange={e=>setBudgetInput(e.target.value)}
       required
      />
     </div>
     <div className="mt-2 flex flex-wrap items-center gap-2">
      <span className="text-xs text-slate-400 font-medium">Quick Select:</span>
      {[
       {label:'₹5,000 (Budget)',val:'5000'},
       {label:'₹15,000 (Standard)',val:'15000'},
       {label:'₹30,000 (Comfort)',val:'30000'},
       {label:'₹50,000 (Luxury)',val:'50000'}
      ].map(p=>(
       <button 
        key={p.val} 
        type="button" 
        onClick={()=>setBudgetInput(p.val)}
        className={`rounded-lg border px-2.5 py-1 text-xs font-semibold transition ${
         budgetInput===p.val
          ? 'border-teal-600 bg-teal-50 dark:bg-teal-950 text-teal-800 dark:text-teal-200'
          : 'border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:bg-slate-100'
        }`}
       >
        {p.label}
       </button>
      ))}
     </div>
    </div>

    {/* Conditional Fields based on Single vs Group */}
    {travelType==='single'?(
     <div>
      <label className="label" htmlFor="gender">Gender (For Community Matchmaking)</label>
      <select className="input" id="gender" name="gender" defaultValue="" required>
       <option value="" disabled>Select gender for profile matching</option>
       <option value="male">Male</option>
       <option value="female">Female</option>
       <option value="other">Other</option>
      </select>
     </div>
    ):(
     <div>
      <label className="label" htmlFor="travellers">Number of Travelers in Group</label>
      <select className="input" id="travellers" name="travellers" defaultValue="2" required>
       {[2,3,4,5,6,7,8,9,10,12,15,20,25,30,40,50].map(count=>(
        <option value={count} key={count}>{count} travelers in group</option>
       ))}
      </select>
      <p className="mt-1 text-xs text-slate-500">The total group budget will be partitioned evenly among all members.</p>
     </div>
    )}

    {err&&<p className="text-sm text-red-600 dark:text-red-400" role="alert">{err}</p>}

    <button 
     type="submit" 
     className="btn w-full !py-3.5 text-base font-bold shadow-lg shadow-teal-700/20" 
     disabled={load}
    >
     {load ? 'Crafting Your AI Itinerary…' : travelType === 'group' ? 'Generate Group Itinerary & Guide →' : 'Continue to Exploration Options →'}
    </button>
   </form>
  </div>
 );
}

export function FindTravelers(){const nav=useNavigate(),location=useLocation(),queryTrip=new URLSearchParams(location.search).get('trip'),[selectedTripId,setSelectedTripId]=useState(queryTrip||''),[data,setData]=useState(),[load,setLoad]=useState(true),[err,setErr]=useState('');const fetchMatches=(tripId='')=>{setLoad(true);setErr('');const param=tripId?`?trip_id=${encodeURIComponent(tripId)}`:'';api.get(`/travelers/matches${param}`).then(res=>{setData(res);if(res.trip?.id)setSelectedTripId(res.trip.id)}).catch(x=>setErr(x.message)).finally(()=>setLoad(false))};useEffect(()=>{fetchMatches(queryTrip||selectedTripId)},[queryTrip]);const connect=async(travellerId,tripId)=>{try{await api.post(`/connections/${travellerId}?trip_id=${encodeURIComponent(tripId||selectedTripId||'')}`);fetchMatches(selectedTripId)}catch(x){alert(x.message)}};if(err)return <div className="shell py-12"><p className="text-red-600">{err}</p><button className="btn mt-4" onClick={()=>nav('/plan')}>Plan a trip</button></div>;if(load&&!data)return <div className="shell py-12">Finding TravelMates…</div>;const currentTrip=data?.trip,matches=data?.matches||[],sameDest=data?.same_destination_travelers||[],allTravelers=[...matches,...sameDest.filter(s=>!matches.some(m=>m.traveller.id===s.traveller.id))];return <div className="shell max-w-5xl py-8">{allTravelers.length>0?<div className="grid gap-4 md:grid-cols-2">{allTravelers.map(m=><article className="card" key={m.traveller.id}><div className="flex items-center gap-3"><Avatar user={m.traveller}/><div><h2 className="font-semibold">{m.traveller.name}</h2><p className="text-sm text-slate-500">{m.trip.current_location_city}{m.trip.gender?` · ${m.trip.gender.charAt(0).toUpperCase()+m.trip.gender.slice(1)}`:''}{m.trip.age?` · ${m.trip.age} yrs`:''}</p></div>{m.match_percentage?<b className="ml-auto text-teal-800">{m.match_percentage}% Match</b>:<span className="ml-auto rounded-full bg-teal-50 px-2.5 py-1 text-xs font-medium text-teal-800">{m.trip.destination}</span>}</div><div className="mt-4 space-y-1 rounded-lg bg-stone-50 p-3 text-sm"><p>✈ <b>Destination:</b> {m.trip.destination}</p><p>📅 <b>Dates:</b> {formatDate(m.trip.start_date)} – {formatDate(m.trip.end_date)} · 💰 ₹{m.trip.budget?.toLocaleString()}</p></div><div className="mt-5">{m.connection_status==='pending'?<button className="btn w-full opacity-70 cursor-not-allowed" disabled>Request Sent</button>:<button className="btn w-full" onClick={()=>connect(m.traveller.id,currentTrip?.id||m.trip.id)}>Connect</button>}</div></article>)}</div>:<section className="card mt-6 py-10 text-center"><h2 className="text-lg font-semibold">No TravelMates found yet</h2><p className="mt-2 text-slate-600">Be the first to connect with other travellers.</p><button className="btn mt-4" onClick={()=>nav('/plan')}>Plan a trip</button></section>}</div>}
export function TravellerProfile(){const {id}=useParams(),nav=useNavigate(),[data,setData]=useState(),[err,setErr]=useState(''),trip=new URLSearchParams(window.location.search).get('trip');useEffect(()=>{api.get(`/travelers/${id}/public-profile?trip_id=${encodeURIComponent(trip||'')}`).then(setData).catch(x=>setErr(x.message))},[id,trip]);if(err)return <div className="shell py-12">{err}</div>;if(!data)return <div className="shell py-12">Loading traveller profile…</div>;return <div className="shell max-w-xl py-12"><section className="card"><Avatar user={data.profile} size="h-20 w-20"/><h1 className="mt-4 text-3xl font-bold">{data.profile.name}</h1><p className="mt-2 text-slate-600">{data.profile.bio||'Travel enthusiast'}</p><p className="mt-4 text-sm"><b>Interests:</b> {data.profile.interests?.join(', ')||'Travel and local experiences'}</p>{data.trip&&<div className="mt-4 space-y-1.5 rounded-lg bg-stone-50 p-3 text-sm"><p>✈ <b>Destination:</b> {data.trip.destination} · {formatDate(data.trip.start_date)} – {formatDate(data.trip.end_date)}</p>{data.trip.current_location_city&&<p>📍 <b>Location:</b> {data.trip.current_location_city}</p>}{data.trip.gender&&<p>👤 <b>Gender:</b> <span className="capitalize">{data.trip.gender}</span></p>}{data.trip.age&&<p>🎂 <b>Age:</b> {data.trip.age} years</p>}<p className="mt-2 text-teal-800 font-semibold">{data.match_percentage}% Match</p></div>}<button className="btn-ghost mt-6" onClick={()=>nav(-1)}>Back to TravelMates</button></section></div>}
function LiveMap({location,trip}){const [map,setMap]=useState(null),[mapError,setMapError]=useState('');useEffect(()=>{let active=true;setMapError('');api.get('/maps/location?location='+encodeURIComponent(location)).then(data=>{if(active)setMap(data.available?data:null)}).catch(()=>active&&setMap(null));return()=>{active=false}},[location]);const openStreetMap=map?`https://www.openstreetmap.org/?mlat=${map.latitude}&mlon=${map.longitude}#map=12/${map.latitude}/${map.longitude}`:'';return <>{trip&&<DayWisePlacesChart trip={trip}/>} {trip?.travel_guide&&<GuideHighlights guide={trip.travel_guide}/>} {map&&<section className="card mt-6"><p className="eyebrow">Live location map</p>{!mapError?<img onError={()=>setMapError('Map preview is unavailable for this MapTiler key.')} className="mt-3 h-64 w-full rounded-lg object-cover" src={api.url('/maps/static?location='+encodeURIComponent(location))} alt={`Map of ${location}`}/>:<p className="mt-3 text-sm text-slate-600">{mapError}</p>}<a className="mt-3 inline-block text-sm font-medium text-teal-700 underline" href={openStreetMap} target="_blank" rel="noreferrer">Open {location} in OpenStreetMap</a><p className="mt-2 text-xs text-slate-500">Location found via MapTiler.</p></section>}</>}
function Listing({url,title}){const [data,setData]=useState([]);useEffect(()=>{api.get(url).then(setData)},[url]);return <div className="shell py-12"><p className="eyebrow">Destination discovery</p><h1 className="mt-2 text-3xl font-bold">{title}</h1><div className="mt-8 grid gap-5 md:grid-cols-3">{data.map(x=><DestinationCard key={x.id} x={x}/>)}</div></div>};export const Explore=()=> <Listing url="/recommendations" title="Explore destinations"/>;
export function Discover(){const [data,setData]=useState([]);useEffect(()=>{api.get('/businesses').then(setData)},[]);return <div className="shell py-12"><p className="eyebrow">Local discovery</p><h1 className="mt-2 text-3xl font-bold">Meet the people behind the place.</h1><div className="mt-8 grid gap-4 md:grid-cols-2">{data.map(x=><article className="card" key={x.id}><p className="eyebrow">{x.category}</p><h2 className="mt-1 text-lg font-semibold">{x.name}</h2><p className="mt-3 text-slate-600">{x.description}</p><p className="mt-4 text-sm">{x.location} · ₹{x.price} · ★ {x.rating} · Verified</p></article>)}</div></div>}
export function ItineraryView({trip,onSave,allTrips=[],selectedId,onTripChange}){const nav=useNavigate();if(!trip)return <div className="shell py-12">Building your itinerary…</div>;const destination=trip.destination?.name||trip.input?.destination||'Destination',days=trip.input?.days||trip.days?.length||1;return <div className="shell py-10"><p className="eyebrow">Your travel plan</p><div className="flex flex-wrap items-end justify-between gap-4"><div><h1 className="mt-2 text-3xl font-bold">{destination} · {days} days</h1><p className="mt-1 text-sm text-slate-500">{formatDate(trip.input?.start_date)} – {formatDate(trip.input?.end_date)} · ₹{trip.input?.budget?.toLocaleString()}</p></div><div className="flex flex-wrap items-center gap-2">{allTrips.length>1&&<label className="flex items-center text-xs font-medium text-slate-500">Choose trip:<select className="input ml-1.5 min-w-44 !py-1.5 !px-2 text-xs" value={selectedId||trip.id} onChange={e=>onTripChange?.(e.target.value)}>{allTrips.map(item=><option value={item.trip.id} key={item.trip.id}>{item.trip.destination?.name||item.trip.input?.destination} · {formatDate(item.trip.input?.start_date)}</option>)}</select></label>}<button onClick={()=>nav('/plan')} className="btn-ghost">Edit</button><button onClick={()=>onSave?.(trip.id)} className="btn"><Save size={16}/> {trip.saved?'Saved':'Save Tour'}</button></div></div>{trip.ai_summary&&<div className="card mt-6 border-teal-200 bg-teal-50"><p className="eyebrow">AI trip brief</p><p className="mt-2">{trip.ai_summary}</p><p className="mt-2 text-sm text-slate-600">{trip.ai_recommendation_reason}</p></div>}<LiveMap location={destination} trip={trip}/>{trip.budget_breakdown&&<aside className="card mt-6"><p className="eyebrow">Budget estimate</p><div className="mt-4 grid gap-3 sm:grid-cols-4">{Object.entries(trip.budget_breakdown).map(([k,v])=><div key={k} className="rounded-lg bg-stone-50 p-3"><p className="text-xs uppercase text-slate-500">{k}</p><p className="mt-1 text-lg font-semibold text-teal-800">₹{Math.round(v).toLocaleString()}</p></div>)}</div></aside>}</div>}
export function Itinerary(){const {id}=useParams(),nav=useNavigate(),[t,setT]=useState(()=>{try{const cached=JSON.parse(sessionStorage.getItem('trip')||'null');return cached?.id===id?cached:null}catch{return null}}),[err,setErr]=useState('');useEffect(()=>{if(!t)api.get('/trips/'+id).then(setT).catch(x=>setErr(x.message))},[id,t]);if(err)return <div className="shell py-12 text-red-600">{err}</div>;if(!t)return <div className="shell py-12">Building your itinerary…</div>;const save=async(tripId)=>{try{const saved=await api.post(`/trips/${tripId}/save`);setT(saved);nav('/saved-tours')}catch(x){setErr(x.message)}};return <ItineraryView trip={t} onSave={save}/>}
export function TourGuide(){const nav=useNavigate(),location=useLocation(),[data,setData]=useState(),[selectedId,setSelectedId]=useState(''),[err,setErr]=useState('');useEffect(()=>{const queryTrip=new URLSearchParams(location.search).get('trip'),latestId=sessionStorage.getItem('latest_trip_id'),cached=JSON.parse(sessionStorage.getItem('trip')||'null');api.get('/trips/history').then(items=>{setData(items);const targetId=queryTrip||latestId||cached?.id;if(targetId&&items.some(item=>item.trip.id===targetId)){setSelectedId(targetId)}else if(items.length){setSelectedId(items[0].trip.id)}}).catch(x=>setErr(x.message))},[location.search]);if(err)return <div className="shell py-12 text-red-600">{err}</div>;if(!data)return <div className="shell py-12">Loading your travel plan…</div>;if(!data.length)return <div className="shell py-12"><p className="eyebrow">Your travel plan</p><h1 className="mt-2 text-3xl font-bold">No travel plan yet</h1><section className="card mt-7 max-w-lg"><p className="text-slate-600">Create a single or group trip to view your complete travel plan here.</p><Link className="btn mt-5" to="/plan">Plan a trip</Link></section></div>;const active=data.find(item=>item.trip.id===selectedId)||data[0],save=async(tripId)=>{try{const saved=await api.post(`/trips/${tripId}/save`);setData(items=>items.map(item=>item.trip.id===tripId?{...item,trip:saved}:item));nav('/saved-tours')}catch(x){setErr(x.message)}};return <ItineraryView trip={active.trip} onSave={save} allTrips={data} selectedId={active.trip.id} onTripChange={setSelectedId}/>}
const GeminiStar=({className="w-7 h-7"})=><svg className={className} viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 0C12 6.627 6.627 12 0 12C6.627 12 12 17.373 12 24C12 17.373 17.373 12 24 12C17.373 12 12 6.627 12 0Z" fill="url(#gemini-grad)"/><defs><linearGradient id="gemini-grad" x1="0" y1="0" x2="24" y2="24" gradientUnits="userSpaceOnUse"><stop stopColor="#1E88E5"/><stop offset="0.35" stopColor="#7C4DFF"/><stop offset="0.7" stopColor="#E040FB"/><stop offset="1" stopColor="#FF6E40"/></linearGradient></defs></svg>;
const indianLanguages=[
 {code:'en',name:'English',native:'English'},
 {code:'hi',name:'Hindi',native:'हिन्दी'},
 {code:'bn',name:'Bengali',native:'বাংলা'},
 {code:'te',name:'Telugu',native:'తెలుగు'},
 {code:'mr',name:'Marathi',native:'मराठी'},
 {code:'ta',name:'Tamil',native:'தமிழ்'},
 {code:'ur',name:'Urdu',native:'اردو'},
 {code:'gu',name:'Gujarati',native:'ગુજરાતી'},
 {code:'kn',name:'Kannada',native:'ಕನ್ನಡ'},
 {code:'ml',name:'Malayalam',native:'മലയാളം'},
 {code:'or',name:'Odia',native:'ଓଡ଼ିଆ'},
 {code:'pa',name:'Punjabi',native:'ਪੰਜਾਬੀ'},
 {code:'as',name:'Assamese',native:'অসমীয়া'},
 {code:'mai',name:'Maithili',native:'मैथिली'},
 {code:'sa',name:'Sanskrit',native:'संस्कृतम्'},
 {code:'ne',name:'Nepali',native:'नेपाली'},
 {code:'sd',name:'Sindhi',native:'सिन्धी'},
 {code:'kok',name:'Konkani',native:'कोंकणी'},
 {code:'doi',name:'Dogri',native:'डोगरी'},
 {code:'mni',name:'Manipuri',native:'মৈতৈলোন্'},
 {code:'brx',name:'Bodo',native:'बड़ो'},
 {code:'sat',name:'Santali',native:'ᱥᱟᱱᱛᱟᱲᱤ'},
 {code:'ks',name:'Kashmiri',native:'कॉशुर'}
];
const geminiPrompts=[
 {icon:'🛕',title:'Varanasi Temples & Ghats',desc:'Ghats, Kashi Vishwanath, famous food & 2-day budget',query:'Varanasi famous places, temples, food, historic sites and per day budget'},
 {icon:'🍲',title:'Kolkata Food & Heritage',desc:'Street food, sweets, Victoria Memorial & cost',query:'Kolkata famous street food, sweets, temples, historic places and daily budget'},
 {icon:'🏰',title:'Jaipur Forts & Culture',desc:'Hawa Mahal, Amer Fort, local cuisine & expenses',query:'Jaipur top forts, famous food, historic sites and 2-day budget'},
 {icon:'🌤️',title:'Live Weather & Travel',desc:'Current live weather, temperature & best travel time',query:'What is the current live weather in Kolkata and Goa, and best time to visit?'}
];
export function Assistant(){
 const [msg,setMsg]=useState([]),[q,setQ]=useState(''),[lang,setLang]=useState('en'),[sending,setSending]=useState(false),[copiedIndex,setCopiedIndex]=useState(null),chatBottomRef=useRef(null),inputRef=useRef(null);
 useEffect(()=>{chatBottomRef.current?.scrollIntoView({behavior:'smooth'})},[msg,sending]);
 const selectedLangObj=indianLanguages.find(l=>l.code===lang)||indianLanguages[0];

 const handleNewChat=()=>{
  setMsg([]);
  setQ('');
  setSending(false);
  setCopiedIndex(null);
  sessionStorage.removeItem('tourmitra_ai_chat');
  setTimeout(()=>{inputRef.current?.focus()},50);
 };

 const handleSendQuery=async(queryText)=>{
  const textToSend=queryText||q.trim();
  if(!textToSend||sending)return;
  setQ('');
  setSending(true);
  setMsg(prev=>[...prev,{role:'user',text:textToSend}]);
  try{
   const d=await api.post('/ai/chat',{message:textToSend,language:lang});
   setMsg(prev=>[...prev,{role:'ai',text:d.message,note:d.source}]);
  }catch{
   setMsg(prev=>[...prev,{role:'ai',text:'Assistant unavailable. Please check backend connection and try again.'}]);
  }finally{
   setSending(false);
  }
 };
 const copyToClipboard=(text,idx)=>{navigator.clipboard.writeText(text);setCopiedIndex(idx);setTimeout(()=>setCopiedIndex(null),2000);};
 return <div className="shell max-w-4xl py-10 min-h-[85vh] flex flex-col justify-between">
  <div className="flex flex-wrap items-center justify-between gap-3 border-b border-slate-100 pb-4 dark:border-slate-800">
   <div className="flex items-center gap-3">
    <GeminiStar className="w-8 h-8"/>
    <div>
     <h1 className="text-xl font-bold bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">Tourmitra</h1>
     <p className="text-xs text-slate-500 font-medium">Smart Indian Destination Intelligence</p>
    </div>
   </div>
   <div className="flex items-center gap-2.5">
    {msg.length>0&&<button type="button" onClick={handleNewChat} className="flex items-center gap-1.5 text-xs font-semibold text-slate-600 hover:text-red-600 dark:text-slate-300 dark:hover:text-red-400 px-3 py-1.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white/80 dark:bg-slate-800/80 shadow-sm hover:border-red-300 dark:hover:border-red-900 transition-all active:scale-95" title="Clear old chat and start new conversation"><RotateCcw size={13}/> <span>New Chat</span></button>}
    <div className="flex items-center gap-1.5 rounded-xl border border-slate-200/90 dark:border-slate-700 bg-white dark:bg-slate-800 px-2.5 py-1.5 shadow-sm">
     <Languages size={15} className="text-purple-600 shrink-0"/>
     <select value={lang} onChange={(e)=>setLang(e.target.value)} disabled={sending} className="bg-transparent text-xs font-semibold text-slate-700 dark:text-slate-200 outline-none cursor-pointer pr-1">
      {indianLanguages.map(l=><option key={l.code} value={l.code} className="text-slate-900 dark:text-slate-100 bg-white dark:bg-slate-800">{l.native} ({l.name})</option>)}
     </select>
    </div>
   </div>
  </div>
  <div className="flex-1 py-6 space-y-6">
   {msg.length===0?<div className="my-auto py-8">
    <div className="max-w-2xl">
     <h2 className="text-3xl sm:text-4xl font-bold tracking-tight text-slate-800 dark:text-slate-100">
      Where would you like to explore in India today?
     </h2>
    </div>
    <div className="mt-8 grid gap-3 sm:grid-cols-2">
     {geminiPrompts.map((p,idx)=><button key={idx} type="button" onClick={()=>handleSendQuery(p.query)} className="group flex flex-col justify-between rounded-2xl border border-slate-200/90 dark:border-slate-800 bg-white/70 dark:bg-slate-900/60 p-4 text-left shadow-sm transition hover:border-purple-300 hover:shadow-md hover:bg-gradient-to-br hover:from-white hover:to-purple-50/40 dark:hover:from-slate-900 dark:hover:to-purple-950/20">
      <div className="flex items-center justify-between"><span className="text-2xl">{p.icon}</span><Sparkles size={15} className="text-slate-300 group-hover:text-purple-600 transition"/></div>
      <div className="mt-4"><p className="text-sm font-semibold text-slate-800 dark:text-slate-200 group-hover:text-purple-700 dark:group-hover:text-purple-300">{p.title}</p><p className="mt-1 text-xs text-slate-500 line-clamp-2">{p.desc}</p></div>
     </button>)}
    </div>
   </div>:<div className="space-y-6">
    {msg.map((m,i)=><div key={i} className={`flex gap-3 ${m.role==='user'?'justify-end':'justify-start'}`}>
     {m.role==='ai'&&<div className="mt-1 shrink-0"><div className="grid h-8 w-8 place-items-center rounded-full bg-gradient-to-tr from-blue-600 via-indigo-600 to-purple-600 text-white shadow-sm shadow-indigo-500/20"><GeminiStar className="w-5 h-5"/></div></div>}
     <div className={`relative max-w-[88%] rounded-2xl p-4 sm:p-5 text-sm sm:text-base leading-relaxed ${m.role==='user'?'bg-gradient-to-r from-slate-800 to-slate-900 text-white shadow-sm rounded-br-sm':'bg-white dark:bg-slate-900 border border-slate-200/80 dark:border-slate-800 text-slate-800 dark:text-slate-200 shadow-sm rounded-bl-sm'}`}>
      <div className="whitespace-pre-wrap">{m.text}</div>
      {m.role==='ai'&&<div className="mt-4 flex flex-wrap items-center justify-between gap-2 border-t border-slate-100 dark:border-slate-800 pt-3 text-xs text-slate-500">
       <span className="inline-flex items-center gap-1.5 text-slate-400"><Sparkles size={12} className="text-purple-500"/>{m.note||'Tourmitra Intelligence'}</span>
       <button type="button" onClick={()=>copyToClipboard(m.text,i)} className="flex items-center gap-1 text-xs text-slate-500 hover:text-slate-900 dark:hover:text-slate-100 transition px-2 py-1 rounded hover:bg-slate-100 dark:hover:bg-slate-800">
        {copiedIndex===i?<><Check size={13} className="text-emerald-600"/><span className="text-emerald-600">Copied</span></>:<><Copy size={13}/><span>Copy</span></>}
       </button>
      </div>}
     </div>
    </div>)}
    {sending&&<div className="flex gap-3">
     <div className="mt-1 shrink-0"><div className="grid h-8 w-8 place-items-center rounded-full bg-gradient-to-tr from-blue-600 via-indigo-600 to-purple-600 text-white animate-pulse"><GeminiStar className="w-5 h-5"/></div></div>
     <div className="max-w-[85%] rounded-2xl border border-slate-200/80 dark:border-slate-800 bg-white/90 dark:bg-slate-900 p-4 shadow-sm">
      <div className="flex items-center gap-2 text-sm font-medium text-slate-600 dark:text-slate-300"><Sparkles size={16} className="text-purple-500 animate-spin" style={{animationDuration:'3s'}}/><span>Tourmitra is analyzing destinations & preparing your guide…</span></div>
      <div className="mt-3 h-1.5 w-48 overflow-hidden rounded-full bg-slate-100 dark:bg-slate-800"><div className="h-full w-full bg-gradient-to-r from-blue-500 via-indigo-500 to-purple-500 animate-[pulse_1.2s_ease-in-out_infinite]"/></div>
     </div>
    </div>}
    <div ref={chatBottomRef}/>
   </div>}
  </div>
  <div className="sticky bottom-4 mt-4">
   <form onSubmit={(e)=>{e.preventDefault();handleSendQuery();}} className="flex items-center gap-2 rounded-3xl border border-slate-200/90 dark:border-slate-700/80 bg-white/95 dark:bg-slate-900/95 p-2 shadow-lg backdrop-blur-md transition focus-within:border-purple-400 focus-within:ring-2 focus-within:ring-purple-400/20">
    <div className="grid h-10 w-10 shrink-0 place-items-center rounded-full bg-gradient-to-tr from-blue-50 via-purple-50 to-pink-50 dark:from-slate-800 dark:to-slate-800 text-purple-600"><Sparkles size={18}/></div>
    <input ref={inputRef} className="flex-1 bg-transparent px-2 py-2 text-sm sm:text-base outline-none placeholder:text-slate-400 text-slate-800 dark:text-slate-100" id="assistant-question" name="assistant-question" value={q} onChange={(e)=>setQ(e.target.value)} placeholder={lang==='en'?"Ask about any Indian city, food, temples, history, per-day budget…":`${selectedLangObj.native} (${selectedLangObj.name}) - Kisi bhi city, food, temples, history ya budget ke baare me poochhein…`} autoComplete="off" disabled={sending}/>
    <button type="submit" disabled={sending||!q.trim()} className="grid h-10 w-10 shrink-0 place-items-center rounded-full bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 text-white shadow-md shadow-indigo-500/20 transition hover:opacity-95 active:scale-95 disabled:opacity-40 disabled:pointer-events-none" aria-label="Send message"><Send size={17}/></button>
   </form>
   <p className="mt-2 text-center text-[11px] text-slate-400 dark:text-slate-500">Tourmitra provides destination insights, real-time weather, authentic food recommendations, and travel budgets.</p>
  </div>
 </div>;
}
export function Saved(){const nav=useNavigate(),[data,setData]=useState(),[err,setErr]=useState(''),[deletingId,setDeletingId]=useState('');useEffect(()=>{api.get('/trips/saved').then(setData).catch(x=>setErr(x.message))},[]);const deleteSaved=async(e,tripId)=>{e.preventDefault();e.stopPropagation();if(!window.confirm('Are you sure you want to delete this tour from your saved collection?'))return;setDeletingId(tripId);try{await api.delete(`/trips/${tripId}`);const remaining=(data||[]).filter(item=>item.trip.id!==tripId);setData(remaining);const cached=JSON.parse(sessionStorage.getItem('trip')||'null');if(cached?.id===tripId)sessionStorage.removeItem('trip');if(remaining.length===0){nav('/plan')}}catch(x){alert(x.message)}finally{setDeletingId('')}};if(err)return <div className="shell py-12 text-red-600">{err}</div>;if(!data)return <div className="shell py-12">Loading saved tours…</div>;return <div className="shell py-12"><p className="eyebrow">Saved tours</p><h1 className="mt-2 text-3xl font-bold">Your saved tour collection</h1><p className="mt-2 text-slate-600">Every guide you save is kept here for quick access.</p><div className="mt-7 grid gap-4 md:grid-cols-2">{data.length?data.map(({trip,group,is_shared})=>{const destination=trip.destination?.name||trip.input?.destination,href=group?`/travel-plan/${group.id}`:`/itinerary/${trip.id}`;return <article key={trip.id} className="card transition hover:border-slate-300"><div className="flex items-start justify-between gap-3"><div><p className="eyebrow">{group?'Group tour':'Solo tour'}</p><h2 className="mt-1 text-xl font-semibold">{destination}</h2></div><div className="flex items-center gap-2"><span className="rounded-full bg-teal-50 px-3 py-1 text-xs font-medium text-teal-800">Saved</span><button type="button" onClick={e=>deleteSaved(e,trip.id)} disabled={deletingId===trip.id} className="flex items-center gap-1.5 rounded-lg border border-red-200 px-3 py-1 text-xs font-medium text-red-600 transition hover:bg-red-50 hover:border-red-400 disabled:opacity-50" title="Delete saved tour"><Trash2 size={14}/> {deletingId===trip.id?'Deleting…':'Delete'}</button></div></div><p className="mt-4 text-sm text-slate-600">{formatDate(trip.input?.start_date)} – {formatDate(trip.input?.end_date)}</p><p className="mt-2 text-sm text-slate-600">₹{trip.input?.budget?.toLocaleString()} · {is_shared?'Joined group tour':group?`${group.member_ids.length} travellers`:'Personal plan'}</p><div className="mt-5"><Link to={href} className="text-sm font-medium text-teal-700 hover:underline">Open saved tour →</Link></div></article>}):<section className="card md:col-span-2"><p>No saved tours yet.</p><p className="mt-2 text-sm text-slate-600">Plan a journey to save it here.</p><Link className="btn mt-5" to="/plan">Plan a trip</Link></section>}</div></div>}
export function PreviousTrips(){const [data,setData]=useState(),[err,setErr]=useState(''),[deletingId,setDeletingId]=useState('');useEffect(()=>{api.get('/trips/history').then(setData).catch(x=>setErr(x.message))},[]);const deleteTrip=async(e,tripId)=>{e.preventDefault();e.stopPropagation();if(!window.confirm('Are you sure you want to delete this trip from your history?'))return;setDeletingId(tripId);try{await api.delete(`/trips/${tripId}`);setData(items=>items.filter(item=>item.trip.id!==tripId));const cached=JSON.parse(sessionStorage.getItem('trip')||'null');if(cached?.id===tripId)sessionStorage.removeItem('trip')}catch(x){alert(x.message)}finally{setDeletingId('')}};if(err)return <div className="shell py-12 text-red-600">{err}</div>;if(!data)return <div className="shell py-12">Loading previous trips…</div>;return <div className="shell py-12"><p className="eyebrow">Travel history</p><h1 className="mt-2 text-3xl font-bold">Previous trips</h1><p className="mt-2 text-slate-600">Your personal plans and every shared trip you joined through TravelMates.</p><div className="mt-7 space-y-4">{data.length?data.map(({trip,group,is_shared})=>{const groupTrip=Boolean(group),destination=trip.destination?.name||trip.input?.destination,href=groupTrip?`/travel-plan/${group.id}`:`/itinerary/${trip.id}`;return <article key={trip.id} className="card transition hover:border-slate-300"><div className="flex flex-wrap items-start justify-between gap-3"><div><p className="eyebrow">{groupTrip?'Group trip':'Solo trip'}</p><h2 className="mt-1 text-xl font-semibold">{destination}</h2></div><div className="flex items-center gap-2"><span className="rounded-full bg-teal-50 px-3 py-1 text-sm font-medium text-teal-800">{groupTrip?`${group.member_ids.length} travellers`:'Personal plan'}</span><button type="button" onClick={e=>deleteTrip(e,trip.id)} disabled={deletingId===trip.id} className="flex items-center gap-1.5 rounded-lg border border-red-200 px-3 py-1 text-xs font-medium text-red-600 transition hover:bg-red-50 hover:border-red-400 disabled:opacity-50" title="Delete trip"><Trash2 size={14}/> {deletingId===trip.id?'Deleting…':'Delete'}</button></div></div><div className="mt-4 grid gap-2 text-sm text-slate-600 sm:grid-cols-3"><p><b>Dates:</b> {formatDate(trip.input?.start_date)} – {formatDate(trip.input?.end_date)}</p><p><b>Budget:</b> ₹{trip.input?.budget?.toLocaleString()}</p><p><b>Type:</b> {is_shared?'Joined via TravelMates':groupTrip?'Created with TravelMates':'Single travel'}</p></div><div className="mt-4"><Link to={href} className="text-sm font-medium text-teal-700 hover:underline">Open trip details →</Link></div></article>}):<section className="card"><p>No previous trips yet.</p><Link className="btn mt-5" to="/plan">Plan a trip</Link></section>}</div></div>}
export function Detail(){const {id}=useParams(),[x,setX]=useState();useEffect(()=>{api.get('/destinations/'+id).then(setX)},[id]);if(!x)return <div className="shell py-12">Loading destination…</div>;return <div className="shell py-10"><img className="h-72 w-full rounded-xl object-cover" src={x.image} alt={x.name}/><div className="mt-8 grid gap-8 md:grid-cols-[1fr_280px]"><div><p className="eyebrow">{x.categories.join(' · ')}</p><h1 className="mt-2 text-4xl font-bold">{x.name}</h1><p className="mt-4 text-lg text-slate-600">{x.description}</p><h2 className="mt-8 text-xl font-semibold">What to do</h2><p className="mt-3">{x.activities.join(' · ')}</p></div><aside className="card"><p>★ {x.rating}</p><p className="mt-3">₹{x.average_cost}/day</p><p className="mt-3">Context crowd: {x.crowd_score<40?'Low':'Moderate'}</p></aside></div></div>}
export function GroupRequests(){const nav=useNavigate(),[data,setData]=useState(),[err,setErr]=useState('');const load=()=>Promise.all([api.get('/connections/received'),api.get('/travel-groups')]).then(([requests,groups])=>setData({requests,groups})).catch(x=>setErr(x.message));useEffect(()=>{load()},[]);const decide=async(id,action)=>{try{await api.post(`/connections/${id}/decision`,{action});if(action==='accept'){nav('/groups')}else{nav('/find-travelers')}}catch(x){setErr(x.message)}};if(err)return <div className="shell py-12 text-red-600">{err}</div>;if(!data)return <div className="shell py-12">Loading travel requests…</div>;const requests=data.requests.filter(item=>item.connection.status==='pending');return <div className="shell max-w-3xl py-12"><p className="eyebrow">TravelMate requests</p><h1 className="mt-2 text-3xl font-bold">Travel requests</h1><p className="mt-2 text-slate-600">Requests received from other travellers going to the same destination.</p><div className="mt-7 space-y-4">{requests.length?requests.map(({connection,traveller,trip})=><article className="card" key={connection.id}><div className="flex items-center gap-3"><Avatar user={traveller}/><div><h2 className="font-semibold">{traveller.name}</h2><p className="text-sm text-slate-500">{trip.current_location_city||'Location'} · {trip.destination}{trip.gender?` · ${trip.gender.charAt(0).toUpperCase()+trip.gender.slice(1)}`:''}{trip.age?` · ${trip.age} yrs`:''}</p></div></div><p className="mt-4 text-sm text-slate-600">📅 {formatDate(trip.start_date)} – {formatDate(trip.end_date)} · 💰 ₹{trip.budget?.toLocaleString()}</p><div className="mt-5 flex gap-3"><button className="btn flex-1 !bg-emerald-700 hover:!bg-emerald-800" onClick={()=>decide(connection.id,'accept')}>Accept</button><button className="btn-ghost flex-1 border-red-200 text-red-700 hover:border-red-500 hover:bg-red-50" onClick={()=>decide(connection.id,'decline')}>Reject</button></div></article>):<section className="card"><p>No pending travel requests.</p></section>}</div>{data.groups.length>0&&<section className="card mt-7 border-teal-200 bg-teal-50"><p className="eyebrow">Connected groups</p><h2 className="mt-2 text-xl font-semibold">Your group chat is ready</h2><p className="mt-2 text-sm text-slate-600">Accepted travellers are added to My Groups, where every member can chat and coordinate the trip.</p><button className="btn mt-5" onClick={()=>nav('/groups')}>Open group chat</button></section>}</div>}
export function TravelGroups(){const [groups,setGroups]=useState(),[active,setActive]=useState(),[messages,setMessages]=useState([]),[text,setText]=useState(''),[err,setErr]=useState('');useEffect(()=>{api.get('/travel-groups').then(data=>{setGroups(data);if(data[0])setActive(data[0])}).catch(x=>setErr(x.message))},[]);useEffect(()=>{if(!active)return;const loadMsg=()=>api.get(`/travel-groups/${active.id}/messages`).then(setMessages).catch(()=>{});loadMsg();const interval=setInterval(loadMsg,3000);return()=>clearInterval(interval)},[active]);const send=async e=>{e.preventDefault();if(!text.trim()||!active)return;try{await api.post(`/travel-groups/${active.id}/messages`,{message:text.trim()});setText('');setMessages(await api.get(`/travel-groups/${active.id}/messages`))}catch(x){setErr(x.message)}};const endGroup=async()=>{if(!active||!window.confirm(`End ${active.name}? This removes the group for every member.`))return;try{await api.delete(`/travel-groups/${active.id}`);const remaining=groups.filter(group=>group.id!==active.id);setGroups(remaining);setActive(remaining[0]);setMessages([])}catch(x){setErr(x.message)}};if(err)return <div className="shell py-12 text-red-600">{err}</div>;if(!groups)return <div className="shell py-12">Loading your travel groups…</div>;return <div className="shell max-w-5xl py-12"><p className="eyebrow">My travel groups</p><h1 className="mt-2 text-3xl font-bold">Plan together</h1>{groups.length?<div className="mt-7 grid gap-5 md:grid-cols-[260px_1fr]"><aside className="space-y-2">{groups.map(group=><button type="button" key={group.id} className={(active?.id===group.id?'btn':'btn-ghost')+' w-full text-left'} onClick={()=>setActive(group)}>{group.name}<span className="mt-1 block text-xs font-normal">{group.destination} · {group.member_ids.length} members</span></button>)}</aside><section className="card min-h-[420px]">{active&&<><div className="flex flex-wrap items-start justify-between gap-3"><div><h2 className="text-xl font-semibold">{active.name}</h2><p className="mt-1 text-sm text-slate-500">{active.destination} · {formatDate(active.start_date)} – {formatDate(active.end_date)}</p></div><div className="flex items-center gap-2"><Link to={`/travel-plan/${active.id}`} className="btn !py-1.5 !px-3 text-xs">View Tour Guide</Link><button type="button" className="btn-ghost border-red-200 text-red-700 hover:border-red-500" onClick={endGroup}>End group travel</button></div></div><div className="mt-5 space-y-3">{messages.length?messages.map(message=><div key={message.id} className="rounded-lg bg-stone-100 p-3"><b className="text-sm">{message.sender.name}</b><p>{message.message}</p></div>):<p className="mt-sm text-slate-500">Start the group conversation.</p>}</div><form onSubmit={send} className="mt-6 flex gap-2"><input className="input" value={text} onChange={e=>setText(e.target.value)} placeholder="Write a message…"/><button className="btn">Send</button></form></>}</section></div>:<section className="card mt-7"><p>No travel groups yet. Accept a TravelMate request to create one.</p></section>}</div>}
