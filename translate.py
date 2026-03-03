import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Language Toggle to index.html
html_updated_en = html.replace(
    '<a href="#consultation"',
    '''<div class="flex items-center space-x-2 border-l border-slate-300 pl-6 mr-6">
                    <span class="text-blue-600 font-bold select-none">EN</span>
                    <span class="text-slate-300">|</span>
                    <a href="id.html" class="text-slate-500 hover:text-blue-600 transition-colors font-semibold">ID</a>
                </div>
                <a href="#consultation"'''
)
# same for mobile
html_updated_en = html_updated_en.replace(
    '<!-- Mobile Menu Button -->\n            <button class="md:hidden',
    '''<!-- Mobile Menu Button & Lang -->
            <div class="flex items-center space-x-4 md:hidden">
                <a href="id.html" class="text-sm font-bold text-slate-500 hover:text-blue-600">ID</a>
                <button class="md:hidden'''
)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_updated_en)

html_id = html_updated_en.replace('lang="en"', 'lang="id"')

# Function to replace text gracefully across newlines
def trans(eng, ind):
    global html_id
    pattern = re.escape(eng).replace(r'\ ', r'\s+')
    html_id = re.sub(pattern, ind, html_id)

# The long paragraphs: I can just find them using the start and end of the strings!
def trans_para(start, end, replacement):
    global html_id
    pattern = re.escape(start) + r'[\s\S]*?' + re.escape(end)
    html_id = re.sub(pattern, replacement, html_id)

trans("Intelligent Workflow Engine", "Mesin Alur Kerja Cerdas")
trans("Transforming Chaos", "Mengubah Kekacauan")
trans("Into Precision.", "Menjadi Presisi.")
trans("Schedule a Consultation", "Jadwalkan Konsultasi")
trans("The Journey to ", "Perjalanan Menuju ")
trans(">Efficiency<", ">Efisiensi<")
trans(">Core <", ">Layanan <")
trans(">Services<", ">Utama<")
trans(">Process<", ">Proses<")
trans(">Solutions<", ">Solusi<")
trans(">Consultation<", ">Konsultasi<")
trans(">Company<", ">Perusahaan<")
trans(">Resources<", ">Sumber Daya<")
trans(">Partner Portal<", ">Portal Mitra<")
trans(">Documentation<", ">Dokumentasi<")
trans(">Privacy Policy<", ">Kebijakan Privasi<")
trans("All rights reserved.", "Hak cipta dilindungi.")
trans("Ready to Scale with Precision?", "Siap Berkembang dengan Presisi?")
trans("Contact Our Team", "Hubungi Tim Kami")

trans_para("We bridge the gap", "AI-Backend systems.", "Kami menjembatani kesenjangan antara pekerjaan manual dan operasi cerdas, membantu perusahaan Indonesia mencapai efisiensi otonom 24/7 melalui sistem AI-Backend mutakhir.")
trans_para("A streamlined, 3-step", "scalability.", "Metodologi profesional 3 langkah yang dirancang untuk gangguan minimal dan skalabilitas operasional maksimum.")
trans_para("We comprehensively assess your", "precision automation.", "Kami menilai logika bisnis Anda secara komprehensif. Pakar kami menentukan dengan tepat di mana pekerjaan manual dapat sepenuhnya diganti dengan otomatisasi presisi.")
trans_para("We act as the bridge between", "ecosystem.", "Dengan menerapkan AI-Backend kami yang aman, kami menghubungkan seluruh alat perangkat lunak Anda menjadi satu ekosistem yang saling berkomunikasi.")
trans_para("Automation is continuously refined.", "zero downtime 24/7.", "Kami tidak hanya membangun jaringan; kami mengoptimalkannya untuk penskalaan dinamis, memastikan logika bisnis Anda beroperasi secara otonom tanpa henti 24/7.")
trans_para("Tailored automation pillars", "transformation.", "Pilar otomatisasi yang dirancang khusus untuk para eksekutif yang mendorong transformasi digital.")

trans(">Intelligent Document Processing<", ">Pemrosesan Dokumen Cerdas<")
trans_para("Stop manual data entry.", "databases.", "Hentikan entri data manual. Kami menerapkan otomatisasi tingkat lanjut untuk mengekstrak dan merutekan data penting dari formulir online dan PDF secara otomatis langsung ke database Anda.")
trans(">Autonomous Business Logic<", ">Logika Bisnis Otonom<")
trans_para("Siloed applications kill efficiency.", "fragmented tools.", "Kami merancang AI-Backend canggih yang berfungsi sebagai sistem saraf pusat organisasi Anda, mengatur puluhan parameter dan logika bisnis yang rumit.")
trans(">Real-time Executive Insights<", ">Wawasan Eksekutif Real-time<")
trans_para("Eliminate guesswork", "undeniable clarity.", "Hilangkan kelambatan pelaporan. Kami menyajikan aliran data operasional mentah menjadi dasbor otomatis secara real-time, memberi eksekutif kejelasan yang tak terbantahkan.")
trans_para("Book a private consultation", "architecture.", "Jadwalkan konsultasi pribadi dengan tim konsultan otomatisasi kami yang berbasis di Jakarta.")

html_id = html_id.replace('''<span class="text-blue-600 font-bold select-none">EN</span>
                    <span class="text-slate-300">|</span>
                    <a href="id.html" class="text-slate-500 hover:text-blue-600 transition-colors font-semibold">ID</a>''', '''<a href="index.html" class="text-slate-500 hover:text-blue-600 transition-colors font-semibold">EN</a>
                    <span class="text-slate-300">|</span>
                    <span class="text-blue-600 font-bold select-none">ID</span>''')
html_id = html_id.replace('<a href="id.html" class="text-sm font-bold text-slate-500 hover:text-blue-600">ID</a>', '<a href="index.html" class="text-sm font-bold text-slate-500 hover:text-blue-600">EN</a>')

with open('id.html', 'w', encoding='utf-8') as f:
    f.write(html_id)
print("Language duplication and translation complete!")
