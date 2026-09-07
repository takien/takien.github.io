# takien.com

Arsip historis dan timeline personal **takien.com** yang direstorasi menggunakan [Astro](https://astro.build) dan dipublikasikan ke [GitHub Pages](https://pages.github.com/).

Repositori ini memuat:
- **800+ artikel & catatan** dari berbagai era (2006–2016, Facebook, Cektkp.com, w3magz, situskamu, imissu, dan dasargo).
- **Sisipan Timeline Hidup & Catatan Penulis Masa Kini**.
- **Koleksi Multimedia**: Desain Photoshop, Koleksi Foto, Arsip YouTube, dan TikTok.

---

## 💻 Menjalankan di Komputer Lokal

```bash
# Instalasi dependensi
npm install

# Menjalankan server dev di background
npx astro dev --background

# Cek status atau log server dev
npx astro dev status
npx astro dev logs

# Matikan server dev
npx astro dev stop
```

- **Akses Website Lokal:** [http://localhost:4321/](http://localhost:4321/)
- **Uji Build Produksi:** `npm run build`

---

## 🔄 Pembaruan Konten ke GitHub

Setiap kali Anda menambah tulisan baru atau mengubah konten:

```bash
git add .
git commit -m "Update konten takien.com"
git push
```

GitHub Actions akan otomatis mem-build dan memperbarui situs di GitHub Pages.
