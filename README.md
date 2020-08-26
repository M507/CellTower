# CellTower

CellTower is a tool used to log credentials, events, and any type of data. The data can be sorted and printed in the command line using Tower-CLI.py or on browsers using Kibana Dashboard. It uses elk stack and other different scripts to be used by other red team tools I wrote on Github.com/M507. 

### Overview
  - Tower-CLI.py, uses pre-made modules.
  
### Dependencies
* Docker-compose
* Python3

### Installation
Install the dependencies and devDependencies and start the server.

```sh
$ apt install python3 docker-compose -y
```

### Note: The tool is not made to face public networks.


### Development

Want to contribute? Great!

CellTower can use extra modules ! The tool made this way to simplify the process of contribution. There are *only* three steps. 
 - Add your customized module inside **modules** directory. 
 - Then Write a function in Utilities.py to call your module.
 - Finally, edit MyPrompt class in Tower-CLI.py to support your module.


License
----

MIT
