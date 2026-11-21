# -*- coding: utf-8 -*-
"""Ochre & Chapter Theme - icon candidates. Code-drawn, transparent, flat."""
import io, math, os
from PIL import Image, ImageDraw, ImageFont

S = 3; W = 1024
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "logo-candidates")

INK = (42, 18, 16, 255)
CREAM = (242, 243, 210, 255)      # #F2F3D2  knit paper
TEAL = (51, 126, 99, 255)         # #337E63  knit green
FOREST = (44, 72, 30, 255)        # #2C481E  christmas green
OCHRE = (171, 134, 61, 255)       # #AB863D  ochre
RED = (177, 17, 17, 255)          # #B11111  red
TERRA = (180, 117, 78, 255)       # #B4754E  terracotta
BROWN = (42, 18, 16, 255)         # #2A1210  cookie dark
RUST = (99, 48, 26, 255)          # #63301A  rust
GOLD = (98, 86, 27, 255)          # #62561B  olive gold

LIGHT_BG = (210, 200, 170, 255)
DARK_BG = (30, 20, 16, 255)
LIGHT_INK = (42, 18, 16, 255)
DARK_INK = (242, 243, 210, 255)
FONT_DIR = r"C:\Windows\Fonts"

def font(n, s):
    try: return ImageFont.truetype(os.path.join(FONT_DIR, n), s)
    except Exception: return ImageFont.load_default()

def scr(p): return (p[0]*S, p[1]*S)
def wd(v): return max(1, int(round(v*S)))
def canvas(): return Image.new("RGBA", (W*S, W*S), (0,0,0,0))
def finish(i): return i.resize((W, W), Image.LANCZOS)
def poly(d, pts, c): d.polygon([scr(p) for p in pts], fill=c)
def disc(d, ctr, r, col):
    d.ellipse([ctr[0]*S-r*S, ctr[1]*S-r*S, ctr[0]*S+r*S, ctr[1]*S+r*S], fill=col)
def rrect(d, box, r, col):
    d.rounded_rectangle([box[0]*S, box[1]*S, box[2]*S, box[3]*S], radius=r*S, fill=col)
def line(d, pts, col, w): d.line([scr(p) for p in pts], fill=col, width=wd(w), joint="curve")
def bez(p0,p1,p2,n=48):
    out=[]
    for i in range(n+1):
        t=i/n; u=1-t
        out.append((u*u*p0[0]+2*u*t*p1[0]+t*t*p2[0],
                    u*u*p0[1]+2*u*t*p1[1]+t*t*p2[1]))
    return out

def leaf(d, cx, cy, ang, ln, col):
    right=bez((0,0),(ln*0.55,-ln*0.45),(0,-ln))
    left=bez((0,-ln),(-ln*0.55,-ln*0.45),(0,0))
    ca,sa=math.cos(ang),math.sin(ang)
    poly(d,[(cx+x*ca-y*sa,cy+x*sa+y*ca) for x,y in right+left],col)

def cand_open_book():
    img=canvas(); d=ImageDraw.Draw(img)
    poly(d,[(512,480),(890,400),(890,780),(512,860)],CREAM)
    poly(d,[(512,480),(134,400),(134,780),(512,860)],CREAM)
    line(d,[(512,480),(512,860)],RUST,14)
    for i,c in enumerate((FOREST,OCHRE,RED,TERRA)):
        y=560+i*66
        d.rectangle([176*S,y*S,464*S,(y+38)*S],fill=c)
        d.rectangle([560*S,y*S,848*S,(y+38)*S],fill=c)
    return finish(img)

def cand_stack():
    img=canvas(); d=ImageDraw.Draw(img)
    for i,c in enumerate((TEAL,OCHRE,RED,TERRA)):
        y=740-i*140
        rrect(d,(212,y-96,812,y+56),18,c)
        rrect(d,(256,y-120,768,y-72),12,CREAM)
    return finish(img)

def cand_leaf_page():
    img=canvas(); d=ImageDraw.Draw(img)
    rrect(d,(268,180,756,844),28,CREAM)
    line(d,[(512,300),(512,800)],RUST,16)
    for i in range(3):
        y=380+i*140
        line(d,[(334,y),(470,y)],OCHRE,14)
        line(d,[(554,y),(690,y)],OCHRE,14)
    leaf(d,650,600,math.radians(-40),220,RED)
    leaf(d,380,470,math.radians(30),180,FOREST)
    return finish(img)

