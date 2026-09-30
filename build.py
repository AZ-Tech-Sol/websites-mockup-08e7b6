#!/usr/bin/env python3
"""Builds the website sales page mockup: the hub and one page per type.
Ruled in Four Doors v11 (2026-09-30) plus the chat rulings after it:
five doors in three types; each type has its own page; only Free and Starter
show prices; every other price is emailed through the Web & Hosting form."""
import pathlib
R = pathlib.Path(__file__).parent
part = lambda n: (R / 'src' / f'{n}.html').read_text()
HEAD, STYLE, HEADER, FOOTER = part('head'), part('style'), part('header'), part('footer')
TW = 'https://n8n.aztechsol.com/form/1ee1be18-95a0-44d8-9da6-bd5c12dc12ef'
SH = 'https://calendly.com/aztechsol/strategy-hour'
OH = 'https://calendly.com/aztechsol/office-hours'
EXT = 'target="_blank" rel="noopener"'
UTIL = f'<div class="utility"><div class="wrap"><a {EXT} href="https://aztechsol.com/office-hours/">Office Hours</a><span></span></div></div>\n'
MOCK = '<div class="mockbar">MOCKUP · not the live site · ruled 2026-09-30 in Four Doors v11 · only Free and Starter show prices; the rest are emailed</div>'

CSS = '''<style>
  .bands{display:grid;gap:34px}
  .band{display:grid;grid-template-columns:260px minmax(0,1fr);gap:28px;align-items:start;padding-top:26px;border-top:1px solid var(--line)}
  .band:first-child{border-top:0;padding-top:0}
  .bandhead h3{font-size:22px;margin:0 0 6px}
  .bandhead p{margin:0 0 12px;color:var(--lsteel);font-size:14.5px}
  .bandhead a{font:700 13px "Exo 2";letter-spacing:.06em;text-transform:uppercase;color:var(--blue);text-decoration:none}
  .c1{grid-template-columns:1fr}
  .band .c2,.pair{grid-template-columns:repeat(2,minmax(0,1fr))}
  @media (max-width:900px){.band{grid-template-columns:1fr;gap:14px}}
  @media (max-width:640px){.band .c2,.pair{grid-template-columns:1fr}}
  a.doorlink{display:flex;flex-direction:column;gap:6px;padding:24px 20px 18px;text-decoration:none;border-radius:10px}
  a.doorlink:hover{border-color:var(--blue)}
  a.doorlink:focus-visible{outline:2px solid var(--blue);outline-offset:2px}
  .who{font:600 12px "Exo 2";letter-spacing:.14em;text-transform:uppercase;color:var(--lsteel)}
  .dtitle{font:700 24px/1.2 "Exo 2",sans-serif;color:var(--fog)}
  .tag{color:var(--body);font-size:15px}
  .go{margin-top:8px;font:700 13px "Exo 2";letter-spacing:.06em;text-transform:uppercase;color:var(--blue);display:flex;justify-content:space-between;border-top:1px solid var(--line);padding-top:12px}
  .door.full{padding:26px 24px}
  .door.full ul{flex:1}
  .ask{font:600 15px Inter;color:var(--fog);margin:14px 0 4px}
  .crumbs{font-size:13px;color:var(--lsteel);margin-bottom:14px}
  .crumbs a{color:var(--blue);text-decoration:none}
  .others{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
  @media (max-width:640px){.others{grid-template-columns:1fr}}
  .pfgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:16px}
  .pfgrid{gap:10px}
  a.pf{position:relative;display:block;text-decoration:none;overflow:hidden}
  a.pf img{width:100%;height:auto;aspect-ratio:3/2;object-fit:cover;display:block;background:var(--carbon);transition:transform .3s}
  a.pf .roll{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center;padding:16px;background:rgba(14,18,26,.86);color:var(--fog);font:700 17px/1.3 "Exo 2",sans-serif;opacity:0;transition:opacity .25s}
  a.pf:hover img,a.pf:focus-visible img{transform:scale(1.03)}
  a.pf:hover .roll,a.pf:focus-visible .roll{opacity:1}
  a.pf:focus-visible{outline:2px solid var(--blue);outline-offset:2px}
  .aicard{background:linear-gradient(160deg,rgba(254,153,1,.10),var(--carbon) 55%);border-color:rgba(254,153,1,.45)}
  .aicard .who{color:var(--amber)}
  .aicard:hover{border-color:var(--amber)}
  .band .c3{grid-template-columns:repeat(3,minmax(0,1fr))}
  @media (max-width:1000px){.band .c3{grid-template-columns:repeat(2,minmax(0,1fr))}}
  @media (max-width:640px){.band .c3{grid-template-columns:1fr}}
  .aisection{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr);gap:30px;padding:30px;background:linear-gradient(150deg,rgba(254,153,1,.09),var(--carbon) 50%);border-color:rgba(254,153,1,.4)}
  @media (max-width:800px){.aisection{grid-template-columns:1fr}}
  .aiside{display:flex;flex-direction:column;gap:12px;justify-content:center}
  .aiul{list-style:none;padding:0;margin:0 0 12px}
  .aiul li{padding:6px 0 6px 24px;position:relative}
  .aiul li:before{content:"";position:absolute;left:4px;top:14px;width:8px;height:8px;border-radius:50%;background:var(--amber)}
  .btn.amber{display:inline-block;background:#FE9901;color:#1a1200;box-shadow:none;font-size:13px;letter-spacing:.06em;text-transform:uppercase;padding:11px 18px}
  .btn.outline{display:inline-block;border:1.5px solid var(--blue);color:var(--blue);font-size:13px;letter-spacing:.06em;text-transform:uppercase;padding:10px 18px}
  .pfmore{margin-top:20px;display:flex;gap:12px;flex-wrap:wrap}
  .utility{background:#009EFF}
  .utility .wrap{display:flex;align-items:center;justify-content:space-between;height:38px}
  .utility a{background:#0E121A;color:#fff;border-radius:999px;padding:5px 14px;font:700 11px "Exo 2";letter-spacing:.04em;text-transform:uppercase;text-decoration:none}
  .partners{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:14px}
  @media (max-width:900px){.partners{grid-template-columns:repeat(3,minmax(0,1fr))}}
  @media (max-width:560px){.partners{grid-template-columns:repeat(2,minmax(0,1fr))}}
  .partners a.pf{font-size:13px}
  @media (prefers-reduced-motion:reduce){a.pf img,a.pf .roll{transition:none}}
</style>'''

