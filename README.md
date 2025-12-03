<h1 align="center">🎭 nmap-decoy 🔥</h1>

<p align="center">
  <b>An advanced Nmap decoy generator built for stealth scanning & red‑team training</b><br>
  This tool hides your real scanning identity by injecting fake IP addresses 🎯🌀 into the target’s logs —<br>
  meaning <b>you perform the real scan</b> 🔍 but the defender only sees the decoy address 🎭.<br>
  Ideal for ethical hacking education, network‑analysis training, and stealth simulations 🔒🛠️.
</p>

<hr>

<h2>📅 Release Date</h2>
<p>Uploaded on: <b>2025‑12‑03</b></p>

<hr>

<h2>🚀 Installation & Usage Guide</h2>

<h3>1️⃣ Clone the Repository</h3>
<pre><code class="language-bash">
git clone https://github.com/zarga33d/nmap-decoy.git
</code></pre>

<h3>2️⃣ Enter the Project Folder</h3>
<pre><code class="language-bash">
cd nmap-decoy
</code></pre>

<h3>3️⃣ Make the Scanner Script Executable</h3>
<pre><code class="language-bash">
chmod +x nmap_decoy_scan.sh
</code></pre>

<h3>4️⃣ Generate the Fake IP Pool</h3>
<pre><code class="language-bash">
python ip-gen.py
</code></pre>

<h3>5️⃣ Run Your Decoy Scan</h3>
<p>The attacker (you) performs the REAL scan — the defender only sees the fake IP list.</p>
<pre><code class="language-bash">
./nmap_decoy_scan.sh --list decoy_part_2.txt 192.168.1.1
</code></pre>

<hr>

<h2>⚡ Features</h2>
<ul>
  <li>✔ True decoy scanning — hides your REAL IP completely</li>
  <li>✔ Defender sees only randomized fake addresses 🎭</li>
  <li>✔ Customizable IP generation with <code>ip-gen.py</code></li>
  <li>✔ Works with all Nmap scan types</li>
  <li>✔ Perfect for red‑team stealth & training simulations</li>
</ul>

<hr>

<h2>📌 Disclaimer</h2>
<p style="color:#ff3333;">
nmap-decoy is for <b>educational purposes and authorized penetration testing ONLY</b>.<br>
We (the developers) are <b>not responsible</b> for any illegal, unethical, or unauthorized misuse.
</p>

<hr>

<h3 align="center">💻 Developed by zarga & ja3ka | GitHub: @zarga33d</h3>
