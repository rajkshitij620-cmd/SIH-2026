import {Link, NavLink, useLocation} from 'react-router-dom';
import {Check, Globe, Menu, Moon, Settings, Sun, X} from 'lucide-react';
import {useEffect, useRef, useState} from 'react';
import {useAuth} from '../context/AuthContext';
import {useTheme} from '../context/ThemeContext';
import {api} from '../services/api';

const linkClass=({isActive})=>`nav-link text-sm font-medium transition hover:text-teal-700 ${isActive?'text-teal-800':'text-slate-600'}`;

const languages = [
  { code: 'en', name: 'English', label: 'English' },
  { code: 'hi', name: 'Hindi', label: 'हिन्दी (Hindi)' },
  { code: 'bn', name: 'Bengali', label: 'বাংলা (Bengali)' },
  { code: 'te', name: 'Telugu', label: 'తెలుగు (Telugu)' },
  { code: 'mr', name: 'Marathi', label: 'मराठी (Marathi)' },
  { code: 'ta', name: 'Tamil', label: 'தமிழ் (Tamil)' },
  { code: 'ur', name: 'Urdu', label: 'اردو (Urdu)' },
  { code: 'gu', name: 'Gujarati', label: 'ગુજરાતી (Gujarati)' },
  { code: 'kn', name: 'Kannada', label: 'ಕನ್ನಡ (Kannada)' },
  { code: 'ml', name: 'Malayalam', label: 'മലയാളം (Malayalam)' },
  { code: 'or', name: 'Odia', label: 'ଓଡ଼ିଆ (Odia)' },
  { code: 'pa', name: 'Punjabi', label: 'ਪੰਜਾਬੀ (Punjabi)' },
  { code: 'as', name: 'Assamese', label: 'অসমীয়া (Assamese)' },
  { code: 'mai', name: 'Maithili', label: 'मैथिली (Maithili)' },
  { code: 'sa', name: 'Sanskrit', label: 'संस्कृतम् (Sanskrit)' },
  { code: 'ne', name: 'Nepali', label: 'नेपाली (Nepali)' },
  { code: 'sd', name: 'Sindhi', label: 'सिन्धी (Sindhi)' },
  { code: 'kok', name: 'Konkani', label: 'कोंकणी (Konkani)' },
  { code: 'doi', name: 'Dogri', label: 'डोगरी (Dogri)' },
  { code: 'mni', name: 'Manipuri', label: 'মৈতৈলোন্ (Manipuri)' },
  { code: 'brx', name: 'Bodo', label: 'बड़ो (Bodo)' },
  { code: 'sat', name: 'Santali', label: 'ᱥᱟᱱᱛᱟᱲᱤ (Santali)' },
  { code: 'ks', name: 'Kashmiri', label: 'कॉशुर (Kashmiri)' }
];

