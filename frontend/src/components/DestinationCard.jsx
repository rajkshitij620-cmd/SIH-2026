import {Link} from 'react-router-dom';
import {MapPin,Star,Users,ArrowRight} from 'lucide-react';

export default function DestinationCard({x,showWhy=true}){
  const crowdIsLow = x.crowd_score < 40;
  return (
    <article className="group relative flex flex-col overflow-hidden rounded-2xl border border-slate-200/90 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl hover:border-teal-400/50">
      <div className="relative h-48 w-full overflow-hidden bg-slate-900">
        <img 
          className="h-full w-full object-cover transition-transform duration-500 ease-out group-hover:scale-105" 
          src={x.image || 'https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=900&q=80'} 
          alt={x.name}
          loading="lazy"
          onError={(e)=>{
            e.currentTarget.onerror = null;
            e.currentTarget.src = 'https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=900&q=80';
          }}
        />
        <div className="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-slate-950/20 to-transparent" />
        
        <div className="absolute top-3 left-3 right-3 flex items-center justify-between gap-2">
          <span className="inline-flex items-center gap-1 rounded-full bg-slate-900/80 backdrop-blur-md px-2.5 py-1 text-xs font-semibold text-amber-300 shadow">
            <Star size={12} className="fill-amber-400 text-amber-400"/>
            {x.rating}
          </span>
          <span className={`inline-flex items-center gap-1 rounded-full px-2.5 py-1 text-xs font-medium backdrop-blur-md shadow ${
            crowdIsLow 
              ? 'bg-emerald-950/80 text-emerald-300 border border-emerald-500/30' 
              : 'bg-amber-950/80 text-amber-300 border border-amber-500/30'
          }`}>
            <Users size={12}/>
            {crowdIsLow ? 'Low Crowd' : 'Moderate Crowd'}
          </span>
        </div>

        <div className="absolute bottom-3 left-3 right-3">
          <h3 className="font-bold text-lg text-white drop-shadow-sm line-clamp-1">{x.name}</h3>
          <p className="flex items-center gap-1 text-xs font-medium text-slate-200/90">
            <MapPin size={12} className="text-teal-400"/>
            {x.location?.city || x.location?.state}, {x.location?.state}
          </p>
        </div>
      </div>

      <div className="flex flex-1 flex-col justify-between p-4">
        {x.categories?.length > 0 && (
          <div className="flex flex-wrap gap-1 mb-3">
            {x.categories.slice(0, 3).map((cat, i) => (
              <span key={i} className="rounded-md bg-teal-50 dark:bg-teal-950/50 px-2 py-0.5 text-[11px] font-medium text-teal-700 dark:text-teal-300 border border-teal-200/60 dark:border-teal-800/60">
                {cat}
              </span>
            ))}
          </div>
        )}

        {showWhy && x.why_recommended?.length > 0 && (
          <div className="mb-4 rounded-xl border-l-2 border-teal-500 bg-slate-50 dark:bg-slate-800/50 p-2.5 text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
            <p className="line-clamp-2">{x.why_recommended[0]}</p>
          </div>
        )}

        <div className="mt-auto flex items-center justify-between border-t border-slate-100 dark:border-slate-800 pt-3">
          <div>
            <span className="text-[10px] uppercase tracking-wider text-slate-400 font-semibold">Avg. Budget</span>
            <p className="text-sm font-bold text-slate-900 dark:text-slate-100">
              ₹{x.average_cost?.toLocaleString()} <span className="text-xs font-normal text-slate-500">/ day</span>
            </p>
          </div>
          <Link 
            className="inline-flex items-center gap-1 rounded-xl bg-teal-50 hover:bg-teal-600 dark:bg-teal-950/50 dark:hover:bg-teal-600 px-3 py-1.5 text-xs font-semibold text-teal-700 hover:text-white dark:text-teal-300 dark:hover:text-white transition-all duration-200 group-hover:bg-teal-600 group-hover:text-white" 
            to={`/destinations/${x.id}`}
          >
            <span>Explore</span>
            <ArrowRight size={13}/>
          </Link>
        </div>
      </div>
    </article>
  );
}

