from  smartBuy.resources.act_functions import *

manage_data = {"pc":{

    {"functions":[function1,function2,function3]},
    {"sons":["son1","son2","son3"]},
    {"values":{"memory":"8" , "cpu-i":"3"}}}}
# patterns are suited to phone_dataset.csv
nameMetaData = {
  "pc": {
    "Cpu": {
      "type": "json",
      "patterns": [
        "%{WORD:producer} Core %{WORD:level} %{WORD:type} %{GREEDYDATA:rate}GHz",
        "%{WORD:producer} %{USERNAME:series} %{USERNAME:type} %{GREEDYDATA:rate}GHz"
      ]
    },
    "ram": {
      "type": "json",
      "patterns": [
        "%{NUMBER:ram}GB"
      ],
      "memory": {
        "type": "json",
        "patterns": [
          "%{NUMBER:memory}GB %{GREEDYDATA:type}"
        ]
      },

      "resolution":{
          "type":"json",
          "patterns" :["%{GREEDYDATA:type} %{NUMBER:height}x%{NUMBER:width}"]},
      "weight": {
            "type": "json",
            "patterns": ["%{NUMBER:height}kg"]},
      "price":{"type":"number"}
    }
  },
  "smartphone": {
    "battery": {
      "value": "number",
      "patterns": [
        "%{WORD:remove} %{WORD:type} %{NUMBER:capacity} mAh battery"
      ]
    }
  }
}


