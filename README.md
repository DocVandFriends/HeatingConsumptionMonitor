# HeatConsumptionMonitor

This tool is used to monitor and analysis heat consumption in my appartement. Our radiators use heat cost allocators that have to be read out manually and do not provide an interface for automatic data acquisition.

The allocators are read manually in unregular intervals. This data is fed into a data storage and made available for other parts of the tool. 


## Feature List
Feature|Description|Implemented
---|---|---
InputWizard | CLI prompt to input new read and save into CSV/XLS | 
InputWizard GUI | GUI for input wizard | 
DB Sync | sync local data with InfluxDB and/or directly feed data to InfluxDB | 
CostCalculator | Calculate current heating costs based on last year's heating bill | 
HeatTransferAnalysis | Analyse heat transfer through heat up and cool down cycles