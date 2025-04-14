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
https://github.com/MarinhoLab/dqrobotics-pyplot/blob/7f8a4b02ef1f2e03bdcafa551b3ea8beadfdcf61/src/dqrobotics_extensions/pyplot/example.py#L31-L67

### Importing the library

https://github.com/MarinhoLab/dqrobotics-pyplot/blob/7f8a4b02ef1f2e03bdcafa551b3ea8beadfdcf61/src/dqrobotics_extensions/pyplot/example.py#L24-L25

### Seting up the plot

`dqrobotics-pyplot` uses `matplotlib.pyplot`, so always remember to create a proper figure and axes with `projection='3d''`. Other settings
are a matter of taste and desired quality.

https://github.com/MarinhoLab/dqrobotics-pyplot/blob/7f8a4b02ef1f2e03bdcafa551b3ea8beadfdcf61/src/dqrobotics_extensions/pyplot/example.py#L33-L36

### Drawing a pose

Calling `dqp.plot()` without additional settings with a `DQ` argument will result in a reference-frame-type plot.

https://github.com/MarinhoLab/dqrobotics-pyplot/blob/7f8a4b02ef1f2e03bdcafa551b3ea8beadfdcf61/src/dqrobotics_extensions/pyplot/example.py#L44-L48

### Drawing a line

Call `dqp.plot()` with `line=True` to plot a line.

https://github.com/MarinhoLab/dqrobotics-pyplot/blob/7f8a4b02ef1f2e03bdcafa551b3ea8beadfdcf61/src/dqrobotics_extensions/pyplot/example.py#L50-L54

### Drawing a plane

Call `dqp.plot()` with `plane=True` to plot a plane.

https://github.com/MarinhoLab/dqrobotics-pyplot/blob/7f8a4b02ef1f2e03bdcafa551b3ea8beadfdcf61/src/dqrobotics_extensions/pyplot/example.py#L56-L60

### Drawing a manipulator

Call `dqp.plot()` with a `DQ_SerialManipulator` as argument and always remember to set the `q` argument, which should be a suitable `np.array`.

https://github.com/MarinhoLab/dqrobotics-pyplot/blob/7f8a4b02ef1f2e03bdcafa551b3ea8beadfdcf61/src/dqrobotics_extensions/pyplot/example.py#L62-L65
