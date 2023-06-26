# Examples

Welcome to the examples!

## Power Blocks

In this example we're going to make a datapack that adds special effects to blue and lime concrete blocks.
The finished datapack will make blue concrete blocks give the player speed and lime concrete blocks jump boost when they
step on it.

First, we need to create the datapack.
Here is what the folder/file structure will look like:

```
Power Blocks/
    data/
        pythonmc/
            tags/
                python/
                    load.json
                    tick.json
        power_blocks/
            python/
                load.py
                tick.py
    pack.mcmeta
```

Here is the contents of the load.json file:

```
{
  "values": ["power_blocks:load"]
}
```

And the contents of the tick.json file:

```
{
  "values": ["power_blocks:tick"]
}
```