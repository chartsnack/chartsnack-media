import sys,re,datetime
# log.py NN "topic" ytid "dd.mm HH:MM"  -> appends row, advances English next slot
n,topic,yt,slot=sys.argv[1:5]
p='/home/claude/chartsnack-media/LOG.md'; s=open(p).read()
d,hm=slot.split()
dd,mm=d.split('.')
date=f"2026-{mm}-{dd}"
row=f"| {date} | {n} | {topic} | {yt} (sched. {slot}) | sched. {slot} (tt{n}, 25 s) |\n"
i=s.index('\nNext free slot:')
s=s[:i].rstrip('\n')+'\n'+row+s[i:]
dt=datetime.datetime(2026,int(mm),int(dd),int(hm[:2]))
nx=dt.replace(hour=19) if dt.hour==12 else (dt+datetime.timedelta(days=1)).replace(hour=12)
s=re.sub(r'Next free slot: \S+ \S+', f"Next free slot: {nx:%Y-%m-%d %H:%M}", s, count=1)
open(p,'w').write(s)
