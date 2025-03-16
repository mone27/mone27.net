# A Draft Draft Manifesto a next-generation point cloud processing library

> This is an early draft! Is incomplete, inconsistent and probably contains several errors.

## TL;DR

Point cloud processing can be made more efficient by developing a modern library and file format.

A good inspiration is to see how polars + arrow + parquet have revolutionized the data science stack. 

This is an overly ambitious manifesto, but I mean we can dream, right?

## Introduction

The data science stack has evolved a lot in the last years, but the point cloud processing world is not there yet.
Moreover, there is a divide between the Earth Observation and the robotics (?) communities, without a unified set of tools. This is especially a challenge for terrestrial lidar, which is between those two worlds.


## Properties

1. support point clouds from different sensors (terrestrial and aerial lidar)
2. work with large scale spatial dataset
3. cloud native support (load subset of the data from the cloud)
4. efficient use of modern hardware and ideally accelerators like GPUs
5. good API, that supports both high-level and low-level operations
6. streaming support
7. parallel processing on machine clusters

### Nerdy details

- columnar format for point clouds using Apache Arrow
- SIMD support
- predicate pushdown
- lazy evaluation
- parallel processing
- efficient use of modern CPU (cache, branch prediction, etc)
- avoid unnecessary data copying

## Limitation current libraries

now I am going to list why none of the existing libraries have those properties

## LAS/LAZ

This is great file format, especially with COPC as it allows to have a spatial index in it.
The main problem is that it is built for Aerial Laser Scanning


## Implementation ideas

I think we should take inspiration from the Polars library and apply the same ideas point cloud processing.

Maybe we could build on something like Data Fusion (https://datafusion.apache.org/) and then implement all the point cloud processing on top of it.

### Programming Language

on top of my mind I see there are 2 options for this:
- Rust, it has great performance and safety, is mature and has good integration with Python/R (but still have a language barrier)
- Mojo, this is at an early stage now, but ideally it will support great performance (especially for GPU) and very good integration with Python

### File format

My idea of a file format is parquet + spatial index in the metadata (like COPC)


### Data Structures

- Point Cloud (obviously) with support for custom attributes and multiple data types (i.e. both floats and integers)
- KD-Tree and Octrees for spatial indexing (probably also with a serialization format for storage and inter-machine communication?)
- Raster
- Mesh


### Memory copies

beside the basics this means that we need to implement a lot of custom algorithm to work with our data structures. For example if we take libraries like Dalnaunalor-cpp or CSF they copy the data in their data structure, which is not great (especially as point clouds can be very big)