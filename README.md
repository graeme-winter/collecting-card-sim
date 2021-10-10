# collecting-card-sim
Simple numpy simulations for card collecting: every year Sainsburys runs
collecting card campaigns where the idea is to collect some 140-odd cards
by getting a pack of 4 every time you drop £10. This simulation is to
illustrate how hard this actually is.

Usage:

```
usage: card_simulator.py [-h] [--count COUNT] [--collected COLLECTED]
                         [--iter ITER] [--pack PACK] [--remain REMAIN]

Collecting card simulator

optional arguments:
  -h, --help            show this help message and exit
  --count COUNT
  --collected COLLECTED
  --iter ITER
  --pack PACK
  --remain REMAIN
```

So if you want to see how many packs you may need to get the last 20 of 
144:

```
--count 144 --collected 124
```

Will output five number summary and key inputs:

```
COUNT COLLECTED MIN Q1 MED Q3 MAX
```

N.B. since this is a _simulation_ the numbers may vary from one run to the next.
For more reliable numbers, `--iter 10000` takes longer but gives better results.
