import os
import re
import shutil

shutil.copy('index.html', 'id.html')

with open('id.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('lang="en"', 'lang="id"')

html = html.replace(
    '''<span class="text-blue-600 font-bold select-none">EN</span>
                    <span class="text-slate-300">|</span>
                    <a href="id.html" class="text-slate-500 hover:text-blue-600 transition-colors font-semibold">ID</a>''',
    '''<a href="index.html" class="text-slate-500 hover:text-blue-600 transition-colors font-semibold">EN</a>
                    <span class="text-slate-300">|</span>
                    <span class="text-blue-600 font-bold select-none">ID</span>'''
)

html = html.replace(
    '''<a href="id.html" class="text-sm font-bold text-slate-500 hover:text-blue-600">ID</a>''',
    '''<a href="index.html" class="text-sm font-bold text-slate-500 hover:text-blue-600">EN</a>'''
)

def t(eng, ind):
    global html
    # Pattern cleanly matches words irrespective of how many spaces/newlines are between them
    pattern = r'\s+'.join(re.escape(word) for word in eng.split())
    html = re.sub(pattern, ind, html, flags=re.IGNORECASE)

# Simple replacements (using replace)
exact_replacements = {
    "Smart Automation for Jakarta Enterprises": "Otomatisasi Cerdas untuk Perusahaan di Jakarta",
    "Intelligent Workflow Engine": "Mesin Alur Kerja Cerdas",
    "Transforming Chaos": "Mengubah Kekacauan",
    "Schedule a Consultation": "Jadwalkan Konsultasi",
    "Ready to Scale with Precision?": "Siap Berkembang dengan Presisi?",
    "Contact Our Team": "Hubungi Tim Kami",
    ">Efficiency<": ">Efisiensi<",
    ">Core <": ">Layanan <",
    ">Services<": ">Utama<",
    ">Process<": ">Proses<",
    ">Solutions<": ">Solusi<",
    ">Consultation<": ">Konsultasi<",
    ">Company<": ">Perusahaan<",
    ">Resources<": ">Sumber Daya<",
    ">Partner Portal<": ">Portal Mitra<",
    ">Documentation<": ">Dokumentasi<",
    ">Privacy Policy<": ">Kebijakan Privasi<",
    "All rights reserved.": "Hak cipta dilindungi.",
    ">Intelligent Document Processing<": ">Pemrosesan Dokumen Cerdas<",
    ">Autonomous Business Logic<": ">Logika Bisnis Otonom<",
    ">Real-time Executive Insights<": ">Wawasan Eksekutif Real-time<",
}

for eng, ind in exact_replacements.items():
    html = html.replace(eng, ind)

t("Into Precision.", "Menjadi Presisi.")
t("The Journey to", "Perjalanan Menuju")

t("We bridge the gap between manual labor and intelligent operations, helping sophisticated businesses achieve 24/7 autonomous efficiency through cutting-edge AI-Backend systems.", "Kami menjembatani kesenjangan antara pekerjaan manual dan operasi cerdas, membantu perusahaan Indonesia mencapai efisiensi otonom 24/7 melalui sistem AI-Backend mutakhir.")

t("A streamlined, 3-step professional methodology designed for minimal disruption and maximum scalability.", "Metodologi profesional 3 langkah yang dirancang untuk gangguan minimal dan skalabilitas operasional maksimum.")

t("We comprehensively assess your current fragmented business logic. Our experts identify operational bottlenecks and pinpoint exactly where manual labor can be entirely replaced by precision automation.", "Kami menilai logika bisnis Anda secara komprehensif. Pakar kami menentukan dengan tepat di mana pekerjaan manual dapat sepenuhnya diganti dengan otomatisasi presisi.")

t("We act as the bridge between your isolated software tools. By deploying our secure AI-Backend, we connect your entire tech stack into a single, cohesive, intelligently communicating ecosystem.", "Dengan menerapkan AI-Backend kami yang aman, kami menghubungkan seluruh alat perangkat lunak Anda menjadi satu ekosistem yang saling berkomunikasi.")

t("Automation is continuously refined. We don't just build pipelines; we optimize them for dynamic scaling, ensuring your business logic operates autonomously with zero downtime 24/7.", "Kami tidak hanya membangun jaringan; kami mengoptimalkannya untuk penskalaan dinamis, memastikan logika bisnis Anda beroperasi secara otonom tanpa henti 24/7.")

t("Tailored automation pillars engineered for executives driving digital transformation.", "Pilar otomatisasi yang dirancang khusus untuk para eksekutif yang mendorong transformasi digital.")

t("Stop manual data entry. We deploy advanced Smart Automation to flawlessly extract, structure, and route critical data from dynamic online forms, financial records, PDFs, and physical receipts directly into your databases.", "Hentikan entri data manual. Kami menerapkan otomatisasi tingkat lanjut untuk mengekstrak dan merutekan data penting dari formulir online dan PDF secara otomatis langsung ke database Anda.")

t("Siloed applications kill efficiency. We architect sophisticated AI-Backends that serve as the central nervous system of your company, dictating seamless conditional logic across your entire suite of fragmented tools.", "Kami merancang AI-Backend canggih yang berfungsi sebagai sistem saraf pusat organisasi Anda, mengatur puluhan parameter dan logika bisnis yang rumit.")

t("Eliminate guesswork and reporting lag. We transform raw, sprawling operational data streams into immaculate, automated dashboards in real-time, empowering executives with undeniable clarity.", "Hilangkan kelambatan pelaporan. Kami menyajikan aliran data operasional mentah menjadi dasbor otomatis secara real-time, memberi eksekutif kejelasan yang tak terbantahkan.")

t("Book a private consultation with our Jakarta-based automation engineers to audit your workflow architecture.", "Jadwalkan konsultasi pribadi dengan tim konsultan otomatisasi kami yang berbasis di Jakarta.")

with open('id.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Regex Fixed and id.html Generated")
