"""
the pyro model from the arxiv paper 1810.09538

import pyro
import torch

def model():                                         
    loc, scale = torch.zeros(20), torch.ones(20)
    z = pyro.sample("z", Normal(loc, scale))  
    w, b = pyro.param("weight"), pyro.param("bias")
    ps = torch.sigmoid(torch.mm(z, w) + b)
    return pyro.sample("x", Bernoulli(ps))

def guide(x):
    pyro.module("encoder", nn_encoder)
    loc, scale = nn_encoder(x)
    return pyro.sample("z", Normal(loc, scale))

def conditioned_model(x):
    return pyro.condition(model, data={"x": x})()

optimizer = pyro.optim.Adam({"lr": 0.001})
loss = pyro.infer.Trace_ELBO()

svi = pyro.infer.SVI(model=conditioned_model, guide=guide, optim=optimizer, loss=loss)

losses = []
for batch in batches:
    losses.append(svi.step(batch))
"""


import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import pyro
import pyro.distributions as dist
from pyro.infer import SVI, Trace_ELBO
from pyro.optim import Adam
import matplotlib.pyplot as plt

torch.manual_seed(0)
pyro.set_rng_seed(0)
pyro.clear_param_store()

# Synthetic Bernoulli data
N,D,H,Z=1000,20,50,2
x_train=torch.bernoulli(torch.rand(N,D))
loader=DataLoader(TensorDataset(x_train),batch_size=64,shuffle=True)

fig=plt.figure(figsize=(8,3))
plt.imshow(x_train[:20],aspect="auto",cmap="Greys")
plt.title("First 20 Bernoulli samples")
plt.xlabel("Feature"); plt.ylabel("Sample")
plt.tight_layout()

class Encoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1=nn.Linear(D,H)
        self.loc=nn.Linear(H,Z)
        self.scale=nn.Linear(H,Z)
    def forward(self,x):
        h=torch.relu(self.fc1(x))
        return self.loc(h), torch.exp(self.scale(h))

class Decoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1=nn.Linear(Z,H)
        self.out=nn.Linear(H,D)
    def forward(self,z):
        return torch.sigmoid(self.out(torch.relu(self.fc1(z))))

enc=Encoder()
dec=Decoder()

def model(x):
    pyro.module("decoder",dec)
    with pyro.plate("data",x.shape[0]):
        z=pyro.sample("z",dist.Normal(x.new_zeros((x.shape[0],Z)),
                                      x.new_ones((x.shape[0],Z))).to_event(1))
        probs=dec(z)
        pyro.sample("obs",dist.Bernoulli(probs).to_event(1),obs=x)

def guide(x):
    pyro.module("encoder",enc)
    with pyro.plate("data",x.shape[0]):
        loc,scale=enc(x)
        pyro.sample("z",dist.Normal(loc,scale).to_event(1))

svi=SVI(model,guide,Adam({"lr":1e-3}),Trace_ELBO())
losses=[]
for epoch in range(50):
    total=0
    for (batch,) in loader:
        total+=svi.step(batch)
    losses.append(total/N)
    if (epoch+1)%10==0:
        print(epoch+1,losses[-1])

plt.figure(figsize=(6,4))
plt.plot(losses)
plt.xlabel("Epoch"); plt.ylabel("ELBO loss")
plt.tight_layout()

with torch.no_grad():
    loc,_=enc(x_train)
plt.figure(figsize=(5,5))
plt.scatter(loc[:,0],loc[:,1],s=8,alpha=0.5)
plt.xlabel("z1"); plt.ylabel("z2")
plt.title("Learned latent means")
plt.tight_layout()
plt.show()