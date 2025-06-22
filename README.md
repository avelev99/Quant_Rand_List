# Quant Rand List

This repository contains a simple Python script that uses IBM Quantum's free
cloud QPUs to select a random element from any list. **An IBM Quantum account
is required** and the script will raise an error if credentials are not
available.

## `quantum_list_picker.py`

Running the script will print a randomly chosen element from a predefined list
of 64 animals and insects.  You can also import `pick_random_element` and pass
any list you like.

### Requirements

- Python 3.8+
- `qiskit==0.45.1`
- `qiskit-ibm-provider==0.11`

Install the requirements and save your IBM Quantum API token once using:

```python
from qiskit_ibm_provider import IBMProvider
IBMProvider.save_account("<TOKEN>")
```

You can obtain a token by signing up at [IBM Quantum](https://quantum.ibm.com/).

After saving the token, execute:

```bash
python quantum_list_picker.py [--backend BACKEND_NAME]
```

To pick from your own list, import the function:

```python
from quantum_list_picker import pick_random_element
print(pick_random_element(["foo", "bar"]))
```

