// ZeaZDev [Frontend Screen Settings API Keys] //
// Project: Auto Bot Trader i18n //
// Version: 1.0.0 (Omega Scaffolding) //
// Author: ZeaZDev Meta-Intelligence (Generated) //
// --- DO NOT EDIT HEADER --- //
"use client";

import React, { useState } from 'react';
import { initI18n } from '../../i18n/client';
import { useTranslation } from 'react-i18next';

export default function SettingsPage({ params }: { params: { lng: string } }) {
  initI18n(params.lng);
  const { t } = useTranslation('translation');
  const [exchange, setExchange] = useState('binance');
  const [apiKey, setApiKey] = useState('');
  const [apiSecret, setApiSecret] = useState('');
  const [status, setStatus] = useState<string | null>(null);

  const save = () => {
    fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000'}/exchange/keys`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ exchange, api_key: apiKey, api_secret: apiSecret })
    })
      .then(r => r.json())
      .then(d => setStatus('OK'))
      .catch(e => setStatus(e.message));
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>{t('settings.title')}</h1>
      <div>
        <label>{t('settings.exchange')}</label>
        <select value={exchange} onChange={e => setExchange(e.target.value)}>
          <option value="binance">Binance</option>
          <option value="bybit">Bybit</option>
        </select>
      </div>
      <div>
        <label>{t('settings.api_key')}</label>
        <input value={apiKey} onChange={e => setApiKey(e.target.value)} type="password" />
      </div>
      <div>
        <label>{t('settings.api_secret')}</label>
        <input value={apiSecret} onChange={e => setApiSecret(e.target.value)} type="password" />
      </div>
      <button onClick={save}>{t('settings.submit')}</button>
      {status && <div>Status: {status}</div>}
    </div>
  );
}