DOORS = {
 'free': dict(type='build', who='A sign on the square', title='Free Site', tag='For Tucson businesses that need to be seen on the square, fast.',
   price='<div class="price"><small>Your cost</small><strong>$0</strong> <span>credit on top</span></div>',
   edits='Paid for by a slim AZ Tech credit bar at the top of every page.',
   items=[('One or two meetings; we build it from the conversation',0),('You own your domain; we host it free',0),('Brochure pages and a simple contact form',0),
          ('An invite to <a href="join.html" '+EXT+'>AZ Professional Partners</a>, our Tucson business Slack',0),('No checkout on the site: take payments through Venmo, Cash App or PayPal',1),('Changes after launch are paid',1)],
   btn='Get started', href=TW, fine='Tucson businesses, plus anyone we invite', ghost=True),
 'starter': dict(type='build', who='Your own sign on the square', title='Starter Site', tag='The free site, with our credit moved down to your footer.',
   price='<div class="price"><small>One time</small><strong>$800</strong></div>',
   edits='Same build and hosting as Free. The top of every page is all yours.',
   items=[('One or two meetings; we build it from the conversation',0),('A small AZ Tech line in the footer, nothing on top',0),('Hosted free, and you own your domain',0),('Changes after launch are paid',1)],
   btn='Get started', href=TW, fine='Books a conversation at Office Hours'),
 'ownit': dict(type='keep', who='A storefront you tend', title='Own-It Site', tag='For the solo owner who wants to make changes without calling anyone.',
   price='<p class="ask">Pay once, and then it\'s yours.</p>',
   edits='Built on Publii: a site you edit on your own laptop, with hosting that costs next to nothing.',
   items=[('Your brand, set up in a site you edit yourself',0),("A teaching session so you're independent from day one",0),('Fast, simple and nothing to hack',0),('Optional retainer meetings after launch',0)],
   btn='Email me the prices', href=TW, fine='We email today\'s prices, then book a conversation'),
 'team': dict(type='keep', who='A shop with a staff', title='Team Site', tag='For businesses where several people publish, and the site has to stay up.',
   price='<p class="ask">A build, then a monthly for keeping it safe.</p>',
   edits='The monthly is monitoring and maintenance: hosting, backups, updates, uptime and security. Content changes are separate.',
   items=[('WordPress, built for your team to edit together',0),('Managed hosting and daily backups',0),('Plugin and core updates handled',0),('Uptime and security watch',0)],
   btn='Email me the prices', href=TW, fine='We email today\'s prices, then book a conversation'),
 'app': dict(type='software', who='A place people gather', title='Custom App', tag='For when people come to your place to <em>do</em> something together: accounts, data, real software.',
   price='<p class="ask">Priced after we understand what it\'s worth to your business.</p>',
   edits='Proof: ConVibe, a convention guest-tracker app, live on the App Store.',
   items=[('Database, users and uptime, engineered for you',0),('Ongoing engineering, not just hosting',0),('Starts with a strategy conversation',0)],
   btn='Book a strategy call', href=SH, fine='Two-day booking window', cls='app'),
}
TYPES = {
 'build': dict(file='build.html', title='We build it, you run your business', sub='A site on the square, built from a conversation. Nobody has to edit it.', doors=['free','starter'],
   intro='Two ways to get a site without learning to run one. We meet once or twice, turn the conversation into your site, and host it for free. The only difference is where our credit sits.',
   faq=[('Why is the Free Site free?','You pay for it in advertising: a slim line at the top of every page that says AZ Tech built it. You own your domain and we host it at no cost to you. At the end you get an invoice showing what the site is worth, $800, with the full amount waived.'),
        ("What's the difference between Free and Starter?",'Only where our credit sits. Free has a slim bar across the top of every page; Starter moves it to a small line in your footer, so your header is all yours. Same site, same free hosting.'),
        ('Can I sell things on my site?',"Yes, but you can't take payments on these sites. List what you sell and link out to a payment platform like Venmo, Cash App or PayPal, and your customers pay there. If you need a full store with a checkout, we build it on the right platform for it."),
        ('What if I want changes later?','Every change has a price we tell you up front, or you can add AI Edits for unlimited content changes. We email you the current prices.')]),
 'keep': dict(file='keep.html', title='You keep it up to date', sub='For owners and teams who make their own changes.', doors=['ownit','team'],
   intro='Sites you run yourself. Own-It is for one person who wants to make their own changes with no monthly bill. Team is for several people publishing on a site that has to be watched. We email you today\'s prices, so you always get current numbers for your business.',
   faq=[("What's the difference between Own-It and Team?","Own-It is for one person making their own changes, and there's no monthly bill. Team is for several people editing a live site that has to be watched, so it comes with monthly monitoring and maintenance."),
        ('Does the Team monthly include changes?','No. It keeps the site safe, updated and running. Changes are separate: pay for each one, or add AI Edits for unlimited changes.'),
        ('Why do you email the prices?',"So you get today's numbers for your business, not a table that went stale. Fill in the short form and they arrive by email, with a time to talk."),
        ('Who owns my domain and my content?','You do. If you ever leave, your name and your words go with you.')]),
 'software': dict(file='software.html', title='People use it', sub='Software your customers log into and do things with.', doors=['app'],
   intro='When a website needs to do more than be read: accounts, bookings, data, a community that logs in. We build it, host it and keep engineering it.',
   faq=[('How much does an app cost?',"It depends on what it's worth to your business, so we start with a strategy conversation, not a price list."),
        ('Can you show me one?','ConVibe, a convention guest-tracker app, is live on the App Store. We built it from database to daily users.')]),
}

