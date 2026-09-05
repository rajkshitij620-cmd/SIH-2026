import {createContext,useContext,useEffect,useState} from 'react';
const ThemeContext=createContext();
export const useTheme=()=>useContext(ThemeContext);
export function ThemeProvider({children}){
 const [theme,setTheme]=useState(()=>localStorage.getItem('tm_theme')||'light');
 useEffect(()=>{document.documentElement.classList.toggle('dark',theme==='dark');localStorage.setItem('tm_theme',theme)},[theme]);
 return <ThemeContext.Provider value={{theme,toggleTheme:()=>setTheme(x=>x==='dark'?'light':'dark')}}>{children}</ThemeContext.Provider>
}
