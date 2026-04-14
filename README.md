Attendance QA Automation

Automation testing untuk fitur attendance (task + absensi) menggunakan Selenium + Pytest.

== [[Requirements]] ==
Python 3.10+
Google Chrome (latest)
ChromeDriver (sesuai versi Chrome)

== [[Setup]] ==
1. Clone repository
git clone <repo-url>
masuk kedalam cd clone
2. Buat virtual environment
python -m venv venv
3. Aktifkan environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
pip install selenium pytest pytest-html

== [[ Run Test]] ==

Pastikan aplikasi frontend berjalan:

cd ../attendance-app
npm run dev

Kemudian jalankan test:

cd ../attendance-qa
pytest

== [[Report]] ==

Hasil test akan tersedia di:

reports/report.html

Buka file tersebut di browser untuk melihat hasil detail.

== [[Test Coverage]] ==

Login user
Tambah task
Checklist task
Absensi siswa

== [[Catatan]] ==

Pastikan data-testid sudah tersedia di frontend (Opsional untuk stability)

== [[Tech Stack]] ==

Selenium
Pytest
Python
