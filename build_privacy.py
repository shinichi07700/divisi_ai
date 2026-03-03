import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the title specifically for this sub-page
html = html.replace('<title>Divisi.AI | Smart Automation for Jakarta Enterprises</title>', '<title>Privacy Policy - Divisi.AI</title>')

nav_end_idx = html.find('</nav>') + 6
header_nav = html[:nav_end_idx]

footer_start_idx = html.find('<!-- Footer -->')
footer = html[footer_start_idx:]

privacy_content = """
    <section class="pt-32 pb-24 relative z-10 bg-white min-h-screen">
        <div class="container mx-auto px-6 md:px-12 max-w-4xl">
            <h1 class="text-4xl md:text-5xl font-bold mb-6 text-slate-900 tracking-tight">Privacy Policy</h1>
            <p class="text-slate-500 mb-12 border-b border-slate-200 pb-8">Effective Date: March 2026</p>
            
            <div class="space-y-12 text-slate-600 leading-relaxed text-lg">
                
                <section>
                    <h2 class="text-2xl font-bold text-slate-900 mb-4">1. Introduction</h2>
                    <p>Welcome to <strong>Divisi.AI</strong> (operated by PT. Prima Mitra Sejahtera). We are committed to protecting the privacy and security of our clients' data. This Privacy Policy explains how we collect, use, process, and protect information when you use our website and business automation frameworks.</p>
                </section>

                <section>
                    <h2 class="text-2xl font-bold text-slate-900 mb-4">2. Information We Collect</h2>
                    <ul class="list-disc pl-6 space-y-2 mt-4">
                        <li><strong>Contact Information:</strong> Names, business email addresses, phone numbers, and company details provided during consultations.</li>
                        <li><strong>Service Data:</strong> Documents, receipts (<em>foto struk</em>), and operational data processed strictly through our Smart Automation workflows on your behalf.</li>
                        <li><strong>Usage Data:</strong> Analytical data regarding your interaction with our website (e.g., IP addresses, browser types, and navigation paths).</li>
                    </ul>
                </section>

                <section>
                    <h2 class="text-2xl font-bold text-slate-900 mb-4">3. How We Use Your Information</h2>
                    <p>We use the collected information exclusively for B2B service delivery, including:</p>
                    <ul class="list-disc pl-6 space-y-2 mt-4 text-slate-600">
                        <li>Deploying, maintaining, and securing your custom AI-Backend infrastructure.</li>
                        <li>Providing technical support and workflow optimization.</li>
                        <li>Responding to consultation requests and managing billing.</li>
                    </ul>
                    <div class="bg-indigo-50 border border-indigo-100 rounded-lg p-6 mt-8">
                        <h4 class="font-bold text-indigo-900 text-xl flex items-center"><svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg> AI Training Policy</h4>
                        <p class="text-indigo-800 mt-2">Divisi.AI strictly isolates all client operational data. <strong>We do not use your private business documents, forms, or proprietary logic workflows to train public-facing AI models.</strong> Your data remains your exclusive property.</p>
                    </div>
                </section>

                <section>
                    <h2 class="text-2xl font-bold text-slate-900 mb-4">4. Data Sharing and Third-Party Processors</h2>
                    <p>Divisi.AI <strong>never sells</strong> your data. We may share necessary routing information with trusted third-party infrastructure providers (such as cloud hosting environments and secure API gateways) solely to facilitate the automation services you have commissioned. All third-party providers are bound by strict enterprise confidentiality agreements.</p>
                </section>

                <section>
                    <h2 class="text-2xl font-bold text-slate-900 mb-4">5. Data Security</h2>
                    <p>We implement uncompromising, industry-standard cryptographic security measures to prevent unauthorized access, disclosure, or alteration of your robust automation ecosystems. While no digital transmission is entirely flawless, our dedicated Jakarta engineers proactively monitor infrastructure integrity.</p>
                </section>

                <section>
                    <h2 class="text-2xl font-bold text-slate-900 mb-4">6. Data Retention and Your Rights</h2>
                    <p>We retain operational data only as long as required to execute your designated business logic or comply with legal obligations. You have the right to request access to, correction of, or permanent deletion of your data from our active servers at any time.</p>
                </section>

                <section>
                    <h2 class="text-2xl font-bold text-slate-900 mb-4">7. Contact Us</h2>
                    <p>If you have questions regarding this Privacy Policy or our data handling architecture, please contact our administrative team:</p>
                    <div class="mt-6 p-8 bg-slate-50 rounded-2xl border border-slate-200 inline-block shadow-sm">
                        <p class="font-bold text-xl text-slate-900 mb-2">PT. Prima Mitra Sejahtera (Divisi.AI)</p>
                        <p>Jl. Pluit Raya no.11</p>
                        <p>Jakarta, 14440</p>
                        <p class="mt-4 font-bold text-blue-600"><a href="mailto:info@divisi.ai">info@divisi.ai</a></p>
                    </div>
                </section>
            </div>
        </div>
    </section>
"""

with open('privacy.html', 'w', encoding='utf-8') as f:
    f.write(header_nav + privacy_content + footer)
print("privacy.html successfully built using inherited design layout.")
