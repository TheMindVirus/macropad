# Tabletop Simulator Scripting Buttons
### Tabletop Simulator running on Unity Engine 2019 does not allow C# Scripting for Custom Assetbundles...
### ...but it does turn numberpad keys into 1->10 as "scripting buttons" for triggering lua events and controlling Unity Components.

# Notes
* The lua scripting takes the following code layout: `function onScriptingButtonDown(index, color) print(index) end`
* Similarly there is also `function onScriptingButtonUp(index, color) print(index) end`
* 0 for whatever reason becomes 10 instead of 0
* The arrow keys which would be WASD will now be 1234
* The rest of the keys will be in order in portrait orientation starting from 5
* 2 keys remain unused and will be open for user-customisable macro keys

# Links
https://api.tabletopsimulator.com/events/#onscriptingbuttondown
https://api.tabletopsimulator.com/components/examples/
https://api.tabletopsimulator.com/types/#vector
https://docs.circuitpython.org/projects/hid/en/latest/api.html

### Tabletop Simulator Saves are usually found in `Documents/My Games/Tabletop Simulator/Saves/`
