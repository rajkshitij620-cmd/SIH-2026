const rawBase = import.meta.env.VITE_API_BASE_URL || import.meta.env.VITE_API_URL || 'http://localhost:8000';
const BASE = rawBase.replace(/\/api\/?$/, '').replace(/\/$/, '');

const errorMessage = detail => {
  if (Array.isArray(detail)) {
    return detail.map(item => item.msg || item.loc?.join('.') || 'Invalid input').join('; ');
  }
  return typeof detail === 'string' ? detail : 'Something went wrong. Please retry.';
};

const wait = ms => new Promise(resolve => setTimeout(resolve, ms));

const request = async (path, opts = {}, retries = 2) => {
  const token = localStorage.getItem('tm_token');
  const headers = {
    'Content-Type': 'application/json',
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
    ...(opts.headers || {})
  };

  try {
    const res = await fetch(BASE + '/api' + path, {
      ...opts,
      headers
    });

    let data;
    try {
      data = await res.json();
    } catch {
      data = { detail: res.statusText || 'Server response error' };
    }

    if (!res.ok) {
      if (res.status === 401) {
        localStorage.removeItem('tm_token');
        window.dispatchEvent(new Event('tm:session-expired'));
      }
      throw new Error(errorMessage(data.detail));
    }
    return data;
  } catch (err) {
    if (retries > 0 && (err.name === 'TypeError' || err.message?.includes('fetch') || err.message?.includes('NetworkError'))) {
      // Backend might be waking up on Render free tier, wait 1.5s and retry automatically
      await wait(1500);
      return request(path, opts, retries - 1);
    }
    throw err;
  }
};

export const api = {
  get: (p) => request(p),
  post: (p, b) => request(p, { method: 'POST', body: JSON.stringify(b) }),
  put: (p, b) => request(p, { method: 'PUT', body: JSON.stringify(b) }),
  delete: (p) => request(p, { method: 'DELETE' }),
  url: (p) => BASE + '/api' + p
};
