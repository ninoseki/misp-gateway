# Reject Cisco Top 20k Domains

This recipe makes it possible to reject Cisco top 20k domains from attributes when creating an event.


```bash
# start the gateway with the recipe
$ uvicorn recipes.reject_cisco_top20k.main:app
INFO:     Started server process [51580]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

```python
# test.py
from pymisp.mispevent import MISPEvent
from pymisp import ExpandedPyMISP

api_key = "YOUR_API_KEY"
misp = ExpandedPyMISP("http://localhost:8000", api_key)


payload = {
    "Event": {
        "date": "2015-01-01",
        "threat_level_id": "1",
        "info": "testevent",
        "published": False,
        "analysis": "0",
        "distribution": "0",
        "Attribute": [
            {
                "type": "domain",
                "category": "Network activity",
                "to_ids": False,
                "distribution": "0",
                "comment": "",
                "value": "something.evil",
            },
            {
                "type": "domain",
                "category": "Network activity",
                "to_ids": False,
                "distribution": "0",
                "comment": "",
                "value": "google.com",
            },
        ],
    }
}

event = MISPEvent()
event.from_dict(**payload)

misp.add_event(event)
```

```bash
python test.py
```

In the above example, the gateway rejects `google.com` attribute from the event, but keeps `something.evil` attribute.

