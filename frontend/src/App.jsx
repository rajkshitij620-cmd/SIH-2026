import {useEffect} from 'react';
import {Routes,Route,Navigate,useLocation} from 'react-router-dom';import Layout from './layouts/Layout';import * as P from './pages/Pages';import {useAuth} from './context/AuthContext';
function Protected({children}){const {user,loading}=useAuth(),location=useLocation();if(loading)return <div className="shell py-12">Loading…</div>;return user?children:<Navigate to="/register" replace state={{from:location.pathname}}/>}

const pageTitles={
  '/':'Tourmitra',
  '/login':'Login | Tourmitra',
  '/register':'Sign Up | Tourmitra',
  '/plan':'Plan Your Trip | Tourmitra',
  '/tour-guide':'Tour Guide | Tourmitra',
  '/previous-trips':'Previous Trips | Tourmitra',
  '/saved-tours':'Saved Tours | Tourmitra',
  '/find-travelers':'Find TravelMates | Tourmitra',
  '/requests':'Group Requests | Tourmitra',
  '/groups':'My Travel Groups | Tourmitra',
  '/explore':'Explore Destinations | Tourmitra',
  '/assistant':'AI Assistant | Tourmitra',
  '/saved':'Saved Itineraries | Tourmitra',
};

function PageTitle(){
  const {pathname}=useLocation();
  useEffect(()=>{
    const title=pathname.startsWith('/itinerary/')?'Your Itinerary | Tourmitra':pathname.startsWith('/destinations/')?'Destination Details | Tourmitra':pathname.startsWith('/travelers/')?'Traveller Profile | Tourmitra':pageTitles[pathname]||'Tourmitra';
    document.title=title;
  },[pathname]);
  return null;
}

export default function App(){const secure=(page)=><Protected>{page}</Protected>;return <Layout><PageTitle/><Routes><Route path="/" element={<P.Home/>}/><Route path="/login" element={<P.Auth/>}/><Route path="/register" element={<P.Auth register/>}/><Route path="/plan" element={secure(<P.Planner/> )}/><Route path="/tour-guide" element={secure(<P.TourGuide/> )}/><Route path="/previous-trips" element={secure(<P.PreviousTrips/> )}/><Route path="/saved-tours" element={secure(<P.Saved/> )}/><Route path="/find-travelers" element={secure(<P.FindTravelers/> )}/><Route path="/requests" element={secure(<P.GroupRequests/> )}/><Route path="/groups" element={secure(<P.TravelGroups/> )}/><Route path="/travel-plan" element={secure(<P.LatestGroupTravelPlan/> )}/><Route path="/travel-plan/:id" element={secure(<P.GroupTravelPlan/> )}/><Route path="/travelers/:id" element={secure(<P.TravellerProfile/> )}/><Route path="/itinerary/:id" element={secure(<P.Itinerary/> )}/><Route path="/explore" element={secure(<P.Explore/> )}/><Route path="/assistant" element={secure(<P.Assistant/> )}/><Route path="/saved" element={secure(<P.Saved/> )}/><Route path="/destinations/:id" element={secure(<P.Detail/> )}/><Route path="*" element={<Navigate to="/" replace/>}/></Routes></Layout>}
