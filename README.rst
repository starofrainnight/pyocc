=====
PyOCC
=====


.. image:: https://img.shields.io/pypi/v/pyocc.svg
        :target: https://pypi.python.org/pypi/pyocc

.. image:: https://img.shields.io/travis/starofrainnight/pyocc.svg
        :target: https://travis-ci.org/starofrainnight/pyocc

.. image:: https://ci.appveyor.com/api/projects/status/75t9t6j0xdel9pdx?svg=true
        :target: https://ci.appveyor.com/project/starofrainnight/pyocc

A wrapper for OpenCC (The Chinese convert solution)

* License: Apache-2.0

Usage
--------

.. code:: python

    from pyocc import PyOCC

    occ = PyOCC()

    print(occ.configs)
    # => ['hk2s', 's2hk', 's2t', 's2tw', 's2twp', 't2hk', 't2s', 't2tw', 'tw2s', 'tw2sp']

    print(occ.translate('中国', 's2t'))
    # => 中國

Credits
---------

This package was created with Cookiecutter_ and the `PyPackageTemplate`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`PyPackageTemplate`: https://github.com/starofrainnight/rtpl-pypackage

