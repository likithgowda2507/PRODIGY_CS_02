<h1>🖼️ Image Encryption & Decryption Tool</h1>

<p>This is a simple Python-based tool that allows users to <strong>encrypt and decrypt images</strong> by manipulating pixel values. The encryption is done using a basic key-based mathematical operation applied to each pixel's RGB values.</p>

<h2>🔐 Features</h2>
<ul>
  <li>Encrypts images by shifting RGB values with a user-provided key.</li>
  <li>Decrypts encrypted images using the same key.</li>
  <li>Supports both <strong>RGB</strong> and <strong>RGBA</strong> (transparency) images.</li>
  <li>Displays the original, encrypted, and decrypted images for visual comparison.</li>
  <li>CLI-based interaction; lightweight and easy to use.</li>
</ul>

<h2>⚙️ How It Works</h2>
<p>Each pixel's RGB components are modified using:</p>

<pre><code>Encrypted = (Original + Key) % 256
Decrypted = (Encrypted - Key) % 256</code></pre>

<p>The alpha channel (transparency) is preserved during processing.</p>

<h2>🛠 Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li>Pillow library: <code>pip install pillow</code></li>
</ul>
