import { useState } from 'react'
import axios from 'axios'
import './App.css'

const API_URL = import.meta.env.VITE_API_URL || '/api/predict'

const defaultForm = {
  gender: 'Female', SeniorCitizen: 0, Partner: 'Yes', Dependents: 'No',
  tenure: 1, PhoneService: 'No', MultipleLines: 'No phone service',
  InternetService: 'DSL', OnlineSecurity: 'No', OnlineBackup: 'Yes',
  DeviceProtection: 'No', TechSupport: 'No', StreamingTV: 'No',
  StreamingMovies: 'No', Contract: 'Month-to-month', PaperlessBilling: 'Yes',
  PaymentMethod: 'Electronic check', MonthlyCharges: 29.85, TotalCharges: 29.85,
}

const Sel = ({ label, name, value, onChange, options }) => (
  <div className="f">
    <label>{label}</label>
    <select name={name} value={value} onChange={onChange}>
      {options.map(o => <option key={o} value={o}>{o}</option>)}
    </select>
  </div>
)

const Num = ({ label, name, value, onChange, step = 1 }) => (
  <div className="f">
    <label>{label}</label>
    <input type="number" name={name} value={value} onChange={onChange} step={step} min="0" />
  </div>
)

export default function App() {
  const [form, setForm] = useState(defaultForm)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleChange = ({ target: { name, value } }) =>
    setForm(p => ({
      ...p,
      [name]: ['tenure', 'SeniorCitizen'].includes(name) ? +value
        : ['MonthlyCharges', 'TotalCharges'].includes(name) ? +value : value
    }))

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true); setError(null); setResult(null)
    try { setResult((await axios.post(API_URL, form)).data) }
    catch { setError('Cannot reach API — run start_server.ps1') }
    finally { setLoading(false) }
  }

  const rc = result?.risk_level === 'High' ? '#ef4444'
    : result?.risk_level === 'Medium' ? '#f59e0b' : '#10b981'
  const pct = result ? (result.churn_probability * 100).toFixed(1) : 0

  return (
    <div className="shell">
      {/* ── HEADER ── */}
      <header className="hdr">
        <div className="hdr-l">
          <span className="logo">⚡ ChurnGuard<em> AI</em></span>
          <span className="badge">v1.0</span>
        </div>
        <span className="hdr-meta">Logistic Regression · Balanced · Recall 78%</span>
        <span className={`dot ${result ? 'blue' : 'green'}`}>
          {loading ? '⏳' : result ? '✅ Done' : '● Live'}
        </span>
      </header>

      {/* ── MAIN ── */}
      <main className="main">

        {/* ══ LEFT: FORM ══ */}
        <form className="form" onSubmit={handleSubmit}>
          <div className="sec-hd">Demographics</div>
          <div className="g4">
            <Sel label="Gender" name="gender" value={form.gender} onChange={handleChange} options={['Female','Male']}/>
            <Sel label="Senior" name="SeniorCitizen" value={form.SeniorCitizen} onChange={handleChange} options={[0,1]}/>
            <Sel label="Partner" name="Partner" value={form.Partner} onChange={handleChange} options={['Yes','No']}/>
            <Sel label="Dependents" name="Dependents" value={form.Dependents} onChange={handleChange} options={['Yes','No']}/>
          </div>

          <div className="sec-hd">Account & Billing</div>
          <div className="g4">
            <Num label="Tenure (mo)" name="tenure" value={form.tenure} onChange={handleChange}/>
            <Sel label="Contract" name="Contract" value={form.Contract} onChange={handleChange} options={['Month-to-month','One year','Two year']}/>
            <Num label="Monthly ($)" name="MonthlyCharges" value={form.MonthlyCharges} onChange={handleChange} step={0.01}/>
            <Num label="Total ($)" name="TotalCharges" value={form.TotalCharges} onChange={handleChange} step={0.01}/>
          </div>
          <div className="g2">
            <Sel label="Paperless Billing" name="PaperlessBilling" value={form.PaperlessBilling} onChange={handleChange} options={['Yes','No']}/>
            <Sel label="Payment Method" name="PaymentMethod" value={form.PaymentMethod} onChange={handleChange}
              options={['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)']}/>
          </div>

          <div className="sec-hd">Services</div>
          <div className="g4">
            <Sel label="Phone" name="PhoneService" value={form.PhoneService} onChange={handleChange} options={['Yes','No']}/>
            <Sel label="Multi Lines" name="MultipleLines" value={form.MultipleLines} onChange={handleChange} options={['Yes','No','No phone service']}/>
            <Sel label="Internet" name="InternetService" value={form.InternetService} onChange={handleChange} options={['DSL','Fiber optic','No']}/>
            <Sel label="Online Security" name="OnlineSecurity" value={form.OnlineSecurity} onChange={handleChange} options={['Yes','No','No internet service']}/>
          </div>
          <div className="g4">
            <Sel label="Backup" name="OnlineBackup" value={form.OnlineBackup} onChange={handleChange} options={['Yes','No','No internet service']}/>
            <Sel label="Device Protect." name="DeviceProtection" value={form.DeviceProtection} onChange={handleChange} options={['Yes','No','No internet service']}/>
            <Sel label="Tech Support" name="TechSupport" value={form.TechSupport} onChange={handleChange} options={['Yes','No','No internet service']}/>
            <Sel label="Streaming TV" name="StreamingTV" value={form.StreamingTV} onChange={handleChange} options={['Yes','No','No internet service']}/>
          </div>
          <div className="g4">
            <Sel label="Streaming Movies" name="StreamingMovies" value={form.StreamingMovies} onChange={handleChange} options={['Yes','No','No internet service']}/>
          </div>

          <button className="btn" type="submit" disabled={loading}>
            {loading ? <><span className="spin"/> Predicting…</> : '⚡ Predict Churn Risk'}
          </button>
        </form>

        {/* ══ RIGHT: RESULT ══ */}
        <aside className="result">

          {!result && !error && (
            <div className="idle">
              <div className="idle-icon">🎯</div>
              <h3>Ready to Predict</h3>
              <p>Fill in the customer profile and click <strong>Predict Churn Risk</strong></p>
            </div>
          )}

          {error && (
            <div className="idle">
              <div className="idle-icon">⚠️</div>
              <h3>Connection Error</h3>
              <p>{error}</p>
            </div>
          )}

          {result && (
            <>
              {/* Ring */}
              <div className="ring" style={{'--rc': rc, '--pct': `${result.churn_probability * 100}%`}}>
                <div className="ring-inner">
                  <span className="ring-pct">{Math.round(result.churn_probability * 100)}<small>%</small></span>
                  <span className="ring-lbl">Churn Risk</span>
                </div>
              </div>

              {/* Verdict */}
              <div className="verdict" style={{color: rc}}>
                {result.risk_level === 'High' ? '🔴' : result.risk_level === 'Medium' ? '🟡' : '🟢'}&nbsp;
                {result.risk_level} Risk · Will Churn: <strong>{result.churn_prediction}</strong>
              </div>

              {/* Bar */}
              <div className="bar-wrap">
                <div className="bar-track">
                  <div className="bar-fill" style={{width:`${pct}%`, background: rc}}/>
                </div>
                <div className="bar-ends"><span>0%</span><span style={{color:rc,fontWeight:700}}>{pct}%</span><span>100%</span></div>
              </div>

              {/* Action */}
              <div className="action" style={{borderColor:`${rc}44`,background:`${rc}0d`}}>
                <strong>💡 Action</strong>
                <p>
                  {result.risk_level === 'High' && 'Trigger retention campaign. Offer 25% discount or free contract upgrade immediately.'}
                  {result.risk_level === 'Medium' && 'Schedule a proactive check-in call. Consider a loyalty bundle offer.'}
                  {result.risk_level === 'Low' && 'Customer is stable. Standard engagement. No action required.'}
                </p>
              </div>

              {/* Pipeline trace */}
              <div className="pipe">
                {['Input','Pydantic','Scaler','OneHot','Model','Output'].map((s,i,a) => (
                  <span key={s}><span className="ps">{s}</span>{i<a.length-1 && <span className="pa">›</span>}</span>
                ))}
              </div>

              {/* Stats row */}
              <div className="stats">
                <div className="stat"><span>Model</span><b>Logistic</b></div>
                <div className="stat"><span>Recall</span><b style={{color:'#10b981'}}>78%</b></div>
                <div className="stat"><span>Accuracy</span><b>74%</b></div>
              </div>
            </>
          )}
        </aside>
      </main>
    </div>
  )
}
