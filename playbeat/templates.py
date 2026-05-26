"""
HTML template fragments for PlayBeat Digital.
Contains reusable HTML components: ticker, header, footer, modals, etc.
"""

TICKER = '''<div class="ticker-bar">
  <div class="ticker-inner">
    <span>🔥 Valorant Elderflame Bundle — $89</span>
    <span>⚡ ChatGPT Plus 1M — $20</span>
    <span>🎮 PS Plus 12M — $59</span>
    <span>💎 Adobe CC All Apps — $54</span>
    <span>🤖 Midjourney Basic — $10</span>
    <span>🆓 Free Gift Card on Orders $50+</span>
    <span>🔒 SSL Secured · Instant Delivery</span>
    <span>🔥 Valorant Elderflame Bundle — $89</span>
    <span>⚡ ChatGPT Plus 1M — $20</span>
    <span>🎮 PS Plus 12M — $59</span>
    <span>💎 Adobe CC All Apps — $54</span>
    <span>🤖 Midjourney Basic — $10</span>
    <span>🆓 Free Gift Card on Orders $50+</span>
    <span>🔒 SSL Secured · Instant Delivery</span>
  </div>
</div>'''

HEADER = '''<header>
  <div class="header-top">
    <div class="header-top-inner">
      <div class="search-wrap">
        <div class="search-bar">
          <div class="search-bar-bg"></div>
          <select class="search-category" id="searchCat" onchange="doSearch()">
            <option value="all">All</option>
            <option value="games">Games</option>
            <option value="ai">AI Tools</option>
            <option value="software">Software</option>
            <option value="giftcards">Gift Cards</option>
            <option value="subs">Subscriptions</option>
            <option value="topup">Top Up</option>
            <option value="items">Game Items</option>
            <option value="accounts">Accounts</option>
          </select>
          <input class="search-input" id="searchInput" type="text"
            placeholder="Search games, AI tools, subscriptions…"
            oninput="doSearch()" autocomplete="off">
          <button class="search-btn" onclick="doSearch()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
              stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
            </svg>
          </button>
        </div>
        <div class="search-dropdown" id="searchDropdown"></div>
      </div>
    </div>
  </div>
  <div class="header-inner">
    <a class="logo" href="index.html">
      <div class="logo-icon">▶</div>
      <div class="logo-text">Play<span>Beat</span></div>
    </a>
    <nav>
      <a href="index.html"          class="nav-item">Home</a>
      <a href="games.html"          class="nav-item">Games</a>
      <a href="gift-cards.html"     class="nav-item">Gift Cards</a>
      <a href="software.html"       class="nav-item">Software</a>
      <a href="ai-tools.html"       class="nav-item">AI Tools</a>
      <a href="game-items.html"     class="nav-item">Game Items</a>
      <a href="accounts.html"       class="nav-item">Accounts</a>
      <a href="subscriptions.html"  class="nav-item">Subscriptions</a>
      <a href="top-up.html"         class="nav-item">Top Up</a>
      <a href="trending.html"       class="nav-item nav-special">🔥 Trending</a>
      <a href="best-value.html"     class="nav-item nav-special">💎 Best Value</a>
    </nav>
    <div class="header-actions">
      <div id="headerGuest" style="display:flex;align-items:center;gap:12px">
        <button class="btn-wishlist-icon" onclick="window.location.href='my-account.html'">
          ♡ <span class="wish-count" id="wishlistCount" style="display:none">0</span>
        </button>
        <button class="btn-login" onclick="openModal('signinModal')">Sign In</button>
        <button class="btn-prime" onclick="openModal('signupModal')">Join Prime</button>
      </div>
      <div id="headerUser" style="display:none;align-items:center;gap:12px">
        <button class="btn-wishlist-icon" onclick="window.location.href='my-account.html'">
          ♡ <span class="wish-count" id="wishlistCount2" style="display:none">0</span>
        </button>
        <div class="user-chip" onclick="window.location.href='my-account.html'">
          <span class="user-chip-avatar">👤</span>
          <span id="headerName">User</span>
        </div>
      </div>
    </div>
  </div>
</header>'''

