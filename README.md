AMT - Artifacts Management Tool
===============================

Statement of Purpose
--------------------
AMT is meant to be a generic means of storing and manipulating artifact data in a human readable text format ideal for colaborative work.

### What AMT is:
* An object oriented heirarchical data management tool.
* Designed to be used from the command line or user interface.
* Intended to manage human readable files captured in a version control system.
* Scriptable (Written in Python with extendable API)
* Embeddable (C++ api to follow)

### What AMT is not:
* Specialized for any task other than the storage and manipulation of artifacts.

### Intended Use Cases:
* Issue Tracking System
* Requirements Management
* Use Case Documentation
* Object Models
* Software Lifecycle/Project Management Documentation Generation
* Simulation Input Files

### Command line tools
Command line tools are executed through subcommands of the amt command.

| Command    | Usage                                                              |
|:----------:|:-------------------------------------------------------------------|
| gui        | Invokes the graphical user interface to the amt tool.              |
| add        | Adds a new object to the current object tree.                      |
| dump       | Dumps an ascii representation of the object tree.                  |
| cannonical | Enforces the canonical representation of the object tree.          |

### Example Python Usage
```python
import amt

# Load
artifacts = amt.load('/path/to/artifacts')

# Read
AMT_OAR_001 = artifacts['Requirements']['AMT-OAR-0001']

# Modify
artifacts['Requirements']['AMT-OAR-0002']['Description'] = 'Be Cool'

# Write
amt.save('/path/to/write/artifacts', artifacts)
```
