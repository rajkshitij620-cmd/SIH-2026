import {createContext,useContext,useEffect,useState} from 'react'; import {api} from '../services/api'
const C=createContext(); export const useAuth=()=>useContext(C)
export function AuthProvider({children}){
  const [user,setUser]=useState(()=>{
    try {
      const saved=localStorage.getItem('tm_user');
      return saved?JSON.parse(saved):null;
    }catch{return null;}
  });
  const [loading,setLoading]=useState(false);
  
  const clearSession=()=>{
    localStorage.removeItem('tm_token');
    localStorage.removeItem('tm_user');
    sessionStorage.removeItem('trip');
    setUser(null);
  };

  useEffect(()=>{
    const expire=()=>{clearSession();setLoading(false);};
    window.addEventListener('tm:session-expired',expire);
    return()=>window.removeEventListener('tm:session-expired',expire);
  },[]);

  useEffect(()=>{
    const token=localStorage.getItem('tm_token');
    if(!token){
      clearSession();
      return;
    }
    api.get('/auth/session').then(data=>{
      if(data.authenticated && data.user){
        setUser(data.user);
        localStorage.setItem('tm_user',JSON.stringify(data.user));
      }else{
        clearSession();
      }
    }).catch(err=>{
      if(err?.status===401 || err?.message?.includes('401') || err?.message?.includes('Unauthorized')){
        clearSession();
      }
    });
  },[]);

  const auth=async(path,body)=>{
    const d=await api.post(path,body);
    sessionStorage.removeItem('trip');
    localStorage.setItem('tm_token',d.access_token);
    if(d.user){
      localStorage.setItem('tm_user',JSON.stringify(d.user));
      setUser(d.user);
    }
    return d.user;
  };

  const logout=()=>clearSession();

  return <C.Provider value={{user,loading,auth,logout,setUser}}>{children}</C.Provider>;
}
