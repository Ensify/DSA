class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        c=0
        d={}
        for w,h in rectangles:
            d[w/h]=d.get(w/h,0)+1

        for v in d.values():
            c+=(v-1)*v//2

        return c