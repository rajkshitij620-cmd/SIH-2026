import {Link, NavLink, useLocation} from 'react-router-dom';
import {Menu, Moon, Sun, X} from 'lucide-react';
import {useEffect, useState} from 'react';
import {useAuth} from '../context/AuthContext';
import {useTheme} from '../context/ThemeContext';
import {api} from '../services/api';

const linkClass=({isActive})=>`nav-link text-sm font-medium transition hover:text-teal-700 ${isActive?'text-teal-800':'text-slate-600'}`;

export default function Layout({children}) {
 const {user,logout}=useAuth();
 const {theme,toggleTheme}=useTheme();
 const {pathname}=useLocation();
 const [menuOpen,setMenuOpen]=useState(false),[hasPreviousTrip,setHasPreviousTrip]=useState(false),[hasSavedTours,setHasSavedTours]=useState(false);
 const closeMenu=()=>setMenuOpen(false);

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

 const planLabel=hasPreviousTrip?'New plan trip':'Plan trip';
 const isMakeGroupPage=['/find-travelers','/requests','/groups'].some(p=>pathname===p||pathname.startsWith(p+'/'));
 const isUnsavedTourView=pathname==='/tour-guide'||pathname.startsWith('/travel-plan/');
 const links = isMakeGroupPage
  ? [['/','Home'],['/plan',planLabel],['/groups','My groups'],['/find-travelers','Find TravelMates'],['/requests','Requests'],['/assistant','AI assistant']]
  : hasSavedTours
  ? [['/','Home'],['/plan',planLabel],['/saved-tours','Saved tours'],['/assistant','AI assistant']]
  : isUnsavedTourView
  ? [['/','Home'],['/plan',planLabel],['/tour-guide','Tour guide'],['/assistant','AI assistant']]
  : [['/','Home'],['/plan',planLabel],['/assistant','AI assistant']];
 return <div className="flex min-h-screen flex-col">
  <header className="site-header sticky top-0 z-40 border-b border-slate-200 bg-stone-50/95 backdrop-blur">
   <div className="shell flex min-h-16 items-center justify-between gap-4">
    <Link to="/" className="flex items-center gap-2" onClick={closeMenu}>
     <img src="/logo.png" alt="Tourmitra" className="h-9 sm:h-11 w-auto max-w-[150px] sm:max-w-[180px] object-contain dark:invert mix-blend-multiply dark:mix-blend-screen" />
    </Link>
    {user&&<nav className="hidden items-center gap-5 md:flex" aria-label="Primary navigation">{links.map(([to,label])=><NavLink key={to} to={to} className={linkClass}>{label}</NavLink>)}</nav>}
    <div className="hidden items-center gap-3 md:flex">
     <button type="button" className="theme-toggle" onClick={toggleTheme} aria-label={`Switch to ${theme==='dark'?'light':'dark'} theme`}>{theme==='dark'?<Sun size={17}/>:<Moon size={17}/>}</button>
     {user?<button type="button" className="btn-ghost !px-3 !py-2" onClick={logout}>Sign out</button>:<NavLink to="/login" className={linkClass}>Sign in</NavLink>}
    </div>
    <div className="flex items-center gap-2 md:hidden"><button type="button" className="theme-toggle" onClick={toggleTheme} aria-label={`Switch to ${theme==='dark'?'light':'dark'} theme`}>{theme==='dark'?<Sun size={17}/>:<Moon size={17}/>}</button><button type="button" className="theme-toggle" onClick={()=>setMenuOpen(open=>!open)} aria-label="Toggle navigation" aria-expanded={menuOpen}>{menuOpen?<X size={19}/>:<Menu size={19}/>}</button></div>
   </div>
   {menuOpen&&<nav className="shell flex flex-col gap-3 border-t border-slate-200 py-4 md:hidden" aria-label="Mobile navigation">{user&&links.map(([to,label])=><NavLink key={to} to={to} className={linkClass} onClick={closeMenu}>{label}</NavLink>)}{user?<button type="button" className="text-left text-sm font-medium text-slate-600" onClick={()=>{logout();closeMenu()}}>Sign out</button>:<NavLink to="/login" className={linkClass} onClick={closeMenu}>Sign in</NavLink>}</nav>}
  </header>
  <main className="flex-1">{children}</main>
  <footer className="border-t border-slate-200 bg-stone-100/70 py-10 transition-colors dark:border-slate-800 dark:bg-stone-900/60">
    <div className="shell grid gap-8 sm:grid-cols-2 md:grid-cols-4">
     <div className="sm:col-span-2">
      <Link to="/" className="inline-block">
       <img src="/logo.png" alt="Tourmitra" className="h-10 sm:h-12 w-auto max-w-[160px] sm:max-w-[200px] object-contain dark:invert mix-blend-multiply dark:mix-blend-screen" />
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
       <li><Link to="/plan" className="hover:text-teal-700">{planLabel}</Link></li>
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
