import React, { useState } from 'react';

// Static translation strings for UI Chrome
const translations = {
  en: {
    title: "90-Second Profile",
    desc: "Tell us about yourself. All fields are optional.",
    findBtn: "Find Opportunities",
    loading: "Searching government databases...",
    dashboard: "Eligible Opportunities",
    noMatches: "No opportunities match your current profile.",
    source: "Official Source"
  },
  hi: {
    title: "90-सेकंड प्रोफ़ाइल",
    desc: "अपने बारे में बताएं। सभी फ़ील्ड वैकल्पिक हैं।",
    findBtn: "अवसर खोजें",
    loading: "सरकारी डेटाबेस खोजा जा रहा है...",
    dashboard: "योग्य अवसर",
    noMatches: "आपकी वर्तमान प्रोफ़ाइल से कोई अवसर मेल नहीं खाता।",
    source: "आधिकारिक स्रोत"
  }
};

export default function App() {
  const [lang, setLang] = useState('en');
  const [profile, setProfile] = useState({ age: '', income: '', state: '', category: '', education: '' });
  const [results, setResults] = useState([]);
  const [hasSearched, setHasSearched] = useState(false);
  const [loading, setLoading] = useState(false);

  const t = translations[lang];

  const handleChange = (e) => {
    setProfile({ ...profile, [e.target.name]: e.target.value });
  };

  const fetchOpportunities = async () => {
    setLoading(true);
    setHasSearched(true);
    
    // Construct the query string for Member 2's API
    const params = new URLSearchParams({
      age: profile.age,
      income: profile.income,
      state: profile.state,
      category: profile.category,
      education: profile.education
    });

    try {
      const response = await fetch(`http://127.0.0.1:5000/api/match?${params}`);
      const data = await response.json();
      setResults(data.matches || []);
    } catch (error) {
      console.error("API Connection Failed. Ensure app.py is running on port 5000.");
      setResults([]);
    }
    
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-slate-50 p-6 font-sans text-slate-800">
      <div className="max-w-xl mx-auto space-y-6">
        
        <div className="flex justify-end">
          <button onClick={() => setLang(lang === 'en' ? 'hi' : 'en')} className="px-4 py-2 bg-white border border-slate-200 rounded-lg text-sm font-semibold">
            {lang === 'en' ? 'हिंदी' : 'English'}
          </button>
        </div>

        <div className="bg-white rounded-3xl shadow-sm border border-slate-200 p-6 md:p-8">
          <h1 className="text-2xl font-bold">{t.title}</h1>
          <p className="text-slate-500 text-sm mt-1 mb-6">{t.desc}</p>

          <form className="space-y-4" onSubmit={e => { e.preventDefault(); fetchOpportunities(); }}>
            <div className="grid grid-cols-2 gap-4">
              <input type="number" name="age" value={profile.age} onChange={handleChange} placeholder="Age" className="w-full px-3 py-2 border rounded-xl" />
              <input type="number" name="income" value={profile.income} onChange={handleChange} placeholder="Income (INR)" className="w-full px-3 py-2 border rounded-xl" />
            </div>
            
            <select name="state" value={profile.state} onChange={handleChange} className="w-full px-3 py-2 border rounded-xl bg-white">
              <option value="">State / Domicile</option>
              <option value="Maharashtra">Maharashtra</option>
              <option value="Delhi">Delhi</option>
            </select>
            
            <select name="category" value={profile.category} onChange={handleChange} className="w-full px-3 py-2 border rounded-xl bg-white">
              <option value="">Reservation Category</option>
              <option value="General">General</option>
              <option value="OBC">OBC</option>
              <option value="SC">SC</option>
              <option value="ST">ST</option>
            </select>
            
            <select name="education" value={profile.education} onChange={handleChange} className="w-full px-3 py-2 border rounded-xl bg-white">
              <option value="">Highest Education</option>
              <option value="10th Pass">10th Pass</option>
              <option value="12th Pass">12th Pass</option>
              <option value="Graduate">Graduate</option>
            </select>

            <button type="submit" className="w-full mt-4 bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-xl transition-colors">
              {t.findBtn}
            </button>
          </form>
        </div>

        {hasSearched && (
          <div className="space-y-4">
            <h2 className="text-xl font-bold">{t.dashboard}</h2>
            {loading ? (
              <p className="text-center text-slate-500 py-8">{t.loading}</p>
            ) : results.length > 0 ? (
              results.map(item => (
                <div key={item.id} className="bg-white rounded-2xl border border-slate-200 p-5">
                  <span className="text-xs font-bold text-blue-600 bg-blue-50 px-2 py-1 rounded-md uppercase">{item.type.replace('_', ' ')}</span>
                  <h3 className="text-lg font-bold mt-2">{item.title[lang]}</h3>
                  <a href={item.official_link} target="_blank" rel="noreferrer" className="inline-block mt-4 bg-slate-900 text-white px-4 py-2 rounded-lg text-sm font-semibold hover:bg-slate-800">
                    {t.source}
                  </a>
                </div>
              ))
            ) : (
              <p className="text-center text-slate-500 py-8">{t.noMatches}</p>
            )}
          </div>
        )}
      </div>
    </div>
  );
}