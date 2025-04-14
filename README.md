# `pyplot` extensions to `dqrobotics`

## License

LGPL

## Installation

```
python3 -m pip install dqrobotics-pyplot
```

## Calling example

After installation, the example script can be called with
```console
dqrobotisc_pyplot_example
```

## Usage example

See the script in

```console
src/dqrobotics_extensions/pyplot/example.py
```
https://github.com/MarinhoLab/dqrobotics-pyplot/blob/7f8a4b02ef1f2e03bdcafa551b3ea8beadfdcf61/src/dqrobotics_extensions/pyplot/example.py#L31-67

### Importing the library

https://github.com/MarinhoLab/dqrobotics-pyplot/blob/7f8a4b02ef1f2e03bdcafa551b3ea8beadfdcf61/src/dqrobotics_extensions/pyplot/example.py#L24-25

### Seting up the plot

`dqrobotics-pyplot` uses `matplotlib.pyplot`, so always remember to create a proper figure and axes with `projection='3d''`. Other settings
are a matter of taste and desired quality.

https://github.com/MarinhoLab/dqrobotics-pyplot/blob/7f8a4b02ef1f2e03bdcafa551b3ea8beadfdcf61/src/dqrobotics_extensions/pyplot/example.py#L33-36

### Drawing a pose

https://github.com/MarinhoLab/dqrobotics-pyplot/blob/7f8a4b02ef1f2e03bdcafa551b3ea8beadfdcf61/src/dqrobotics_extensions/pyplot/example.py#L44-48

### Drawing a line

https://github.com/MarinhoLab/dqrobotics-pyplot/blob/7f8a4b02ef1f2e03bdcafa551b3ea8beadfdcf61/src/dqrobotics_extensions/pyplot/example.py#L50-54

### Drawing a plane

https://github.com/MarinhoLab/dqrobotics-pyplot/blob/7f8a4b02ef1f2e03bdcafa551b3ea8beadfdcf61/src/dqrobotics_extensions/pyplot/example.py#L56-60

### Drawing a manipulator

https://github.com/MarinhoLab/dqrobotics-pyplot/blob/7f8a4b02ef1f2e03bdcafa551b3ea8beadfdcf61/src/dqrobotics_extensions/pyplot/example.py#L62-65