def cand_spine():
    img=canvas(); d=ImageDraw.Draw(img)
    rrect(d,(300,160,724,864),26,BROWN)
    for i,c in enumerate((CREAM,TEAL,OCHRE,RED,TERRA)):
        y=220+i*124
        d.rectangle([300*S,y*S,724*S,(y+90)*S],fill=c)
    rrect(d,(470,160,554,864),14,GOLD)
    return finish(img)

def cand_leaf_wheel():
    img=canvas(); d=ImageDraw.Draw(img)
    cols=(FOREST,OCHRE,RED,TERRA,GOLD,TEAL)
    for i,c in enumerate(cols):
        a=-math.pi/2+i*math.pi/3
        leaf(d,512,512,a+math.pi/2,250,c)
    disc(d,(512,512),92,CREAM)
    return finish(img)

def cand_bookmark():
    img=canvas(); d=ImageDraw.Draw(img)
    rrect(d,(300,220,724,830),24,CREAM)
    for i in range(4):
        y=320+i*110
        line(d,[(364,y),(660,y)],OCHRE,18)
    poly(d,[(560,180),(660,180),(660,720),(610,660),(560,720)],RED)
    return finish(img)

CANDIDATES=[
 ("01","open-book",cand_open_book),("02","chapter-stack",cand_stack),
 ("03","leaf-page",cand_leaf_page),("04","spine",cand_spine),
 ("05","leaf-wheel",cand_leaf_wheel),("06","bookmark",cand_bookmark),
]

def centered(d, ctr, text, f, col):
    b=d.textbbox((0,0),text,font=f)
    d.text((ctr[0]-(b[2]-b[0])/2-b[0],ctr[1]-(b[3]-b[1])/2-b[1]),text,font=f,fill=col)

def sheet(icons,bg,ink,path):
    cw,ch=420,540; m,g,h=40,26,118
    sw=m*2+cw*3+g*2; sh=m+h+ch*2+g+m
    im=Image.new("RGBA",(sw,sh),bg); d=ImageDraw.Draw(im)
    ft=font("segoeuib.ttf",40); fn=font("segoeuib.ttf",30)
    fna=font("segoeui.ttf",26); fs=font("segoeui.ttf",20)
    centered(d,(sw/2,m+34),"OCHRE & CHAPTER THEME",ft,ink)
    centered(d,(sw/2,m+82),"icon candidates",fs,ink)
    for i,(num,name,icon) in enumerate(icons):
        r,c=divmod(i,3); gx=m+c*(cw+g); gy=m+h+r*(ch+g)
        im.alpha_composite(icon.resize((260,260),Image.LANCZOS),(gx+(cw-260)//2,gy+30))
        centered(d,(gx+cw/2,gy+330),num,fn,ink)
        centered(d,(gx+cw/2,gy+372),name,fna,ink)
        centered(d,(gx+cw/2,gy+404),"1024 x 1024  PNG",fs,ink)
    save(im.convert("RGB"),path)

def strip(icons,path):
    sz,g,m=150,18,30
    sw=m*2+sz*len(icons)+g*(len(icons)-1); sh=m*2+sz+34
    im=Image.new("RGBA",(sw,sh),LIGHT_BG); d=ImageDraw.Draw(im)
    f=font("segoeuib.ttf",20)
    for i,(num,_n,icon) in enumerate(icons):
        x=m+i*(sz+g)
        im.alpha_composite(icon.resize((sz,sz),Image.LANCZOS),(x,m))
        centered(d,(x+sz/2,m+sz+16),num,f,LIGHT_INK)
    save(im.convert("RGB"),path)

def save(img,path):
    buf=io.BytesIO(); img.save(buf,format="PNG")
    os.makedirs(os.path.dirname(path),exist_ok=True)
    with open(path,"wb") as fh: fh.write(buf.getvalue())

def main():
    os.makedirs(OUT,exist_ok=True)
    icons=[]
    for num,name,fn in CANDIDATES:
        icon=fn(); box=icon.getbbox()
        if box is None: raise AssertionError(name+" empty")
        if box[0]<70 or box[1]<70 or box[2]>954 or box[3]>954:
            raise AssertionError(name+" out of safe area: "+str(box))
        save(icon,os.path.join(OUT,"%s-%s.png"%(num,name)))
        print("wrote",num,name,box)
        icons.append((num,name,icon))
    sheet(icons,LIGHT_BG,LIGHT_INK,os.path.join(OUT,"contact-light.png"))
    sheet(icons,DARK_BG,DARK_INK,os.path.join(OUT,"contact-dark.png"))
    strip(icons,os.path.join(OUT,"inline-strip.png"))
    print("wrote contact sheets")

if __name__=="__main__": main()