import json
PF = {x['id']: x for x in json.loads((R / 'src' / 'portfolio.json').read_text())}
PROOF = {  # portfolio items from aztechsol.com (Avada portfolio), chosen per type
 'build': dict(title='Local owners we\'ve built for', sub="Small businesses we've built sites and brands for, from the AZ Tech portfolio.", ids=[3301,1694,1692,1681,1698,1679,1677], cat='door-build'),
 'keep': dict(title='Teams and organisations that trust us', sub='Sites that several people publish on, and that have to stay up.', ids=[1696,1683,2964,1471,2963,2973,2972,2959], cat='door-keep'),
 'software': dict(title='Software we\'ve shipped', sub='Apps, AI assistants and automation, as case studies.', ids=[3234,2798,2390,2849,3118], cat='door-software'),
}
PARTNERS = [2927,2928,2939,3090,3144]

def tiles(ids, cls='pf'):
    out=''
    for i in ids:
        x = PF[i]
        out += f'<a class="{cls}" {EXT} href="{x['link']}"><img loading="lazy" src="{x['img']}" alt="{x['title']}" width="768" height="512"><span class="roll">{x['title']}</span></a>'
    return out

def proof_section(k):
    p = PROOF[k]
    return f'''
<!-- PORTFOLIO · Avada: [fusion_portfolio cat_slug="{p['cat']}" layout="grid" columns="3"] once the items carry that category -->
<section class="container">
  <div class="wrap">
    <div class="eyebrow">Reputation</div>
    <h2 style="font-size:30px;margin-bottom:6px">{p['title']}</h2>
    <p style="margin:0 0 22px;color:var(--lsteel)">{p['sub']}</p>
    <div class="pfgrid">{tiles(p['ids'])}</div>
    <div class="pfmore"><a class="btn amber" {EXT} href="https://aztechsol.com/our-work/">Browse the full portfolio →</a><a class="btn outline" {EXT} href="https://aztechsol.com/partners/">Meet the partners →</a></div>
  </div>
</section>
'''


