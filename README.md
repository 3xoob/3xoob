
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&family=Outfit:wght@400;600;700;900&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{background:#080810}
.rm{font-family:'Outfit',sans-serif;background:#080810;color:#f0f0ff;padding:2.5rem 1.5rem;position:relative;overflow:hidden}
.scanlines{position:absolute;inset:0;pointer-events:none;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,0.08) 2px,rgba(0,0,0,0.08) 4px)}
.c{position:relative;z-index:1;max-width:660px;margin:0 auto}

.hero{margin-bottom:2.5rem;padding-bottom:2rem;border-bottom:1px solid rgba(255,255,255,0.06)}
.hero-top{display:flex;align-items:center;gap:20px;margin-bottom:1.2rem}
.av{width:80px;height:80px;border-radius:16px;background:#0f0f1a;border:2px solid #5eead4;display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace;font-size:28px;font-weight:800;color:#5eead4;flex-shrink:0;position:relative}
.av::after{content:'';position:absolute;inset:-4px;border-radius:20px;border:1px solid rgba(94,234,212,0.2)}
.hero-name{flex:1}
.name-line{font-size:2rem;font-weight:900;line-height:1;color:#fff;letter-spacing:-0.02em}
.name-line span{color:#5eead4}
.role-line{font-family:'JetBrains Mono',monospace;font-size:12px;color:#64748b;margin-top:6px}
.role-line b{color:#a78bfa}
.badges-row{display:flex;flex-wrap:wrap;gap:8px;margin-top:1rem}
.badge{font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;padding:4px 12px;border-radius:999px;border:1px solid}
.b-green{color:#5eead4;border-color:rgba(94,234,212,0.35);background:rgba(94,234,212,0.07)}
.b-purple{color:#a78bfa;border-color:rgba(167,139,250,0.35);background:rgba(167,139,250,0.07)}
.b-amber{color:#fbbf24;border-color:rgba(251,191,36,0.35);background:rgba(251,191,36,0.07)}
.b-red{color:#f87171;border-color:rgba(248,113,113,0.35);background:rgba(248,113,113,0.07)}
.tagline{margin-top:1rem;font-size:1rem;color:#94a3b8;line-height:1.7;border-left:3px solid #5eead4;padding-left:14px}
.tagline strong{color:#f0f0ff;font-weight:700}

.slabel{font-family:'JetBrains Mono',monospace;font-size:10px;color:#a78bfa;letter-spacing:.18em;text-transform:uppercase;margin-bottom:12px;display:flex;align-items:center;gap:8px}
.slabel::before{content:'▸';color:#5eead4}
.sec{margin-bottom:2rem}

.edu-card{background:#0d0d1a;border:1px solid rgba(167,139,250,0.25);border-radius:14px;padding:1.2rem 1.4rem;display:flex;align-items:flex-start;gap:16px;position:relative;overflow:hidden}
.edu-card::before{content:'';position:absolute;top:0;left:0;width:3px;height:100%;background:linear-gradient(180deg,#a78bfa,#5eead4);border-radius:3px 0 0 3px}
.edu-icon{font-size:32px;flex-shrink:0;margin-top:2px}
.edu-body{flex:1}
.edu-body strong{display:block;font-size:15px;font-weight:700;color:#f0f0ff;margin-bottom:8px}
.edu-tags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:8px}
.etag{font-family:'JetBrains Mono',monospace;font-size:10px;padding:3px 9px;border-radius:5px;border:1px solid}
.et-cs{color:#a78bfa;border-color:rgba(167,139,250,0.3);background:rgba(167,139,250,0.07)}
.et-hw{color:#fbbf24;border-color:rgba(251,191,36,0.3);background:rgba(251,191,36,0.07)}
.et-sys{color:#5eead4;border-color:rgba(94,234,212,0.3);background:rgba(94,234,212,0.07)}
.et-math{color:#f87171;border-color:rgba(248,113,113,0.3);background:rgba(248,113,113,0.07)}
.edu-status{flex-shrink:0;text-align:right;min-width:100px}
.prog-label{font-family:'JetBrains Mono',monospace;font-size:10px;color:#64748b;margin-bottom:6px}
.prog-bar{width:100px;height:6px;background:rgba(255,255,255,0.06);border-radius:3px;overflow:hidden}
.prog-fill{height:100%;background:linear-gradient(90deg,#a78bfa,#5eead4);border-radius:3px;animation:progAnim 1.5s ease-out forwards}
@keyframes progAnim{from{width:0}to{width:85%}}
.prog-pct{font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:800;color:#a78bfa;margin-top:5px;text-align:right}

.work-card{background:#0d0d1a;border:1px solid rgba(94,234,212,0.2);border-radius:14px;padding:1.2rem 1.4rem;margin-bottom:10px;position:relative;overflow:hidden}
.work-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,#5eead4,#a78bfa,#fbbf24)}
.wh{display:flex;align-items:center;gap:12px;margin-bottom:10px}
.wico{width:42px;height:42px;border-radius:10px;background:#131326;border:1px solid rgba(94,234,212,0.25);display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:800;color:#5eead4}
.wm strong{display:block;font-size:14px;font-weight:700;color:#fff}
.wm span{font-size:11px;color:#5eead4;font-family:'JetBrains Mono',monospace}
.wrole{margin-left:auto;font-family:'JetBrains Mono',monospace;font-size:10px;color:#a78bfa;background:rgba(167,139,250,0.1);border:1px solid rgba(167,139,250,0.25);border-radius:6px;padding:3px 10px}
.wdesc{font-size:12px;color:#64748b;line-height:1.65;margin-bottom:12px}
.projs{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.pcard{background:#0a0a18;border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:12px;transition:border-color .2s}
.pcard:hover{border-color:rgba(94,234,212,0.3)}
.pcard a{text-decoration:none;color:inherit;display:block}
.pn{font-size:13px;font-weight:700;color:#f0f0ff;margin-bottom:4px;display:flex;align-items:center;gap:6px}
.ptag{font-size:9px;font-family:'JetBrains Mono',monospace;padding:2px 7px;border-radius:4px}
.t-live{background:rgba(94,234,212,0.12);color:#5eead4;border:1px solid rgba(94,234,212,0.25)}
.t-saas{background:rgba(167,139,250,0.12);color:#a78bfa;border:1px solid rgba(167,139,250,0.25)}
.pd{font-size:11px;color:#475569;line-height:1.5;margin-bottom:5px}
.pu{font-family:'JetBrains Mono',monospace;font-size:10px;color:#5eead4}

.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.acard{background:#0d0d1a;border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:14px;display:flex;align-items:flex-start;gap:10px;transition:border-color .2s}
.acard:hover{border-color:rgba(94,234,212,0.25)}
.acard .ico{font-size:20px;flex-shrink:0;margin-top:1px}
.acard strong{display:block;font-size:12px;font-weight:700;color:#e2e8f0;margin-bottom:3px}
.acard span,.acard a{font-size:11px;color:#475569;font-family:'JetBrains Mono',monospace}
.acard a{color:#a78bfa;text-decoration:none}
.acard a:hover{text-decoration:underline}

.quote-block{background:#0d0d1a;border:1px solid rgba(251,191,36,0.2);border-radius:12px;padding:1.2rem 1.4rem;margin-bottom:1.5rem;position:relative}
.quote-block::before{content:'"';position:absolute;top:-10px;left:16px;font-size:48px;color:#fbbf24;font-family:Georgia,serif;line-height:1;opacity:0.4}
.quote-block p{font-size:13px;color:#94a3b8;line-height:1.75;font-style:italic}
.quote-block p strong{color:#fbbf24;font-style:normal}

.stack-section{margin-bottom:2rem}
.stack-cat{margin-bottom:14px}
.cat-title{font-family:'JetBrains Mono',monospace;font-size:10px;color:#374151;letter-spacing:.12em;text-transform:uppercase;margin-bottom:8px;padding-left:2px}
.stack-row{display:flex;flex-wrap:wrap;gap:6px}
.stk{font-family:'JetBrains Mono',monospace;font-size:11px;padding:5px 10px;border-radius:6px;border:1px solid rgba(255,255,255,0.08);color:#64748b;background:#0d0d1a;transition:all .15s;cursor:default}
.stk:hover{background:#131326;border-color:rgba(94,234,212,0.3);color:#5eead4}
.stk.core{border-color:rgba(94,234,212,0.3);color:#5eead4;background:rgba(94,234,212,0.06)}
.stk.mob{border-color:rgba(251,191,36,0.28);color:#fbbf24;background:rgba(251,191,36,0.06)}
.stk.cloud{border-color:rgba(96,165,250,0.28);color:#60a5fa;background:rgba(96,165,250,0.06)}
.stk.tool{border-color:rgba(255,255,255,0.1);color:#64748b;background:#0d0d1a}

.stat-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:1.5rem}
.scard{background:#0d0d1a;border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:14px;text-align:center}
.snum{font-family:'JetBrains Mono',monospace;font-size:20px;font-weight:800;color:#5eead4;display:block}
.slb{font-size:10px;color:#374151;margin-top:3px;display:block}

.lbar{display:flex;gap:2px;border-radius:6px;overflow:hidden;height:8px;margin:10px 0}
.l1{flex:3.2;background:#f1e05a}.l2{flex:2.1;background:#3178c6}.l3{flex:1.4;background:#3572A5}.l4{flex:1;background:#4F5D95}.l5{flex:0.8;background:#02569B}.l6{flex:2;background:#2d2d2d}
.lleg{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:1.5rem}
.li{display:flex;align-items:center;gap:5px;font-size:11px;color:#475569;font-family:'JetBrains Mono',monospace}
.ld{width:8px;height:8px;border-radius:50%}

.cta-row{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:2rem}
.cbtn{display:inline-flex;align-items:center;gap:8px;padding:10px 20px;border-radius:10px;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:700;text-decoration:none;border:1px solid;transition:all .18s}
.c-li{background:rgba(10,102,194,0.1);border-color:rgba(10,102,194,0.3);color:#60a5fa}
.c-li:hover{background:rgba(10,102,194,0.2)}
.c-gh{background:rgba(255,255,255,0.04);border-color:rgba(255,255,255,0.1);color:#e2e8f0}
.c-gh:hover{background:rgba(255,255,255,0.08)}
.c-rc{background:rgba(94,234,212,0.07);border-color:rgba(94,234,212,0.25);color:#5eead4}
.c-rc:hover{background:rgba(94,234,212,0.13)}
.foot{border-top:1px solid rgba(255,255,255,0.05);padding-top:1rem;font-family:'JetBrains Mono',monospace;font-size:10px;color:#1e293b;text-align:center;letter-spacing:.1em}
.foot span{color:#334155}
</style>

<div class="rm">
<div class="scanlines"></div>
<div class="c">

  <div class="hero">
    <div class="hero-top">
      <div class="av">A!</div>
      <div class="hero-name">
        <div class="name-line">Hey, I'm <span>Ali</span> 👋🔥</div>
        <div class="role-line">// <b>Full Stack Developer</b> · Builder · Learner · Loud in Code</div>
      </div>
    </div>
    <div class="badges-row">
      <span class="badge b-green">⚡ Full Stack Dev</span>
      <span class="badge b-purple">🎓 BSc Comp Eng · Almost Done</span>
      <span class="badge b-amber">🏗️ @ Raincode</span>
      <span class="badge b-red">🚀 2 Live Products</span>
    </div>
    <div class="tagline" style="margin-top:1.2rem">
      I build things that <strong>actually ship</strong>. From idea to production — frontend, backend, mobile, cloud, IoT. I talk about code like I mean it, and I mean it loud. Turning ideas into <strong>real products</strong> while finishing my degree.
    </div>
  </div>

  <div class="sec">
    <div class="slabel">education</div>
    <div class="edu-card">
      <div class="edu-icon">🎓</div>
      <div class="edu-body">
        <strong>BSc Computer Engineering</strong>
        <div class="edu-tags">
          <span class="etag et-cs">Algorithms</span>
          <span class="etag et-cs">Data Structures</span>
          <span class="etag et-cs">OOP</span>
          <span class="etag et-sys">Operating Systems</span>
          <span class="etag et-sys">Computer Networks</span>
          <span class="etag et-sys">Databases</span>
          <span class="etag et-hw">Computer Architecture</span>
          <span class="etag et-hw">Digital Logic</span>
          <span class="etag et-hw">Embedded Systems</span>
          <span class="etag et-math">Discrete Math</span>
          <span class="etag et-math">Linear Algebra</span>
          <span class="etag et-math">Probability & Stats</span>
        </div>
      </div>
      <div class="edu-status">
        <div class="prog-label">Progress</div>
        <div class="prog-bar"><div class="prog-fill"></div></div>
        <div class="prog-pct">85%</div>
      </div>
    </div>
  </div>

  <div class="sec">
    <div class="slabel">work experience</div>
    <div class="work-card">
      <div class="wh">
        <div class="wico">RC</div>
        <div class="wm">
          <strong>Raincode</strong>
          <span>raincode.tech · Remote</span>
        </div>
        <div class="wrole">Full Developer</div>
      </div>
      <p class="wdesc">Elite AI & full-stack tech consulting bridging strategy and execution for ambitious companies. Embedded in client teams building production-grade products end to end — DB schema to deployed UI, APIs to app stores.</p>
      <div class="projs">
        <div class="pcard">
          <a href="https://foremarket.se" target="_blank">
            <div class="pn">⛳ Foremarket <span class="ptag t-live">Live & Scaling</span></div>
            <div class="pd">Largest online golf marketplace — 90k+ golfers, BankID auth, secure payments, unified iOS + Android codebase, 30+ daily listings.</div>
            <div class="pu">foremarket.se ↗</div>
          </a>
        </div>
        <div class="pcard">
          <a href="https://reduca.se" target="_blank">
            <div class="pn">📋 Reduca <span class="ptag t-saas">SaaS</span></div>
            <div class="pd">Digital board portal — meeting management, BankID e-signatures, video meetings and encrypted document workflows.</div>
            <div class="pu">reduca.se ↗</div>
          </a>
        </div>
      </div>
    </div>
  </div>

  <div class="sec">
    <div class="slabel">about me</div>
    <div class="quote-block">
      <p>I don't just write code — I <strong>build things people use</strong>. I'm the guy who stays up debugging a weird edge case because it matters. I talk about what I'm working on everywhere, and I genuinely get <strong>excited</strong> about every part of the stack — CSS animations to database indexes to IoT sensors. If you want someone quiet, wrong repo. 😄</p>
    </div>
    <div class="about-grid">
      <div class="acard"><div class="ico">🌱</div><div><strong>Currently grinding</strong><span>Full Stack Dev + BSc Comp Eng</span></div></div>
      <div class="acard"><div class="ico">🤝</div><div><strong>Always down to help</strong><span>dm me. seriously.</span></div></div>
      <div class="acard"><div class="ico">💬</div><div><strong>Let's talk about</strong><span>code, products, ideas</span></div></div>
      <div class="acard"><div class="ico">📄</div><div><strong>Experience</strong><a href="https://www.linkedin.com/in/aliabdulhussain3" target="_blank">linkedin/aliabdulhussain3 ↗</a></div></div>
      <div class="acard"><div class="ico">🔥</div><div><strong>Fun fact</strong><span>I debug in prod (sometimes)</span></div></div>
      <div class="acard"><div class="ico">📍</div><div><strong>Based in</strong><span>Bahrain 🇧🇭</span></div></div>
    </div>
  </div>

  <div class="stack-section">
    <div class="slabel">tech stack</div>

    <div class="stack-cat">
      <div class="cat-title">⚡ Frontend · Core</div>
      <div class="stack-row">
        <span class="stk core">HTML</span><span class="stk core">CSS</span><span class="stk core">JavaScript</span><span class="stk core">TypeScript</span><span class="stk core">React</span><span class="stk core">Next.js</span><span class="stk core">Tailwind</span><span class="stk core">SolidJS</span><span class="stk core">jQuery</span><span class="stk core">Vite</span>
      </div>
    </div>

    <div class="stack-cat">
      <div class="cat-title">📱 Mobile · Cross-platform</div>
      <div class="stack-row">
        <span class="stk mob">Flutter</span><span class="stk mob">React Native</span><span class="stk mob">Expo</span>
      </div>
    </div>

    <div class="stack-cat">
      <div class="cat-title">🔧 Backend · APIs</div>
      <div class="stack-row">
        <span class="stk core">Node.js</span><span class="stk core">PHP</span><span class="stk core">Laravel</span><span class="stk core">Python</span><span class="stk core">Go</span><span class="stk core">Java</span><span class="stk core">GraphQL</span><span class="stk core">REST APIs</span>
      </div>
    </div>

    <div class="stack-cat">
      <div class="cat-title">🗄️ Databases</div>
      <div class="stack-row">
        <span class="stk core">MySQL</span><span class="stk core">SQLite</span><span class="stk mob">Firebase</span><span class="stk mob">DynamoDB</span>
      </div>
    </div>

    <div class="stack-cat">
      <div class="cat-title">☁️ Cloud · IoT · DevOps</div>
      <div class="stack-row">
        <span class="stk cloud">AWS</span><span class="stk cloud">AWS IoT Core</span><span class="stk cloud">Azure</span><span class="stk cloud">Cloudflare</span><span class="stk cloud">Vercel</span><span class="stk cloud">Docker</span><span class="stk cloud">GitHub Actions</span>
      </div>
    </div>

    <div class="stack-cat">
      <div class="cat-title">🛠️ Tools · Systems · Other</div>
      <div class="stack-row">
        <span class="stk tool">Git</span><span class="stk tool">Linux</span><span class="stk tool">Bash</span><span class="stk tool">PowerShell</span><span class="stk tool">Figma</span><span class="stk tool">Postman</span><span class="stk tool">VS Code</span><span class="stk tool">IntelliJ IDEA</span><span class="stk tool">Replit</span><span class="stk tool">npm</span><span class="stk tool">BankID</span><span class="stk tool">Arduino</span><span class="stk tool">C</span><span class="stk tool">C++</span><span class="stk tool">MATLAB</span><span class="stk tool">WordPress</span><span class="stk tool">Kali Linux</span><span class="stk tool">Ubuntu</span><span class="stk tool">Regex</span><span class="stk tool">Markdown</span><span class="stk tool">Discord</span>
      </div>
    </div>
  </div>

  <div class="sec">
    <div class="slabel">github</div>
    <div class="stat-grid">
      <div class="scard"><span class="snum">3xoob</span><span class="slb">username</span></div>
      <div class="scard"><span class="snum">2</span><span class="slb">live products</span></div>
      <div class="scard"><span class="snum">∞</span><span class="slb">commits per coffee ☕</span></div>
    </div>
    <div class="slabel">top languages</div>
    <div class="lbar">
      <div class="l1"></div><div class="l2"></div><div class="l3"></div><div class="l4"></div><div class="l5"></div><div class="l6"></div>
    </div>
    <div class="lleg">
      <div class="li"><div class="ld" style="background:#f1e05a"></div>JavaScript</div>
      <div class="li"><div class="ld" style="background:#3178c6"></div>TypeScript</div>
      <div class="li"><div class="ld" style="background:#3572A5"></div>Python</div>
      <div class="li"><div class="ld" style="background:#4F5D95"></div>PHP</div>
      <div class="li"><div class="ld" style="background:#02569B"></div>Dart</div>
      <div class="li"><div class="ld" style="background:#444"></div>Other</div>
    </div>
  </div>

  <div class="sec">
    <div class="slabel">connect with me</div>
    <div class="cta-row">
      <a href="https://www.linkedin.com/in/aliabdulhussain3" target="_blank" class="cbtn c-li">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
        LinkedIn
      </a>
      <a href="https://github.com/3xoob" target="_blank" class="cbtn c-gh">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/></svg>
        GitHub · 3xoob
      </a>
      <a href="https://raincode.tech" target="_blank" class="cbtn c-rc">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 010 20M12 2a15.3 15.3 0 000 20"/></svg>
        Raincode
      </a>
    </div>
  </div>

  <div class="foot">
    <span>ALI ABD AL-HUSSAIN</span> · FULL STACK DEV @ RAINCODE · BSC COMP ENG · FOREMARKET.SE · REDUCA.SE · BAHRAIN 🇧🇭
  </div>

</div>
</div>
