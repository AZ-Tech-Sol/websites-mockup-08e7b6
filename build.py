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
  .band{display:grid;grid-template-columns:1fr;gap:22px;align-items:start;padding:26px;background:#131d2a;border:1px solid var(--line);border-radius:16px}
  .band .card{background:#1a2a3b}
  .band .aicard{background:linear-gradient(160deg,rgba(254,153,1,.12),#1a2a3b 55%)}
  .bandhead{display:grid;grid-template-columns:150px minmax(0,1fr);gap:24px;align-items:center}
  .bandhead .typeart{max-width:150px;margin:0}
  .bandhead h3{font-size:26px}
  .bands{gap:26px}
  @media (max-width:640px){.band{padding:16px}}
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
  .herogrid{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:44px;align-items:center}
  .heroart{width:100%;height:auto;border-radius:14px;display:block}
  .hero .herogrid h1{margin-left:0;max-width:none;text-align:left}
  @media (max-width:860px){.herogrid{grid-template-columns:1fr}.heroart{max-width:420px}}
  .typeart{width:100%;max-width:220px;height:auto;border-radius:12px;display:block;margin-bottom:14px}
  .typehero{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr);gap:40px;align-items:center}
  .typeart.big{max-width:360px;justify-self:end;margin:0}
  @media (max-width:860px){.typehero{grid-template-columns:1fr}.typeart.big{justify-self:start;max-width:280px}}
  .lgrow{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-bottom:6px}
  .lg{display:block;border-radius:6px}
  .lglab{font:600 12px Inter;color:var(--lsteel)}
  .combo .dtitle{font-size:28px}
  .combos{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:8px}
  .combos span{border:1px solid var(--line);border-radius:8px;padding:10px 12px;font-size:14px;color:var(--body)}
  .combos b{display:block;font:700 15px "Exo 2";color:var(--fog)}
  .combos .ailine{border-color:rgba(254,153,1,.45)}
  .combos .ailine b{color:var(--amber)}
  @media (max-width:640px){.combos{grid-template-columns:1fr}}
  .fit{display:grid;gap:6px;margin:10px 0 4px;padding:12px 14px;background:rgba(0,158,255,.06);border-radius:8px}
  .fitlab{font:700 11px "Exo 2";letter-spacing:.12em;text-transform:uppercase;color:var(--blue)}
  .fi{position:relative;padding-left:22px;font-size:14.5px;color:var(--fog)}
  .fi:before{content:"✓";position:absolute;left:2px;top:0;color:var(--blue);font-weight:700}
  .aicard .fit{background:rgba(254,153,1,.07)} .aicard .fitlab,.aicard .fi:before{color:var(--amber)}
  .keys{font:600 13px Inter;color:var(--lsteel);margin-top:4px}
  a.doorlink{padding:26px 24px 20px}
  @media (max-width:560px){.bandhead{grid-template-columns:90px minmax(0,1fr)}.bandhead .typeart{max-width:90px}}
  .ttable{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;align-items:stretch}
  @media (max-width:980px){.ttable{grid-template-columns:1fr}}
  .tcol{background:#131d2a;border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column}
  .timg{width:100%;height:auto;aspect-ratio:1/1;object-fit:cover;display:block;max-height:300px}
  .tbody{padding:22px 22px 24px;display:flex;flex-direction:column;gap:10px;flex:1}
  .tbody h3{font-size:24px;margin:0}
  .tsub{margin:0;color:var(--lsteel);font-size:14.5px}
  .tfit,.tins{list-style:none;padding:0;margin:0 0 6px;display:grid;gap:6px}
  .tfit li{position:relative;padding-left:22px;font-size:14.5px;color:var(--fog)}
  .tfit li:before{content:"✓";position:absolute;left:2px;color:var(--blue);font-weight:700}
  .tins li{border:1px solid var(--line);border-radius:8px;padding:10px 12px;background:#1a2a3b;display:flex;gap:12px;align-items:center}
  .insic{display:flex;gap:6px;flex:none}
  .instx{display:grid;gap:1px}
  .builtwith{display:flex;gap:6px;align-items:center;margin-top:4px;font-size:11.5px;color:var(--lsteel)}
  .builtwith .lg{border-radius:3px}
  .tins li b{display:block;font:700 15px "Exo 2";color:var(--fog)}
  .tins li span{font-size:13px;color:var(--body)}
  .tins li.ai{border-color:rgba(254,153,1,.45)} .tins li.ai b{color:var(--amber)}
  .tbody .btn{margin-top:auto}
  .own{border-left:3px solid var(--amber);background:rgba(254,153,1,.07);border-radius:0 8px 8px 0;padding:9px 12px;font-size:14px;color:var(--fog)}
  .ownlab{display:block;font:700 11px "Exo 2";letter-spacing:.12em;text-transform:uppercase;color:var(--amber);margin-bottom:2px}
  .steps1{text-align:center;margin:28px 0 0;color:var(--lsteel);font:600 15px "Exo 2";letter-spacing:.02em}
  .steps1 b{display:inline-grid;place-items:center;width:24px;height:24px;border-radius:50%;background:var(--royal);color:#fff;font-size:13px;margin-right:4px}
  .steps1 span{margin:0 10px;color:var(--steel)}
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
 'free': dict(type='build', who='A cart under our umbrella', title='Free Site', tag='For Arizona businesses that need a storefront online, fast.',
   price='<div class="price"><small>Your cost</small><strong>$0</strong> <span>credit on top</span></div>',
   edits='Paid for by a slim AZ Tech credit bar at the top of every page.',
   items=[('One or two meetings; we build it from the conversation',0),('You own your domain; we host it free',0),('Brochure pages and a simple contact form',0),
          ('An invite to <a href="join.html" '+EXT+'>AZ Professional Partners</a>, our Tucson business Slack',0),('No checkout on the site: take payments through Venmo, Cash App or PayPal',1),('Changes after launch are paid',1)],
   btn='Get started', href=TW, fine='Arizona businesses, plus anyone we invite', ghost=True, logos=(['github'],'Hosted on GitHub')),
 'starter': dict(type='build', who='Your own cart, your name on the umbrella', title='Starter Site', tag='The free site, with our credit moved down to your footer.',
   price='<div class="price"><small>One time</small><strong>$800</strong></div>',
   edits='Same build and hosting as Free. The top of every page is all yours.',
   items=[('One or two meetings; we build it from the conversation',0),('A small AZ Tech line in the footer, nothing on top',0),('Hosted free, and you own your domain',0),('Changes after launch are paid',1)],
   btn='Get started', href=TW, fine='Books a conversation at Office Hours', logos=(['github'],'Hosted on GitHub')),
 'ownit': dict(type='keep', who='A storefront you tend', title='Own-It Site', tag='For the solo owner who wants to make changes without calling anyone.',
   price='<p class="ask">Pay once, and then it\'s yours.</p>',
   edits='Built on Publii: a site you edit on your own laptop, with hosting that costs next to nothing.',
   items=[('Your brand, set up in a site you edit yourself',0),("A teaching session so you're independent from day one",0),('Fast, simple and nothing to hack',0),('Optional retainer meetings after launch',0)],
   btn='Email me the prices', href=TW, fine='We email today\'s prices, then book a conversation', logos=(['publii'],'')),
 'team': dict(type='keep', who='A shop with a staff', title='Team Site', tag='For businesses where several people publish, and the site has to stay up.',
   price='<p class="ask">A build, then a monthly for keeping it safe.</p>',
   edits='The monthly is monitoring and maintenance: hosting, backups, updates, uptime and security. Content changes are separate.',
   items=[('WordPress, built for your team to edit together',0),('Managed hosting and daily backups',0),('Plugin and core updates handled',0),('Uptime and security watch',0)],
   btn='Email me the prices', href=TW, fine='We email today\'s prices, then book a conversation', logos=(['wordpress'],'')),
 'app': dict(type='software', who='A building where the work gets done', title='Custom App', tag='For when customers come to your store to <em>do</em> something: accounts, bookings, data, real software.',
   price='<p class="ask">Priced after we understand what it\'s worth to your business.</p>',
   edits='Proof: ConVibe, a convention guest-tracker app, live on the App Store.',
   items=[('Database, users and uptime, engineered for you',0),('Ongoing engineering, not just hosting',0),('Starts with a strategy conversation',0)],
   btn='Book a strategy call', href=SH, fine='Two-day booking window', cls='app', logos=(['react','javascript','python','html5','json','graphql','n8n'],'')),
}
TYPES = {
 'build': dict(img='assets/type-build.svg', alt='A fruit cart under a striped umbrella', file='build.html', title='We build it, you run your business', sub='A storefront built from a conversation. Nobody has to edit it.', doors=['free','starter'],
   intro='Two ways to get a site without learning to run one. We meet once or twice, turn the conversation into your site, and host it for free. The only difference is where our credit sits.',
   faq=[('Why is the Free Site free?','You pay for it in advertising: a slim line at the top of every page that says AZ Tech built it. You own your domain and we host it at no cost to you. At the end you get an invoice showing what the site is worth, $800, with the full amount waived.'),
        ("What's the difference between Free and Starter?",'Only where our credit sits. Free has a slim bar across the top of every page; Starter moves it to a small line in your footer, so your header is all yours. Same site, same free hosting.'),
        ('Can I sell things on my site?',"Yes, but you can't take payments on these sites. List what you sell and link out to a payment platform like Venmo, Cash App or PayPal, and your customers pay there. If you need a full store with a checkout, we build it on the right platform for it."),
        ('What if I want changes later?','Every change has a price we tell you up front, or you can add AI Edits for unlimited content changes. We email you the current prices.')]),
 'keep': dict(img='assets/type-keep.svg', alt='A small shop storefront with a striped awning', file='keep.html', title='You keep it up to date', sub='For owners and teams who make their own changes.', doors=['ownit','team'],
   intro='Sites you run yourself. Own-It is for one person who wants to make their own changes with no monthly bill. Team is for several people publishing on a site that has to be watched. We email you today\'s prices, so you always get current numbers for your business.',
   faq=[("What's the difference between Own-It and Team?","Own-It is for one person making their own changes, and there's no monthly bill. Team is for several people editing a live site that has to be watched, so it comes with monthly monitoring and maintenance."),
        ('Does the Team monthly include changes?','No. It keeps the site safe, updated and running. Changes are separate: pay for each one, or add AI Edits for unlimited changes.'),
        ('Why do you email the prices?',"So you get today's numbers for your business, not a table that went stale. Fill in the short form and they arrive by email, with a time to talk."),
        ('Who owns my domain and my content?','You do. If you ever leave, your name and your words go with you.')]),
 'software': dict(img='assets/type-software.svg', alt='An industrial building with a loading dock and a truck', file='software.html', title='People use it', sub='Software your customers log into and do things with.', doors=['app'],
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
          {keyline('ai-'+k)}{fitlist('ai-'+k) if ('ai-'+k) in FIT else ''}
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


LOGOS = {  # Simple Icons marks (brand colours; JSON and GitHub lightened for the dark page); Publii's own mark from getpublii.com
 'github': ('GitHub', '#EEF3F7'), 'publii': ('Publii', None), 'wordpress': ('WordPress', '#3C9FD6'),
 'react': ('React Native', '#61DAFB'), 'javascript': ('JavaScript', '#F7DF1E'), 'python': ('Python', '#4B8BBE'),
 'html5': ('HTML5', '#E34F26'), 'apple': ('iOS', '#EEF3F7'), 'android': ('Android', '#34A853'), 'wpengine': ('WP Engine', '#0ECAD4'), 'aztech': ('AZ Tech', None), 'json': ('JSON', '#C7CED9'), 'graphql': ('GraphQL', '#E10098'), 'n8n': ('n8n', '#EA4B71'),
}
def logo(slug, size=34):
    name, col = LOGOS[slug]
    if col is None:
        return f'<img class="lg" src="assets/logos/{slug}.svg" alt="{name}" title="{name}" width="{size}" height="{size}">'
    svg = (R / 'assets' / 'logos' / f'{slug}.svg').read_text()
    svg = svg.replace('<svg ', f'<svg class="lg" width="{size}" height="{size}" fill="{col}" aria-label="{name}" ', 1)
    return svg
def logorow(slugs, label=''):
    lab = f'<span class="lglab">{label}</span>' if label else ''
    return f'<span class="lgrow">{"".join(logo(s) for s in slugs)}{lab}</span>'

def build_combo():
    return f'''
        <a class="card door doorlink combo" href="build.html" data-door="build">
          {logorow(['github'],'Hosted on GitHub')}
          <span class="who">A cart on the corner</span><span class="dtitle">Free Site or Starter Site</span>
          <span class="tag">We build your storefront from a conversation and host it free. It's free with our name on the umbrella, or $800 with your name on it.</span>
          {fitlist('build')}
          <span class="combos"><span><b>Free</b> $0 · our credit on top</span><span><b>Starter</b> $800 · credit in the footer</span></span>
          <span class="go">See both <b aria-hidden="true">→</b></span>
        </a>'''


FIT = {'ai-build': ["You'd rather email a change than make it", 'You change hours, photos or specials now and then', 'You want it cheaper than a retainer with a person'], 'build': ['You need to be found on Google, fast', "You don't want to learn to edit a website", 'A few pages says it all: what you do, your hours, how to reach you'], 'ownit': ['You run the business yourself', "You'd rather make your own changes than call someone", 'You want to pay once, with no monthly bill'], 'team': ['More than one person updates the site', 'It has to stay up, because customers depend on it', 'You want someone watching updates and security'], 'ai-keep': ["You'd rather describe a change than make it", 'You change the site often', "You want a person checking the AI's work"], 'app': ['Customers log in, book or buy', 'You have data to manage, not just pages to show', "Off-the-shelf tools don't fit how you work"], 'ai-software': ['The same job repeats in your business every day', 'Your team answers the same questions over and over', 'You want an AI with a name, and a person supervising it']}  # "Right for you if": three checks per card
KEYS = {'ai-build': 'Retainer with our AI · prices emailed · Angel supervises', 'ownit': 'You edit it on your laptop · no monthly bill', 'team': 'A build plus a monthly · changes are separate', 'ai-keep': 'Retainer · prices emailed · Angel supervises', 'app': 'Built, hosted and engineered by us · priced after a conversation', 'ai-software': 'The Clockwork Desk · for Team sites and custom apps'}  # one line of facts above the link
def fitlist(key):
    return '<span class="fit"><span class="fitlab">Right for you if</span>' + ''.join(f'<span class="fi">{x}</span>' for x in FIT[key]) + '</span>'
def keyline(key):
    return f'<span class="keys">{KEYS[key]}</span>' if key in KEYS else ''

TYPEFIT = {
 'build': ["You need to be found on Google, fast", "You don't want to learn to edit a website", "A few pages says it all: what you do, your hours, how to reach you"],
 'keep': ["You'd rather make your own changes, or have our AI make them", "More than one person may update it", "It has to stay up, with updates and security watched"],
 'software': ["Customers log in, book or buy", "You have data to manage, not just pages to show", "Off-the-shelf tools don't fit how you work"],
}
TYPELOGOS = {'build': (['github'], 'Hosted free on GitHub'), 'keep': (['github','wpengine'], 'Hosted on GitHub or WP Engine'), 'software': (['aztech'], 'Hosted and run by AZ Tech')}
TYPEWHO = {'build': 'A cart on the corner', 'keep': 'A storefront on the street', 'software': 'A building where the work gets done'}
INSIDE = {
 'build': [('Free Site', '$0 · our credit on top', ['html5'], None), ('Starter Site', '$800 · credit in the footer', ['html5'], None), ('AI Edits', 'changes by email · prices emailed', ['aztech'], None)],
 'keep': [('Own-It Site', 'you edit it · no monthly bill', ['publii'], None), ('Team Site', 'a build plus a monthly', ['wordpress'], None), ('Supervised AI Care', 'our AI makes the changes · Angel supervises', ['aztech'], None)],
 'software': [('Custom App', 'on the App Store and Google Play · priced after a conversation', ['apple','android'], ['react','javascript','python','graphql','n8n']), ('AI Employees', 'the Clockwork Desk · Angel supervises', ['aztech'], None)],
}


OWN = {  # ownership at every level: what the customer keeps if they ever leave
 'build': 'Your site lives in a GitHub repo you can clone any time. Leave, and the site leaves with you.',
 'keep': 'The Publii site files, or the whole WordPress site and its content, are yours to export and move.',
 'software': 'The code and the data are yours. We build it in your accounts, not ours.',
}
def type_table():
    cols = ''
    for k, tp in TYPES.items():
        fit = ''.join(f'<li>{x}</li>' for x in TYPEFIT[k])
        ins = ''.join(
            f'<li class="{"ai" if "AI" in n.split()[0:2] else ""}"><span class="insic">{"".join(logo(x, 30) for x in ic)}</span>'
            f'<span class="instx"><b>{n}</b><span>{d}</span>'
            + (f'<span class="builtwith">built with {"".join(logo(x, 18) for x in bw)}</span>' if bw else '')
            + '</span></li>' for n, d, ic, bw in INSIDE[k])
        cols += f'''
      <div class="tcol">
        <img class="timg" src="{tp['img']}" alt="{tp['alt']}" width="1024" height="1024">
        <div class="tbody">
          <div class="who">{TYPEWHO[k]}</div>
          <h3>{tp['title']}</h3>
          <p class="tsub">{tp['sub']}</p>
          {logorow(*TYPELOGOS[k])}
          <div class="fitlab">Right for you if</div>
          <ul class="tfit">{fit}</ul>
          <div class="own"><span class="ownlab">You own it</span>{OWN[k]}</div>
          <div class="fitlab" style="color:var(--lsteel)">What's inside</div>
          <ul class="tins">{ins}</ul>
          <a class="btn primary" href="{tp['file']}">{ {'build':'See the cart options','keep':'See the storefront options','software':'See the building options'}[k] } →</a>
        </div>
      </div>'''
    return f'<div class="ttable">{cols}\n    </div>'

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
          {logorow(*d['logos']) if d.get('logos') else ''}<span class="who">{d['who']}</span><span class="dtitle">{d['title']}</span><span class="tag">{d['tag']}</span>
          {keyline(slug)}{fitlist(slug)}
          <span class="go">{'See pricing' if slug in ('free','starter') else 'See what it includes'} <b aria-hidden="true">→</b></span>
        </a>'''

def full(slug):
    d = DOORS[slug]
    lis = ''.join(f'<li{" class=\"no\"" if n else ""}>{x}</li>' for x, n in d['items'])
    return f'''
      <div class="card door full {d.get('cls','')}" id="{slug}">
        {logorow(*d['logos']) if d.get('logos') else ''}<div class="who">{d['who']}</div>
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
    cols = 'c2' if k == 'build' else ('c3' if len(t['doors']) > 1 else 'c2')
    bands += f'''
    <div class="band">
      <div class="bandhead"><img class="typeart" src="{t['img']}" alt="{t['alt']}" width="1024" height="1024"><div><h3>{t['title']}</h3><p>{t['sub']}</p><a href="{t['file']}">Open this type →</a></div></div>
      <div class="row {cols}">{(build_combo() if k == 'build' else ''.join(summary(s) for s in t['doors'])) + ai_card(k)}
      </div>
    </div>'''
SECURITY = '''
<!-- SECURITY HERITAGE · Avada: [fusion_portfolio] hand-picked, or a new security-heritage category (employer-proof also holds n8n and Intuit) -->
<section class="container">
  <div class="wrap">
    <div class="center" style="margin-bottom:30px">
      <div class="eyebrow">Security heritage</div>
      <h2 style="font-size:34px">Built by someone who came up in cybersecurity</h2>
      <p class="lead">Before AZ Tech, Angel built security automation at Palo Alto Networks, BlackCloak and ThreatConnect. Every site we host is watched with the same habits.</p>
    </div>
    <div class="pfgrid" style="grid-template-columns:repeat(auto-fill,minmax(300px,1fr))">''' + tiles([3154, 3152, 3298]) + '''</div>
  </div>
</section>
'''
old = (R / 'src' / 'hub_rest.html').read_text().replace('<!-- CONTAINER 7', SECURITY + '<!-- CONTAINER 7').replace('{{STOREFRONTS}}',
    '<!-- Avada: [fusion_portfolio cat_slug="case-studies,prior-client" columns="3"] or a hand-picked set -->'
    f'<div class="pfgrid" style="grid-template-columns:repeat(auto-fill,minmax(300px,1fr))">{tiles([1694,1692,1696,2964,2775,3118])}</div>'
    f'<div class="pfmore" style="justify-content:center"><a class="btn amber" {EXT} href="https://aztechsol.com/our-work/">Browse the full portfolio →</a></div>')
hub = f'''
<section class="container hero">
  <div class="wrap herogrid">
    <img class="heroart" src="assets/hero-digital.svg" alt="A small shop turning into pixels that flow up into a browser window" width="1024" height="1024">
    <div>
      <div class="eyebrow">Websites</div>
      <h1 style="margin:0 0 .4em">Your website is your storefront</h1>
      <p class="lead">It used to be a cart on the corner or a shop on Main Street. Now it's the place people find you, see what you sell and decide to come in. Five ways to open yours, in three kinds: a cart on the corner, a storefront on the street, or a building where the work gets done.</p>
      <div class="question"><b>?</b> Who's minding the store?</div>
    </div>
  </div>
</section>
<section class="container" id="doors" style="padding-top:20px">
  <div class="wrap">{type_table()}
    <p class="steps1"><b>1</b> Pick your storefront <span>·</span> <b>2</b> Book a conversation <span>·</span> <b>3</b> Choose from three options</p>
  </div>
</section>
<!-- PARTNERS · Avada: [fusion_portfolio cat_slug="partners" columns="5"] -->
<section class="container" style="padding-top:10px">
  <div class="wrap">
    <div class="eyebrow">Community Builders</div>
    <h2 style="font-size:28px;margin-bottom:18px">Businesses that partner with us</h2>
    <div class="partners">{tiles(PARTNERS)}</div>
    <div class="pfmore"><a class="btn outline" {EXT} href="https://aztechsol.com/partners/">Meet the partners →</a></div>
  </div>
</section>
''' + old
(R / 'index.html').write_text(page('Your Storefront Online — AZ Tech Solutions (mockup)', hub, TRACK))
(R / 'square.html').write_text(page('Your Storefront Online — AZ Tech Solutions (mockup)', hub, TRACK))

for k, t in TYPES.items():
    pair = 'pair' if len(t['doors']) > 1 else 'c1'
    others = ''.join(f'<a class="card door doorlink" href="{o["file"]}"><span class="dtitle" style="font-size:20px">{o["title"]}</span><span class="tag">{o["sub"]}</span><span class="go">Open <b aria-hidden="true">→</b></span></a>' for kk, o in TYPES.items() if kk != k)
    body = f'''
<section class="container hero" style="padding-bottom:36px">
  <div class="wrap typehero">
    <div>
      <div class="crumbs"><a href="index.html">Websites</a> › {t['title']}</div>
      <div class="eyebrow">{t['sub']}</div>
      <h1 style="font-size:clamp(32px,4.6vw,50px);max-width:860px;margin:0 0 .4em">{t['title']}</h1>
      <p class="lead">{t['intro']}</p>
    </div>
    <img class="typeart big" src="{t['img']}" alt="{t['alt']}" width="1024" height="1024">
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