LUPITA = 'https://aztechsol.com/portfolio-items/lupita-cplc-ai-assistant/'
AI = {  # the AI tier beside each site type; every AI tier works under Angel's supervision, and prices are emailed
 'build': dict(who='The AI tier', title='AI Edits', tag='Email our AI with a change and it makes it. Cheaper than a retainer with Angel.',
   body='For Free and Starter sites. Instead of paying for each change, you get a retainer with our AI: send it an email saying what to change (new hours, a new photo, a new page in your design) and it makes the change, with Angel supervising.',
   items=['Changes by email, as often as you need them','Cheaper than a retainer with Angel','Angel supervises every change'],
   note='Prices are emailed, so they can change as the AI gets better.'),
 'keep': dict(who='The AI tier', title='Supervised AI Care', tag='A retainer where our AI makes the changes for you, and Angel supervises.',
   body='For Own-It and Team sites. You tell us what you want, in a meeting or an email, and our AI does the work on your site under Angel\'s supervision. What supervision means will grow as the AI does, but a person always signs off.',
   items=['Our AI makes the changes; you don\'t have to','Angel supervises every change','Meetings are recorded, and the AI works from them'],
   note='Team sites can also add an AI employee from the Clockwork Desk.'),
 'software': dict(who='The AI tier', title='AI Employees · the Clockwork Desk', tag='A custom AI that joins your team, with a name, a job and Angel supervising it.',
   body='For Team sites and custom apps. We build an AI employee around one job in your business. Lupita answers CPLC\'s community in English and Spanish. VIKI reviews a convention app\'s catalogue every night and posts what it finds to the team\'s Slack; its review queue has reached zero.',
   items=['Named, trained on your business, and in your tools','Works alongside your team, not instead of it','Angel supervises it as it learns'],
   note='', link=('Read the Lupita case study →', LUPITA)),
}

def ai_card(k):
    a = AI[k]; tp = TYPES[k]
    return f'''
        <a class="card door doorlink aicard" href="{tp['file']}#ai" data-door="ai-{k}">
          <span class="who">{a['who']}</span><span class="dtitle">{a['title']}</span><span class="tag">{a['tag']}</span>
          <span class="go">See the AI tier <b aria-hidden="true">→</b></span>
        </a>'''

def ai_section(k):
    a = AI[k]
    lis = ''.join(f'<li>{x}</li>' for x in a['items'])
    link = f'<a class="btn outline" {EXT} href="{a["link"][1]}">{a["link"][0]}</a>' if a.get('link') else ''
    note = f'<div class="fine" style="text-align:left">{a["note"]}</div>' if a['note'] else ''
    return f'''
<section class="container" id="ai" style="padding-top:10px">
  <div class="wrap">
    <div class="card aisection">
      <div>
        <div class="eyebrow" style="color:var(--amber)">{a['who']}</div>
        <h2 style="font-size:30px;margin-bottom:8px">{a['title']}</h2>
        <p style="margin:0 0 14px;max-width:62ch">{a['body']}</p>
        <ul class="aiul">{lis}</ul>
        {note}
      </div>
      <div class="aiside">
        <p class="ask" style="margin-top:0">Prices are emailed.</p>
        <a class="btn primary" {EXT} href="{TW}" data-door-cta="ai-{k}">Email me the prices</a>
        {link}
      </div>
    </div>
  </div>
</section>
'''

def page(title, body, extra=''):
    h = HEAD.replace(HEAD[HEAD.index('<title>'):HEAD.index('</title>')+8], f'<title>{title}</title>')
    return h + STYLE + CSS + '\n</head>\n<body>\n' + MOCK + '\n' + UTIL + HEADER + body + FOOTER + extra + '\n</body>\n</html>\n'

TRACK = '''<script>
document.querySelectorAll('[data-door-cta]').forEach(function(a){
  a.addEventListener('click',function(){ try{ window.umami && umami.track('door_cta',{door:a.dataset.doorCta}); }catch(e){} });
});
</script>'''

def summary(slug):
    d = DOORS[slug]; t = TYPES[d['type']]
    return f'''
        <a class="card door doorlink {d.get('cls','')}" href="{t['file']}#{slug}" data-door="{slug}">
          <span class="who">{d['who']}</span><span class="dtitle">{d['title']}</span><span class="tag">{d['tag']}</span>
          <span class="go">{'See pricing' if slug in ('free','starter') else 'See what it includes'} <b aria-hidden="true">→</b></span>
        </a>'''

