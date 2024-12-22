with open("input.in") as f:
    A,B=f.read().strip().split("\n\n")
A=A.split("\n")
H,W=len(A),len(A[0])
walls=set()
boxes=set()
px,py=0,0
walls=set()
boxes=set()
px,py=0,0
for y in range(H):
    for x in range(W):
        ch=A[y][x]
        if ch=="#": walls.add((x,y))
        if ch=="O": boxes.add((x,y))
        if ch=="@": px,py=x,y
def go(dx,dy):
    global px,py
    nx,ny=px+dx,py+dy
    if (nx,ny) in walls:
        return
    if (nx,ny) not in boxes:
        px,py=nx,ny; return
    a,b=nx,ny
    while (a,b) in boxes:
        a,b=a+dx,b+dy
    if (a,b) in walls: return
    boxes.remove((nx,ny))
    boxes.add((a,b))
    px,py=nx,ny           
for code in B:
    if code=="<": go(-1,0)
    if code==">": go(1,0)
    if code=="^": go(0,-1)
    if code=="v": go(0,1)       
Part1=sum(100*y+x for (x,y) in boxes)
def canpush(x,y,dx,dy):
    nx,ny=x+dx,y+dy
    if (nx,ny) in walls:
        return False
    if dx==1:
        if (nx,ny) not in boxes:
            return True
        return canpush(nx+1,ny,dx,dy)
    if dx==-1:
        if (nx-1,ny) not in boxes:
            return True
        return canpush(nx-1,ny,dx,dy)  
    else:
        if (nx,ny) not in boxes and (nx-1,ny) not in boxes:
            return True
        if (nx,ny) in boxes: return canpush(nx,ny,dx,dy) and canpush(nx+1,ny,dx,dy)
        if (nx-1,ny) in boxes: return canpush(nx,ny,dx,dy) and canpush(nx-1,ny,dx,dy)             
def trypush(x,y,dx,dy):
    nx,ny=x+dx,y+dy
    if (nx,ny) in walls:
        return False
    if dx==1:
        if (nx,ny) not in boxes:
            return True
        ok=trypush(nx+1,ny,dx,dy)
        if ok: boxes.remove((nx,ny)); boxes.add((nx+1,ny)); return True
        return False
    if dx==-1:
        if (nx-1,ny) not in boxes:
            return True
        ok=trypush(nx-1,ny,dx,dy)
        if ok: boxes.remove((nx-1,ny)); boxes.add((nx-2,ny)); return True
        return False
    else:
        if (nx,ny) not in boxes and (nx-1,ny) not in boxes:
            return True
        ok1,ok2=False,False
        if (nx,ny) in boxes: ok1= trypush(nx,ny,dx,dy) and trypush(nx+1,ny,dx,dy)
        if (nx-1,ny) in boxes: ok2= trypush(nx-1,ny,dx,dy) and trypush(nx,ny,dx,dy)
        if ok1:boxes.remove((nx,ny)); boxes.add((nx+dx,ny+dy)); return True
        if ok2:boxes.remove((nx-1,ny)); boxes.add((nx-1+dx,ny+dy)); return True
        return False
walls=set()
boxes=set()
for y in range(H):
    for x in range(W):
        ch=A[y][x]
        if ch=="#": walls.add((2*x,y));walls.add((2*x+1,y))
        if ch=="O": boxes.add((2*x,y))
        if ch=="@": px,py=2*x,y
for i,code in enumerate(B):
        if code=="<" and canpush(px,py,-1,0): trypush(px,py,-1,0);px-=1
        if code==">" and canpush(px,py,1,0):trypush(px,py,1,0);px+=1
        if code=="^" and canpush(px,py,0,-1):trypush(px,py,0,-1);py-=1
        if code=="v" and canpush(px,py,0,1):trypush(px,py,0,1);py+=1
Part2=sum(100*y+x for (x,y) in boxes)
print("Part 1 solution:", Part1)
print("Part 2 solution:", Part2)
