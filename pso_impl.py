#!/usr/bin/env python3
"""PSO — particle swarm optimization for continuous functions."""
import random
class Particle:
    def __init__(self,dim,bounds):
        self.pos=[random.uniform(b[0],b[1]) for b in bounds]
        self.vel=[random.uniform(-1,1) for _ in range(dim)]
        self.best_pos=list(self.pos);self.best_val=float('inf')
def pso(fn,dim,bounds,n_particles=30,iterations=100,w=0.7,c1=1.5,c2=1.5):
    particles=[Particle(dim,bounds) for _ in range(n_particles)]
    global_best=None;global_val=float('inf')
    for p in particles:
        val=fn(p.pos);p.best_val=val
        if val<global_val:global_val=val;global_best=list(p.pos)
    for _ in range(iterations):
        for p in particles:
            for d in range(dim):
                r1,r2=random.random(),random.random()
                p.vel[d]=w*p.vel[d]+c1*r1*(p.best_pos[d]-p.pos[d])+c2*r2*(global_best[d]-p.pos[d])
                p.pos[d]+=p.vel[d]
                p.pos[d]=max(bounds[d][0],min(bounds[d][1],p.pos[d]))
            val=fn(p.pos)
            if val<p.best_val:p.best_val=val;p.best_pos=list(p.pos)
            if val<global_val:global_val=val;global_best=list(p.pos)
    return global_best,global_val
def main():
    random.seed(42)
    best,val=pso(lambda x:sum(xi**2 for xi in x),2,[(-10,10)]*2)
    print(f"Min at {[round(x,4) for x in best]}, val={val:.6f}")
if __name__=="__main__":main()
