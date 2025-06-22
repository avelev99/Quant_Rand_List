# Quant Rand List

This repository contains a simple Python script that uses IBM Quantum's free
cloud QPUs to select a random element from any list. The script requires an
IBM Quantum account and will fail if one is not configured.

## `quantum_list_picker.py`

Running the script will print a randomly chosen element from a predefined list
of 64 animals and insects.  You can import `pick_random_element` and pass your
own list.

### Requirements

- Python 3.8+
- `qiskit`
- `qiskit-ibm-provider`

After installing the requirements and saving your IBM Quantum API token using
`IBMProvider.save_account('<TOKEN>')`, execute:


```bash
python quantum_list_picker.py
```
