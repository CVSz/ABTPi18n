# SECURITY MODEL

## หลักการเข้ารหัส
- ใช้ AES-GCM (Authenticated Encryption)
- Key ขนาด: 256-bit (Base64 ใน ENV)
- IV แบบสุ่ม 96-bit ต่อการเข้ารหัส

## Lifecycle
1. รับ API Key/Secret ผ่าน HTTPS → ไม่ Log ค่า plaintext
2. เรียก `encrypt_data()` → ส่งออก ciphertext และ iv (base64)
3. เก็บในตาราง `ExchangeKey`
4. ใช้ตอนต้องสร้าง instance ของ CCXT → decrypt → ใส่ memory → ไม่บันทึกลง log
5. หลังใช้งานไม่ Cache ระยะยาว

## การป้องกัน
- ENV `ENCRYPTION_KEY` ต้องมาจาก Secret Manager
- Rotate Key (แนะนำทุก 90 วัน) → ต้องมี Migration Re-Encrypt
- เพิ่ม HMAC ชั้นสอง (Roadmap Phase 5)
- ป้องกัน Replay: GCM Tag ตรวจสอบถูก

## แนวทาง Hardening
- เปิด HTTP Security Headers บน Frontend (Next.js Middleware)
- เปิด Rate Limit /auth และ /exchange/keys
- ใช้ JWT สำหรับ Session (ลงนามด้วย Private Key)
- เพิ่ม Database Row-Level Encryption (เสริมในอนาคต)