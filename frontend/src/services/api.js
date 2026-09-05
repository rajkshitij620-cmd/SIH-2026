const rawBase = import.meta.env.VITE_API_BASE_URL || import.meta.env.VITE_API_URL || 'http://localhost:8000';
const BASE = rawBase.replace(/\/api\/?$/, '').replace(/\/$/, '');
const errorMessage=detail=>Array.isArray(detail)?detail.map(item=>item.msg||'Invalid input').join(' '):(typeof detail==='string'?detail:'Something went wrong')
const request=async(path,opts={})=>{const token=localStorage.getItem('tm_token');const res=await fetch(BASE+'/api'+path,{headers:{'Content-Type':'application/json',...(token?{Authorization:`Bearer ${token}`}:{})},...opts});const data=await res.json();if(!res.ok){if(res.status===401){localStorage.removeItem('tm_token');window.dispatchEvent(new Event('tm:session-expired'))}throw new Error(errorMessage(data.detail))}return data}
export const api={get:(p)=>request(p),post:(p,b)=>request(p,{method:'POST',body:JSON.stringify(b)}),put:(p,b)=>request(p,{method:'PUT',body:JSON.stringify(b)}),delete:(p)=>request(p,{method:'DELETE'}),url:(p)=>BASE+'/api'+p}