export default function Layout({children}) {
 const {user,logout}=useAuth();
 const {theme,toggleTheme}=useTheme();
 const {pathname}=useLocation();
 const [menuOpen,setMenuOpen]=useState(false),[hasPreviousTrip,setHasPreviousTrip]=useState(false),[hasSavedTours,setHasSavedTours]=useState(false);
 const [settingsOpen, setSettingsOpen] = useState(false);
 const [currentLang, setCurrentLang] = useState(() => localStorage.getItem('tourmitra_lang') || 'English');
 const [langSearch, setLangSearch] = useState('');
 const [scrolled, setScrolled] = useState(false);
 const settingsRef = useRef(null);

 const closeMenu=()=>setMenuOpen(false);

 const handleLangChange = (lang) => {
  setCurrentLang(lang.name);
  localStorage.setItem('tourmitra_lang', lang.name);
  localStorage.setItem('tourmitra_lang_code', lang.code);
  window.dispatchEvent(new CustomEvent('tourmitra_lang_changed', { detail: lang.name }));

  const cookieVal = lang.code === 'en' ? '' : `/en/${lang.code}`;
  const domain = window.location.hostname;
  const date = new Date();
  date.setTime(date.getTime() + (365*24*60*60*1000));
  const expires = "; expires=" + date.toUTCString();

  if (lang.code === 'en') {
    document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    document.cookie = `googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=${domain};`;
  } else {
    document.cookie = `googtrans=${cookieVal}${expires}; path=/;`;
    document.cookie = `googtrans=${cookieVal}${expires}; path=/; domain=${domain};`;
    if (domain.includes('.')) {
      const parts = domain.split('.');
      if (parts.length >= 2) {
        const rootDomain = parts.slice(-2).join('.');
        document.cookie = `googtrans=${cookieVal}${expires}; path=/; domain=.${rootDomain};`;
      }
    }
  }

  const combo = document.querySelector('.goog-te-combo');
  if (combo) {
    combo.value = lang.code;
    combo.dispatchEvent(new Event('change'));
  } else {
    window.location.reload();
  }
 };

 // Listen to window scroll position
 useEffect(() => {
  const handleScroll = () => {
   setScrolled(window.scrollY > 40);
  };
  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
  return () => window.removeEventListener('scroll', handleScroll);
 }, []);

 // Click outside to close settings dropdown
 useEffect(() => {
  const handleClickOutside = (e) => {
   if (settingsRef.current && !settingsRef.current.contains(e.target)) {
    setSettingsOpen(false);
   }
  };
  document.addEventListener('mousedown', handleClickOutside);
  return () => document.removeEventListener('mousedown', handleClickOutside);
 }, []);

 useEffect(()=>{
  if(!user){setHasPreviousTrip(false);setHasSavedTours(false);return}
  Promise.all([
   api.get('/trips/history').catch(()=>[]),
   api.get('/trips/saved').catch(()=>[])
  ]).then(([trips,saved])=>{
   setHasPreviousTrip(trips.length>0);
   setHasSavedTours(saved.length>0);
  });
 },[user,pathname]);

  const isMakeGroupPage=['/find-travelers','/requests','/groups'].some(p=>pathname===p||pathname.startsWith(p+'/'));
  const isUnsavedTourView=pathname==='/tour-guide'||pathname.startsWith('/travel-plan/');
  const links = isMakeGroupPage
  ? [['/','Home'],['/plan','Plan Trip'],['/groups','My Groups'],['/find-travelers','TravelMates'],['/requests','Requests'],['/assistant','AI Assistant']]
  : hasSavedTours
  ? [['/','Home'],['/plan','Plan Trip'],['/saved-tours','Saved Tours'],['/assistant','AI Assistant']]
  : isUnsavedTourView
  ? [['/','Home'],['/plan','Plan Trip'],['/tour-guide','Tour Guide'],['/assistant','AI Assistant']]
  : [['/','Home'],['/plan','Plan Trip'],['/assistant','AI Assistant']];
  const isHomePage = pathname === '/';
  return <div className="flex min-h-screen flex-col">
   <header className={`site-header sticky top-0 z-40 transition-all duration-300 ${
     isHomePage 
       ? scrolled
         ? '!bg-white/95 dark:!bg-slate-900/95 !backdrop-blur-md !shadow-md !border-b !border-slate-200/90 dark:!border-slate-800'
         : '!bg-transparent !border-b-0 !border-transparent !shadow-none !backdrop-blur-none' 
       : 'border-b border-slate-200 bg-stone-50/95 backdrop-blur shadow-sm'
   }`}>
    <div className="shell flex min-h-16 items-center justify-between gap-4">
    <Link to="/" className="flex items-center gap-2 py-1" onClick={closeMenu}>
     <img src="/logo.png" alt="Tourmitra" className="h-11 sm:h-14 md:h-16 w-auto object-contain dark:invert" />
    </Link>
    {user&&<nav className="hidden items-center gap-5 md:flex" aria-label="Primary navigation">{links.map(([to,label])=><NavLink key={to} to={to} className={linkClass}>{label}</NavLink>)}</nav>}
    <div className="flex items-center gap-3">
     {/* Universal Settings Dropdown (Theme & Language) */}
     <div className="relative" ref={settingsRef}>
      <button 
        type="button" 
        onClick={()=>setSettingsOpen(o=>!o)} 
        className={`theme-toggle !bg-white/60 dark:!bg-slate-800/60 backdrop-blur-sm transition-all ${settingsOpen ? 'ring-2 ring-teal-600/40 text-teal-700 dark:text-teal-300' : ''}`} 
        aria-label="Settings & Preferences"
        title="Settings (Dark/Light mode & Language)"
      >
        <Settings size={18} className={`transition-transform duration-300 ${settingsOpen ? 'rotate-90' : ''}`}/>
      </button>

      {settingsOpen && (
       <div className="absolute right-0 top-full mt-2 w-72 sm:w-80 max-w-[calc(100vw-2rem)] rounded-2xl bg-white/95 dark:bg-slate-900/95 border border-slate-200 dark:border-slate-700 shadow-2xl p-4 z-50 backdrop-blur-md animate-in fade-in zoom-in-95 duration-150">
        <div className="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-3">
         <div className="flex items-center gap-2">
          <Settings size={16} className="text-teal-600 dark:text-teal-400" />
          <h3 className="text-xs font-bold uppercase tracking-wider text-slate-900 dark:text-white">Settings & Preferences</h3>
         </div>
         <button 
          type="button" 
          onClick={()=>setSettingsOpen(false)}
          className="rounded-lg p-1 text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-600 dark:hover:text-slate-200 transition"
          aria-label="Close settings"
         >
          <X size={16} />
         </button>
        </div>

        {/* Theme Mode Selector */}
        <div className="mt-3.5">
         <label className="text-[11px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-2 block">
          Appearance Mode
         </label>
         <div className="grid grid-cols-2 gap-2 bg-slate-100 dark:bg-slate-800/80 p-1 rounded-xl">
          <button
           type="button"
           onClick={()=>theme!=='light'&&toggleTheme()}
           className={`flex items-center justify-center gap-2 py-2 rounded-lg text-xs font-semibold transition ${
            theme === 'light' 
             ? 'bg-white text-slate-900 shadow-sm' 
             : 'text-slate-500 hover:text-slate-800 dark:text-slate-400 dark:hover:text-white'
           }`}
          >
           <Sun size={15} className={theme === 'light' ? 'text-amber-500' : ''} />
           <span>Light</span>
          </button>
          <button
           type="button"
           onClick={()=>theme!=='dark'&&toggleTheme()}
           className={`flex items-center justify-center gap-2 py-2 rounded-lg text-xs font-semibold transition ${
            theme === 'dark' 
             ? 'bg-slate-950 text-white shadow-sm' 
             : 'text-slate-500 hover:text-slate-800 dark:text-slate-400 dark:hover:text-white'
           }`}
          >
           <Moon size={15} className={theme === 'dark' ? 'text-teal-400' : ''} />
           <span>Dark</span>
          </button>
         </div>
        </div>

        {/* Language Selector */}
        <div className="mt-4">
         <label className="text-[11px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-2 flex items-center justify-between">
          <span className="flex items-center gap-1.5"><Globe size={13}/> Language / भाषा</span>
          <span className="text-[10px] text-teal-600 dark:text-teal-400 font-semibold">{currentLang}</span>
         </label>
         <input
          type="text"
          value={langSearch}
          onChange={e=>setLangSearch(e.target.value)}
          placeholder="Search language / भाषा खोजें..."
          className="mb-2 w-full rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800/80 px-2.5 py-1.5 text-xs text-slate-900 dark:text-white placeholder:text-slate-400 focus:border-teal-600 focus:outline-none"
         />
         <div className="max-h-48 overflow-y-auto space-y-1 pr-1">
          {languages
            .filter(l=>!langSearch || l.name.toLowerCase().includes(langSearch.toLowerCase()) || l.label.toLowerCase().includes(langSearch.toLowerCase()))
            .map((l)=>(
             <button
              key={l.code}
              type="button"
              onClick={()=>handleLangChange(l)}
              className={`w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-medium transition text-left ${
               currentLang === l.name 
                ? 'bg-teal-50 dark:bg-teal-950/60 text-teal-800 dark:text-teal-200 font-semibold' 
                : 'text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800'
              }`}
             >
              <span>{l.label}</span>
              {currentLang === l.name && <Check size={14} className="text-teal-600 dark:text-teal-400" />}
             </button>
          ))}
         </div>
        </div>
       </div>
      )}
     </div>

     {/* Sign in / Sign out button on desktop */}
     <div className="hidden md:flex items-center">
      {user?<button type="button" className="btn-ghost !px-3 !py-2 !bg-white/80 dark:!bg-slate-800/80 backdrop-blur-sm" onClick={logout}>Sign out</button>:<NavLink to="/login" className={`${linkClass} font-semibold !text-slate-900 dark:!text-white`}>Sign in</NavLink>}
     </div>

     {/* Mobile hamburger menu toggle */}
     <button type="button" className="theme-toggle !bg-white/60 dark:!bg-slate-800/60 backdrop-blur-sm md:hidden" onClick={()=>setMenuOpen(open=>!open)} aria-label="Toggle navigation" aria-expanded={menuOpen}>
      {menuOpen?<X size={19}/>:<Menu size={19}/>}
     </button>
    </div>
   </div>
   {menuOpen&&<nav className="shell flex flex-col gap-3 border-t border-slate-200/60 dark:border-slate-800/60 py-4 md:hidden bg-stone-50/95 dark:bg-slate-900/95 backdrop-blur-md rounded-b-2xl shadow-xl" aria-label="Mobile navigation">{user&&links.map(([to,label])=><NavLink key={to} to={to} className={linkClass} onClick={closeMenu}>{label}</NavLink>)}{user?<button type="button" className="text-left text-sm font-medium text-slate-600 dark:text-slate-300" onClick={()=>{logout();closeMenu()}}>Sign out</button>:<NavLink to="/login" className={linkClass} onClick={closeMenu}>Sign in</NavLink>}</nav>}
  </header>
  <main className="flex-1">{children}</main>
  <footer className="border-t border-slate-200 bg-stone-100/70 py-10 transition-colors dark:border-slate-800 dark:bg-stone-900/60">
    <div className="shell grid gap-8 sm:grid-cols-2 md:grid-cols-4">
     <div className="sm:col-span-2">
      <Link to="/" className="inline-block">
       <img src="/logo.png" alt="Tourmitra" className="h-14 sm:h-16 md:h-20 w-auto object-contain dark:invert" />
      </Link>
      <p className="mt-3 max-w-sm text-sm text-slate-600">
       Your AI-powered companion for smart, sustainable, and crowd-aware travel planning across India.
      </p>
      <p className="mt-3 text-xs text-slate-500">
       Smart destination guides · Budget stays & food · TravelMate group matching
      </p>
     </div>
     <div>
      <h3 className="text-xs font-semibold uppercase tracking-wider text-slate-800">Quick Links</h3>
      <ul className="mt-3 space-y-2 text-sm text-slate-600">
       <li><Link to="/" className="hover:text-teal-700">Home</Link></li>
       <li><Link to="/plan" className="hover:text-teal-700">Plan Trip</Link></li>
       <li><Link to="/explore" className="hover:text-teal-700">Explore Destinations</Link></li>
       <li><Link to="/assistant" className="hover:text-teal-700">AI Travel Assistant</Link></li>
      </ul>
     </div>
     <div>
      <h3 className="text-xs font-semibold uppercase tracking-wider text-slate-800">Travel Modes</h3>
      <ul className="mt-3 space-y-2 text-sm text-slate-600">
       <li><Link to="/plan" className="hover:text-teal-700">Group Travel</Link></li>
       <li><Link to="/find-travelers" className="hover:text-teal-700">Find TravelMates</Link></li>
       <li><Link to="/saved-tours" className="hover:text-teal-700">Saved Tours</Link></li>
       <li><Link to="/groups" className="hover:text-teal-700">My Travel Groups</Link></li>
      </ul>
     </div>
    </div>
    <div className="shell mt-8 flex flex-wrap items-center justify-between gap-4 border-t border-slate-200/80 pt-6 text-xs text-slate-500 dark:border-slate-800">
     <p>© {new Date().getFullYear()} Tourmitra. All rights reserved.</p>
     <p>Made with ♥ for Smart Tourism in India</p>
    </div>
   </footer>
 </div>;
}
