# explainability function

Later on when more features are implemented, a new system could be implemented.

Say for example, you have a complex feature made of multiple base features:

```python
example_signal = rolling_mean(...)
```

we can implement a useful function for QoL and research purposes when features get too big, called "explain" with which we could examine the constituent base features:

```python
engine.explain(signal)
```

which could output something like

```
rolling_mean(window=100, trigger=Trade)
└── subtract
    ├── trade_pricex
    └── divide
        ├── add
        │   ├── bid_price
        │   └── ask_price
        └── constant(2)
```

