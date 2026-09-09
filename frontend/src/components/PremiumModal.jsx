import { useState, useEffect } from 'react';
import { Crown, Check, Sparkles, Zap, X, CreditCard, QrCode, ArrowRight, CheckCircle2, Lock } from 'lucide-react';
import { api } from '../services/api';
import { useAuth } from '../context/AuthContext';

export default function PremiumModal({ isOpen, onClose, onSuccess, initialReason = '' }) {
  const { user, setUser } = useAuth();
  const [plans, setPlans] = useState([]);
  const [selectedPlan, setSelectedPlan] = useState('pro_monthly');
  const [loading, setLoading] = useState(false);
  const [paymentStep, setPaymentStep] = useState('plans'); // 'plans' | 'checkout' | 'success'
  const [paymentMethod, setPaymentMethod] = useState('upi'); // 'upi' | 'card' | 'demo'
  const [error, setError] = useState('');

  useEffect(() => {
    if (isOpen) {
      setPaymentStep('plans');
      setError('');
      api.get('/premium/plans')
        .then(res => {
          if (res.plans) setPlans(res.plans);
        })
        .catch(() => {
          // Fallback static plans if offline
          setPlans([
            {
              id: 'pro_monthly',
              name: 'TourMitra Pro Monthly',
              price: 0,
              original_price: 199,
              billing: '₹0 (Free Offer)',
              period: 'monthly',
              badge: 'Free Special Offer',
              popular: true,
              description: 'Unlock same-city TravelMate matchmaking & VIP group features for ₹0',
              features: [
                'Same Current City to Destination TravelMate Matching',
                'AI Compatibility Score & Mutual Match Connections',
                'Dedicated Group Room Chat & Shared Live Itinerary',
                'Golden VIP 👑 Profile Crown Badge',
                'Offline PDF Travel Itinerary Download',
                'High-Priority 24/7 Safety SOS & Support'
              ]
            },
            {
              id: 'pro_annual',
              name: 'TourMitra Pro Annual',
              price: 0,
              original_price: 1499,
              billing: '₹0 (Free Offer)',
              period: 'annual',
              badge: '100% Free VIP',
              popular: false,
              description: 'Full VIP access unlocked for all SIH participants & judges for ₹0',
              features: [
                'All Pro Monthly Features Included',
                '100% Free Special Access (₹0)',
                'Verified Annual Pro 👑 Badge',
                'Unlimited Trip Replans & AI Rerouting',
                'Exclusive Live Festival & Crowd Alerts',
                'Priority Smart Emergency Response'
              ]
            }
          ]);
        });
    }
  }, [isOpen]);

  if (!isOpen) return null;

  const currentPlanObj = plans.find(p => p.id === selectedPlan) || plans[0] || {
    id: 'pro_monthly',
    name: 'TourMitra Pro Monthly',
    price: 0
  };

  const handleActivate = async (method = paymentMethod) => {
    setLoading(true);
    setError('');
    try {
      const res = await api.post('/premium/upgrade', {
        plan_id: selectedPlan,
        payment_method: method
      });
      if (res.user) {
        setUser(prev => ({ ...prev, ...res.user, is_premium: true, premium_tier: selectedPlan }));
      }
      setPaymentStep('success');
      setTimeout(() => {
        if (onSuccess) onSuccess();
        onClose();
      }, 1600);
    } catch (err) {
      setError(err.message || 'Failed to activate premium membership. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/80 backdrop-blur-md animate-in fade-in duration-200">
      <div 
        className="relative w-full max-w-2xl max-h-[92vh] flex flex-col rounded-3xl bg-white dark:bg-slate-900 border border-amber-300/40 dark:border-amber-500/30 shadow-2xl shadow-amber-500/10 overflow-hidden"
        role="dialog"
        aria-modal="true"
      >
        {/* Glowing Top Banner */}
        <div className="relative bg-gradient-to-r from-amber-500 via-amber-600 to-yellow-500 px-6 py-5 text-white flex items-center justify-between overflow-hidden">
          <div className="absolute -right-6 -top-6 w-32 h-32 bg-white/10 rounded-full blur-xl pointer-events-none" />
          <div className="relative z-10 flex items-center gap-3">
            <div className="h-11 w-11 rounded-2xl bg-white/20 backdrop-blur-md flex items-center justify-center shadow-inner text-yellow-100">
              <Crown size={24} className="animate-bounce" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xs font-bold uppercase tracking-widest text-amber-100">TourMitra VIP</span>
                <span className="rounded-full bg-white/25 px-2 py-0.5 text-[10px] font-extrabold uppercase tracking-wide">Pro</span>
              </div>
              <h2 className="text-xl sm:text-2xl font-extrabold leading-tight">Unlock Same-City Group Matching</h2>
            </div>
          </div>

          <button
            type="button"
            onClick={onClose}
            className="rounded-full p-1.5 text-amber-100 hover:bg-white/20 hover:text-white transition"
            aria-label="Close"
          >
            <X size={20} />
          </button>
        </div>

        {/* Content Body */}
        <div className="flex-1 overflow-y-auto p-6 sm:p-7 space-y-6">
          {initialReason && (
            <div className="rounded-2xl border border-amber-200 dark:border-amber-900/60 bg-amber-50/80 dark:bg-amber-950/40 p-4 text-xs sm:text-sm text-amber-900 dark:text-amber-200 flex items-start gap-2.5">
              <Sparkles size={18} className="text-amber-600 shrink-0 mt-0.5" />
              <span>{initialReason}</span>
            </div>
          )}

          {paymentStep === 'plans' && (
            <>
              {/* Value Highlights */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50/60 dark:bg-slate-800/40 p-3.5 flex items-start gap-3">
                  <div className="h-8 w-8 rounded-xl bg-teal-100 dark:bg-teal-950/80 text-teal-700 dark:text-teal-300 grid place-items-center shrink-0">
                    <Zap size={16} />
                  </div>
                  <div>
                    <h4 className="text-xs font-bold text-slate-900 dark:text-white">Same-City Matching</h4>
                    <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">Connect with travelers from your exact city heading to same destination.</p>
                  </div>
                </div>

                <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50/60 dark:bg-slate-800/40 p-3.5 flex items-start gap-3">
                  <div className="h-8 w-8 rounded-xl bg-amber-100 dark:bg-amber-950/80 text-amber-700 dark:text-amber-300 grid place-items-center shrink-0">
                    <Crown size={16} />
                  </div>
                  <div>
                    <h4 className="text-xs font-bold text-slate-900 dark:text-white">👑 VIP Profile Badge</h4>
                    <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">Golden crown badge on your profile and TravelMate listings.</p>
                  </div>
                </div>
              </div>

              {/* Plan Cards */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {plans.filter(p => p.id !== 'free').map(p => {
                  const isSelected = selectedPlan === p.id;
                  return (
                    <div
                      key={p.id}
                      onClick={() => setSelectedPlan(p.id)}
                      className={`relative cursor-pointer rounded-2xl p-5 border-2 transition-all flex flex-col justify-between ${
                        isSelected
                          ? 'border-amber-500 bg-amber-50/40 dark:bg-amber-950/30 shadow-lg shadow-amber-500/10'
                          : 'border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700 bg-white dark:bg-slate-900'
                      }`}
                    >
                      {p.badge && (
                        <span className={`absolute -top-3 right-4 rounded-full px-2.5 py-0.5 text-[10px] font-extrabold uppercase tracking-wide shadow-sm ${
                          p.popular
                            ? 'bg-gradient-to-r from-amber-500 to-amber-600 text-white'
                            : 'bg-teal-600 text-white'
                        }`}>
                          {p.badge}
                        </span>
                      )}

                      <div>
                        <div className="flex items-center justify-between">
                          <h3 className="font-bold text-base text-slate-900 dark:text-white">{p.name}</h3>
                          <div className={`h-5 w-5 rounded-full border flex items-center justify-center ${
                            isSelected ? 'border-amber-600 bg-amber-500 text-white' : 'border-slate-300 dark:border-slate-700'
                          }`}>
                            {isSelected && <Check size={12} strokeWidth={3} />}
                          </div>
                        </div>

                        <div className="mt-3 flex items-baseline gap-1.5">
                          <span className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">₹{p.price}</span>
                          {p.original_price && (
                            <span className="text-xs text-slate-400 line-through">₹{p.original_price}</span>
                          )}
                          <span className="text-xs text-slate-500 dark:text-slate-400 font-medium">/{p.period === 'annual' ? 'year' : 'mo'}</span>
                        </div>

                        <p className="mt-2 text-xs text-slate-600 dark:text-slate-300">{p.description}</p>
                      </div>

                      <div className="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800 space-y-1.5">
                        {p.features?.slice(0, 4).map((f, i) => (
                          <div key={i} className="flex items-center gap-2 text-xs text-slate-700 dark:text-slate-200">
                            <Check size={13} className="text-amber-600 shrink-0" />
                            <span className="truncate">{f}</span>
                          </div>
                        ))}
                      </div>
                    </div>
                  );
                })}
              </div>

              {/* Action Buttons */}
              <div className="space-y-2 pt-2">
                <button
                  type="button"
                  onClick={() => setPaymentStep('checkout')}
                  className="btn w-full !py-3.5 !bg-gradient-to-r !from-amber-600 !via-amber-500 !to-yellow-500 text-white font-extrabold text-base shadow-lg shadow-amber-500/25 flex items-center justify-center gap-2 hover:scale-[1.01] transition"
                >
                  <Crown size={18} />
                  <span>Upgrade to {currentPlanObj.name} ({currentPlanObj.price === 0 ? 'Free · ₹0' : `₹${currentPlanObj.price}`})</span>
                  <ArrowRight size={16} />
                </button>

                {/* 1-Click Instant SIH Demo Activation */}
                <button
                  type="button"
                  onClick={() => handleActivate('demo_instant')}
                  disabled={loading}
                  className="w-full py-2.5 px-4 rounded-xl border border-teal-200 dark:border-teal-800/80 bg-teal-50/70 dark:bg-teal-950/40 text-teal-800 dark:text-teal-300 text-xs font-bold hover:bg-teal-100 dark:hover:bg-teal-900/60 transition flex items-center justify-center gap-1.5"
                >
                  <Sparkles size={14} />
                  <span>⚡ 1-Click Free Upgrade (SIH Judge Demo Mode)</span>
                </button>
              </div>
            </>
          )}

          {paymentStep === 'checkout' && (
            <div className="space-y-5 animate-in fade-in">
              <div className="flex items-center justify-between pb-3 border-b border-slate-100 dark:border-slate-800">
                <div>
                  <h3 className="font-bold text-lg text-slate-900 dark:text-white">{currentPlanObj.name}</h3>
                  <p className="text-xs text-slate-500">Total payable: <b className="text-emerald-700 dark:text-emerald-400 font-extrabold">{currentPlanObj.price === 0 ? '₹0 (100% Free Special Offer)' : `₹${currentPlanObj.price}`}</b></p>
                </div>
                <button
                  type="button"
                  onClick={() => setPaymentStep('plans')}
                  className="text-xs font-semibold text-teal-700 dark:text-teal-400 hover:underline"
                >
                  Change Plan
                </button>
              </div>

              {/* Payment Methods */}
              <div className="space-y-2">
                <label className="text-xs font-bold uppercase tracking-wider text-slate-600 dark:text-slate-300">Select Payment / Activation Method</label>
                <div className="grid grid-cols-2 gap-3">
                  <button
                    type="button"
                    onClick={() => setPaymentMethod('upi')}
                    className={`p-3.5 rounded-xl border-2 text-left flex items-center gap-3 transition ${
                      paymentMethod === 'upi'
                        ? 'border-amber-500 bg-amber-50/50 dark:bg-amber-950/40'
                        : 'border-slate-200 dark:border-slate-800'
                    }`}
                  >
                    <QrCode size={20} className={paymentMethod === 'upi' ? 'text-amber-600' : 'text-slate-400'} />
                    <div>
                      <p className="text-xs font-bold text-slate-900 dark:text-white">UPI / QR Code</p>
                      <p className="text-[10px] text-slate-500">GPay, PhonePe, Paytm (₹0)</p>
                    </div>
                  </button>

                  <button
                    type="button"
                    onClick={() => setPaymentMethod('card')}
                    className={`p-3.5 rounded-xl border-2 text-left flex items-center gap-3 transition ${
                      paymentMethod === 'card'
                        ? 'border-amber-500 bg-amber-50/50 dark:bg-amber-950/40'
                        : 'border-slate-200 dark:border-slate-800'
                    }`}
                  >
                    <CreditCard size={20} className={paymentMethod === 'card' ? 'text-amber-600' : 'text-slate-400'} />
                    <div>
                      <p className="text-xs font-bold text-slate-900 dark:text-white">Instant / Card</p>
                      <p className="text-[10px] text-slate-500">Zero-fee Activation</p>
                    </div>
                  </button>
                </div>
              </div>

              {/* Payment Preview */}
              {paymentMethod === 'upi' ? (
                <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950/50 p-4 text-center space-y-3">
                  <div className="inline-block p-3 bg-white rounded-2xl shadow-sm border border-slate-200">
                    <img 
                      src={`https://api.qrserver.com/v1/create-qr-code/?size=140x140&data=upi://pay?pa=tourmitra@upi&pn=TourMitra%20Pro&am=${currentPlanObj.price}&cu=INR`} 
                      alt="TourMitra UPI QR" 
                      className="w-32 h-32 mx-auto object-contain"
                    />
                  </div>
                  <div>
                    <p className="text-xs font-bold text-slate-800 dark:text-slate-200">Scan & Activate (Payable: ₹{currentPlanObj.price})</p>
                    <p className="text-[11px] text-slate-500">UPI ID: <span className="font-mono font-semibold text-teal-600">tourmitra@upi</span></p>
                  </div>
                </div>
              ) : (
                <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950/50 p-4 space-y-2.5">
                  <input className="input text-xs" placeholder="Card Number (Demo: 4532 •••• •••• 8890)" defaultValue="4532 8921 4452 8890" disabled />
                  <div className="grid grid-cols-2 gap-2">
                    <input className="input text-xs" placeholder="MM/YY" defaultValue="12/28" disabled />
                    <input className="input text-xs" placeholder="CVV" defaultValue="789" disabled />
                  </div>
                </div>
              )}

              {error && <p className="text-xs text-red-600 dark:text-red-400 font-medium">{error}</p>}

              <div className="flex gap-3">
                <button
                  type="button"
                  onClick={() => setPaymentStep('plans')}
                  className="btn-ghost flex-1"
                  disabled={loading}
                >
                  Back
                </button>
                <button
                  type="button"
                  onClick={() => handleActivate()}
                  disabled={loading}
                  className="btn flex-2 !bg-gradient-to-r !from-amber-600 !to-yellow-500 text-white font-bold"
                >
                  {loading ? 'Activating Pro…' : currentPlanObj.price === 0 ? 'Activate Pro Membership Free (₹0) 👑' : `Pay ₹${currentPlanObj.price} & Activate Pro 👑`}
                </button>
              </div>

              <p className="text-[10px] text-center text-slate-400 flex items-center justify-center gap-1">
                <Lock size={11} /> 256-Bit Encrypted Simulated Test Payment Gateway (SIH Demo)
              </p>
            </div>
          )}

          {paymentStep === 'success' && (
            <div className="py-8 text-center space-y-4 animate-in zoom-in-95">
              <div className="h-16 w-16 mx-auto rounded-full bg-emerald-100 dark:bg-emerald-950 text-emerald-600 dark:text-emerald-300 grid place-items-center shadow-lg">
                <CheckCircle2 size={36} />
              </div>
              <div>
                <span className="text-2xl">👑</span>
                <h3 className="text-2xl font-extrabold text-slate-900 dark:text-white mt-1">Welcome to TourMitra Pro!</h3>
                <p className="text-sm text-slate-600 dark:text-slate-300 mt-1">
                  Your VIP membership is now active. You can now match with TravelMates from your same city!
                </p>
              </div>
              <div className="inline-flex items-center gap-2 rounded-full bg-amber-50 dark:bg-amber-950/60 border border-amber-300 dark:border-amber-700 px-4 py-1.5 text-xs font-bold text-amber-800 dark:text-amber-200">
                <Crown size={14} className="text-amber-500" />
                <span>VIP Pro Member Activated</span>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

