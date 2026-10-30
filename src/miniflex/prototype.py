from miniflex.features import RollingMean



def process_events(events):
    mid = None
    rolling = RollingMean(10)

    for event in events:
        if event["type"] == "book":
            # at each tick (denoted by book), calculate a FV from mid price
            mid = (event["bid"]+event["ask"])/2
        
        elif event["type"] == 'trade':
            #if a trade has occurred, record the distance from calc FV of this trade in the history
            d = event['price']-mid

            rolling.update(d)


    return rolling.evaluate()



events = [
    {"type": "book", "bid": 99, "ask": 101},
    {"type": "trade", "price": 101},
    {"type": "trade", "price": 102},
    {"type": "book", "bid": 101, "ask": 103},
    {"type": "trade", "price": 104},
]



print(process_events(events))