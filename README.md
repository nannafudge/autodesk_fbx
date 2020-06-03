autodesk_fbx
======

A wheel implementation of Autodesk's FBX python bindings library. Contains several
build distributions available for download from PyPi.

Install
-------

```bash
pip install autodesk_fbx
```

This will (hopefully) provide a distribution that will work out of the box
with Windows and most Linux distributions.

Python FBX Bindings
---
> FBX(Filmbox) is a proprietary file format (.fbx) developed by
> Kaydara and owned by [Autodesk](https://en.wikipedia.org/wiki/Autodesk)
> since 2006. It is used to provide interoperability between digital
> content creation applications.
>
> from [Wikipedia](https://en.wikipedia.org/wiki/FBX)

Autodesk provide a python binding module to allow for native calls to the original
Autodesk FBX library. However, compiling and distributing such files can be a pain,
which is why I created this library.

This library will attempt to build and distribute the most appropriate Python package
for your system.

Original License
-----------------------
The Original source/implementation of the project was provided by
Autodesk, therefore all contents of the FBX package itself are managed under
their proprietary license.

[The ReadMe can be found here](../blob/master/AUTODESKLICENSE.rtf)