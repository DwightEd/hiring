"""矩形相交面积
题意与思路：轴对齐矩形，输入 (x1,y1,x2,y2)，x1<=x2、y1<=y2；返回相交面积而非 IoU。
复杂度：O(1) 时间和空间。
来源：公开面经题型；见 companies/README.md 的逐题映射。
"""

def overlap_area(a,b):
    width=max(0,min(a[2],b[2])-max(a[0],b[0]))
    height=max(0,min(a[3],b[3])-max(a[1],b[1]))
    return width*height
