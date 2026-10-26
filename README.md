# sysflex

a fast minimal system information fetcher built using python.

run it in your terminal. It instantly gets your system specs (OS, CPU, RAM, disk and uptime) and displays them next to a clean piece of ASCII art. No big dependencies, a simple nice-looking terminal tool.

## Usage

Run it directly from your terminal:

```bash
python sysflex.py
```

## Options

arguments: none needed.

| Option | What it does |
| --- | --- |
| `-c`, `--color` | output colour: green, blue, cyan, magenta or yellow |
| `--no-art` | print only the specs, without the ASCII art |
| `-h`, `--help` | show help |

## Example

```bash
$ python sysflex.py -c cyan

        \   /         OS: Windows 11
         .-.          CPU: AMD Ryzen 9 5900X
      ― (   ) ―       RAM: 16.4 GB / 32.0 GB
         '-'          Disk: 240 GB / 1000 GB
        /   \         Uptime: 4 days, 2 hours
```