def full(slug):
    d = DOORS[slug]
    lis = ''.join(f'<li{" class=\"no\"" if n else ""}>{x}</li>' for x, n in d['items'])
    return f'''
      <div class="card door full {d.get('cls','')}" id="{slug}">
        <div class="who">{d['who']}</div>
        <h3 style="font-size:28px;margin:6px 0 4px">{d['title']}</h3>
        <p class="tag">{d['tag']}</p>
        {d['price']}
        <div class="edits">{d['edits']}</div>
        <ul>{lis}</ul>
        <a class="btn {'ghost' if d.get('ghost') else 'primary'}" {EXT} href="{d['href']}" data-door-cta="{slug}">{d['btn']}</a>
        <div class="fine">{d['fine']}</div>
      </div>'''

def faq(items):
    return ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items)

# the hub
bands = ''
for k, t in TYPES.items():
    cols = 'c3' if len(t['doors']) > 1 else 'c2'
    bands += f'''
    <div class="band">
      <div class="bandhead"><h3>{t['title']}</h3><p>{t['sub']}</p><a href="{t['file']}">Open this type →</a></div>
      <div class="row {cols}">{''.join(summary(s) for s in t['doors'])}{ai_card(k)}
      </div>
    </div>'''
old = (R / 'src' / 'hub_rest.html').read_text()
hub = f'''
<section class="container hero center">
  <div class="wrap">
    <div class="eyebrow">Websites, rebuilt as places</div>
    <h1>Take your place in the digital town square</h1>
    <p class="lead">A website used to be a brochure. Now it's where your town finds you, talks to you and comes back. Five ways to take your place, in three kinds, from a sign on the square to a building people gather in.</p>
    <div class="question"><b>?</b> Who will gather at your place, and who keeps it open?</div>
  </div>
</section>
<section class="container" id="doors" style="padding-top:20px">
  <div class="wrap"><div class="bands">{bands}
  </div></div>
</section>
<!-- PARTNERS · Avada: [fusion_portfolio cat_slug="partners" columns="5"] -->
<section class="container" style="padding-top:10px">
  <div class="wrap">
    <div class="eyebrow">Partners</div>
    <h2 style="font-size:28px;margin-bottom:18px">Businesses that partner with us</h2>
    <div class="partners">{tiles(PARTNERS)}</div>
    <div class="pfmore"><a class="btn outline" {EXT} href="https://aztechsol.com/partners/">Meet the partners →</a></div>
  </div>
</section>
''' + old
(R / 'index.html').write_text(page('Your Place Online — AZ Tech Solutions (mockup)', hub, TRACK))
(R / 'square.html').write_text(page('Your Place Online — AZ Tech Solutions (mockup)', hub, TRACK))

for k, t in TYPES.items():
    pair = 'pair' if len(t['doors']) > 1 else 'c1'
    others = ''.join(f'<a class="card door doorlink" href="{o["file"]}"><span class="dtitle" style="font-size:20px">{o["title"]}</span><span class="tag">{o["sub"]}</span><span class="go">Open <b aria-hidden="true">→</b></span></a>' for kk, o in TYPES.items() if kk != k)
    body = f'''
<section class="container hero" style="padding-bottom:36px">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Websites</a> › {t['title']}</div>
    <div class="eyebrow">{t['sub']}</div>
    <h1 style="font-size:clamp(32px,4.6vw,50px);max-width:860px;margin:0 0 .4em">{t['title']}</h1>
    <p class="lead">{t['intro']}</p>
  </div>
</section>
<section class="container" style="padding-top:0">
  <div class="wrap"><div class="row {pair}">{''.join(full(s) for s in t['doors'])}
  </div></div>
</section>
''' + ai_section(k) + proof_section(k) + f'''<section class="container alt">
  <div class="wrap" style="max-width:900px">
    <div class="eyebrow">Questions</div>
    <h2 style="font-size:30px">Before you pick</h2>
    {faq(t['faq'])}
  </div>
</section>
<section class="container">
  <div class="wrap">
    <h2 style="font-size:26px;margin-bottom:18px">Not quite right? The other kinds</h2>
    <div class="others">{others}</div>
  </div>
</section>
'''
    (R / t['file']).write_text(page(f"{t['title']} — AZ Tech Solutions (mockup)", body, TRACK))
print('built:', ', '.join(['index.html', 'square.html'] + [t['file'] for t in TYPES.values()]))
