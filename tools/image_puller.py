import urllib.request
from bs4 import BeautifulSoup
import re
import logging
import ssl

logging.basicConfig(level=logging.INFO)


names = ['201708supplydemand', '201708bigday', '201708altright', '201708revanchism', '201708anteup', '201708tourism', '201708backstory', '201709bonfire', '201709identity', '201709voltage', '201709journos', '201708amazon', '201708genocide', '201708media', '201708culturewar', '201708diversity', '201708sargon']

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for name in names:
    with open('../%s/index.html' % name) as f:
        page = BeautifulSoup(f, "html.parser").findAll('div',{'aria-label': 'Embedded'})

    urls = []

    for p in page:
        style = p["style"]
        url = re.findall('url\("(.*?)\?', style)
        urls = urls + url

    for u in urls:
        url = u + ".jpg:large"
        res = urllib.request.urlopen(url, context=ctx)
        fname = u.split('/')[-1]
        logging.info(fname)
        with open("../%s/%s.jpg" % (name, fname), 'wb') as f:
            f.write(res.read())

#https://pbs.twimg.com/media/DGv7ScqVoAALoq9.jpg:large

#<a class="_2YXT0EI-" href="https://mobile.twitter.com/FrameGames/status/895085266251206656/photo/1"><div aria-label="Embedded" class="kHlKyFGV _3hLw5mbC _1ninV_xt _1YeWCqJF _2kX66DOK" style="width: 100%; background-image: url(&quot;https://pbs.twimg.com/media/DGv7ScqVoAALoq9?format=jpg&amp;name=small&quot;);"><img alt="Embedded" src="SupplyDemand_files/DGv7ScqVoAALoq9" class="_16WH7Eyq"></div></a>

#https://video.twimg.com/ext_tw_video/904563003764310016/pu/vid/558x640/axgoUUsjKZ-gU-f1.mp4

#<a class="_1_aozdMe" href="https://mobile.twitter.com/FrameGames/status/904563089357422592/video/1"><div class="kHlKyFGV _3wMe7_pL"><div class="kHlKyFGV sEQESZ5E"><span class="ttWiH_Hj">0:09</span></div><div alt="" class="kHlKyFGV _3hLw5mbC _17xHsokI _2kX66DOK" style="background-image: url(&quot;https://pbs.twimg.com/ext_tw_video_thumb/904563003764310016/pu/img/Uhh-cloFJl1Lc5vd.jpg:small&quot;);"><img alt="" src="./Voltage2_files/Uhh-cloFJl1Lc5vd.jpg-small" class="_16WH7Eyq"></div><span class="_3IqdI_Qe"><svg class="_3bEbQ02C" viewBox="0 0 24 24" style="display: inline-block; fill: currentcolor; height: 1.25em; max-width: 100%; position: relative; user-select: none; vertical-align: text-bottom;"><g><circle cx="12" cy="12" r="10"></circle><path fill="#FFF" d="M16.036 11.58l-6-3.82a.5.5 0 0 0-.77.42v7.64a.498.498 0 0 0 .77.419l6-3.817c.145-.092.23-.25.23-.422s-.085-.33-.23-.42z"></path><path fill="#FFF" d="M12 22.75C6.072 22.75 1.25 17.928 1.25 12S6.072 1.25 12 1.25 22.75 6.072 22.75 12 17.928 22.75 12 22.75zm0-20C6.9 2.75 2.75 6.9 2.75 12S6.9 21.25 12 21.25s9.25-4.15 9.25-9.25S17.1 2.75 12 2.75z"></path></g></svg></span></div></a>