FOOTER = '''<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="logo" href="index.html" style="margin-bottom:0;display:inline-flex">
          <div class="logo-icon">▶</div>
          <div class="logo-text">Play<span>Beat</span></div>
        </a>
        <p>The premier destination for digital products. Games, AI tools, subscriptions,
           gift cards &amp; more — delivered instantly, globally.</p>
      </div>
      <div class="footer-col">
        <h4>Marketplace</h4>
        <ul>
          <li><a href="games.html">Games</a></li>
          <li><a href="ai-tools.html">AI Tools</a></li>
          <li><a href="software.html">Software</a></li>
          <li><a href="gift-cards.html">Gift Cards</a></li>
          <li><a href="subscriptions.html">Subscriptions</a></li>
          <li><a href="game-items.html">Game Items</a></li>
          <li><a href="accounts.html">Accounts</a></li>
          <li><a href="top-up.html">Top Up</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Discover</h4>
        <ul>
          <li><a href="trending.html">🔥 Trending</a></li>
          <li><a href="best-value.html">💎 Best Value</a></li>
          <li><a href="outsource.html">Outsource</a></li>
          <li><a href="our-team.html">Our Team</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="contact.html">Contact Us</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Legal</h4>
        <ul>
          <li><a href="privacy.html">Privacy Policy</a></li>
          <li><a href="terms.html">Terms of Service</a></li>
          <li><a href="refund.html">Refund Policy</a></li>
          <li><a href="my-account.html">My Account</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 <span>PlayBeat Digital</span>. All rights reserved.</span>
      <span>Built for prime members worldwide ⭐</span>
    </div>
  </div>
</footer>'''

