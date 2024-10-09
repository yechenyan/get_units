# GET UNITS

Retrieve all unit types from https://databus.openenergyplatform.org/sedos-project/collections/sedos-project

```
Files
｜- all_units.json  All units in the table, not deduplicated
｜- main.py  Skriptcode
｜- opm.txt  URL of the table
｜- unique_units.json  deduplicated units (uniqueness based on unit + type)
```

## Get Start
Script Execution:

```
python main.py
```
## All unit

All the units are here:
```
%,%/h,EUR/(vehicle*a),EUR/MW,EUR/MW*a,EUR/MW/a,EUR/MWh,EUR/kW,EUR/kW*a,EUR/kWh,EUR/pkm,EUR/vehicle,GW,GWh,Gpkm,Gtkm,Kt,Kt/Kt,Kt/Million units,Kt/Mt,Kt/PJ,MEUR/Mt,MEUR/Mt*a,MW,MWh,MWh/MWh,MWh/t,Million units,Million units/Million units,Mt,Mt/Mt,Mt/PJ,M€/GW,M€/Kt CO2-eq,M€/Million units,M€/Mt,M€/PJ,PJ,PJ, Mt,PJ/Million units,PJ/Mt,PJ/PJ,[0,1],a,kW,kW/kW,kWh,kWh/100km,kWh/kWh,kWh/km,kg/t,kg_CH4/TJ_input,kg_N2O/TJ_input,km/a,kt/Kt,kt/Mt,percent,persons/vehicle,pkm,pkm or tkm or kWh,t/MWh,t/t,t/vehicle,t_CO2/TJ_input,tkm,vehicles,€/MW,€/MW*a,€/MWh,€/MWj,€/t
```