MODALS = '''<!-- ===== SIGN IN MODAL ===== -->
<div class="modal-overlay" id="signinModal">
  <div class="modal-box">
    <button class="modal-close" onclick="closeModal('signinModal')">✕</button>
    <div class="modal-logo">Play<span>Beat</span></div>
    <div class="modal-sub">Prime Digital Marketplace</div>
    <div class="modal-title">Sign In</div>
    <div class="modal-success" id="signinSuccess">✓ Signed in successfully!</div>
    <button class="btn-social">🔵 Continue with Google</button>
    <button class="btn-social">🐙 Continue with GitHub</button>
    <div class="modal-divider">or use email</div>
    <div class="form-group">
      <label class="form-label">Email</label>
      <input class="form-input" id="siEmail" type="email" placeholder="you@email.com">
    </div>
    <div class="form-group">
      <label class="form-label">Password</label>
      <input class="form-input" id="siPass" type="password" placeholder="••••••••">
    </div>
    <div class="modal-error" id="siError">Invalid email or password.</div>
    <div style="text-align:right;margin-bottom:20px">
      <a style="color:var(--gold);font-size:12px;cursor:pointer;font-family:'Share Tech Mono',monospace">Forgot password?</a>
    </div>
    <button class="btn-hero-primary" style="width:100%;padding:13px;border-radius:4px" onclick="doSignIn()">Sign In →</button>
    <div class="modal-switch">Don't have an account? <a onclick="switchModal('signinModal','signupModal')">Create one free</a></div>
  </div>
</div>

<!-- ===== SIGN UP MODAL ===== -->
<div class="modal-overlay" id="signupModal">
  <div class="modal-box">
    <button class="modal-close" onclick="closeModal('signupModal')">✕</button>
    <div class="modal-logo">Play<span>Beat</span></div>
    <div class="modal-sub">Prime Digital Marketplace</div>
    <div class="modal-title">Create Account</div>
    <div class="modal-success" id="signupSuccess">✓ Account created! Welcome aboard.</div>
    <button class="btn-social">🔵 Continue with Google</button>
    <button class="btn-social">🐙 Continue with GitHub</button>
    <div class="modal-divider">or use email</div>
    <div class="form-row">
      <div class="form-group"><label class="form-label">First Name</label><input class="form-input" id="suFirst" type="text" placeholder="Alex"></div>
      <div class="form-group"><label class="form-label">Last Name</label><input class="form-input" id="suLast" type="text" placeholder="Carter"></div>
    </div>
    <div class="form-group"><label class="form-label">Email</label><input class="form-input" id="suEmail" type="email" placeholder="you@email.com"></div>
    <div class="form-group"><label class="form-label">Password</label><input class="form-input" id="suPass" type="password" placeholder="Min. 6 characters"></div>
    <div class="modal-error" id="suError">Please fill all fields correctly.</div>
    <div class="checkbox-row">
      <input type="checkbox" id="suTerms">
      <label for="suTerms">I agree to the <a href="terms.html">Terms of Service</a> and <a href="privacy.html">Privacy Policy</a></label>
    </div>
    <button class="btn-hero-primary" style="width:100%;padding:13px;border-radius:4px" onclick="doSignUp()">Create Account →</button>
    <div class="modal-switch">Already have an account? <a onclick="switchModal('signupModal','signinModal')">Sign in</a></div>
  </div>
</div>

<!-- ===== CHECKOUT MODAL ===== -->
<div class="modal-overlay" id="checkoutModal">
  <div class="modal-box" style="max-width:680px">
    <button class="modal-close" onclick="closeModal('checkoutModal')">✕</button>
    <div class="modal-title" id="checkoutTitle">Checkout</div>
    <div style="font-family:'Share Tech Mono',monospace;font-size:11px;color:#555;margin-bottom:24px;letter-spacing:2px">SECURE PAYMENT · INSTANT DELIVERY</div>
    <div id="checkoutForm">
      <div class="checkout-grid">
        <div>
          <div style="font-family:'Share Tech Mono',monospace;font-size:10px;color:#555;letter-spacing:2px;margin-bottom:14px">ORDER SUMMARY</div>
          <div class="checkout-summary">
            <div class="checkout-item">
              <div class="checkout-item-icon" id="coIcon">🎮</div>
              <div>
                <div class="checkout-item-name" id="coName">Product</div>
                <div class="checkout-item-cat"  id="coCat">Category</div>
              </div>
              <div class="checkout-item-price" id="coPrice">$0</div>
            </div>
            <div class="checkout-total">
              <div><div class="checkout-total-label">Total</div></div>
              <div class="checkout-total-price" id="coTotal">$0</div>
            </div>
          </div>
        </div>
        <div>
          <div style="font-family:'Share Tech Mono',monospace;font-size:10px;color:#555;letter-spacing:2px;margin-bottom:14px">PAYMENT METHOD</div>
          <div class="payment-methods">
            <div class="pay-method selected" onclick="selectPay(this)">💳 Card</div>
            <div class="pay-method" onclick="selectPay(this)">🅿️ PayPal</div>
            <div class="pay-method" onclick="selectPay(this)">₿ Crypto</div>
            <div class="pay-method" onclick="selectPay(this)">🍎 Apple Pay</div>
          </div>
          <div id="cardFields">
            <div class="form-group"><label class="form-label">Card Number</label><input class="form-input" id="coCard" type="text" placeholder="1234 5678 9012 3456" maxlength="19" oninput="formatCardNumber()"></div>
            <div class="form-row">
              <div class="form-group"><label class="form-label">Expiry</label><input class="form-input" id="coExp" type="text" placeholder="MM/YY" maxlength="5"></div>
              <div class="form-group"><label class="form-label">CVV</label><input class="form-input" id="coCvv" type="password" placeholder="•••" maxlength="4"></div>
            </div>
            <div class="form-group"><label class="form-label">Name on Card</label><input class="form-input" id="coCardName" type="text" placeholder="Alex Carter"></div>
          </div>
          <div class="modal-error" id="coError" style="margin-top:-4px">Please complete all card details.</div>
          <button class="btn-hero-primary" style="width:100%;padding:14px;border-radius:4px;margin-top:8px" onclick="doCheckout()">🔒 Pay &amp; Get Instant Delivery</button>
          <div style="text-align:center;font-size:11px;color:#333;font-family:'Share Tech Mono',monospace;margin-top:10px;letter-spacing:1px">256-bit SSL · Verified Secure</div>
        </div>
      </div>
    </div>
    <div class="checkout-success" id="checkoutSuccess">
      <div class="big-icon">🎉</div>
      <h3>Order Complete!</h3>
      <p>Your digital product has been delivered instantly.</p>
      <div class="key-box" id="deliveryKey">XXXX-XXXX-XXXX-XXXX</div>
      <p style="font-size:12px;color:#444;font-family:'Share Tech Mono',monospace">Save this key · Check email for full details</p>
      <button class="btn-hero-primary" style="margin-top:20px;padding:12px 32px;border-radius:4px"
        onclick="closeModal('checkoutModal');window.location.href='my-account.html'">View My Orders</button>
    </div>
  </div>
</div>'''

TRUST = '''<div class="trust-strip">
  <div class="trust-item"><span class="icon">⚡</span><div><strong>Instant Delivery</strong><span>Keys sent in seconds</span></div></div>
  <div class="trust-item"><span class="icon">🔒</span><div><strong>256-bit SSL</strong><span>Bank-grade security</span></div></div>
  <div class="trust-item"><span class="icon">✅</span><div><strong>Verified Products</strong><span>100% authentic keys</span></div></div>
  <div class="trust-item"><span class="icon">🌍</span><div><strong>Global Access</strong><span>Available in 100+ countries</span></div></div>
  <div class="trust-item"><span class="icon">💬</span><div><strong>24/7 Support</strong><span>Real humans, always on</span></div></div>
</div>'''
